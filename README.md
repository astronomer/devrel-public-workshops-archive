# Play Astro

Welcome to Play Astro: an immersive learning quest for building GenAI pipelines with Apache Airflow and Amazon Bedrock!

This workshop is designed to get you familiar with some of the biggest features in Apache Airflow 3. You'll learn about the new UI, Assets (the evolution of datasets), human-in-the-loop workflows, Dag versioning, and event-driven scheduling with Amazon SQS and how to integrate Amazon Bedrock.

## Workshop overview

In this hands-on workshop, you'll build an automated personalized newsletter system using Airflow 3's latest features. The workshop includes:

- **ETL pipeline**: Retrieve data from APIs, format it, and create newsletter templates
- **Personalization pipeline**: Generate personalized newsletters based on user preferences
- **Advanced features**: Human-in-the-loop approval, Dag versioning, and event-driven scheduling and GenAI integration

# About Astro

[Astronomer](https://www.astronomer.io/) is the leading data orchestration platform built on Apache Airflow, trusted by hundreds of organizations to reliably run their most critical data workflows at scale.

## What is Astro?

Astro is a fully managed Apache Airflow service that removes the complexity of running Airflow infrastructure while providing enterprise-grade features for data teams.

### Key benefits

- **Fully managed**: No infrastructure management required
- **Enterprise security**: SOC 2 Type II certified with advanced security features
- **Scalable**: Auto-scaling workers and flexible resource allocation
- **Developer experience**: Enhanced IDE, CI/CD integration, and debugging tools
- **Observability**: Advanced monitoring, alerting, and lineage tracking

## Astro platform components

### Astro IDE

- Cloud-based development environment
- Integrated code editor with Airflow-specific features
- Real-time Dag validation and testing
- Seamless deployment to Airflow environments

### Astro Runtime

- Certified Apache Airflow distribution
- Enhanced with additional operators and features
- Regular security updates and patches
- Optimized performance and reliability

### Astro CLI

- Command-line interface for local development
- Project scaffolding and management
- Local Airflow testing capabilities
- Deployment automation

# Use case and architecture

This workshop demonstrates Airflow 3's capabilities through building a **personalized newsletter system** that showcases modern data orchestration patterns.

![Demo architecture diagram](img/etl_genai_newsletter_architecture_diagram_bedrock.png)

## Workshop use case

The use case for this workshop is using Airflow to create an automated and personalized newsletter. The end-to-end solution includes two different processes, interacting via assets:

1. The `create_newsletter` process retrieves quotes from the ZenQuotes API, and prepares a newsletter based on a template. It consists of three `@asset` decorated functions, which means, three Dags with a single task each implementing the business logic, communicating via assets. You will learn more about assets while exploring this documentation.
2. The `personalize_newsletter` process personalizes the newsletter based on user input. It's a task-oriented pipeline, which is taking the user's location, and the reader's favorite sci-fi character into account. This is used with a LLM through Amazon Bedrock to write content in the voice/style of the sci-fi character they chose.

## Airflow 3 features demonstrated

### Assets (data-aware scheduling)

An [asset](https://www.astronomer.io/docs/learn/airflow-datasets) is a logical representation of data, such as a table, model, or file, or exists only as a made-up construct to have an object to define cross-Dag dependencies. It's used to establish dependencies between pipelines. Assets can be explicitly defined (⁠`Asset("name")`) or implicitly referenced (when using ⁠`@asset`, the function itself is the asset reference). Both refer to the same underlying asset and can be used interchangeably in task ⁠outlets or ⁠schedule parameters. Assets enable cross-Dag dependencies without sensors, make data lineage visible in the Airflow UI, and work across both imperative and declarative authoring approaches.

An **asset event** is a record that indicates an asset has been updated, created automatically when an asset producing function finishes successfully. These events are what actually trigger downstream consumer Dags that are scheduled on those assets, and they can optionally contain extra metadata about the update. You can create these events also via the API or directly within the Airflow UI, with or without materializing the asset.

**Materialize** means to run the underlying function that produces and updates an asset. When you materialize an asset, you're executing the code that generates or updates the data that asset represents.

The `@asset` decorator is a **declarative shorthand that creates a complete Dag with a single task and one asset** in one function declaration (use `@asset.multi` for multiple assets).

```py
@asset(schedule="@daily")
def raw_zen_quotes():
    """
    Extracts a random set of quotes.
    """
    import requests
    r = requests.get("https://zenquotes.io/api/quotes/random")
    return r.json()
```

This asset-oriented approach puts the data asset front and center, automatically generating the Dag structure, task definition, and asset production with minimal boilerplate code.

### Enhanced UI

- React-based interface with improved navigation
- Better visualization of workflows and dependencies
- Enhanced debugging and monitoring capabilities

> [!TIP]
> [Introduction to the Airflow UI](https://www.astronomer.io/docs/learn/airflow-ui)

### Human-in-the-loop operators

- Manual intervention points in automated workflows
- Approval/rejection workflows with rich content display
- Batch processing of approval requests

Check the  guide for more details and an overview of all available options.

> [!TIP]
> [Human-in-the-loop workflows with Airflow](https://www.astronomer.io/docs/learn/airflow-human-in-the-loop)

### Built-in backfills

- UI-driven historical data processing (can also be triggered via API and CLI)
- Progress tracking and monitoring
- Flexible reprocessing options

> [!TIP]
> [Rerun Airflow Dags and tasks](https://www.astronomer.io/docs/learn/rerunning-dags#backfill)

### Dag versioning

- Automatic tracking of structural changes
- Visual comparison between versions
- Code history and change management

> [!TIP]
> [Dag Versioning and Dag Bundles](https://www.astronomer.io/docs/learn/airflow-dag-versioning)

### Event-driven scheduling

- SQS integration for real-time triggers
- Dynamic workflow execution based on external events
- Scalable processing of user requests

> [!TIP]
> [Event-driven scheduling](https://www.astronomer.io/docs/learn/airflow-event-driven-scheduling)

## Technology stack

### Core platform

- **[Apache Airflow 3](https://airflow.apache.org/)**: Latest workflow orchestration features
- **[Astro IDE](https://www.astronomer.io/product/ide/)**: Author, test, and release production-ready Dags from your browser
- **[Astro](https://www.astronomer.io/product/)**: Managed Airflow platform
- **[Python](https://www.python.org/)**: Primary development language
- **[Git](https://git-scm.com/)**: Version control and collaboration

### External integrations

- **[ZenQuotes API](https://zenquotes.io/)**: Motivational quote source
- **[Open-Meteo API](https://open-meteo.com/)**: Weather data provider
- **[Amazon SQS](https://aws.amazon.com/sqs/)**: Event-driven messaging
- **[Amazon Bedrock](https://aws.amazon.com/bedrock/)**: GenAI capabilities

This architecture provides a comprehensive foundation for understanding modern data orchestration while demonstrating practical, real-world applications of Airflow 3's enhanced capabilities.

# Prerequisites

Before starting this workshop, please ensure you have the following prerequisites in place.

## Required knowledge

### Technical background

- **Basic Python programming**: Understanding of Python syntax, functions, and basic data structures
- **Command line familiarity**: Comfortable using terminal/command prompt for basic operations
- **Git basics**: Understanding of git clone, checkout, and basic version control concepts

### Apache Airflow concepts

- **Dags (directed acyclic graphs)**: Understanding of workflow concepts and task dependencies
- **Tasks and Operators**: Basic knowledge of how Airflow executes work
- **Scheduling**: Familiarity with cron expressions and time-based scheduling concepts

> [!TIP]
> If you're new to Airflow, we recommend reviewing the [introduction to Apache Airflow®](https://www.astronomer.io/docs/learn/intro-to-airflow) before starting this workshop.

#### TL;DR

- **Dag**: Your entire pipeline from start to finish, consisting of one or more tasks
- **Task**: A unit of work within your pipeline
- **Operators and decorators**: The template/class that defines what work a task does, serving as the building blocks of pipelines
  - Traditional: `task = PythonOperator(...)` → returns operator directly
  - TaskFlow: `@task def my_task(): ...` → creates operator, wraps in `XComArg`
    - Many decorators available: `@task`, `@task.bash`, `@task.docker`, `@task.kubernetes`, etc.
    - `XComArg`: wrapper enabling automatic data passing and dependency inference
- **Asset** (object): Logical representation of data (table, model, file) used to establish dependencies, can be used imperatively (code-based) or declaratively (implicit definition via decorator). It is an abstract representation of data. You could create a Dag, with a task triggering your coffee machine, and define an asset with the name `my_morning_coffee`.
  - **Asset event**: Indicates that an asset has been updated
  - **Materialize**: Run the underlying function that updates the asset
- **@asset**: Declarative shortcut in form of a decorator, creates a Dag with a single task and one or more assets in one declaration
- **Time-driven scheduling**: You define a time-based schedule, and the Dag runs at that time, regardless of external factors. Examples: `@daily`, `0 30 * * *`.
- **Asset-aware scheduling**: With assets, Dags can have explicit, visible relationships based on assets, and Dags can be scheduled based on updates to these assets. Example: `schedule=Asset("selected_quotes")`.
- **Event-driven scheduling**: A subtype of data-aware scheduling where a Dag triggers when messages arrive in a message queue. It connects an AssetWatcher to an asset that monitors one or more triggers. Each trigger is an asynchronous Python process responsible for polling messages from the queue.

## Required accounts and access

### GitHub

- **GitHub**: Have your account ready to be able to fork the workshop repository during the process

### Astro trial

- **Free Astro Trial**: You'll create this during the workshop setup
- **No credit card required**: The trial provides everything needed for the workshop
- **Email access**: Ability to receive and verify email for account creation

### Development environment

- **Modern web browser**: Chrome, Firefox, Safari, or Edge (latest versions)
- **Stable internet connection**: Required for accessing cloud services and APIs
- **Local terminal access**: Command line interface for running CLI commands

### AWS account requirements

- **Active AWS account**
- **IAM permissions** for the following services:
  - Amazon SQS (Simple Queue Service)
  - Amazon Bedrock (for GenAI capabilities)
  - Basic IAM role and policy management

#### AWS service access

- **Amazon Bedrock model access**: May require requesting access to specific AI models
- **SQS queue creation**: Ability to create and manage SQS queues
- **AWS CLI or Console access**: For configuring services and monitoring

### Required software

- **Astro CLI**: Will be installed following provided instructions
- **Git**: For cloning the workshop repository
- **Web browser**: For accessing Astro IDE and Airflow UI

## Ready to begin?

Once you've verified all prerequisites, you're ready to start the workshop!

> [!IMPORTANT]
> All prerequisites confirmed? Let's move on to the Setup section to begin building your Airflow 3 environment!

# Module 0: Astro and Astro IDE

The final preparation step is to setup a **free** trial of Astro to run Airflow and the Astro IDE to write Dags. It is not necessary to understand all details of the Astro platform, but in a nutshell: Each customer has a dedicated Organization on Astro. One Organization can have multiple Workspaces (e.g. per team). A Workspace is a collection of Deployments. Each Workspace can have multiple Deployments. A Deployment is an Airflow environment hosted on Astro.

1. Create a [free trial of Astro](https://www.astronomer.io/lp/signup/?utm_source=conference&utm_medium=web&utm_campaign=reinvent-25).
   - After creating an account and logging in, choose `Start a Free Astro Trial` (click link Create Organization)
   - When being asked how you want to use Astro, choose Personal
   - Choose an Organization name and a Workspace name
   - When asked to select a template, click `None`. Leave all other settings and click `Create Deployment in Astro`. Note that you will not need this Deployment for this workshop, but you can use it for the remaining duration of your trial.
   - You should now see the UI of the Astro platform. Leave it for now, we'll come back to it in a few steps.
2. Install the free [Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli).
3. [Fork this repository](https://github.com/astronomer/devrel-public-workshops/fork). Make sure you uncheck the `Copy the main branch only` option when forking.

   ![Forking the repository](img/fork_repo.png)

4. Clone your fork. Get the URL by clicking on Code -> Copy to clipboard. Then run `git clone <url>`.
5. Run `git checkout airflow-3-reinvent` to switch to the airflow 3 branch.
6. Ensure you are authenticated to your Astro trial by running `astro login` in your terminal. It will prompt you to go to your browser to sign in.
7. Export your project to the Astro IDE by running `astro ide project export` in your terminal. Choose `y` to create a new project, and give your project a name when prompted. Your new Astro IDE project should automatically open in a browser.
8. To start Airflow, click the `Start test deployment` button. This will create a small Airflow Deployment for you to run your dags. It may take a few minutes to spin up.
9. To enable scheduled dag runs in your new Airflow Deployment, click on the drop down next to `Sync to test`, and click `Test Deployment Details`.

   ![Test deployment details](img/deployment-change-1.png)

   - Go to the `Environment` tab, click `Edit Deployment Variables`, and delete the `AIRFLOW__SCHEDULER__USE_JOB_SCHEDULE` variable.

   ![Env var](img/deployment-change-4.png)

10. Go back to the Astro IDE, and in the drop down next to `Sync to Test`, click on `Open Airflow`.

> [!NOTE]
> Environment ready! Proceed to the modules to start exploring Airflow.

# Module 1: Explore the Airflow UI and assets

Airflow 3 has a completely refreshed UI that is React-based and easier to navigate. In this exercise, you'll explore the new interface and understand the relationship between Dags and Assets.

## 1. Explore the home page

1. Once you have started Airflow, navigate to the **Home** page
2. Initially, there won't be much content, but this will change as you progress through the exercises

## 2. Navigate Dags and assets

1. Explore the **Dags** view to see the available workflows

> [!IMPORTANT]
> You will see 4 Dags in this view, all of them already activated. Compare those to the architecture diagram to get a better understanding of the functionality.

2. Check the schedule column and identify which Dag is triggered time-based, and which Dags are triggered asset-aware
3. Open the **Assets** view to understand data dependencies

> [!IMPORTANT]
> You will see 4 assets in this view. These are updated via the Dags you saw before.

4. Click on the `raw_zen_quotes` to open the asset graph, and explore how the Dags and assets are connected

## 3. Run Dags

1. **Run** the `raw_zen_quotes` Dag
2. Observe how all Dags are being triggered via their asset dependencies
3. Once all Dags finished successfully, open each Dag one by one, and open the recent run by clicking the bar in the grid view on the left or by clicking the latest run in the Runs tab

   ![Dag run view](img/dag_run_view.png)

4. Within the Dag runs, click on the tasks to see the logs
5. Specifically, check the task logs for the `create_personalized_newsletter` task in the `personalize_newsletter` Dag, it should show the generated newsletter

## 4. Explore UI features

Try out these new UI features:

1. **Switch themes**: Toggle between light mode and dark mode 😎
2. **Change language**: Try a different language from the `User` menu
3. **Navigation**: Notice how easy it is to navigate between different views

## 5. (Bonus) Trigger via asset events

Let us assume the `raw_zen_quotes` Dag takes a long time to finish, and we don't want to wait for it. In this case, we can also generate asset update events in the Airflow UI, without running the underlying function (materializing).

1. Navigate to the Assets view in the UI, click on the play button next to the `raw_zen_quotes` asset
2. Select Manual and add the following extra JSON:

   ```json
   {
      "run_date": "2025-12-04"
   }
   ```
   This is used in our implementation to determine for which day the newsletter is generated, and is also part of the final newsletter file name. Click on Create Event.

   ![Dag run view](img/create_asset_event.png)

3. Go back to the Dags view and see how the Dags are running, without `raw_zen_quotes` being executed. You will see 2 runs for each Dag except `raw_zen_quotes`.

# Module 2: Add human-in-the-loop

Airflow 3.1 introduced human-in-the-loop (HITL) operators, allowing manual intervention in automated workflows. In this exercise, you'll add an approval step for newsletter personalization.

1. In the **Astro IDE** code editor, open the `personalize_newsletter.py` file
2. Add the import at the top of the file:

   ```python
   from airflow.providers.standard.operators.hitl import ApprovalOperator
   ```

3. Add this operator to your Dag after the `create_personalized_newsletter` task:

   ```python
   approve_personalization = ApprovalOperator(
      task_id="approve_personalization",
      subject="Your task:",
      body="{{ ti.xcom_pull(task_ids='create_personalized_newsletter') }}",
      defaults="Approve", # other option: "Reject"
   )
   ```

4. Modify the task dependencies to include the approval step:

   ```python
   create_personalized_newsletter.expand(user=_get_weather_info) >> approve_personalization
   ```
   Make sure the approval task comes after `create_personalized_newsletter` in your workflow.

5. Save the file
6. Click `Sync to Test` in the upper right corner and wait for the sync to complete

_Switch back to the Airflow UI._

7. Run the `raw_zen_quotes` Dag again to trigger an end-to-end run
8. The workflow will pause at the approval step
9. Navigate to **Browse** → **Required Actions** in the Airflow UI

   The **Required Actions** view provides:
      - Instance-wide view of all pending approvals
      - Easy access to review content
      - Batch approval capabilities for multiple items

10. Open the pending action, review the newsletter content, and either **Approve** or **Reject** the results
11. Try to change the `body` of your `ApprovalOperator`. Change it to a multi-line-string and add Markdown as it will be rendered in the Airflow UI.

# Module 3: Use Dag versioning

Dag versioning is a new feature in Airflow 3 that tracks changes to your Dag code over time. In this exercise, you'll explore how versioning works and compare different versions of your Dags.

1. Navigate to the **Dags** view in the Airflow UI
2. Click on the `personalize_newsletter` Dag
3. Go to the **Graph** view
4. Click on **Options** in the top menu
5. Notice the **Dag Version** dropdown
6. Check how many versions are available in the dropdown, you should see multiple versions from the changes made in the previous module

> [!NOTE]
> 💡 Why do you have multiple versions? Each time you modified the Dag structure (adding the HITL operator), Airflow created a new version to track these changes. But only, if a Dag run is between the changes.

7. Toggle between different versions using the dropdown
8. Observe the changes in the **Graph** view:
   - **Version 1**: Original Dag structure
   - **Version 2**: After adding the HITL operator
9. Navigate to the **Code** tab
10. Use the version dropdown to toggle between different versions, and observe the code differences

# Module 4: GenAI, event-driven scheduling, and some sci-fi

This module demonstrates a more realistic version of the newsletter pipeline using Amazon Bedrock for GenAI personalization and SQS for event-driven scheduling.

We will also spice up the newsletter by using the user's favorite sci-fi character.

## Prerequisites

> [!IMPORTANT]
> This exercise requires an AWS account with access to SQS and Amazon Bedrock

You'll need:
- AWS account with appropriate permissions
- Access to Amazon Bedrock (may require model access requests)
- SQS queue creation permissions

## 1. Update the Dag code

1. Navigate to `dags/personalize_newsletter.py`
2. Replace the entire contents with the code from `solutions/personalize_newsletter_genai.py`

## 2. Configure environment variables

1. Copy the contents of `.env_example` to `.env`
2. Update the `AIRFLOW_CONN_AWS_DEFAULT` with your AWS credentials:

   ```bash
   AIRFLOW_CONN_AWS_DEFAULT=aws://YOUR_ACCESS_KEY:YOUR_SECRET_KEY@/?region_name=us-east-1
   ```

> [!IMPORTANT]
> Add the `.env` file to `.gitignore` to avoid pushing credentials to GitHub

## 3. Create SQS queue

1. Log into your AWS Console
2. Navigate to **Amazon SQS**
3. Create a new queue (standard queue is sufficient)
4. Copy the queue URL
5. Add the URL to your `.env` file:

   ```bash
   SQS_QUEUE_URL=https://sqs.us-east-1.amazonaws.com/123456789012/your-queue-name
   ```

## 4. Configure bedrock access

1. In AWS Console, navigate to **Amazon Bedrock**
2. Go to **Model access** in the left sidebar
3. Request access to a model (e.g., Claude or Titan models)
4. Wait for approval (this may take a few minutes)

## 5. Restart Airflow

Restart your Airflow test deployment to load the new environment variables

## 6. Test event-driven scheduling

1. Navigate to your SQS queue in the AWS Console
2. Send a message with this JSON format:

   ```json
   {
   "id": 300,
   "name": "Your Name",
   "location": "Your City",
   "motivation": "Your motivational theme",
   "favorite_sci_fi_character": "Your favorite character"
   }
   ```

3. The `personalize_newsletter` Dag should automatically start running
4. Monitor the Dag execution in the Airflow UI

## 7. Review Results

1. Check the Dag execution logs
2. Review your personalized newsletter in the `include/newsletters` folder
3. Notice how the GenAI integration creates more sophisticated personalization

## 8. (Bonus) Adjust the Prompt

Notice how the prompt in the code uses the user's favorite sci‑fi character? Have some fun—adjust the prompt and see how unique a newsletter you can create.

> [!IMPORTANT]
> Module complete! You've now experienced the full power of Airflow 3's new features.
