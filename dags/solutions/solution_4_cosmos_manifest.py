
"""
Airflow DAG to run a Jaffle Shop dbt project using Cosmos.
from airflow import DAG
"""
from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ProjectConfig, ProfileConfig, RenderConfig
from cosmos.constants import LoadMode


DBT_PROJECT_DIR = Path(__file__).parent.parent.parent / "dbt/jaffle_shop"
PROFILE_NAME = "bq_profile"
TARGET_NAME = "dev"
PROFILE_YML_FILEPATH = DBT_PROJECT_DIR / "profiles.yml"
DBT_MANIFEST_PATH = "/usr/local/airflow/include/manifest.json"

profile_config = ProfileConfig(
    profile_name=PROFILE_NAME,
    target_name=TARGET_NAME,
    profiles_yml_filepath=PROFILE_YML_FILEPATH,
)

render_config = RenderConfig(
    load_method=LoadMode.DBT_MANIFEST,
)

solution_4_cosmos_manifest = DbtDag(
    dag_id="solution_4_cosmos_manifest",
    start_date=datetime(2025, 10, 8),
    project_config=ProjectConfig(
        DBT_PROJECT_DIR,
        manifest_path=DBT_MANIFEST_PATH
    ),
    render_config=render_config,
    profile_config=profile_config,
)
