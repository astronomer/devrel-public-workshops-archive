# Airflow AI Workshop

## Exercises

- [Exercise 0: Astro and Astro IDE](#exercise-0-astro-and-astro-ide)
- [Exercise 1: Analyze reviews with an LLM](#exercise-1-analyze-reviews-with-an-llm)
- [Exercise 2: Route reviews with LLM branching](#exercise-2-route-reviews-with-llm-branching)
- [Challenge: Mission control](#challenge-mission-control)
- [Exercise 3: Embed reviews and find similar complaints](#exercise-3-embed-reviews-and-find-similar-complaints)
- [Exercise 4: AI agent with human-in-the-loop](#exercise-4-ai-agent-with-human-in-the-loop)

---

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
    - **BRANCH**: `workshops/astrotrips/ai`
    - **AUTHENTICATION TYPE**: `None (public repository)`
    - Click _Connect_. The IDE will import and open the project for you.

    ![Connect Git project in Astro IDE](doc/screenshot-select-git-repo.png)

**You now have the Astro IDE with the project ready to go.**

![Astro IDE](doc/screenshot-astro-ide.png)

> [!TIP]
> The Astro IDE comes with an integrated AI assistant, optimized for workflow orchestration with Apache Airflow. Feel free to interact with it during this workshop to learn more about certain concepts.

## Set Up the Connection

This workshop relies on a DuckDB database. To ensure your test environments can connect to it, the next step is to create a workspace-wide connection.

> [!NOTE]
> The next two steps take place in the main Astro platform UI, not inside the Astro IDE. If you collapsed the sidebar, expand it to navigate.

1. In Astro, navigate to _Environment_ → _Connections_ and click the _+ Connection_ button.
2. In the dialog, search for and select _Generic_, then enter the following details:

    ![Select generic type](doc/screenshot-add-connection-generic.png)

    - **CONNECTION ID**: `duckdb_astrotrips`
    - **TYPE**: `duckdb`
    - **HOST**: `include/astrotrips.duckdb`
    - Set **AUTOMATICALLY LINK TO ALL DEPLOYMENTS** to _On_

    ![Add connection](doc/screenshot-add-connection.png)

3. Click _Create Connection_.

> [!TIP]
> Learn more about [Airflow connections](https://www.astronomer.io/docs/learn/connections).

## Add the OpenAI API key

The AI exercises require an OpenAI API key (or any compatible provider). We will set this as an environment variable, to make it available for our Airflow instance.

1. In Astro, navigate to _Environment_ → _Environment Variables_ and click the _+ Environment Variable_ button.
2. Enter the following details:
    - **KEY**: `OPENAI_API_KEY`
    - **VALUE**: your API key
    - Mark it as **Secret**
    - Set **AUTOMATICALLY LINK TO ALL DEPLOYMENTS** to _On_

    ![Add environment variable](doc/screenshot-add-env-var.png)

3. Click _Create Environment Variable_.

## Start the test deployment and run the setup Dag

The final setup step is to start a test deployment (a fully functional Airflow environment) and run the `setup` Dag, which creates the DuckDB database with tables and sample data for the following exercises.

> [!CAUTION]
> Do not close the Astro IDE browser tab during the workshop. Always use this tab to return to the Astro IDE instead of reopening it to preserve your session. If you close it, you will need to create a new test deployment.

1. Navigate to the _Astro IDE_ and click _Start Test Deployment_ in the top right corner. The deployment takes 3-5 minutes to spin up.
2. While the deployment is starting, click the dropdown next to _Sync to Test_ and select _Test Deployment Details_.

    ![Open test deployment details](doc/screenshot-open-deployment-details.png)

3. Navigate to the _Environment_ tab and click _Edit Deployment Variables_.
4. In the popup, remove the `AIRFLOW__SCHEDULER__USE_JOB_SCHEDULE` variable to enable scheduling for the test deployment.
5. Click _Update Environment Variables_.

    ![Change environment variables](doc/screenshot-env-vars.png)

> [!NOTE]
> Scheduling is disabled by default for test deployments to prevent Dags from running automatically. This gives you maximum control during development and helps avoid unwanted side effects. However, for this workshop, we want Dags to be scheduled based on asset updates, so we enable scheduling accordingly.

6. Back in the Astro IDE, once the test deployment is ready, select _Open Airflow_, from the same dropdown menu.

    ![Open Airflow](doc/screenshot-open-airflow.png)

7. In the Airflow UI, open the Dags view from the left menu and trigger the `setup` Dag using the play button.

    ![Trigger setup Dag](doc/screenshot-trigger-setup-dag.png)

**Once the Dag run completes successfully, your database is ready.**

> [!IMPORTANT]
> Running this Dag resets and re-creates the database. If you encounter any issues in the following exercises, simply run this Dag again.

## AstroTrips support portal

Before we start coding, take a look at the **AstroTrips Support Portal**. In the Airflow sidebar, click the _AstroTrips_ link to open it.

![AstroTrips support portal](doc/screenshot-support-portal-base.png)

This is a custom **Airflow plugin** built with FastAPI, one of the new extension points in Airflow 3. It provides a dashboard that visualizes the state of all customer reviews as they move through the pipeline.

Right now, all 8 reviews show as _pending_. As you work through the exercises, you will see reviews progress through analysis, routing, response drafting, and approval, all reflected on this dashboard.

This is not only a feedback mechanism that gives you something visual to review after each exercise, but also a great example of how Airflow's potential use cases have evolved with new features.

> [!NOTE]
> Building plugins is not part of this workshop. The portal is pre-built to support the exercises and give you a visual overview of your progress. If you're curious about the implementation, explore `plugins/support_portal.py` after the workshop.

> [!CAUTION]
> You will also see a `plugin_sync` Dag in the Airflow UI. This Dag keeps the support portal data in sync and triggers automatically whenever a pipeline Dag completes. **Leave it activated and do not modify it.**

> [!TIP]
> Learn more about [Airflow plugins](https://www.astronomer.io/docs/learn/using-airflow-plugins).

---

# Exercise 1: Analyze reviews with an LLM

In this exercise, you will build a Dag that uses an LLM to analyze customer reviews. The LLM extracts structured data (_sentiment, category, and a summary_) from each review. Some reviews include photos, so the Dag also uses vision capabilities to describe what the image shows.

**What you will learn:**

- Calling an LLM with `@task.llm` and getting structured output via a Pydantic model.
- Sending images to a vision-capable LLM with `BinaryContent`.
- Using `.expand_kwargs()` to dynamically map over multiple arguments.
- Publishing an asset to trigger downstream Dags.

## Create the Dag file

1. In the Astro IDE, create a new file `dags/analyze_reviews.py`.
2. Add the following imports and constants:

    ```python
    import airflow_ai_sdk as ai_sdk
    import os
    from pendulum import duration
    from airflow.configuration import AIRFLOW_HOME
    from airflow.providers.common.sql.operators.sql import (
        SQLExecuteQueryOperator,
        SQLInsertRowsOperator,
    )
    from airflow.sdk import Asset, chain, dag, task
    from pydantic_ai import BinaryContent
    from typing import Literal

    _DUCKDB_CONN_ID = "duckdb_astrotrips"
    ```

3. Define the Dag:

    ```python
    @dag(
        tags=["astrotrips", "ai", "reviews"],
        template_searchpath=f"{AIRFLOW_HOME}/include/sql",
        default_args={"retries": 3, "retry_delay": duration(seconds=10)},
    )
    def analyze_reviews():
        pass

    analyze_reviews()
    ```

> [!NOTE]
> This Dag has no `schedule` — it is triggered manually. The `default_args` add retry logic since DuckDB can throw temporary lock errors when multiple tasks write concurrently.

> [!NOTE]
> `pass` is a null operation that acts as a placeholder when a statement is syntactically required but no action needs to run. We use it as a temporary placeholder for Dag or task implementations, which we will complete step by step during the workshop exercises.

## Define the output model

The LLM should return structured data, not free text.

1. Define a Pydantic model **above** the `@dag` function that describes the expected output:

    ```python
    class ReviewAnalysis(ai_sdk.BaseModel):
        sentiment: Literal["positive", "negative", "neutral"]
        category: Literal["safety", "service", "value", "experience"]
        summary: str
        image_description: str | None = None
    ```

The `airflow-ai-sdk` provides its own `BaseModel` that auto-serializes results for XCom. Using `Literal` types constrains the LLM to only return valid values.

## Add the query and formatting tasks

1. Inside the Dag function (`analyze_reviews()`) function, add a `SQLExecuteQueryOperator` to run a query, which fetches all pending reviews:

    ```python
    _reviews = SQLExecuteQueryOperator(
        task_id="get_reviews",
        conn_id=_DUCKDB_CONN_ID,
        sql=(
            "SELECT review_id, booking_id, review_text, image_path, "
            "CAST(submitted_at AS VARCHAR) AS submitted_at "
            "FROM trip_reviews WHERE status = 'pending'"
        ),
    )
    ```

2. Add a task to format the query results into the shape expected by the LLM task:

    ```python
    @task
    def format_context(query_result):
        return [
            {"review_text": row[2], "image_path": row[3]}
            for row in query_result
        ]

    _formatted_context = format_context(_reviews.output)
    ```

> [!NOTE]
> When passing the result of a `SQLExecuteQueryOperator` to a `@task` function, you must use `.output` to get the XCom value. This is one way of passing data between classic operators and TaskFlow API based tasks.

## Add the LLM analysis task

This is the core of the exercise. The `@task.llm` decorator turns a regular Python function into an LLM-powered task.

1. Add the LLM task:

    ```python
    @task.llm(
        model="gpt-5-mini",
        system_prompt=(
            "You are a customer review analyst for AstroTrips, an interplanetary travel company. "
            "Analyze the given trip review and extract:\n"
            "- sentiment: positive, negative, or neutral\n"
            "- category: the primary category of the review:\n"
            "  - safety: concerns about travel safety, turbulence, landings, equipment\n"
            "  - service: crew/staff quality, communication, onboard experience\n"
            "  - value: pricing, billing, value-for-money complaints\n"
            "  - experience: the trip itself, destinations, sightseeing, overall enjoyment\n"
            "- summary: a single concise sentence summarizing the review\n"
            "- image_description: if an image is attached, describe what it shows in 1-2 sentences. "
            "If no image is attached, set this to null."
        ),
        output_type=ReviewAnalysis,
        max_active_tis_per_dagrun=1
    )
    def analyze_review(review_text: str, image_path: str | None = None) -> str | list:
        if image_path:
            full_path = os.path.join(AIRFLOW_HOME, "include", image_path)
            with open(full_path, "rb") as f:
                image_data = f.read()
            return [review_text, BinaryContent(data=image_data, media_type="image/jpeg")]
        return review_text
    ```

    The function body is a **translation function**, it returns the prompt that gets sent to the LLM. When an image is present, it returns a list with both the text and the image data. The LLM receives both and can describe what it sees. Take note how the system prompt is defined as an argument of the decorator.

2. Next, we analyze each review individually, along with its image (_if present_). The number of task instances is determined at runtime. To create parallel task instances at runtime, we use a feature called dynamic task mapping. We do this by calling `expand` on a task, or in this case, `expand_kwargs` to pass multiple arguments:

    ```python
    _analyses = analyze_review.expand_kwargs(_formatted_context)
    ```

> [!NOTE]
> We use `.expand_kwargs()` instead of `.expand()` here because each review needs **two** arguments (`review_text` and `image_path`). With `.expand()`, passing two keyword arguments would create a cross product of all combinations. The `expand_kwargs()` method maps them as pairs.

> [!NOTE]
> We can limit parallelism using `max_active_tis_per_dagrun`. In this case, we process each review one at a time to keep the load on our test deployment as low as possible.

> [!TIP]
> Learn more about the [airflow-ai-sdk](https://github.com/astronomer/airflow-ai-sdk) and [dynamic task mapping](https://www.astronomer.io/docs/learn/dynamic-tasks).

## Add the save task

The LLM results need to be written back to the database. We'll collect all analyses together with the original review data and insert them using a delete-then-insert pattern.

1. Add a task to combine the original query data with the LLM output:

    ```python
    @task
    def prepare_rows(query_result, analyses):
        rows = []
        for row, analysis in zip(query_result, analyses):
            review_id, booking_id, review_text, image_path, submitted_at = row
            rows.append((
                review_id,
                booking_id,
                review_text,
                image_path,
                submitted_at,
                "analyzed",
                analysis["sentiment"],
                analysis["category"],
                analysis["summary"],
                analysis.get("image_description"),
            ))
        return rows

    _prepared_rows = prepare_rows(_reviews.output, _analyses)
    ```

2. Add the `SQLInsertRowsOperator` to save the results. The `outlets` parameter declares that this task updates the `analyzed-reviews` asset, which will trigger downstream Dags:

    ```python
    _save_analysis = SQLInsertRowsOperator(
        task_id="save_analyses",
        conn_id=_DUCKDB_CONN_ID,
        table_name="trip_reviews",
        rows=_prepared_rows,
        columns=[
            "review_id", "booking_id", "review_text", "image_path", "submitted_at",
            "status", "sentiment", "category", "summary", "image_analysis",
        ],
        preoperator="DELETE FROM trip_reviews WHERE status = 'pending'",
        outlets=[Asset("analyzed-reviews")],
    )
    ```

3. Wire it up:

    ```python
    chain(_prepared_rows, _save_analysis)
    ```

## Test your Dag

1. Sync your changes to the test deployment by clicking _Sync to Test_ within the Astro IDE.

> [!TIP]
> **Sync tips:**
> - Changes to Dag files sync fast. Changes to files in `include/` trigger an image rebuild, which takes longer.
> - While waiting for a sync, you can ask the Astro IDE AI questions about your Dag or about Airflow.
> - You don't need to commit your changes. If you want to keep your code after the workshop, fork the repository first.

2. Trigger the `analyze_reviews` Dag.
3. Once complete, open the **AstroTrips Support Portal**. You should see all 8 reviews with AI analysis results (sentiment, category, summary) and image descriptions for the 3 reviews that have photos.

![AstroTrips analyzed review](doc/screenshot-analyzed-review.png)

---

# Exercise 2: Route reviews with LLM branching

In this exercise, you will build a Dag that routes each analyzed review to the right support team using LLM-powered branching. The LLM reads each review and decides which downstream task to run.

**What you will learn:**

- Using `@task.llm_branch` for LLM-powered Dag branching.
- Combining branching with `@task_group` and `.expand()` for per-item routing.
- Asset-aware scheduling to trigger this Dag automatically.

## Create the Dag file

1. Create `dags/route_reviews.py` with the following imports:

    ```python
    import pendulum
    from airflow.configuration import AIRFLOW_HOME
    from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
    from airflow.sdk import Asset, dag, task, task_group, chain

    _DUCKDB_CONN_ID = "duckdb_astrotrips"
    ```

2. Define the Dag with **asset-aware scheduling**. This Dag should trigger automatically whenever the `analyzed-reviews` asset is updated:

    ```python
    @dag(
        schedule=Asset("analyzed-reviews"),
        tags=["astrotrips", "ai", "reviews"],
        template_searchpath=f"{AIRFLOW_HOME}/include/sql",
        default_args={"retries": 3, "retry_delay": pendulum.duration(seconds=10)},
    )
    def route_reviews():
        pass

    route_reviews()
    ```

> [!TIP]
> Learn more about [asset-aware scheduling](https://www.astronomer.io/docs/learn/airflow-datasets).

## Add the query and formatting tasks

1. Inside the `route_reviews()` function, fetch all analyzed reviews and format them:

    ```python
    _reviews = SQLExecuteQueryOperator(
        task_id="get_reviews",
        conn_id=_DUCKDB_CONN_ID,
        sql=(
            "SELECT review_id, review_text, sentiment, category, summary "
            "FROM trip_reviews WHERE status = 'analyzed' "
            "ORDER BY submitted_at ASC"
        ),
    )

    @task
    def prepare_review_list(query_result):
        if not query_result:
            return []
        return [
            {
                "review_id": row[0],
                "text": row[1],
                "sentiment": row[2],
                "category": row[3],
                "summary": row[4],
            }
            for row in query_result
        ]

    _review_list = prepare_review_list(_reviews.output)
    ```

## Build the routing task group

Dynamic task mapping lets you create parallel instances of an atomic task at runtime. But what if a single task is not enough? You can also apply this feature to task groups, which contain one or more tasks (or other task groups). This approach allows you to dynamically generate parallel instances of more complex workflows.

Each review needs to be routed individually. We use a `@task_group` with `.expand()` to process each review as its own branching pipeline.

1. As a first step, define the task group which receives a single review as an argument, together with a task to prepare the context we will later pass to the LLM branching task:

    ```python
    @task_group(default_args={"max_active_tis_per_dagrun": 1})
    def handle_review(review_data):

        @task
        def format_context(data):
            return (
                f"Review #{data['review_id']} (sentiment: {data['sentiment']}, "
                f"category: {data['category']}):\n"
                f"Summary: {data['summary']}\n\n"
                f"Full review:\n{data['text']}"
            )

        _formatted_context = format_context(review_data)
    ```

2. Add the LLM branching task **inside of the task group**! The `@task.llm_branch` decorator lets the LLM choose which downstream task to execute. The downstream task IDs become the options:

    ```python
        @task.llm_branch(
            model="gpt-5-mini",
            system_prompt=(
                "You are a support ticket router for AstroTrips, an interplanetary travel company. "
                "Based on the customer review below, decide which team should handle it.\n\n"
                "Choose exactly one of the following task IDs:\n"
                "- route_refund: The customer has a billing complaint, feels overcharged, "
                "or is questioning the value for money. Route here for potential refund processing.\n"
                "- route_safety: The customer reports a safety concern such as rough landings, "
                "turbulence, equipment warnings, or anything that could endanger passengers.\n"
                "- route_marketing: The customer left a very positive review praising "
                "the experience. Route here so marketing can use it as a testimonial.\n"
                "- route_general: The review contains mixed feedback about service quality, "
                "suggestions for improvement, or does not clearly fit the other categories."
            ),
        )
        def route_review(review_text: str) -> str:
            return review_text

        _route_review = route_review(_formatted_context)
    ```

    The LLM reads the system prompt (which describes the options) and the formatted review, then returns one of the task IDs. Airflow uses that to decide which downstream branch to run.

## Add the routing handlers

Each branch runs a `SQLExecuteQueryOperator` that updates the review's status and assigned team in the database.

**Ensure to add the code of all three steps within the task group**!

1. Add a helper task and the four routing handlers inside the task group. Each one uses the **`parameters`** keyword with DuckDB's `$variable` syntax for safe parameter binding:

    ```python
        @task
        def extract_id(review_data):
            return review_data["review_id"]

        _id = extract_id(review_data)
    ```

2. Now create the four `SQLExecuteQueryOperator` tasks. One for each routing destination. **Your task:** Add the refund task, and create the remaining three operators, using the task IDs: `route_safety`, `route_marketing`, and `route_general`, following the same pattern, changing only the `routed_to` value:

    ```python
        _route_refund = SQLExecuteQueryOperator(
            task_id="route_refund",
            conn_id=_DUCKDB_CONN_ID,
            sql="UPDATE trip_reviews SET status = 'routed', routed_to = 'refund' WHERE review_id = $id::INT",
            parameters={"id": _id}
        )

        # TODO: Add _route_safety (task_id = 'route_safety', routed_to = 'safety')
        # TODO: Add _route_marketing (task_id = 'route_marketing', routed_to = 'marketing')
        # TODO: Add _route_general (task_id = 'route_general', routed_to = 'general')
    ```

3. Wire the branch to the handlers within the task group:

    ```python
        chain(
            _route_review, [
                _route_refund,
                _route_safety,
                _route_marketing,
                _route_general,
            ]
        )
    ```

## Wire up the Dag

**Outside the task group**, expand it over the review list, add a completion task that emits an asset, and wire everything together.

1. Add the completion task and wire up the Dag:

    ```python
    @task(outlets=[Asset("routed-reviews")], trigger_rule="none_failed_min_one_success")
    def routing_complete():
        print("Routing complete for all new reviews")

    chain(
        handle_review.expand(review_data=_review_list),
        routing_complete(),
    )
    ```

## Test your Dag

1. Sync and trigger the `analyze_reviews` Dag. Once it completes, the `route_reviews` Dag should trigger **automatically** via the asset.
2. While it is running, check the graph view of `route_reviews`. You should see the task group expanded with branching per review. Make yourself familiar with the different views Airflow offers, can you find the log output of individual task instances?
3. Open the **AstroTrips Support Portal**! Reviews should now show a purple **ROUTED TO** box indicating the assigned team.

![AstroTrips routed review](doc/screenshot-routed-review.png)

---

# Challenge: Mission control

It is time for a challenge. The workshop provides a custom `MissionControlOperator` that generates an interstellar clearance code based on your implementation. Only if you finished all tasks successfully, including using the correct task IDs and dependencies, the code will be correct.

Within your `route_reviews` Dag:

1. Import the `MissionControlOperator` from `include.mission_control`.
2. Create a task instance with `task_id="mission_control"`.
3. Add it as the **last step** in the `route_reviews` Dag's task chain (after `routing_complete`).
4. Sync your changes and trigger `route_reviews` manually from the Dags page.
5. Open the latest run and check the `mission_control` task logs for your clearance code and share it!

> [!IMPORTANT]
> The first 3 that finish this challenge successfully receive a gift from Astronomer!

---

# Exercise 3: Embed reviews and find similar complaints

wip
