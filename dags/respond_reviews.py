import os
import time

import duckdb
import pendulum
from airflow.configuration import AIRFLOW_HOME
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from duckdb_provider.hooks.duckdb_hook import DuckDBHook
from airflow.providers.standard.operators.hitl import HITLBranchOperator
from airflow.sdk import Asset, chain, dag, task, task_group
from pydantic_ai import Agent

_DUCKDB_CONN_ID = "duckdb_astrotrips"
_DB_PATH = os.path.join(
    os.environ.get("AIRFLOW_HOME", "/usr/local/airflow"),
    "include",
    "astrotrips.duckdb",
)


def _db_write(sql, params):
    hook = DuckDBHook(duckdb_conn_id=_DUCKDB_CONN_ID)
    for attempt in range(5):
        try:
            conn = hook.get_conn()
            conn.execute(sql, params)
            conn.close()
            return
        except duckdb.IOException:
            if attempt < 4:
                time.sleep(0.5 * (attempt + 1))
            else:
                raise


def lookup_booking(booking_id: int) -> str:
    """Look up booking details including customer, route, dates, and fare."""
    conn = duckdb.connect(_DB_PATH, read_only=True)
    rows = conn.execute(
        "SELECT b.booking_id, c.full_name, p.planet_name, r.base_fare_usd, "
        "b.departure_date, b.return_date, b.passengers, b.promo_code, "
        "pay.amount_usd "
        "FROM bookings b "
        "JOIN customers c ON c.customer_id = b.customer_id "
        "JOIN routes r ON r.route_id = b.route_id "
        "JOIN planets p ON p.planet_id = r.destination_id "
        "JOIN payments pay ON pay.booking_id = b.booking_id "
        "WHERE b.booking_id = ?",
        [booking_id],
    ).fetchall()
    conn.close()

    if not rows:
        return f"No booking found with ID {booking_id}"
    row = rows[0]
    return (
        f"Booking #{row[0]}: Customer {row[1]}, traveling to {row[2]}. "
        f"Base fare: ${row[3]:,}, paid: ${row[8]:,}. "
        f"Departure: {row[4]}, return: {row[5]}. "
        f"Passengers: {row[6]}, promo code: {row[7] or 'none'}."
    )


def find_similar_reviews(review_id: int) -> str:
    """Find reviews that are most similar to the given review based on embeddings."""
    conn = duckdb.connect(_DB_PATH, read_only=True)

    target = conn.execute(
        "SELECT embedding FROM review_embeddings WHERE review_id = ?",
        [review_id],
    ).fetchall()

    if not target:
        conn.close()
        return f"No embedding found for review #{review_id}. Run the embed_reviews Dag first."

    target_emb = target[0][0]

    others = conn.execute(
        "SELECT re.review_id, tr.review_text, tr.sentiment, tr.category, re.embedding "
        "FROM review_embeddings re "
        "JOIN trip_reviews tr ON tr.review_id = re.review_id "
        "WHERE re.review_id != ?",
        [review_id],
    ).fetchall()
    conn.close()

    if not others:
        return "No other embedded reviews found."

    def cosine_sim(a, b):
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = sum(x * x for x in a) ** 0.5
        norm_b = sum(x * x for x in b) ** 0.5
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot / (norm_a * norm_b)

    scored = []
    for row in others:
        sim = cosine_sim(target_emb, row[4])
        scored.append((row[0], row[1], row[2], row[3], sim))

    scored.sort(key=lambda x: x[4], reverse=True)
    top_3 = scored[:3]

    lines = [f"Top 3 similar reviews to review #{review_id}:"]
    for rid, text, sentiment, category, sim in top_3:
        lines.append(
            f"  - Review #{rid} (similarity: {sim:.2f}, {sentiment}/{category}): "
            f"{text[:120]}..."
        )
    return "\n".join(lines)


