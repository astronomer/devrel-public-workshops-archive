# GenAI with Airflow Workshop

Welcome! 🚀

Productionizing GenAI applications often relies on multi-stage, complex pipelines that manage data ingestion, creation of vector embeddings, vector storage, querying, and response construction. These pipelines need to run reliably, scale efficiently, and recover from failure without manual intervention. Apache Airflow, a leading open-source orchestration framework, provides the structure and flexibility required to operationalize GenAI workloads with production-grade reliability. 

In this workshop, you'll learn the basics of using Airflow to build and orchestrate end-to-end GenAI workflows. 


## Introduction

This workshop explores using Airflow to orchestrate GenAI workflows through the lens of a Retrieval-Augmented Generation (RAG) use case: a book recommendation system that embeds book descriptions, loads them into a vector database, queries them based on user input, and provides LLM-generated summaries. You’ll learn how to implement this process with Airflow Dags, and make use of foundational orchestration features like scheduling, task dependency management, and parallel execution. You will also learn how to use the [Airflow AI SDK](https://github.com/astronomer/airflow-ai-sdk) to easily interact with large language models from your pipelines. 

Set up your environment by following the instructions in the [Setup](#setup) section below. All Dags in this repository can be run locally using open source tools, including Airflow and Weaviate. There are also optional exercises that require an OpenAI API key.

Sample solutions for Dag-writing related exercises can be found in the [`solutions/`](/solutions/) folder of the repo.

### Setup

To set up a local Airflow environment you have two options, you can either use the Astro CLI or GitHub Codespaces.

#### Option 1: Astro CLI

1. Make sure you have [Docker](https://docs.docker.com/get-docker/) or Podman installed and running on your machine.
2. Install the free [Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli).
3. Fork this repository and clone it to your local machine. Make sure you uncheck the `Copy the main branch only` option when forking.

   ![Forking the repository](img/fork_repo.png)

4. Clone the repository and run `git checkout genai-with-airflow` to switch to the correct branch.
5. Create a new file called `.env` in the root directory. Copy the contents of the `.env_example` file into `.env`. If you have an OpenAI API key, replace `<your-openai-api-key>` with it. Save the file.
6. Run `astro dev start` in the root of the cloned repository to start the Airflow environment.
7. Access the Airflow UI at `localhost:8080` in your browser. Log in using `admin` as both the username and password.

#### Option 2: GitHub Codespaces

If you can't install the CLI, you can run the project from your forked repo using GitHub Codespaces.

1. Fork this repository. Make sure you uncheck the `Copy the main branch only` option when forking.

   ![Forking the repository](img/fork_repo.png)

2. Make sure you are on the `genai-with-airflow` branch.
3. Create a new file called `.env` in the root directory. Copy the contents of the `.env_example` file into `.env`. If you have an OpenAI API key, replace `<your-openai-api-key>` with it. Save the file.
4. Click on the green "Code" button and select the "Codespaces" tab. 
5. Click on the 3 dots and then `+ New with options...` to create a new Codespace with a configuration, make sure to select a Machine type of at least `4-core`.

   ![Start GH Codespaces](img/start_codespaces.png)

6. Run `astro dev start -n --wait 5m` in the Codespaces terminal to start the Airflow environment using the Astro CLI. This can take a few minutes.

   ![Start the Astro CLI in Codespaces](img/codespaces_start_astro.png)

   Once you see the following printed to your terminal, the Airflow environment is ready to use:

   ```text
   ✔ Project image has been updated
   ✔ Project started
   ➤ Airflow UI: http://localhost:8080
   ➤ Postgres Database: postgresql://localhost:5435/postgres
   ➤ The default Postgres DB credentials are: postgres:postgres
   ```

7. Once the Airflow project has started, access the Airflow UI by clicking on the Ports tab and opening the forward URL for port `8080`.

> [!TIP]
> If when accessing the forward URL you get an error like `{"detail":"Invalid or unsafe next URL"}`, you will need to modify the forwarded URL. Delete everything forward of `next=....` (this should be after `/login?`, ). The URL will update, adn then remove `:8080`, so your URL should endd in `.app.github.dev`

8. Log into the Airflow UI using `admin` as both the username and password. It is possible that after logging in you see an error, in this case you have to open the URL again from the ports tab.

# Exercises

After you have Airflow running locally, complete these exercises to get more familiar with how to turn GenAI prototypes into production-ready pipelines.

## Exercise 1: Explore the Airflow UI

Airflow 3 has a modern, React-based UI that is often the first stop to monitor what's going on in your pipelines. Once you have started Airflow, explore the new UI to develop your workflow. For more background on the Airflow UI, see [An Introduction to the Airflow UI](https://www.astronomer.io/docs/learn/airflow-ui).

1. Review the new Home page. There won't be much here to start, but you'll change that momentarily!
2. Explore the Dags and Assets tabs. See if you can get an understanding of the relationship between the DAGs in the environment so far. What dependencies currently exist?
3. Switch between light mode and dark mode 😎
4. Try a different language from the User menu.

## Exercise 2: Run the RAG pipeline

In the previous exercise, you explored the UI and saw that in your current Airflow environment, you have two Dags (`fetch_data`, and `query_data`). Conceptually, each Dag is a data pipeline: `fetch_data` is gathers data from a couple of text files in your include directory, creates a Weaviate collection to store them, creates vector embeddings, and loads them to the vector db. `query_data` searches the vector db for a book based on the input you provide.

1. From the Dags page, unpause both Dags. `fetch_data` should run automatically, `query_data` should be triggered afterwards.
2. Review the `fetch_data` Dag in more detail by looking at the grid and graph views. See if you can get an understanding of what the tasks in this Dag are doing. It can be helpful to look at the code for the Dag, which is shown in the UI (though you can't update the code here)!
3. Now look at the `query_data` Dag in more detail. When it was triggered automatically, it ran with the default input, which is "A philosophical book". Trigger the Dag manually, and input a different genre of book into the `query_str` parameter.
4. Once the Dag has completed, check the task logs for the `search_vector_db_for_a_book` task to see what book was recommended. 

## Exercise 3: Review features for running in production

Airflow has many features that make it ideal for orchestrating data pipelines of all kinds, including GenAI workflows. Let's take a look at some of those used in this example!

1. First, let's look at the schedules for these Dags. When will `fetch_data` run? 
   You also will have noticed in Exercises 1 and 2 that when you trigger `fetch_data`, `query_data` runs automatically afterwards. This is because there's no sense querying data that doesn't exist, so it doesn't make sense to use a time-based schedule for  `query_data`. Instead, we schedule it using an asset, so it only runs when the data it needs is available. For more on assets, see [our guide](https://www.astronomer.io/docs/learn/airflow-datasets).
2. Another great feature of Airflow is the ability to dynamically adapt your pipelines at runtime. Take a look at the graph of the `fetch_data` Dag. You'll see that two of the tasks -  `transform_book_description_files` and `create_vector_embeddings` - have brackets after the task name `[0]`. This means the tasks are dynamically mapped, so copies of them will be created based when the Dag runs based on upstream input. Add a new file in the `include/data/` directory called `book_descriptions_3.txt`. For contents of the file, you can either copy from `book_descriptions_2.txt` (duplicates are not a problem here), or you can add you own books in the same format! Save the file, and then rerun the `fetch_data` Dag. See how the mapped instances changed now that there is a new file. For more on dynamic task mapping, see [our guide](https://www.astronomer.io/docs/learn/dynamic-tasks).
3. 


## (Optional) Exercise 4: Add an LLM task

> [!Note]
> This task requires an OpenAI API Key. If you don't have one, it's okay to skip this exercise and only watch the demo.