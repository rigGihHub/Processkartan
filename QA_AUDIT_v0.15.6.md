# QA Audit v0.15.6

## Scope
Make the left formatting panel clearly reflect the selected object type.

## Verified behavior
- Connector selection shows `Pil`.
- Single-node selection shows `Ruta`.
- Multi-node selection shows `Flera rutor`.
- No selection shows `Formatering`.
- Contextual help text changes with the selection.
- Connector formatting no longer repeats an inner `Pil / koppling` heading.
- Existing connector formatting, label, drag and width behavior remain intact.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 192/192 passed.
- JavaScript suites: 25/25 passed.
- Chromium browser interaction smoke: passed.
- Browser verified `Pil` and `Ruta` heading transitions and matching help text.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed. This release is intentionally prepared as a local push candidate only.
