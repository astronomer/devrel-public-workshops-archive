"""
This Dag is responsible for setting up the DuckDB database with the necessary
schema and fixtures for the workshop.

Please do not change this code during the workshop!
"""

from pendulum import duration
from airflow.configuration import AIRFLOW_HOME
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.sdk import dag, chain, Asset

from include.mission_control import MissionControlOperator

_DUCKDB_CONN_ID = "duckdb_astrotrips"


@dag(
    tags=["astrotrips", "setup"],
    template_searchpath=f"{AIRFLOW_HOME}/include/sql",
    default_args={
        "retries": 3,
        "retry_delay": duration(seconds=10),
    },
    doc_md=__doc__
)
def setup():

    _cleanup = SQLExecuteQueryOperator(
        task_id="cleanup",
        conn_id=_DUCKDB_CONN_ID,
        sql="cleanup.sql"
    )

    _schema = SQLExecuteQueryOperator(
        task_id="schema",
        conn_id=_DUCKDB_CONN_ID,
        sql="schema.sql"
    )

    _fixtures = SQLExecuteQueryOperator(
        task_id="fixtures",
        conn_id=_DUCKDB_CONN_ID,
        sql="fixtures.sql"
    )

    _ai_schema = SQLExecuteQueryOperator(
        task_id="ai_schema",
        conn_id=_DUCKDB_CONN_ID,
        sql="ai_schema.sql"
    )

    _ai_fixtures = SQLExecuteQueryOperator(
        task_id="ai_fixtures",
        conn_id=_DUCKDB_CONN_ID,
        sql="ai_fixtures.sql"
    )

    chain(
        _cleanup,
        _schema,
        _fixtures,
        _ai_schema,
        _ai_fixtures,
        MissionControlOperator(task_id="mission_control", outlets=[Asset("astrotrips-setup")]),
    )


setup_dag = setup()

if __name__ == "__main__":
    setup_dag.test(
        conn_file_path="include/connections.yaml"
    )
