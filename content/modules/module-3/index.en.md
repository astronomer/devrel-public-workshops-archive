---
title: "Module 3: Add Human-in-the-Loop"
weight: 30
---

# Module 3: Add Human-in-the-Loop

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

### 1. Open the Personalize Newsletter DAG

1. In the **Astro IDE** code editor, open the `personalize_newsletter.py` file
2. Locate the `create_personalized_newsletter` task

### 2. Import the ApprovalOperator

Add the import at the top of the file:

```python
from airflow.operators.approval import ApprovalOperator
```

### 3. Add the HITL Operator

Add this operator to your DAG after the `create_personalized_newsletter` task:

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
# Add this line to set up the dependency
create_personalized_newsletter >> approve_personalization
```

Make sure the approval task comes after `create_personalized_newsletter` in your workflow.

### 5. Deploy Your Changes

1. Save the file
2. Click `Sync to Test` in the upper right corner
3. Wait for the sync to complete

::alert[Syncing may take a few minutes]{type="info"}

### 6. Test the HITL Workflow

1. Run the `personalize_newsletter` DAG again
2. The workflow will pause at the approval step
3. Navigate to **Browse** → **Required Actions** in the Airflow UI
4. Review the newsletter content and either **Approve** or **Reject** the results

### 7. Explore Required Actions

The **Required Actions** view provides:
- Instance-wide view of all pending approvals
- Easy access to review content
- Batch approval capabilities for multiple items

## Understanding HITL Operators

### ApprovalOperator Parameters

- **task_id**: Unique identifier for the task
- **subject**: Brief description of what needs approval
- **body**: Content to review (can use Jinja templating)
- **defaults**: Default action ("Approve" or "Reject")

### Templating in HITL

The `body` parameter supports Jinja templating, allowing you to:
- Pull XCom values from previous tasks
- Include dynamic content based on execution context
- Format data for human review

Example:
```python
body="{{ ti.xcom_pull(task_ids='create_personalized_newsletter') }}"
```

## Best Practices

### When to Use HITL

- **Quality Control**: Review generated content before publishing
- **Compliance**: Ensure regulatory requirements are met
- **Business Logic**: Apply human judgment to automated decisions
- **Exception Handling**: Manual intervention for edge cases

### HITL Design Patterns

1. **Sequential Approval**: Single approval point in workflow
2. **Parallel Review**: Multiple reviewers for the same content
3. **Escalation**: Different approval levels based on criteria
4. **Conditional Approval**: Approval only under certain conditions

## Troubleshooting

If you don't see the Required Actions:
1. Ensure the DAG has run and reached the approval task
2. Check that the task is in a "waiting for approval" state
3. Refresh the Airflow UI

## Key Concepts

After completing this exercise, you should understand:

- How to implement human approval workflows
- The Required Actions interface for managing approvals
- Templating in HITL operators for dynamic content
- When and why to use human-in-the-loop patterns

## Next Steps

In Module 4, you'll learn about backfills to reprocess historical data.

::alert[Approval workflow complete! Ready to learn about backfills in Module 4?]{type="success"}