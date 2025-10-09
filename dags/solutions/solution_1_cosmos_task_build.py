"""
Airflow DAG to run a Jaffle Shop dbt project using Cosmos.
from airflow import DAG
"""
from pathlib import Path

from airflow.sdk import DAG
from cosmos import DbtBuildLocalOperator, ProfileConfig


DBT_PROJECT_DIR = Path(__file__).parent.parent / "dbt/jaffle_shop"
DBT_BIN_PATH = "dbt"
PROFILE_NAME = "bq_profile"
TARGET_NAME = "dev"
PROFILE_YML_FILEPATH = DBT_PROJECT_DIR / "profiles.yml"


profile_config = ProfileConfig(
    profile_name=PROFILE_NAME,
    target_name=TARGET_NAME,
    profiles_yml_filepath=PROFILE_YML_FILEPATH,
)

with DAG("solution_1_cosmos_task_build") as dag:
    build = DbtBuildLocalOperator(
        task_id="build",
        profile_config=profile_config,
        project_dir=DBT_PROJECT_DIR,
    )
    build
