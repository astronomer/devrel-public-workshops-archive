"""
Airflow DAG to run a Jaffle Shop dbt project using Cosmos.
from airflow import DAG
"""
import os
from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ProjectConfig, ProfileConfig
from cosmos.profiles.postgres.user_pass import PostgresUserPasswordProfileMapping


DBT_PROJECT_DIR = Path(__file__).parent.parent / "dbt/jaffle_shop"

BIGQUERY_CONN_ID = os.getenv("BIGQUERY_CONN_ID", "bigquery_default")

profile_config = ProfileConfig(
    profile_name="airflow_db",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="airflow_metadata_db",
        profile_args={"schema": "dbt"},
    ),
)

solution_2_cosmos_profile_mapping_custom = DbtDag(
    dag_id="solution_2_cosmos_profile_mapping_postgres",
    start_date=datetime(2025, 10, 8),
    project_config=ProjectConfig(DBT_PROJECT_DIR),
    profile_config=profile_config,
)
