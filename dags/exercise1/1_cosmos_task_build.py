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

# TODO: Complete the code below with the correct parameters and values
#with DAG("1_cosmos_task_build") as dag:
#    build = DbtBuildLocalOperator(
#    )
#    build
