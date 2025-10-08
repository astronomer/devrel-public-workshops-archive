FROM astrocrpublic.azurecr.io/runtime:3.1-1

RUN pip install astronomer-cosmos
RUN pip install dbt-bigquery
