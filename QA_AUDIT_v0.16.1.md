# QA Audit v0.16.1

## Scope
Dependency Coach for direct Activity → Activity links.

## Verified behavior
- Manual Activity → Activity connection can trigger `coachDirectActivityLink()`.
- Direct connector is selected and `Infoga steg` opens.
- `Objekt / resultat` is the first connector insertion choice.
- Inserting Object splits the connector using existing connector-split logic.
- Process Check flags direct Activity → Activity links with code `direct_activity`.
- Finding severity is warning and includes the connector index.
- Object-mediated flows are not flagged by this rule.

## Verified release gates
- `py_compile`: passed.
- `pytest`: 199/199 passed.
- JavaScript suites: 25/25 passed.
- Focused Chromium dependency-coach smoke: passed.
- Core JavaScript syntax: passed.
- Embedded editor JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Note
The long legacy browser smoke still contains the known nested-menu state flake from older releases; the v0.16.1 interaction path was therefore verified in a dedicated focused Chromium smoke.

## Deployment
Not pushed or deployed.
