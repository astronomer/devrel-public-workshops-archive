---
title: "Use Case & Architecture"
weight: 10
---

# Use Case & Architecture

This workshop demonstrates Airflow 3's capabilities through building a **personalized newsletter system** that showcases modern data orchestration patterns.

![Demo architecture diagram](/static/img/etl_genai_newsletter_architecture_diagram_bedrock.png)

## Workshop Use Case

The use case for this workshop is using Airflow to create an automated and personalized newsletter. The end-to-end solution includes two different processes, interacting via assets:

1. The `create_newsletter` process retrieves quotes from the ZenQuotes API, and prepares a newsletter based on a template. It consists of three `@asset` decorated functions, which means, three Dags with a single task each implementing the business logic, communicating via assets. You will learn more about assets while exploring this documentation.
2. The `personalize_newsletter` pipeline personalizes the newsletter based on user input. It's a task-oriented pipeline, which is taking the user's location, and the reader's favorite sci-fi character into account. This is used with a LLM through Amazon Bedrock to write content in the voice/style of the sci-fi character they chose.

## Airflow 3 Features Demonstrated

### Assets (Data-Aware Scheduling)
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

::alert[More information: [Introduction to the Airflow UI](https://www.astronomer.io/docs/learn/airflow-ui)]{type="info"}

Learn more about the UI in the .

### Human-in-the-Loop Operators
- Manual intervention points in automated workflows
- Approval/rejection workflows with rich content display
- Batch processing of approval requests

Check the  guide for more details and an overview of all available options.

::alert[More information: [Human-in-the-loop workflows with Airflow](https://www.astronomer.io/docs/learn/airflow-human-in-the-loop)]{type="info"}

### Built-in Backfills
- UI-driven historical data processing (can also be triggered via API and CLI)
- Progress tracking and monitoring
- Flexible reprocessing options

::alert[More information: [Rerun Airflow Dags and tasks](https://www.astronomer.io/docs/learn/rerunning-dags#backfill)]{type="info"}

### DAG Versioning
- Automatic tracking of structural changes
- Visual comparison between versions
- Code history and change management

::alert[More information: [Dag Versioning and Dag Bundles](https://www.astronomer.io/docs/learn/airflow-dag-versioning)]{type="info"}

### Event-Driven Scheduling
- SQS integration for real-time triggers
- Dynamic workflow execution based on external events
- Scalable processing of user requests

::alert[More information: [Event-driven scheduling](https://www.astronomer.io/docs/learn/airflow-event-driven-scheduling)]{type="info"}

## Technology Stack

### Core Platform
- **[Apache Airflow 3](https://airflow.apache.org/)**: Latest workflow orchestration features
- **[Astro IDE](https://www.astronomer.io/product/ide/)**: Author, test, and release production-ready DAGs from your browser
- **[Astro](https://www.astronomer.io/product/)**: Managed Airflow platform
- **[Python](https://www.python.org/)**: Primary development language
- **[Git](https://git-scm.com/)**: Version control and collaboration

### External Integrations
- **[ZenQuotes API](https://zenquotes.io/)**: Motivational quote source
- **[Open-Meteo API](https://open-meteo.com/)**: Weather data provider
- **[Amazon SQS](https://aws.amazon.com/sqs/)**: Event-driven messaging
- **[Amazon Bedrock](https://aws.amazon.com/bedrock/)**: GenAI capabilities

This architecture provides a comprehensive foundation for understanding modern data orchestration while demonstrating practical, real-world applications of Airflow 3's enhanced capabilities.
