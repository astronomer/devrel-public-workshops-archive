from pathlib import Path
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator


DBT_PROJECT_DIR = Path(__file__).parent.parent.parent / "dbt/jaffle_shop"
DBT_BIN_PATH = "dbt"
PROFILE_NAME = "bq_profile"
TARGET_NAME = "dev"

BASE_DBT_CMD = f"{DBT_BIN_PATH} %s --profiles-dir {DBT_PROJECT_DIR} --project-dir {DBT_PROJECT_DIR} --profile {PROFILE_NAME} --target {TARGET_NAME}"

DBT_DEPS =  BASE_DBT_CMD % " deps"
DBT_SEED =  BASE_DBT_CMD % " seed"
DBT_RUN =  BASE_DBT_CMD % " run"
DBT_TEST =  BASE_DBT_CMD % " test"


with DAG(
    "1_bashoperator",
    description="A sample Airflow DAG to invoke dbt runs using a BashOperator",
    schedule=None,
) as dag:

    seed = BashOperator(
        task_id="seed",
        bash_command=f"{DBT_DEPS} && {DBT_SEED}",
    )

    run = BashOperator(
        task_id="run",
        bash_command=f"{DBT_DEPS} && {DBT_RUN}"
    )

    test = BashOperator(
        task_id="test",
        bash_command=f"{DBT_DEPS} && {DBT_TEST}"
    )

    seed >> run >> test