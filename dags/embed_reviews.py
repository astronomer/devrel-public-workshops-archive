from airflow.configuration import AIRFLOW_HOME
from airflow.providers.common.sql.operators.sql import (
    SQLExecuteQueryOperator,
    SQLInsertRowsOperator,
)
from airflow.sdk import Asset, chain, dag, task

_DUCKDB_CONN_ID = "duckdb_astrotrips"


@dag(
    schedule=Asset("routed-reviews"),
    tags=["astrotrips", "ai", "reviews", "embeddings"],
    template_searchpath=f"{AIRFLOW_HOME}/include/sql",
)
def embed_reviews():

    _reviews = SQLExecuteQueryOperator(
        task_id="get_reviews",
        conn_id=_DUCKDB_CONN_ID,
        sql="SELECT review_id, review_text FROM trip_reviews WHERE status != 'pending'",
    )

    @task
    def extract_texts(query_result):
        return [row[1] for row in query_result]

    @task
    def extract_ids(query_result):
        return [row[0] for row in query_result]

    @task.embed(
        model_name="all-MiniLM-L12-v2",
        encode_kwargs={"normalize_embeddings": True},
    )
    def embed_review(review_text: str) -> str:
        return review_text

    _texts = extract_texts(_reviews)
    _ids = extract_ids(_reviews)

    _embeddings = embed_review.expand(review_text=_texts)

    @task
    def prepare_rows(review_ids, embeddings):
        """Combine review IDs with their embedding vectors into insertable rows."""
        rows = []
        for review_id, embedding in zip(review_ids, embeddings):
            rows.append((review_id, embedding))
        return rows

    _prepared_rows = prepare_rows(_ids, _embeddings)

    _save_embeddings = SQLInsertRowsOperator(
        task_id="save_embeddings",
        conn_id=_DUCKDB_CONN_ID,
        table_name="review_embeddings",
        rows=_prepared_rows,
        columns=["review_id", "embedding"],
        preoperator="DELETE FROM review_embeddings",
    )

    _get_embedded_reviews = SQLExecuteQueryOperator(
        task_id="get_embedded_reviews",
        conn_id=_DUCKDB_CONN_ID,
        sql=(
            "SELECT re.review_id, tr.review_text, tr.category, re.embedding "
            "FROM review_embeddings re "
            "JOIN trip_reviews tr ON tr.review_id = re.review_id "
            "ORDER BY re.review_id"
        ),
    )

    @task(outlets=[Asset("embedded-reviews")])
    def compute_similarity(rows):
        """Compute pairwise cosine similarity and print clusters."""
        if not rows:
            print("No embeddings found.")
            return

        def cosine_sim(a, b):
            dot = sum(x * y for x, y in zip(a, b))
            norm_a = sum(x * x for x in a) ** 0.5
            norm_b = sum(x * x for x in b) ** 0.5
            if norm_a == 0 or norm_b == 0:
                return 0.0
            return dot / (norm_a * norm_b)

        print("::group::Top similar review pairs")
        pairs = []
        for i in range(len(rows)):
            for j in range(i + 1, len(rows)):
                sim = cosine_sim(rows[i][3], rows[j][3])
                pairs.append((rows[i][0], rows[j][0], sim, rows[i][2], rows[j][2]))

        pairs.sort(key=lambda x: x[2], reverse=True)

        for r1_id, r2_id, sim, cat1, cat2 in pairs[:10]:
            marker = " <-- same cluster" if cat1 == cat2 else ""
            print(f"  Review #{r1_id} ({cat1}) <-> Review #{r2_id} ({cat2}): {sim:.3f}{marker}")
        print("::endgroup::")

    chain(_prepared_rows, _save_embeddings, _get_embedded_reviews)
    compute_similarity(_get_embedded_reviews)


embed_reviews()
