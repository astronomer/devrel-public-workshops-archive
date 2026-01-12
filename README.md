# Workshop base

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
