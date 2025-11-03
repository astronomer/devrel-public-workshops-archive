---
title: "Module 1: Explore the New UI"
weight: 10
---

# Module 1: Explore the New UI

Airflow 3 has a completely refreshed UI that is React-based and easier to navigate. In this exercise, you'll explore the new interface and understand the relationship between DAGs and Assets.

## Learning Objectives

- Navigate the new Airflow 3 React-based UI
- Understand the relationship between DAGs and Assets
- Trigger DAGs using different methods
- Explore the enhanced user experience features

## Background

The new UI provides improved navigation, better performance, and enhanced visualization of workflows. You'll notice significant improvements in how data dependencies are displayed and managed.

## Steps

### 1. Explore the Home Page

1. Once you have started Airflow, navigate to the **Home** page
2. Initially, there won't be much content, but this will change as you progress through the exercises

### 2. Navigate DAGs and Assets

1. Explore the **DAGs** tab to see the available workflows
2. Click on the **Assets** tab to understand data dependencies
3. Try to identify the relationship between the DAGs in the environment

::alert[Look for dependencies between `raw_zen_quotes`, `selected_quotes`, and `personalize_newsletter` DAGs]{type="info"}

### 3. Unpause and Run DAGs

1. **Unpause** the `raw_zen_quotes` and `selected_quotes` DAGs
2. **Run** the `raw_zen_quotes` DAG using one of these methods:
   - Trigger the DAG directly
   - Create an asset event

::expand[What's the difference between triggering a DAG vs creating an asset event?]{header="💡 Think About It"}
When you trigger a DAG directly, you're starting that specific workflow. When you create an asset event, you're indicating that data has been updated, which may trigger downstream DAGs that depend on that asset.
::

### 4. Observe Downstream Effects

1. After `raw_zen_quotes` has completed, observe what happens
2. Note which other DAGs run automatically
3. This demonstrates **asset-based scheduling** in action

### 5. Test the Personalize Newsletter DAG

1. **Unpause** the `personalize_newsletter` DAG
2. It should run automatically once, but will fail (this is expected)
3. Navigate to the task logs to understand what went wrong

::alert[The failure is intentional - you'll fix it in Exercise 2]{type="warning"}

### 6. Explore UI Features

Try out these new UI features:

1. **Switch themes**: Toggle between light mode and dark mode 😎
2. **Change language**: Try a different language from the `User` menu
3. **Navigation**: Notice how easy it is to navigate between different views

## Key Observations

After completing this exercise, you should understand:

- How the new UI improves workflow visualization
- The relationship between DAGs and Assets
- Different methods for triggering workflows
- How asset-based scheduling creates automatic dependencies

## Next Steps

In the next module, you'll work with Assets to complete the ETL pipeline and fix the failing `personalize_newsletter` DAG.

::alert[Ready to move on? Proceed to Module 2 to work with Assets!]{type="success"}