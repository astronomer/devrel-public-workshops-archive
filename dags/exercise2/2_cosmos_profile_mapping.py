"""
Airflow DAG to run a Jaffle Shop dbt project using Cosmos.
from airflow import DAG
"""
import os
from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ProjectConfig, ProfileConfig
from cosmos.profiles.bigquery.service_account_file import GoogleCloudServiceAccountFileProfileMapping


DBT_PROJECT_DIR = Path(__file__).parent.parent / "dbt/jaffle_shop"
DBT_BIN_PATH = "dbt"
PROFILE_NAME = "bq_profile"
TARGET_NAME = "dev"
PROFILE_YML_FILEPATH = DBT_PROJECT_DIR / "profiles.yml"

BIGQUERY_CONN_ID = os.getenv("BIGQUERY_CONN_ID", "bigquery_default")


# TODO: use GoogleCloudServiceAccountFileProfileMapping and the connection BIGQUERY_CONN_ID to map an Airlfow connection to a dbt profile
# profile_config = ProfileConfig(
#     profile_name=PROFILE_NAME,
#     target_name=TARGET_NAME,
#     profiles_yml_filepath=PROFILE_YML_FILEPATH,
# )

#exercise2_cosmos_profile_mapping = DbtDag(
#    start_date=datetime(2025, 10, 8),
#    dag_id="2_cosmos_profile_mapping",
#    project_config=ProjectConfig(DBT_PROJECT_DIR),
#   profile_config=profile_config,
#)
