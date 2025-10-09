"""
Airflow DAG to run a Jaffle Shop dbt project using Cosmos.
from airflow import DAG
"""
from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ProjectConfig, ProfileConfig


DBT_PROJECT_DIR = Path(__file__).parent.parent.parent / "dbt/jaffle_shop"
DBT_BIN_PATH = "dbt"
PROFILE_NAME = "bq_profile"
TARGET_NAME = "dev"
PROFILE_YML_FILEPATH = DBT_PROJECT_DIR / "profiles.yml"


profile_config = ProfileConfig(
    profile_name=PROFILE_NAME,
    target_name=TARGET_NAME,
    profiles_yml_filepath=PROFILE_YML_FILEPATH,
)

solution_1_cosmos_dbtdag = DbtDag(
    dag_id="solution_1_cosmos_dbtdag",
    start_date=datetime(2025, 10, 8),
    project_config=ProjectConfig(DBT_PROJECT_DIR),
    profile_config=profile_config,
)
