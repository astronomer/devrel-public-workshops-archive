# Workshop base

## Scenario: AstroTrips

## Workshop repo structure

_todo: this section belongs to `main` but while this new base in development, it is kept here._

This repository uses branches to represent individual workshops.

New workshops follow a structured naming scheme:
```
workshops/<scenario>/<workshop-name>
```

Using slash-separated branch names allows many tools (for example GitHub, GitLab, and IDE integrations) to render branches in a tree-like structure, making related workshops easier to discover and navigate.

Each scenario has a base branch:
```
workshops/<scenario>/_base
```

which contains all shared components for the scenario, such as:
- scenario description and context
- shared utilities
- setup DAGs and helper functions
- reusable operators

**This branch is not a runnable workshop on its own. It serves as a template and foundation for all scenario-based workshops.**

Individual workshops are created as separate branches derived from `_base`, for example:
```
workshops/astrotrips/etl
```

These branches extend the base scenario with workshop-specific components, Dags, exercises, and instructions.

## Gamification

The base project comes with a custom `MissionControlOperator` ([include/utils.py](include/utils.py)).

If gamification is required (for example to hand out swag during a workshop), an additional exercise can be added at the very end. In this exercise, participants are asked to add the `MissionControlOperator` as the final task in their Dag. If multiple Dags are part of the workshop, just select one specific of them.

When the Dag is executed successfully, this task will emit a clearance code in the task logs, for example:
```
🔐 Interstellar clearance code: ORBIT-PM5G2-CLVHG-TT64U
```

The clearance code consists of four parts:
```
<prefix>-<types_hash>-<edges_hash>-<names_hash>
```
- `types_hash` is derived from the operator types used in the Dag
- `edges_hash` is derived from how tasks are connected
- `names_hash` is derived from the task IDs

Before the workshop, the host runs the same operator as part of the solution Dag to obtain the reference clearance code. Solutions and codes can be kept in an Astronomer interal repo if required.

Once participants have their code, they can submit it to the host (in person or via chat, depending on the workshop setup). The host can then compare it with the reference code from the solution.

If participants implemented the correct Dag structure but used different task IDs, only the last part of the code will differ, for example:
```
Solution:           ORBIT-PM5G2-CLVHG-Y5P5X
Different task IDs: ORBIT-PM5G2-CLVHG-TT64U
```

This allows the host to quickly assess how close a solution is to the intended outcome and decide whether the code is still acceptable.

Since the clearance code is derived from the Dag structure and requires the workshop solution to be executed, it is difficult to fake and therefore provides a lightweight but effective form of cheat resistance without an external dependency.

![Mission control](doc/mission-control.png)
