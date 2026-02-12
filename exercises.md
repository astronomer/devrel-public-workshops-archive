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

> [!IMPORTANT]
> You will also see a `plugin_sync` Dag in the Airflow UI. This Dag keeps the support portal data in sync and triggers automatically whenever a pipeline Dag completes. **Leave it activated and do not modify it.**

> [!TIP]
> Learn more about [Airflow plugins](https://www.astronomer.io/docs/learn/using-airflow-plugins).

---

# Exercise 1: Analyze reviews with an LLM

wip
