---
title: "Module 2: Use Assets"
weight: 20
---

# Module 2: Use Assets

Assets are the next evolution of Airflow datasets, representing collections of logically related data. In this exercise, you'll complete the ETL pipeline by creating a new asset and implementing asset-based scheduling.

## Learning Objectives

- Create and configure Assets in Airflow 3
- Implement asset-oriented scheduling
- Complete the newsletter ETL pipeline
- Understand the difference between asset-oriented and task-oriented DAGs

## Background

In your current environment, you have:
- **Asset-oriented DAGs**: `raw_zen_quotes`, `selected_quotes` 
- **Task-oriented DAG**: `personalize_newsletter`
- **Assets**: `raw_zen_quotes`, `selected_quotes`, `personalized_newsletters`

The ETL pipeline creates a newsletter template by retrieving data from an API, formatting it, and bringing it together. Currently, the "load" step is missing.

## Steps

### 1. Open the Code Editor

1. Go back to the **Astro IDE**
2. Open the `create_newsletter.py` file in the code editor

### 2. Create the Formatted Newsletter Asset

Create a new asset called `formatted_newsletter` by adding this code to `create_newsletter.py`:

```python
@asset(
    schedule=[Asset("selected_quotes")]
)
def formatted_newsletter(context):
    """
    Formats the newsletter.
    """
    from airflow.io.path import ObjectStoragePath

    object_storage_path = ObjectStoragePath(
       f"{OBJECT_STORAGE_SYSTEM}://{OBJECT_STORAGE_PATH_NEWSLETTER}",
       conn_id=OBJECT_STORAGE_CONN_ID,
    )

    selected_quotes = context["ti"].xcom_pull(
          dag_id="selected_quotes",
          task_ids=["selected_quotes"],
          key="return_value",
          include_prior_dates=True,
       )[0]

    # fetch the run date of the pipeline
    run_date = context["triggering_asset_events"][Asset("selected_quotes")][0].extra[
       "run_date"
    ]

    newsletter_template_path = object_storage_path / "newsletter_template.txt"

    newsletter_template = newsletter_template_path.read_text()

    newsletter = newsletter_template.format(
       quote_text_1=selected_quotes["short_q"]["q"],
       quote_author_1=selected_quotes["short_q"]["a"],
       quote_text_2=selected_quotes["median_q"]["q"],
       quote_author_2=selected_quotes["median_q"]["a"],
       quote_text_3=selected_quotes["long_q"]["q"],
       quote_author_3=selected_quotes["long_q"]["a"],
       date=run_date,
    )

    date_newsletter_path = object_storage_path / f"{run_date}_newsletter.txt"

    date_newsletter_path.write_text(newsletter)

    # attach the run date to the asset event
    yield Metadata(Asset("formatted_newsletter"), {"run_date": run_date})
```

### 3. Configure Asset Scheduling

The asset should be scheduled to run when the `selected_quotes` asset is available. Notice the `schedule=[Asset("selected_quotes")]` parameter in the decorator.

### 4. Update Personalize Newsletter Scheduling

1. Open the `personalize_newsletter.py` file
2. The DAG is currently set to run daily, but it fails if the `formatted_newsletter` asset hasn't been updated
3. Change the schedule to run when the right data is available:

```python
schedule=[Asset("formatted_newsletter")]
```

### 5. Personalize User Data

1. Navigate to the `include/user_data` folder
2. Update `user_100.json` to include your own name and location
3. **Bonus**: Try adding additional user files and see how it affects the pipeline

### 6. Deploy Changes

1. Save all your changes
2. Click `Sync to Test` in the upper right corner
3. This will send your changes to the test Deployment

::alert[Syncing may take a few minutes]{type="info"}

### 7. Test the Complete Pipeline

1. Use the **reparse dag** function in the UI for the `personalize_newsletter` dag
2. Run your full pipeline by **materializing** the `raw_zen_quotes` DAG
3. This should trigger all downstream assets and tasks to complete

### 8. Verify the Asset Graph

1. Check out your new asset graph in the Airflow UI
2. You should see your complete ETL pipeline with three DAGs and three assets
3. Observe how the dependencies flow through the system

## Troubleshooting

::alert[The open-meteo weather API is occasionally flaky. If you get a failure in your `get_weather_info` task, let it retry - it will usually resolve.]{type="warning"}

If you added additional users, you may need to implement a pool to avoid hitting API rate limits. Ask your workshop leader for help with this.

## Key Concepts

After completing this exercise, you should understand:

- How to create and configure Assets
- The difference between asset-oriented and task-oriented DAGs  
- How asset-based scheduling creates automatic data dependencies
- How to pass metadata between assets using `Metadata` and `yield`

## Next Steps

In Module 3, you'll add human-in-the-loop functionality to create approval workflows.

::alert[Pipeline complete! Ready to add human approval workflows in Module 3?]{type="success"}