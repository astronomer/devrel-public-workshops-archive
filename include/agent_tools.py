import os

import duckdb
from airflow.configuration import AIRFLOW_HOME
from airflow.sdk import BaseHook

_conn = BaseHook.get_connection("duckdb_astrotrips")
_DB_PATH = os.path.join(AIRFLOW_HOME, _conn.host)


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
