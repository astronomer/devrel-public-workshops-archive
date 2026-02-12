"""
Syncs DuckDB data to an Airflow Variable.

Workaround for Astro deployments where the Support Portal plugin runs on the
API server, which does not share the worker's filesystem.  This Dag reads all
review data from DuckDB (on the worker) and writes it as JSON to an Airflow
Variable that the plugin can read from anywhere.

This is only applicable for this workshop scenario, as we works with a controlled
and low amount of data.

Locally this Dag is optional, the plugin falls back to reading DuckDB directly.

This workaround can also be avoided entirely by using a cloud-hosted DuckDB
via MotherDuck (https://motherduck.com). Both the worker and the API server
can then connect to the same remote database.

Please do not change this code during the workshop!
"""

import json
from datetime import datetime

from pendulum import duration
from airflow.models import Variable
from airflow.sdk import Asset, dag, task
from duckdb_provider.hooks.duckdb_hook import DuckDBHook

_DUCKDB_CONN_ID = "duckdb_astrotrips"

_REVIEWS_SQL = (
    "SELECT r.review_id, r.review_text, r.status, r.sentiment, r.category, "
    "r.summary, r.routed_to, r.ai_response, r.submitted_at, r.approved_at, "
    "c.full_name, p.planet_name, b.passengers, pay.amount_usd, "
    "r.image_path, r.image_analysis "
    "FROM trip_reviews r "
    "JOIN bookings b ON b.booking_id = r.booking_id "
    "JOIN customers c ON c.customer_id = b.customer_id "
    "JOIN routes rt ON rt.route_id = b.route_id "
    "JOIN planets p ON p.planet_id = rt.destination_id "
    "JOIN payments pay ON pay.booking_id = b.booking_id "
    "ORDER BY r.submitted_at DESC"
)

_EMBEDDINGS_SQL = (
    "SELECT re.review_id, tr.category, tr.sentiment, re.embedding, tr.review_text "
    "FROM review_embeddings re "
    "JOIN trip_reviews tr ON tr.review_id = re.review_id"
)


def _serialize(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Cannot serialize {type(obj)}")


@dag(
    schedule=(
        Asset("astrotrips-setup")
        | Asset("analyzed-reviews")
        | Asset("routed-reviews")
        | Asset("embedded-reviews")
        | Asset("responded-reviews")
    ),
    tags=["astrotrips", "plugin"],
    default_args={
        "retries": 3,
        "retry_delay": duration(seconds=10),
    },
    doc_md=__doc__,
)
def plugin_sync():

    @task
    def sync_to_variable():
        hook = DuckDBHook(duckdb_conn_id=_DUCKDB_CONN_ID)
        conn = hook.get_conn()

        reviews = conn.execute(_REVIEWS_SQL).fetchall()

        try:
            embeddings = conn.execute(_EMBEDDINGS_SQL).fetchall()
        except Exception:
            embeddings = []

        conn.close()

        Variable.set(
            "support_portal_data",
            json.dumps(
                {"reviews": reviews, "embeddings": embeddings},
                default=_serialize,
            ),
        )

    sync_to_variable()


plugin_sync()
