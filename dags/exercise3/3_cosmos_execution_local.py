"""
Airflow DAG to run a Jaffle Shop dbt project using Cosmos.
from airflow import DAG
"""
import os
from datetime import datetime
from pathlib import Path
import re

from cosmos import DbtDag, ExecutionConfig,ProjectConfig, ProfileConfig, RenderConfig
from cosmos.constants import ExecutionMode, InvocationMode
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

# TODO: Check the Dockerfile to see the isolated dbt venv installed and update the execution_config to use it
# don't forget to also update the InvocationMode to SUBPROCESS
#execution_config = ExecutionConfig(
#)

#exercise_3_cosmos_execution_local = DbtDag(
#    dag_id="3_cosmos_execution_local",
#    start_date=datetime(2025, 10, 8),
#    project_config=ProjectConfig(DBT_PROJECT_DIR),
#    profile_config=profile_config,
#    render_config=render_config
#)
