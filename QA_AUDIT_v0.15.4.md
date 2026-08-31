# QA Audit v0.15.4

## Scope
Selected-connector interaction polish prepared locally; no deployment required.

## Verified behavior
- Connector text label, drag handle and routing quick toolbar no longer stack.
- With text present, label and toolbar are positioned on opposite sides of the connector.
- Without text, toolbar remains offset from the drag handle.
- Full and incremental redraws share the same placement helper.
- Existing connector label ownership, free dragging, node-follow and Undo remain intact.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 190/190 passed.
- JavaScript suites: 25/25 passed.
- Chromium browser interaction smoke: passed.
- Spatial separation assertion in Chromium: passed.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed. This release is intentionally prepared as a local push candidate only.
