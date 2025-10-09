# 🚀 Productionising dbt Core with Airflow

Welcome to the official repository for Astronomer’s [**Productionising dbt Core with Airflow**](https://airflowsummit.org/sessions/2025/productionising-dbt-core/) workshop, delivered at **Airflow Summit 2025**.

This hands-on, 2.5-hour workshop introduces key features of [**Astronomer Cosmos**](https://github.com/astronomer/astronomer-cosmos), a powerful library for orchestrating dbt Core projects with Airflow.

> 🔗 [**Workshop Slides**](https://docs.google.com/presentation/d/1QlOrxCoPUtmrBceY_yZAyhAEg7qZVUd__wzje1gNnKw/edit?slide=id.g3878061f0be_0_170)

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

- **[Astro](https://www.astronomer.io)** – a managed Airflow platform (free trial available)
- **Astro CLI** – to manage projects locally
- **Astro IDE** – a web-based development environment

Follow the steps below to get started:

### ✅ Step 1: Create a Free Astro Trial

1. Go to [this special signup link](https://www.astronomer.io/lp/signup/afsummit/?utm_campaign=event-airflow-summit-10-25) to create a free trial.
2. Follow the prompts:
   - Choose **"Personal"** as usage type.
   - Create an **Organization** and a **Workspace**.
   - Skip the deployment setup for now by clicking **"None"**, then **"Create Deployment in Astro"** (you won’t need it for the workshop).

---

### ✅ Step 2: Install Astro CLI

Install the Astro CLI on your local machine using the instructions here:  
🔗 [Install Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli)

---

### ✅ Step 3: Clone the Workshop Repository

Clone this repo and switch to the correct branch:

```bash
git clone https://github.com/astronomer/devrel-public-workshops.git
cd devrel-public-workshops
git checkout dbt-in-airflow
```

---

### ✅ Step 4: Log Into Astro

Run the following command to authenticate the Astro:

```bash
astro login cloud.astronomer.io
```

- This will open your browser to complete login.
- Make sure to select the organization you created during signup.

### ✅ Step 5: Update BigQuery dataset name 

- Update your BigQuery dataset name in dbt/jaffle_shop/profiles.yml

### ✅ Step 6: Update GCP Service Account Key

- Add your GCP Service Account Key in include/key.json

### ✅ Step 7: Export Project to Astro IDE

Use the following command to export the current project to Astro IDE:

```bash
astro ide project export
```

- When prompted:
    - Select "Yes" to create a new project
    - Provide a project name of your choice
- The Astro IDE will open in your browser with the new project

### ✅ Step 8: Start a Test Deployment

1. In Astro IDE, click the "Start test deployment" button
2. This will spin up a Airflow deployment (takes a few minutes)
3. When ready, click the dropdown next to "Sync to test" and select "Test Deployment Details"

### ✅ Step 9: Open Airflow UI

- Go to Astro UI
- Click on Deployment 
- Select "Open Airflow"

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
