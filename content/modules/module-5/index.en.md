---
title: "Module 5: Use DAG Versioning"
weight: 50
---

# Module 5: Use DAG Versioning

DAG versioning is a new feature in Airflow 3 that tracks changes to your DAG code over time. In this exercise, you'll explore how versioning works and compare different versions of your DAGs.

## Learning Objectives

- Understand DAG versioning with `LocalDagBundle`
- Navigate between different DAG versions in the UI
- Compare structural and code changes across versions
- Understand when new versions are created

## Background

DAG versioning provides:
- **Change tracking**: Automatic recording of DAG modifications
- **Version comparison**: Visual diff between DAG versions
- **Code history**: Access to previous versions of DAG code
- **Structural analysis**: Understanding how DAG structure evolves

The `LocalDagBundle` automatically sets up versioning for your DAGs, creating new versions when structural changes are detected.

## Steps

### 1. Access DAG Versioning

1. Navigate to the **DAGs** view in the Airflow UI
2. Click on the `personalize_newsletter` DAG
3. Go to the **Graph** view
4. Click on **Options** in the top menu
5. Notice the **DAG Version** dropdown

### 2. Explore Version History

1. Check how many versions are available in the dropdown
2. You should see multiple versions from the changes made in Modules 2 and 3

::expand[Why do you have multiple versions?]{header="💡 Think About It"}
Each time you modified the DAG structure (adding the asset scheduling in Exercise 2, adding the HITL operator in Exercise 3), Airflow created a new version to track these changes.
::

### 3. Compare Graph Versions

1. Toggle between different versions using the dropdown
2. Observe the changes in the **Graph** view:
   - **Version 1**: Original DAG structure
   - **Version 2**: After adding asset-based scheduling
   - **Version 3**: After adding the HITL operator

3. Notice how the graph visualization changes with each version

### 4. Compare Code Versions

1. Navigate to the **Code** tab
2. Use the version dropdown to toggle between different versions
3. Observe the code differences:
   - Import statements
   - Task definitions
   - Scheduling configuration
   - Task dependencies

### 5. Analyze Version Metadata

For each version, note:
- **Creation timestamp**: When the version was created
- **Structural changes**: What changed in the DAG structure
- **Code differences**: Specific code modifications

## Understanding Version Creation

### When New Versions Are Created

New DAG versions are created when:
- **Task structure changes**: Adding, removing, or modifying tasks
- **Dependency changes**: Altering task relationships
- **Scheduling changes**: Modifying DAG schedule or triggers
- **Operator changes**: Switching operator types

### When Versions Are NOT Created

Versions are not created for:
- **Code comments**: Adding or modifying comments
- **Task implementation**: Changes within task logic that don't affect structure
- **Variable values**: Changing variable assignments
- **Cosmetic changes**: Formatting or whitespace modifications

::alert[New DAG versions are only created when the DAG's structure changes since the last run. Making changes to task code will not prompt a new version.]{type="info"}

## Version Comparison Features

### Graph Comparison
- **Visual diff**: Side-by-side comparison of DAG structures
- **Task highlighting**: New, modified, or removed tasks are highlighted
- **Dependency tracking**: Changes in task relationships are visible

### Code Comparison
- **Line-by-line diff**: Detailed code changes between versions
- **Syntax highlighting**: Improved readability of code differences
- **Change annotations**: Clear indicators of additions, deletions, and modifications

## Best Practices

### Version Management

1. **Meaningful changes**: Structure changes thoughtfully to create logical versions
2. **Documentation**: Use commit messages and comments to explain changes
3. **Testing**: Test DAG changes before deploying to production
4. **Rollback planning**: Understand how to revert to previous versions if needed

### Version Analysis

1. **Regular review**: Periodically review version history for insights
2. **Change impact**: Analyze how structural changes affect performance
3. **Debugging**: Use versions to identify when issues were introduced
4. **Compliance**: Maintain version history for audit requirements

## Practical Applications

### Development Workflow
- **Feature development**: Track incremental changes during development
- **Code review**: Compare versions during peer review processes
- **Debugging**: Identify when issues were introduced
- **Rollback**: Understand previous working configurations

### Production Management
- **Change tracking**: Monitor production DAG evolution
- **Impact analysis**: Understand the effect of changes on pipeline performance
- **Compliance**: Maintain audit trails for regulatory requirements
- **Documentation**: Automatic documentation of DAG evolution

## Troubleshooting

### Missing Versions
If you don't see expected versions:
1. Ensure structural changes were made (not just code changes)
2. Verify the DAG has been parsed after changes
3. Check that the `LocalDagBundle` is properly configured

### Version Confusion
If versions seem incorrect:
1. Remember that only structural changes create versions
2. Check the timestamp to understand when changes occurred
3. Use the code comparison to see exact differences

## Key Concepts

After completing this exercise, you should understand:

- How DAG versioning automatically tracks structural changes
- The difference between structural and code-only changes
- How to navigate and compare different DAG versions
- When and why new versions are created
- Best practices for managing DAG evolution

## Next Steps

In Module 6 (optional), you'll explore advanced event-driven scheduling with GenAI integration.

::alert[Versioning mastered! Ready for the advanced GenAI module, or proceed to the summary?]{type="success"}