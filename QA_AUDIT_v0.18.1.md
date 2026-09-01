# QA Audit v0.18.1

## Scope
Properties-panel UX for structured process information.

## Verified
- Essential process information is immediately visible: what happens, responsible role, system and duration.
- Instruction, risk, control and KPI are collapsed under `Fördjupa beskrivningen`.
- Existing responsible-role and system values in the current process appear as reusable suggestions.
- Suggestion lists are deduplicated and sorted.
- Completion uses optional wording (`x av 8`) and the advanced section reports its own filled count.
- Ctrl/Cmd+Enter saves the active metadata field and returns focus to the selected canvas node.
- Read-only state disables textareas as well as inputs/selects/buttons.
- Focused Chromium smoke created two activities, persisted role/system on the first, verified suggestions on the second, and verified advanced-field count.

## Gates
- py_compile: passed.
- pytest: 214/214 passed.
- JavaScript suites: 26/26 passed.
- Focused Chromium properties UX smoke: passed.
- Core JavaScript syntax: passed.
- Embedded JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
