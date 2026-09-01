# QA Audit v0.17.2

## Scope
Atomic undo safety for destructive, layout and process-scale operations.

## Verified behavior
- Clear Entire Canvas creates exactly one Undo checkpoint; one Undo restores all nodes and connectors.
- Smart Layout and Automatic Cleanup group node movement and connector normalization into one checkpoint.
- Nested history writes are suppressed inside atomic operations.
- Process-scale slider creates one checkpoint across multiple input events in the same gesture.
- A gesture checkpoint is committed only when the process state actually changes.
- Existing Redo behavior remains compatible with restored process snapshots.

## Gates
- py_compile: passed.
- pytest: 210/210 passed.
- JavaScript suites: 25/25 passed.
- Focused Chromium clear/cleanup/scale atomic-undo smoke: passed.
- Core JavaScript syntax: passed.
- Embedded JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
