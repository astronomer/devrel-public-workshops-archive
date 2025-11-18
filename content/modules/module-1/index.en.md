---
title: "Module 1: Explore the New UI"
weight: 10
---

# Module 1: Explore the Airflow UI and Assets

Airflow 3 has a completely refreshed UI that is React-based and easier to navigate. In this exercise, you'll explore the new interface and understand the relationship between Dags and Assets.

## Learning Objectives

- Navigate the new Airflow 3 React-based UI
- Understand the relationship between Dags and Assets
- Trigger Dags using different methods
- Explore the enhanced user experience features

## Background

The new UI provides improved navigation, better performance, and enhanced visualization of workflows. You'll notice significant improvements in how data dependencies are displayed and managed.

## Tasks

### 1. Explore the Home Page

1. Once you have started Airflow, navigate to the **Home** page
2. Initially, there won't be much content, but this will change as you progress through the exercises

### 2. Navigate Dags and Assets

1. Explore the **Dags** view to see the available workflows

::alert[You will see 4 Dags in this view, all of them already activated. Compare those to the architecture diagram to get a better understanding of the functionality.]{type="info"}

2. Check the schedule column and identify which Dag is triggered time-based, and which Dags are triggered asset-aware
3. Open the **Assets** view to understand data dependencies

::alert[You will see 4 assets in this view. These are updated via the Dags you saw before.]{type="info"}

4. Click on the `raw_zen_quotes` to open the asset graph, and explore how the Dags and assets are connected

### 3. Run Dags

1. **Run** the `raw_zen_quotes` Dag
2. Observe how all Dags are being triggered via their asset dependencies
3. Once all Dags finished successfully, open each Dag one by one, and open the recent run by clicking the bar in the grid view on the left or by clicking the latest run in the Runs tab

   ![Dag run view](/static/img/dag_run_view.png)

4. Within the Dag runs, click on the tasks to see the logs
5. Specifically, check the task logs for the `create_personalized_newsletter` task in the `personalize_newsletter` Dag, it should show the generated newsletter

### 4. Explore UI Features

Try out these new UI features:

1. **Switch themes**: Toggle between light mode and dark mode 😎
2. **Change language**: Try a different language from the `User` menu
3. **Navigation**: Notice how easy it is to navigate between different views

### 5. (Bonus) Trigger via Asset Events

Let us assume the `raw_zen_quotes` Dag takes a long time to finish, and we don't want to wait for it. In this case, we can also generate asset update events in the Airflow UI, without running the underlying function (materializing).

1. Navigate to the Assets view in the UI, click on the play button next to the `raw_zen_quotes` asset
2.  Select Manual and add the following extra JSON:
   ```json
   {
      "run_date": "2025-12-04"
   }
   ```
   This is used in our implementation to determine for which day the newsletter is generated, and is also part of the final newsletter file name. Click on Create Event.

   ![Dag run view](/static/img/create_asset_event.png)
3. Go back to the Dags view and see how the Dags are running, without `raw_zen_quotes` being executed. You will see 2 runs for each Dag except `raw_zen_quotes`.

## Key Observations

After completing this exercise, you should understand:

- How the new UI improves workflow visualization
- The relationship between Dags and Assets
- Different methods for triggering workflows
- How asset-based scheduling creates automatic dependencies

## Next Steps

In the next module, you'll add human-in-the-loop functionality to create approval workflows.

::alert[Ready to add human approval workflows in the next module?]{type="success"}
