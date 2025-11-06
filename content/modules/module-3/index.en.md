---
title: "Module 3: Use Dag Versioning"
weight: 30
---

# Module 3: Use Dag Versioning

Dag versioning is a new feature in Airflow 3 that tracks changes to your Dag code over time. In this exercise, you'll explore how versioning works and compare different versions of your Dags.

## Learning Objectives

- Understand Dag versioning with `LocalDagBundle`
- Navigate between different Dag versions in the UI
- Compare structural and code changes across versions
- Understand when new versions are created

## Steps

### 1. Access Dag Versioning

1. Navigate to the **Dags** view in the Airflow UI
2. Click on the `personalize_newsletter` Dag
3. Go to the **Graph** view
4. Click on **Options** in the top menu
5. Notice the **Dag Version** dropdown

### 2. Explore Version History

1. Check how many versions are available in the dropdown
2. You should see multiple versions from the changes made in the previous module

::expand[Each time you modified the Dag structure (adding the HITL operator), Airflow created a new version to track these changes. But only, if a Dag run is between the changes.]{header="💡 Why do you have multiple versions?"}

### 3. Compare Graph Versions

1. Toggle between different versions using the dropdown
2. Observe the changes in the **Graph** view:
   - **Version 1**: Original Dag structure
   - **Version 2**: After adding the HITL operator

3. Notice how the graph visualization changes with each version

### 4. Compare Code Versions

1. Navigate to the **Code** tab
2. Use the version dropdown to toggle between different versions
3. Observe the code differences

## Key Concepts

After completing this exercise, you should understand:

- How Dag versioning automatically tracks structural changes
- The difference between structural and code-only changes
- How to navigate and compare different Dag versions
- When and why new versions are created

## Next Steps

In the next module, you'll explore advanced event-driven scheduling with GenAI integration.

::alert[Versioning mastered! Ready for integrating Amazon SQS and Amazon Bedrock?]{type="success"}
