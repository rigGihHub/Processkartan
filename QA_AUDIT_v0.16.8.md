# QA Audit v0.16.8

## Scope
Clarify Object in/out semantics without splitting the technical Object node type.

## Verified behavior
- Palette exposes Object in and Object out with semantic role hints.
- Both persist as `type: object`.
- Object role is limited to `input`, `output`, or `intermediate`.
- Older Object nodes default safely to `intermediate`.
- Object nodes display compact role chips.
- + Next from Activity creates an output/result Object.
- Properties guidance explains the selected Object role.

## Gates
- py_compile: passed.
- pytest: 206/206 passed.
- JavaScript suites: 25/25 passed.
- Focused Chromium Object UX smoke: passed.
- Core JavaScript syntax: passed.
- Embedded JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
