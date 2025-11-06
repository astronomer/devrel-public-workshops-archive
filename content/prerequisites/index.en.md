---
title: "Prerequisites"
weight: 15
---

# Prerequisites

Before starting this workshop, please ensure you have the following prerequisites in place.

## Required Knowledge

### Technical Background
- **Basic Python programming**: Understanding of Python syntax, functions, and basic data structures
- **Command line familiarity**: Comfortable using terminal/command prompt for basic operations
- **Git basics**: Understanding of git clone, checkout, and basic version control concepts

### Apache Airflow Concepts
- **Dags (directed acyclic graphs)**: Understanding of workflow concepts and task dependencies
- **Tasks and Operators**: Basic knowledge of how Airflow executes work
- **Scheduling**: Familiarity with cron expressions and time-based scheduling concepts

::alert[If you're new to Airflow, we recommend reviewing the [introduction to Apache Airflow®](https://www.astronomer.io/docs/learn/intro-to-airflow) before starting this workshop.]{type="info"}

#### TL;DR

* **Dag**: Your entire pipeline from start to finish, consisting of one or more tasks
* **Task**: A unit of work within your pipeline
* **Operators and decorators**: The template/class that defines what work a task does, serving as the building blocks of pipelines
  * Traditional: `task = PythonOperator(...)` → returns operator directly
  * TaskFlow: `@task def my_task(): ...` → creates operator, wraps in `XComArg`
    * Many decorators available: `@task`, `@task.bash`, `@task.docker`, `@task.kubernetes`, etc.
    * `XComArg`: wrapper enabling automatic data passing and dependency inference
* **Asset** (object): Logical representation of data (table, model, file) used to establish dependencies, can be used imperatively (code-based) or declaratively (implicit definition via decorator). It is an abstract representation of data. You could create a Dag, with a task triggering your coffee machine, and define an asset with the name `my_morning_coffee`.
  * **Asset event**: Indicates that an asset has been updated
  * **Materialize**: Run the underlying function that updates the asset
* **@asset**: Declarative shortcut in form of a decorator, creates a Dag with a single task and one or more assets in one declaration
* **Time-driven scheduling**: You define a time-based schedule, and the Dag runs at that time, regardless of external factors. Examples: `@daily`, `0 30 * * *`.
* **Asset-aware scheduling**: With assets, Dags can have explicit, visible relationships based on assets, and Dags can be scheduled based on updates to these assets. Example: `schedule=Asset("selected_quotes")`.
* **Event-driven scheduling**: A subtype of data-aware scheduling where a Dag triggers when messages arrive in a message queue. It connects an AssetWatcher to an asset that monitors one or more triggers. Each trigger is an asynchronous Python process responsible for polling messages from the queue.

## Required Accounts and Access

### GitHub
- **GitHub**: Have your account ready to be able to fork the workshop repository during the process

### Astro Trial
- **Free Astro Trial**: You'll create this during the workshop setup
- **No credit card required**: The trial provides everything needed for the workshop
- **Email access**: Ability to receive and verify email for account creation

### Development Environment
- **Modern web browser**: Chrome, Firefox, Safari, or Edge (latest versions)
- **Stable internet connection**: Required for accessing cloud services and APIs
- **Local terminal access**: Command line interface for running CLI commands

### AWS Account Requirements
- **Active AWS account**
- **IAM permissions** for the following services:
  - Amazon SQS (Simple Queue Service)
  - Amazon Bedrock (for GenAI capabilities)
  - Basic IAM role and policy management

#### AWS Service Access
- **Amazon Bedrock model access**: May require requesting access to specific AI models
- **SQS queue creation**: Ability to create and manage SQS queues
- **AWS CLI or Console access**: For configuring services and monitoring

### Required Software

- **Astro CLI**: Will be installed following provided instructions
- **Git**: For cloning the workshop repository
- **Web browser**: For accessing Astro IDE and Airflow UI

## Ready to Begin?

Once you've verified all prerequisites, you're ready to start the workshop!

::alert[All prerequisites confirmed? Let's move on to the Setup section to begin building your Airflow 3 environment!]{type="success"}
