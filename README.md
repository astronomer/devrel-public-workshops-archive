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

## Key benefits

- **Fully managed**: No infrastructure management required
- **Enterprise security**: SOC 2 Type II certified with advanced security features
- **Scalable**: Auto-scaling workers and flexible resource allocation
- **Developer experience**: Enhanced IDE, CI/CD integration, and debugging tools
- **Observability**: Advanced monitoring, alerting, and lineage tracking

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
    - Many decorators available: `@task`, `@task.bash`, `@tak.docker`, `@task.kubernetes`, etc.
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

- **Web browser**: For accessing Astro IDE and Airflow UI

## Ready to begin?

Once you've verified all prerequisites, you're ready to start the workshop!

> [!IMPORTANT]
> All prerequisites confirmed? Let's move on to the [modules](modules.md) to begin building your Airflow 3 environment!

➡️ Open [modules.md](modules.md) to continue!