response_agent = Agent(
    "gpt-5-mini",
    system_prompt=(
        "You are a customer service agent for AstroTrips, an interplanetary travel company. "
        "Your job is to draft a professional, empathetic response to a customer's trip review.\n\n"
        "Guidelines:\n"
        "- Use the lookup_booking tool to find the customer's booking details.\n"
        "- Use the find_similar_reviews tool to see how similar feedback was handled.\n"
        "- Address the customer's specific concerns with empathy.\n"
        "- Reference concrete details from their booking (destination, dates, fare paid).\n"
        "- For safety concerns: acknowledge and assure investigation.\n"
        "- For billing issues: reference actual amounts and offer to review.\n"
        "- For positive reviews: thank them warmly and invite them back.\n"
        "- Keep the response under 200 words.\n"
        "- Sign off as 'AstroTrips Customer Experience Team'."
    ),
    tools=[lookup_booking, find_similar_reviews],
)


@task.agent(agent=response_agent)
def draft_response(prompt: str) -> str:
    return prompt


@dag(
    schedule=(Asset("routed-reviews") & Asset("embedded-reviews")),
    start_date=pendulum.datetime(2025, 1, 1),
    catchup=False,
    tags=["astrotrips", "ai", "reviews", "hitl"],
    template_searchpath=f"{AIRFLOW_HOME}/include/sql",
)
def respond_reviews():
    get_reviews = SQLExecuteQueryOperator(
        task_id="get_reviews",
        conn_id=_DUCKDB_CONN_ID,
        sql=(
            "SELECT review_id, booking_id, review_text, sentiment, category, summary "
            "FROM trip_reviews WHERE status = 'routed' AND ai_response IS NULL "
            "ORDER BY submitted_at ASC"
        ),
    )

    @task
    def prepare_review_list(query_result):
        if not query_result:
            return []
        return [
            {
                "review_id": row[0],
                "booking_id": row[1],
                "text": row[2],
                "sentiment": row[3],
                "category": row[4],
                "summary": row[5],
            }
            for row in query_result
        ]

    reviews = prepare_review_list(get_reviews.output)

    @task_group
    def respond_one_review(review_data):
        @task
        def build_prompt(data):
            return (
                f"Please draft a response to this customer review.\n\n"
                f"Review #{data['review_id']} (booking #{data['booking_id']}):\n"
                f"Category: {data['category']} | Sentiment: {data['sentiment']}\n"
                f"Summary: {data['summary']}\n\n"
                f"Full review:\n{data['text']}\n\n"
                f"Use the lookup_booking tool with booking_id={data['booking_id']} "
                f"to get booking details. "
                f"Use the find_similar_reviews tool with review_id={data['review_id']} "
                f"to find similar reviews."
            )

        @task(max_active_tis_per_dagrun=1)
        def save_draft(data, response_text):
            _db_write(
                "UPDATE trip_reviews SET status = 'response_drafted', "
                "ai_response = ? WHERE review_id = ?",
                [response_text, data["review_id"]],
            )
            return {"review_id": data["review_id"], "response": response_text}

        @task(max_active_tis_per_dagrun=1)
        def finalize(data):
            _db_write(
                "UPDATE trip_reviews SET status = 'approved', "
                "approved_at = CURRENT_TIMESTAMP WHERE review_id = ?",
                [data["review_id"]],
            )

        @task(max_active_tis_per_dagrun=1)
        def mark_rejected(data):
            _db_write(
                "UPDATE trip_reviews SET status = 'rejected' WHERE review_id = ?",
                [data["review_id"]],
            )

        prompt = build_prompt(review_data)
        response = draft_response(prompt)
        saved = save_draft(review_data, response)

        review_branch = HITLBranchOperator(
            task_id="review_response",
            subject="Review response approval",
            body=(
                "Please review the AI-drafted response and approve or reject it.\n\n"
                "**Review ID:** {{ ti.xcom_pull(task_ids='respond_one_review.save_draft', map_indexes=ti.map_index)['review_id'] }}\n\n"
                "**Drafted response:**\n\n"
                "{{ ti.xcom_pull(task_ids='respond_one_review.save_draft', map_indexes=ti.map_index)['response'] }}"
            ),
            options=["Approve", "Reject"],
            options_mapping={
                "Approve": "respond_one_review.finalize",
                "Reject": "respond_one_review.mark_rejected",
            },
        )

        chain(saved, review_branch, [finalize(review_data), mark_rejected(review_data)])

    respond_one_review.expand(review_data=reviews)


respond_reviews()
