# Exercise 0: Astro and Astro IDE

## Set Up Astro IDE

This workshop does not require any local Airflow installation. Instead, all development takes place within Astro and the Astro IDE. The first step is to set up a **free** Astro trial to run Airflow and access the Astro IDE for Dag development.

While a deep understanding of the Astro platform is not required, here is a quick overview: Each customer has a dedicated Organization on Astro. An Organization can contain multiple Workspaces (for example, one per team). Each Workspace can have multiple Deployments, where a Deployment is a fully hosted Airflow environment.

1. Create a [free trial of Astro](https://www.astronomer.io/lp/signup/?utm_source=conference&utm_medium=web&utm_campaign=devrel-workshop).

    - After creating an account, verifying your email, and logging in, choose _Personal_ in the first step.
    - Next, choose an _Organization_ and _Workspace_ name. These can be fictional names and you can change them later.
    - In the third step, click the small link at the bottom under the two boxes: _Or skip this and go to your workspace_.

    ![Create an empty environment](doc/screenshot-trial-setup.png)

    - You should now see the Astro platform UI.

2. Open the _Astro IDE_ from the left navigation and select _Connect Git project..._
3. Under _Select a Git provider for manual configuration_, select _GitHub_ and enter the following details:

    - **ACCOUNT**: `astronomer`
    - **REPOSITORY**: `devrel-public-workshops`
    - _Keep Astro Project Path empty_
    - **BRANCH**: `workshops/astrotrips/<workshop>` (for example: `workshops/astrotrips/etl`)
    - **AUTHENTICATION TYPE**: `None (public repository)`
    - Click _Connect_. The IDE will import and open the project for you.

    ![Connect Git project in Astro IDE](doc/screenshot-select-git-repo.png)

**You now have the Astro IDE with the project ready to go.**

![Astro IDE](doc/screenshot-astro-ide.png)

## Set Up the Connection

This workshop relies on a DuckDB database. To ensure your test environments can connect to it, the next step is to create a workspace-wide connection.

1. In Astro, navigate to _Environment_ → _Connections_ and click the _+ Connection_ button.
2. In the dialog, select _Generic_ and enter the following details:

    - Set **AUTOMATICALLY LINK TO ALL DEPLOYMENTS** to _On_
    - **CONNECTION ID**: `duckdb_astrotrips`
    - **TYPE**: `duckdb`
    - **HOST**: `include/astrotrips.duckdb`

    ![Add connection](doc/screenshot-add-connection.png)

3. Click _Create Connection_.

> [!TIP]
> Learn more about [Airflow connections](https://www.astronomer.io/docs/learn/connections).

## Start the Test Deployment and Run the Setup Dag

The final setup step is to start a test deployment (a fully functional Airflow environment) and run the `setup` Dag, which creates the DuckDB database with tables and sample data for the following exercises.

1. Navigate to the _Astro IDE_ and click _Start Test Deployment_ in the top right corner.
2. While the deployment is starting, click the dropdown next to _Sync to Test_ and select _Test Deployment Details_.

    ![Open test deployment details](doc/screenshot-open-deployment-details.png)

3. Navigate to the _Environment_ tab and click _Edit Deployment Variables_.
4. In the popup, remove the `AIRFLOW__SCHEDULER__USE_JOB_SCHEDULE` variable to enable cron scheduling for the test deployment.

5. Click _Update Environment Variables_.

    ![Change environment variables](doc/screenshot-env-vars.png)

6. Back in the Astro IDE, from the same dropdown menu, select _Open Airflow_.

    ![Open Airflow](doc/screenshot-open-airflow.png)

7. In the Airflow UI, open the Dags view from the left menu and trigger the `setup` Dag using the play button.

    ![Trigger setup Dag](doc/screenshot-trigger-setup-dag.png)

**Once the Dag run completes successfully, your database is ready.**

> [!IMPORTANT]
> Running this Dag resets and re-creates the database. If you encounter any issues in the following exercises, simply run this Dag again.

---

# Exercise 1: Build the daily report Dag

In this exercise, you will create a Dag that ingests new booking data, generates a daily report, and validates the output. The validated report is then published as an **asset**, making it available to downstream consumers.

**What you will learn:**

- Running parameterized SQL queries with `SQLExecuteQueryOperator`.
- Validating data with `SQLColumnCheckOperator`.
- Publishing an asset to signal data availability.

## Create the Dag file

1. In the Astro IDE, create a new file `dags/daily_report.py`.
2. Add the following imports and connection constant:

    ```python
    from airflow.configuration import AIRFLOW_HOME
    from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator, SQLColumnCheckOperator
    from airflow.sdk import dag, chain, Asset
    from pendulum import datetime

    _DUCKDB_CONN_ID = "duckdb_astrotrips"
    ```

3. Define the Dag using the `@dag` decorator:

    ```python
    @dag(
        schedule="@daily",
        start_date=datetime(2026, 1, 1),
        tags=["astrotrips", "reporting"],
        template_searchpath=f"{AIRFLOW_HOME}/include/sql"
    )
    def daily_report():
        pass

    daily_report()
    ```

    The `template_searchpath` parameter tells Airflow where to find SQL files referenced by name.

> [!TIP]
> Learn more about [Airflow decorators and the TaskFlow API](https://www.astronomer.io/docs/learn/airflow-decorators).

## Add the ingest task

The first task simulates ingesting new booking data by calling a SQL script that generates random bookings.

1. Inside the `daily_report()` function, add:

    ```python
    _ingest_data = SQLExecuteQueryOperator(
        task_id="ingest",
        conn_id=_DUCKDB_CONN_ID,
        sql="generate.sql",
        params={ "n_bookings": 5 }
    )
    ```

    The `params` dictionary passes variables to the SQL template. Open `include/sql/generate.sql` to see how `{{ params.n_bookings }}` is used.

> [!NOTE]
> **`parameters` vs `params`**
>
> These two attributes serve different purposes:
>
> - **`parameters`** uses database-level parameter binding. The placeholder syntax depends on your database driver (e.g., `$reportDate` for DuckDB, `%(name)s` for Postgres). This is the preferred and secure approach since the database driver handles escaping, preventing SQL injection. You can still use Jinja templating for the values themselves, when instantiating the operator.
>
> - **`params`** uses Jinja templating before the query reaches the database driver. It treats your SQL as a plain string and replaces `{{ params.name }}` placeholders. This is useful when the SQL structure itself needs to be dynamic, like repeating query fragments multiple times.
>
> Learn more about parameters vs params [in this video](https://www.youtube.com/watch?v=QNAzQgvcQGM). It also demonstrates the risk of SQL injection.

> [!NOTE]
> **How `SQLExecuteQueryOperator` works under the hood**
>
> The `SQLExecuteQueryOperator` is a generic operator for running SQL workloads from Airflow. It relies on the [`DbApiHook`](https://airflow.apache.org/docs/apache-airflow-providers-common-sql/stable/_api/airflow/providers/common/sql/hooks/sql/index.html) abstract base class, which is designed to work with Python's [DB-API 2.0 (PEP 249)](https://peps.python.org/pep-0249/) specification, the standard interface for database access in Python.
>
> Each database provider (Postgres, Snowflake, DuckDB, etc.) ships its own hook that inherits from `DbApiHook` and wraps the native database driver. As long as the provider package is installed and implements a proper `DbApiHook` subclass, you can use this operator with any compliant database.

> [!TIP]
> Learn more about [executing SQL with Airflow](hhttps://www.astronomer.io/docs/learn/airflow-sql).

## Add the report generation task

The second task aggregates booking data into a daily report per planet.

1. Open `include/sql/report.sql` and review the query. Notice that it expects a `$reportDate` parameter and uses an upsert pattern (`ON CONFLICT ... DO UPDATE`) to handle re-runs gracefully.
2. The query is missing the `total_paid_usd` column. Find the `-- TODO` comment in the SQL file and add the missing aggregation following the pattern of the other columns.
3. Create a `SQLExecuteQueryOperator` with task_id `generate_report` that:
    - Uses the `report.sql` file
    - Passes the logical date formatted as `YYYY-MM-DD` as a parameter named `reportDate`

    Unlike the previous task which used `params` for Jinja templating, this task needs to use `parameters` to pass values directly to the database driver (for DuckDB's `$variable` syntax).

> [!TIP]
> You need to find the right Airflow template variable for the formatted logical date. See the [templates reference](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html).

## Add data validation

Before publishing the report, validate that the data meets quality expectations.

1. Add a `SQLColumnCheckOperator` task:

    ```python
    _validate_report = SQLColumnCheckOperator(
        task_id="validate_report",
        conn_id=_DUCKDB_CONN_ID,
        table="daily_planet_report",
        column_mapping={
            "planet_name": {
                "null_check":     {"equal_to": 0},
                "distinct_check": {"geq_to": 3},
            },
            "total_passengers": {
                "null_check":     {"equal_to": 0},
                "min":            {"geq_to": 1},
            }
        },
        outlets=Asset("daily_report")
    )
    ```

    The `outlets` parameter declares that this task produces the `daily_report` asset. Downstream Dags can subscribe to this asset to trigger automatically when new data is available.

> [!TIP]
> Learn more about [data quality checks](https://www.astronomer.io/docs/learn/airflow-sql-data-quality) and [assets](https://www.astronomer.io/docs/learn/airflow-datasets).

## Wire up the tasks

Use `chain()` to define the execution order.

1. At the end of the `daily_report()` function, add:

    ```python
    chain(
        _ingest_data,
        _generate_report,
        _validate_report
    )
    ```

## Test your Dag

1. In the Astro IDE, click _Sync to Test_ to deploy your changes.
2. Open the Airflow UI and trigger the `daily_report` Dag.
3. Verify all tasks complete successfully.
4. Check the _assets_ view in Airflow to confirm the `daily_report` asset was updated.

## See data validation in action

To understand how data quality checks protect your pipeline, let's intentionally trigger a failure.

1. In your `_validate_report` task, change the `distinct_check` threshold from `3` to `42`:

    ```python
    "distinct_check": {"geq_to": 42},
    ```

2. Sync and trigger the Dag again.
3. Observe that the `validate_report` task fails. Open the task logs to see the validation error message.
4. Notice that the `daily_report` asset was **not** updated this time, the quality gate prevented bad data from being published.
5. Change the threshold back to `3`, sync, and run the Dag once more to confirm it passes.

---

# Exercise 2: Asset-aware scheduling

tbd

_Add next exercise here._
