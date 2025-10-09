# 🚀 Productionising dbt Core with Airflow

Welcome to the official repository for Astronomer’s [**Productionising dbt Core with Airflow**](https://airflowsummit.org/sessions/2025/productionising-dbt-core/) workshop, delivered at **Airflow Summit 2025**.

This hands-on, 2.5-hour workshop introduces key features of [**Astronomer Cosmos**](https://github.com/astronomer/astronomer-cosmos), a powerful library for orchestrating dbt Core projects with Airflow.

> 🔗 [**Workshop Slides**](https://docs.google.com/presentation/d/1QlOrxCoPUtmrBceY_yZAyhAEg7qZVUd__wzje1gNnKw/edit?slide=id.g3878061f0be_0_170)


During the workshop, we strongly recommend attendees to use the recently published eBook [Orchestrating dbt with Airflow using Cosmos](https://www.astronomer.io/ebook/orchestrating-dbt-with-airflow-using-cosmos/). You can find more examples of how to use Cosmos in the [eBook companion repository](https://github.com/astronomer/cosmos-ebook-companion).

---

## 🎯 Workshop Objectives

By the end of this workshop, you'll be able to:

- Run dbt Core projects in Airflow using different orchestration strategies
- Understand how Cosmos simplifies dbt orchestration
- Customize DAG generation and dbt execution modes
- Manage secrets and credentials securely
- Scale dbt workloads effectively with Airflow

**Key topics include:**

- Running dbt via Cosmos
- Database credential management
- Execution modes and dependency management
- DAG customization (selectors, tests, sources)
- Integrating dbt Docs
- Running dbt at scale with deferrable operators

---

## 🛠️ Setup Instructions

To participate in the workshop, you’ll use:

Follow the steps below to get started:

### ✅ Step 1: Clone this repo

Clone this repo and switch to the correct branch:

```bash
git clone https://github.com/astronomer/devrel-public-workshops.git
cd devrel-public-workshops
git checkout dbt-in-airflow
```

### ✅ Step 2: Prepare your Python virtual enviroment

We recommend using Python 3.12:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ✅ Step 3: Export environment variables

Before exporting, replace `<your dataset>` by your dataset and `<absolute path to your keyfile>` by the absolute path to your keyfile.
```
export AIRFLOW__CORE__LOAD_EXAMPLES=False

export no_proxy='*'
export PYTHONFAULTHANDLER=true
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES

export BIGQUERY_DATASET=<your dataset>
export GCP_PROJECT_ID=airflowintegrations
export AIRFLOW_CONN_BIGQUERY_DEFAULT='{"conn_type":"google_cloud_platform","extra":{"dataset":"<your dataset>>", "project":"airflowintegrations","key_path":"<absolute path to your keyfile>"}}'
```

### ✅ Step 4: Attempt to run a first DAG

```bash
airflow dags test 1_bashoperator
```

### ✅ Step 5: Attempt to use Airflow standalone

```bash
AIRFLOW_HOME=`pwd` airflow standalone
```

## 🧪 Workshop Structure

Each exercise follows this format:
- Introduction (~3 minutes)
- Hands-on Exercise (~12 minutes)
- Solution Review (~5 minutes)

Don’t worry if you don’t finish each exercise – you’ll still be able to follow the rest of the workshop.


## 📁 dbt Projects Used

We’ll use the following dbt project for the exercises:

- [Jaffle Shop](https://github.com/astronomer/devrel-public-workshops/tree/dbt-in-airflow/dbt/jaffle_shop)

You’re encouraged to explore with your own dbt projects as well!
