# QA Audit – Maplini v0.20.51

## Release focus
**Lös konflikter före ritning**: multi-document conflicts are turned into explicit user decisions before a process proposal can be drawn.

## Functional scope verified
- Conflicts expose stable IDs and explicit alternatives.
- Responsibility conflicts can be resolved to either source value or a custom value.
- System conflicts can be resolved to either source value or a custom value.
- Step-type conflicts can be resolved to Activity or Decision.
- Direct-order conflicts can be resolved to A → B, B → A, or no direct connection.
- `Rita processförslag` remains disabled while any document conflict is unresolved.
- Selected order resolution controls which previously conflicting sequence edge is allowed onto the canvas.
- Document content remains browser-local in this release; no Supabase/RLS/schema changes.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python test suite: **411/411 PASS**
- JavaScript test files: **32/32 PASS**
- Core JavaScript syntax checks: **24/24 PASS**
- Desktop Chromium interaction smoke: PASS
- Mobile Read/Follow smoke: PASS
- Mobile canvas fit/readability smoke: PASS
- v0.20.46 paste-to-process browser regression: PASS
- v0.20.48 document interpretation browser regression: PASS
- v0.20.49 real document flow browser regression: PASS
- v0.20.50 multi-document synthesis browser regression: PASS
- v0.20.51 document conflict resolution browser test: PASS

## DOM / packaging checks
- Static/runtime editor HTML IDs: **356**
- Duplicate IDs: **0**
- Critical DOM ancestor contract (`.p48-body`, sidebar, scroll, controls, canvas): PASS
- No new database migration required.
- Release is prepared locally only; **not pushed and not verified live**.
