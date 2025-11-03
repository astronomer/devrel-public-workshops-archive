---
title: "Module 4: Run a Backfill"
weight: 40
---

# Module 4: Run a Backfill

Backfills are a first-class feature in Airflow 3, making it easy to reprocess historical data for time-dependent ETL pipelines. In this exercise, you'll create and monitor backfill operations.

## Learning Objectives

- Create backfills using the Airflow UI
- Configure backfill parameters and date ranges
- Monitor backfill progress and status
- Understand downstream effects of backfill operations
- Manage multiple approval requests from backfilled runs

## Background

For ETL pipelines that are time-dependent, you may occasionally need to reprocess historical data. Common scenarios include:

- **Data corrections**: Fixing issues in historical data
- **New deployments**: Processing data for newly deployed pipelines  
- **Schema changes**: Reprocessing data after pipeline modifications
- **Recovery**: Rebuilding data after system failures

## Steps

### 1. Access the Backfill Interface

1. Navigate to the **DAGs** view in the Airflow UI
2. Find the `raw_zen_quotes` DAG
3. Click the blue **Trigger** button
4. Select **Backfill** from the dropdown menu

### 2. Configure the Backfill

In the **Backfill** form, you'll configure:

#### Date Range Selection
- **Start Date**: Choose a date 2-3 days in the past
- **End Date**: Choose yesterday's date
- The form will show how many runs will be triggered based on your selections

#### Reprocessing Behavior
- **Clear existing runs**: Whether to clear previous task instances
- **Reset DAG runs**: Whether to reset existing DAG run states
- **Ignore dependencies**: Whether to ignore task dependencies

::alert[Try to select settings that will trigger exactly 2 DAG runs]{type="info"}

### 3. Start the Backfill

1. Review your configuration
2. Click **Start Backfill**
3. The system will create a backfill job and begin processing

### 4. Monitor Backfill Progress

1. Navigate back to the DAGs view
2. Look for the **progress bar** in the UI (you may need to refresh the page)
3. Notice how backfilled runs appear differently in the **Grid** view
4. Observe the visual indicators that distinguish backfill runs from regular runs

### 5. Observe Downstream Effects

Pay attention to what happens with other DAGs:

1. Were downstream DAGs (`selected_quotes`, `personalize_newsletter`) triggered automatically?
2. How does asset-based scheduling handle backfilled data?
3. What's the impact on the overall pipeline?

### 6. Handle Multiple Approvals

With the HITL operator from Exercise 3, you'll have multiple approval requests:

1. Navigate to **Browse** → **Required Actions**
2. You'll see multiple pending approvals from the backfilled runs
3. Try the **instance-wide view** for managing multiple approvals efficiently
4. You can approve/reject items individually or in batches

## Understanding Backfill Behavior

### Backfill vs Regular Runs

**Visual Differences:**
- Backfilled runs have special indicators in the Grid view
- Progress bars show backfill completion status
- Run metadata indicates backfill source

**Execution Differences:**
- Backfills respect DAG scheduling and dependencies
- Asset events are generated for each backfilled run
- Downstream DAGs are triggered based on asset updates

### Backfill Configuration Options

#### Date Range Options
- **Specific dates**: Target exact date ranges
- **Relative dates**: Use relative time periods
- **Schedule intervals**: Respect DAG scheduling intervals

#### Processing Options
- **Parallel execution**: Run multiple date ranges simultaneously
- **Sequential execution**: Process dates one at a time
- **Dependency handling**: Include or ignore task dependencies

## Best Practices

### When to Use Backfills

1. **Historical data processing**: Process data for past periods
2. **Pipeline testing**: Validate changes against historical data
3. **Data recovery**: Rebuild missing or corrupted data
4. **Compliance**: Ensure complete data coverage for audits

### Backfill Planning

1. **Resource consideration**: Ensure sufficient compute resources
2. **Dependency mapping**: Understand downstream impacts
3. **Approval workflows**: Plan for manual intervention points
4. **Monitoring**: Set up alerts for backfill completion/failures

## Troubleshooting

### Common Issues

- **Resource constraints**: Backfills may consume significant resources
- **Dependency conflicts**: Existing runs may conflict with backfill logic
- **Approval bottlenecks**: Multiple HITL tasks require attention

### Solutions

- **Resource management**: Use pools to limit concurrent tasks
- **Clear existing runs**: Use backfill options to handle conflicts
- **Batch approvals**: Use instance-wide Required Actions view

## Key Concepts

After completing this exercise, you should understand:

- How to create and configure backfill operations
- The difference between backfilled and regular DAG runs
- How backfills interact with asset-based scheduling
- Managing multiple approval workflows efficiently
- Best practices for backfill planning and execution

## Next Steps

In Module 5, you'll explore DAG versioning to track changes over time.

::alert[Backfill complete! Ready to explore DAG versioning in Module 5?]{type="success"}