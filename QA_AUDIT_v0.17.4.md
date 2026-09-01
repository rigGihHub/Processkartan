# QA Audit v0.17.4

## Scope
Unify recent process-building features into one clearer UX flow.

## Verified behavior
- Single-node selection shows a contextual methodology cue such as Object → Activity or Activity → Object out.
- The alternative Next menu highlights the recommended choice without hiding other step types.
- The primary contextual Next action remains one-click.
- New next steps remain selected, enter inline editing and are brought into the visible viewport.
- Status feedback explains the fast continuation shortcut: Ctrl/Cmd+Enter.
- Core palette additions use consistent continuation guidance.

## Gates
- py_compile: passed.
- pytest: 212/212 passed.
- JavaScript suites: 25/25 passed.
- Focused Chromium build-flow UX smoke: passed.
- Core JavaScript syntax: passed.
- Embedded JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
