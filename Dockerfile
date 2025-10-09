FROM astrocrpublic.azurecr.io/runtime:3.1-1

ENV BIGQUERY_CONN_ID="bigquery_default"
ENV GCP_PROJECT_ID="airflowintegrations"
ENV BIGQUERY_DATASET="afs2025_schema_60"
ENV BIGQUERY_KEY_PATH="/usr/local/airflow/include/key.json"

ENV AIRFLOW_CONN_BIGQUERY_DEFAULT='{"conn_type":"google_cloud_platform","extra":{"project":"astronomer-dag-authoring","dataset":"release_18","key_path":"/usr/local/airflow/include/key.json"}}'

# set a connection to the airflow metadata db to use for testing, only works locally
ENV AIRFLOW_CONN_AIRFLOW_METADATA_DB=postgresql+psycopg2://postgres:postgres@postgres:5432/postgres

ENV AIRFLOW__COSMOS__DBT_DOCS_PROJECTS='{"jaffle-shop":{"dir":"/usr/local/airflow/dbt/jaffle_shop/target","index":"index.html","name":"dbt Docs (jaffle-shop)"}}'

RUN pip install astronomer-cosmos==1.11.0a8
RUN pip install dbt-bigquery

ENV AIRFLOW__CORE__DAGBAG_IMPORT_TIMEOUT=600

RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-postgres==1.8.2 && deactivate
