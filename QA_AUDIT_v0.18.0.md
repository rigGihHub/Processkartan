# QA Audit v0.18.0

## Scope
Structured process information foundation.

## Verified
- Activity, Subprocess and Decision expose structured process information in the properties panel.
- Description, responsible role, system, instruction, risk, control, KPI and duration persist on the selected node.
- Metadata remains off-canvas.
- Visual formatting is secondary/collapsible.
- Old nodes without processInfo normalize safely to empty metadata.
- Existing Input/Output behavior remains.
- Chromium smoke edited description, role and system and verified persisted node data plus 3/8 completeness.

## Gates
- py_compile: passed.
- pytest: 213/213 passed.
- JavaScript suites: 26/26 passed.
- Focused Chromium process-information smoke: passed.
- Core JavaScript syntax: passed.
- Embedded JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
