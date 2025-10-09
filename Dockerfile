FROM astrocrpublic.azurecr.io/runtime:3.1-1

ENV AIRFLOW__COSMOS__DBT_DOCS_PROJECTS='{"jaffle-shop":{"dir":"/usr/local/airflow/dbt/jaffle_shop/target","index":"index.html","name":"dbt Docs (jaffle-shop)"}}'
