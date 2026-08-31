# QA Audit v0.15.10

## Scope
- Full-content zoom using the top-bar + / - controls.
- Ctrl/Cmd-click node multi-selection.
- Selection-context hardening for connector formatting.

## Verified behavior
- Zoom transform now lives inside the embedded editor iframe.
- + / - scales the canvas itself, so nodes, node text, connectors, connector labels, process logo and canvas guides scale together.
- Canvas data and logical coordinates are not rewritten by zoom.
- Ctrl/Cmd-click toggles nodes into and out of the current selection.
- Normal click remains single-select.
- Connector formatting is hard-hidden when there is no selected connector.
- Clearing/opening a process explicitly resets formatting context.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 196/196 passed.
- JavaScript suites: 25/25 passed.
- Chromium interaction smoke: passed. One pre-existing transient export-menu state flake occurred in an earlier run; rerun passed.
- Browser smoke verified zoom transform changes, reset to 100%, hard-hidden connector panel and Ctrl multi-selection.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
