# QA Audit – Maplini v0.19.6

## Scope
Visual connector polish: rounded orthogonal corners and clearer semantic Ja/Nej labels.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **230/230 passed**
- JavaScript test files: **27/27 passed**
- Full Chromium `tests/browser_interaction_smoke.py`: PASS
- Critical DOM order/hierarchy check: PASS
- Duplicate HTML IDs: **0**
- APP_VERSION: **0.19.6**
- ZIP integrity: PASS

## Behavior preserved
- Straight connectors remain straight.
- Free/manual routing is not normalized by the visual corner treatment.
- Connector selection and drag handling remain in the existing interaction path.
- Ja/Nej routing used by Follow Process still reads the same stored connector labels.
- No Supabase migration is required.

## Note
A spreadsheet-runtime warmup warning appeared during Python startup in this environment, but `py_compile` and pytest both exited successfully. It is unrelated to Maplini.
