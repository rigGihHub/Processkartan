# QA Audit v0.15.5

## Scope
Clean up connector formatting so node and connector controls no longer overlap visually or conceptually.

## Verified behavior
- Connector formatting has dedicated color and width controls.
- Node border color/width are hidden during connector selection.
- Connector width changes only the selected connector.
- Connector color does not write into node border-color UI.
- Connector wording is clearer Swedish (`Pilform`, `Fästning`).
- Existing connector labels, routing, dragging and Undo remain intact.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 191/191 passed.
- JavaScript suites: 25/25 passed.
- Chromium browser interaction smoke: passed.
- Browser verified connector-width change to 4 px.
- Browser verified node border controls hidden during connector selection.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed. This release is intentionally prepared as a local push candidate only.
