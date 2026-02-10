import os
from typing import Literal

import airflow_ai_sdk as ai_sdk
import pendulum
from airflow.configuration import AIRFLOW_HOME
from airflow.providers.common.sql.operators.sql import (
    SQLExecuteQueryOperator,
    SQLInsertRowsOperator,
)
from airflow.sdk import Asset, chain, dag, task
from pydantic_ai import BinaryContent

_DUCKDB_CONN_ID = "duckdb_astrotrips"


class ReviewAnalysis(ai_sdk.BaseModel):
    sentiment: Literal["positive", "negative", "neutral"]
    category: Literal["safety", "service", "value", "experience"]
    summary: str
    image_description: str | None = None


@dag(
    schedule=None,
    start_date=pendulum.datetime(2025, 1, 1),
    catchup=False,
    tags=["astrotrips", "ai", "reviews"],
    template_searchpath=f"{AIRFLOW_HOME}/include/sql",
)
def analyze_reviews():
    get_reviews = SQLExecuteQueryOperator(
        task_id="get_reviews",
        conn_id=_DUCKDB_CONN_ID,
        sql=(
            "SELECT review_id, booking_id, review_text, image_path, "
            "CAST(submitted_at AS VARCHAR) AS submitted_at "
            "FROM trip_reviews WHERE status = 'pending'"
        ),
    )

    @task
    def prepare_analysis_inputs(query_result):
        return [
            {"review_text": row[2], "image_path": row[3]}
            for row in query_result
        ]

    @task.llm(
        model="gpt-5-mini",
        system_prompt=(
            "You are a customer review analyst for AstroTrips, an interplanetary travel company. "
            "Analyze the given trip review and extract:\n"
            "- sentiment: positive, negative, or neutral\n"
            "- category: the primary category of the review:\n"
            "  - safety: concerns about travel safety, turbulence, landings, equipment\n"
            "  - service: crew/staff quality, communication, onboard experience\n"
            "  - value: pricing, billing, value-for-money complaints\n"
            "  - experience: the trip itself, destinations, sightseeing, overall enjoyment\n"
            "- summary: a single concise sentence summarizing the review\n"
            "- image_description: if an image is attached, describe what it shows in 1-2 sentences. "
            "If no image is attached, set this to null."
        ),
        output_type=ReviewAnalysis,
    )
    def analyze_review(review_text: str, image_path: str | None = None) -> str | list:
        # note: in a production setup, images should be stored in a dedicated object storage service instead of local filesystem
        if image_path:
            full_path = os.path.join(AIRFLOW_HOME, "include", image_path)
            with open(full_path, "rb") as f:
                image_data = f.read()
            return [review_text, BinaryContent(data=image_data, media_type="image/jpeg")]
        return review_text

    inputs = prepare_analysis_inputs(get_reviews.output)
    analyses = analyze_review.expand_kwargs(inputs)

    @task
    def prepare_rows(query_result, analyses):
        rows = []
        for row, analysis in zip(query_result, analyses):
            review_id, booking_id, review_text, image_path, submitted_at = row
            rows.append((
                review_id,
                booking_id,
                review_text,
                image_path,
                submitted_at,
                "analyzed",
                analysis["sentiment"],
                analysis["category"],
                analysis["summary"],
                analysis.get("image_description"),
            ))
        return rows

    prepared = prepare_rows(get_reviews.output, analyses)

    save = SQLInsertRowsOperator(
        task_id="save_analyses",
        conn_id=_DUCKDB_CONN_ID,
        table_name="trip_reviews",
        rows=prepared,
        columns=[
            "review_id", "booking_id", "review_text", "image_path", "submitted_at",
            "status", "sentiment", "category", "summary", "image_analysis",
        ],
        preoperator="DELETE FROM trip_reviews WHERE status = 'pending'",
        outlets=[Asset("analyzed-reviews")],
    )

    chain(prepared, save)


analyze_reviews()
