# QA Audit – Maplini v0.20.46

Release: **Klistra in → process**

## Scope
- Deterministic multi-step paste/import.
- Available from empty canvas and `••• Mer`.
- Bullet/number cleanup.
- Existing quick-build inference reused for decision detection.
- Up to 80 imported steps.
- No AI, schema, Supabase or RLS changes.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **384/384 PASS**
- JavaScript test files: **28/28 PASS**
- Core JavaScript syntax: **23/23 PASS**
- Desktop Chromium interaction smoke: PASS
- Mobile Read/Follow Chromium smoke: PASS
- Mobile canvas fit/readability smoke: PASS
- First-process regression: PASS
- Process-control regression: PASS
- Version-history regression: PASS
- Dedicated paste-process Chromium test: PASS

## DOM / packaging
- Parsed HTML IDs: **339**
- Duplicate IDs: **0**
- Critical DOM ancestor contract: PASS
- No database/schema migration required.

## Product constraints preserved
- Imported decision questions are recognized, but Ja/Nej branches are not guessed.
- Existing canvas is only replaced after explicit confirmation.
- Import is a drafting accelerator, not an AI process-authoring feature.
