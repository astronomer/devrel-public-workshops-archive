from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ProjectConfig, ProfileConfig


jaffle_shop_path = Path("/usr/local/airflow/dbt/jaffle_shop")
profile_config = ProfileConfig(
                    profile_name="bq_profile",
                    target_name="dev",
                    profiles_yml_filepath="/usr/local/airflow/dbt/jaffle_shop/profiles.yml"
                )

simple_dag = DbtDag(
    # dbt/cosmos-specific parameters
    project_config=ProjectConfig(jaffle_shop_path),
    profile_config=profile_config,
    # normal dag parameters
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    dag_id="simple_dag",
)

