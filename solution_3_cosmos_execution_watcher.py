"""
Airflow DAG to run a Jaffle Shop dbt project using Cosmos.
from airflow import DAG
"""
import os
from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ExecutionConfig,ProjectConfig, ProfileConfig
from cosmos.constants import ExecutionMode
from cosmos.profiles.bigquery.service_account_file import GoogleCloudServiceAccountFileProfileMapping


DBT_PROJECT_DIR = Path(__file__).parent.parent / "dbt/jaffle_shop"
DBT_BIN_PATH = "/usr/local/airflow/dbt_venv/bin/dbt"
BIGQUERY_CONN_ID = os.getenv("BIGQUERY_CONN_ID", "bigquery_default")


profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=GoogleCloudServiceAccountFileProfileMapping(
        conn_id=BIGQUERY_CONN_ID
    )
)

execution_config = ExecutionConfig(
    execution_mode=ExecutionMode.WATCHER,
)

solution_3_cosmos_execution_watcher = DbtDag(
    dag_id="solution_3_cosmos_execution_watcher",
    start_date=datetime(2025, 10, 8),
    execution_config=execution_config,
    project_config=ProjectConfig(DBT_PROJECT_DIR),
    profile_config=profile_config,
)
