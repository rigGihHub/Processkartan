# QA Audit v0.16.2

## Scope
Make whole-process scaling easier to discover and repeatedly use.

## Verified behavior
- `Skala process` is a top-level toolbar control.
- It is no longer nested inside `Mer`.
- −10% keeps the menu open after each click.
- +10% keeps the menu open after each click.
- Focused Chromium smoke performed multiple consecutive − / + presses without reopening the menu.
- Fit-to-page remains a one-shot action that closes after completion.
- Existing proportional process-scale implementation is unchanged.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 200/200 passed.
- JavaScript suites: 25/25 passed.
- Focused Chromium scale-menu smoke: passed.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
