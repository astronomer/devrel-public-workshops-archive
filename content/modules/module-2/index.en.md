---
title: "Module 2: Add Human-in-the-Loop"
weight: 20
---

# Module 2: Add Human-in-the-Loop

Airflow 3.1 introduced human-in-the-loop (HITL) operators, allowing manual intervention in automated workflows. In this exercise, you'll add an approval step for newsletter personalization.

## Learning Objectives

- Implement Human-in-the-Loop operators
- Create approval/rejection workflows
- Understand manual intervention patterns in automated pipelines
- Navigate the Required Actions interface

## Background

Human-in-the-loop workflows are essential when you need:
- Manual review and approval processes
- Quality control checkpoints
- Business decision points in automated workflows
- Compliance and audit requirements

In this use case, you want a human to review the newsletter personalization results before sending.

## Steps

### 1. Open the Personalize Newsletter Dag

In the **Astro IDE** code editor, open the `personalize_newsletter.py` file

### 2. Import the ApprovalOperator

Add the import at the top of the file:

```python
from airflow.providers.standard.operators.hitl import ApprovalOperator
```

### 3. Add the HITL Operator

Add this operator to your Dag after the `create_personalized_newsletter` task:

```python
approve_personalization = ApprovalOperator(
   task_id="approve_personalization",
   subject="Your task:",
   body="{{ ti.xcom_pull(task_ids='create_personalized_newsletter') }}",
   defaults="Approve", # other option: "Reject"
)
```

### 4. Update Task Dependencies

Modify the task dependencies to include the approval step:

```python
create_personalized_newsletter.expand(user=_get_weather_info) >> approve_personalization
```

Make sure the approval task comes after `create_personalized_newsletter` in your workflow.

### 5. Deploy Your Changes

1. Save the file
2. Click `Sync to Test` in the upper right corner
3. Wait for the sync to complete

### 6. Test the HITL Workflow

1. Run the `raw_zen_quotes` Dag again to trigger an end-to-end run
2. The workflow will pause at the approval step
3. Navigate to **Browse** → **Required Actions** in the Airflow UI
4. Review the newsletter content and either **Approve** or **Reject** the results

### 7. Explore Required Actions

The **Required Actions** view provides:
- Instance-wide view of all pending approvals
- Easy access to review content
- Batch approval capabilities for multiple items

### 8. (Bonus) Change the Body

Try to change the `body` of your `ApprovalOperator`. Change it to a multi-line-string and add Markdown as it will be rendered in the Airflow UI.

## Best Practices

### When to Use HITL

- **Quality Control**: Review generated content before publishing
- **Compliance**: Ensure regulatory requirements are met
- **Business Logic**: Apply human judgment to automated decisions
- **Exception Handling**: Manual intervention for edge cases

## Key Concepts

After completing this exercise, you should understand:

- How to implement human approval workflows
- The Required Actions interface for managing approvals
- Templating in HITL operators for dynamic content
- When and why to use human-in-the-loop patterns

## Next Steps

In Module 3, you'll learn about Dag versioning.

::alert[Ready for some time travel? Let's move to the next module!]{type="success"}