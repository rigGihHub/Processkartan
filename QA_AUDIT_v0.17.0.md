# QA Audit v0.17.0

## Scope
Process Flow Assistant for direct Activity-to-Activity dependencies.

## Verified behavior
- Direct Activity → Activity links open a contextual methodology coach.
- One-click insertion creates an Object/result between the Activities and splits the connector.
- The inserted node remains a normal `object` type.
- Users can explicitly keep a direct Activity link.
- Intentional direct links persist a methodology override and are not repeatedly flagged.
- Process Analysis offers a one-click fix for unacknowledged direct Activity links.

## Gates
- py_compile: passed.
- pytest: 208/208 passed.
- JavaScript suites: 25/25 passed.
- Focused Chromium coach/insert/keep smoke: passed.
- Core JavaScript syntax: passed.
- Embedded JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
