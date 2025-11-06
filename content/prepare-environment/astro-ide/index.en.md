---
title: "Astro and Astro IDE"
weight: 30
---

# Astro and Astro IDE

The final preparation step is to setup a **free** trial of Astro to run Airflow and the Astro IDE to write Dags. It is not necessary to understand all details of the Astro platform, but in a nutshell: Each customer has a dedicated Organization on Astro. One Organization can have multiple Workspaces (e.g. per team). A Workspace is a collection of Deployments. Each Workspace can have multiple Deployments. A Deployment is an Airflow environment hosted on Astro.

1. Create a [free trial of Astro](https://www.astronomer.io/lp/signup/?utm_source=conference&utm_medium=web&utm_campaign=reinvent-25).
   - After creating an account and logging in, choose `Start a Free Astro Trial` (click link Create Organization)
   - When being asked how you want to use Astro, choose Personal
   - Choose an Organization name and a Workspace name
   - When asked to select a template, click `None`. Leave all other settings and click `Create Deployment in Astro`. Note that you will not need this Deployment for this workshop, but you can use it for the remaining duration of your trial.
   - You should now see the UI of the Astro platform. Leave it for now, we'll come back to it in a few steps.
2. Install the free [Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli).
3. [Fork this repository](https://github.com/astronomer/devrel-public-workshops/fork). Make sure you uncheck the `Copy the main branch only` option when forking.

   ![Forking the repository](/static/img/fork_repo.png)

4. Clone your fork. Get the URL by clicking on Code -> Copy to clipboard. Then run `git clone <url>`.
5. Run `git checkout airflow-3-reinvent` to switch to the airflow 3 branch.
6. Ensure you are authenticated to your Astro trial by running `astro login` in your terminal. It will prompt you to go to your browser to sign in.
7. Export your project to the Astro IDE by running `astro ide project export` in your terminal. Choose `y` to create a new project, and give your project a name when prompted. Your new Astro IDE project should automatically open in a browser.
8. To start Airflow, click the `Start test deployment` button. This will create a small Airflow Deployment for you to run your dags. It may take a few minutes to spin up.
9. To enable scheduled dag runs in your new Airflow Deployment, click on the drop down next to `Sync to test`, and click `Test Deployment Details`.

   ![Test deployment details](/static/img/deployment-change-1.png)

   - Go to the `Environment` tab, click `Edit Deployment Variables`, and delete the `AIRFLOW__SCHEDULER__USE_JOB_SCHEDULE` variable.

   ![Env var](/static/img/deployment-change-4.png)

10. Go back to the Astro IDE, and in the drop down next to `Sync to Test`, click on `Open Airflow`.

::alert[Environment ready! Proceed to the modules to start exploring Airflow.]{type="success"}
