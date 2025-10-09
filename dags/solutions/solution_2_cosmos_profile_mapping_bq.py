"""
Airflow DAG to run a Jaffle Shop dbt project using Cosmos.
from airflow import DAG
"""
import os
from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ProjectConfig, ProfileConfig
from cosmos.profiles.bigquery.service_account_file import GoogleCloudServiceAccountFileProfileMapping


DBT_PROJECT_DIR = Path(__file__).parent.parent.parent / "dbt/jaffle_shop"

BIGQUERY_CONN_ID = os.getenv("BIGQUERY_CONN_ID", "bigquery_default")

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=GoogleCloudServiceAccountFileProfileMapping(
        conn_id=BIGQUERY_CONN_ID
    )
)

solution_2_cosmos_profile_mapping = DbtDag(
    dag_id="solution_2_cosmos_profile_mapping",
    start_date=datetime(2025, 10, 8),
    project_config=ProjectConfig(DBT_PROJECT_DIR),
    profile_config=profile_config,
)
