# QA Audit v0.17.1

## Scope
One-click automatic process cleanup.

## Verified behavior
- `Ordna processen automatiskt` is the primary action inside `Snygga till`.
- Existing connector geometry is used to infer horizontal vs vertical layout direction.
- Current process shape is the fallback when links are insufficient.
- Smart Layout aligns nodes, evens spacing and reduces crossings.
- Connector routes are normalized after cleanup.
- Node count and connection graph are unchanged by cleanup.
- The operation is undoable through the existing single Smart Layout history checkpoint.
- Manual orientation controls remain available.

## Gates
- py_compile: passed.
- pytest: 209/209 passed.
- JavaScript suites: 25/25 passed.
- Focused Chromium automatic-cleanup smoke: passed.
- Core JavaScript syntax: passed.
- Embedded JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
