# QA Audit – Maplini v0.20.50

## Release
**v0.20.50 – Flera dokument → en gemensam process**

## Scope
- Multi-file document import: up to 8 PDF/DOCX/TXT/MD/CSV files, 15 MB each.
- Deterministic merge of overlapping process steps.
- Source provenance per proposed step.
- Conflict detection for responsibility, system, step type and opposing direct sequence.
- Conflicting sequence edges are shown for review but not auto-drawn on canvas.
- No Supabase schema, RLS, workspace, OAuth or cloud model changes.

## Verification
- `python -m py_compile app.py`: PASS
- Python pytest: **405/405 PASS**
- JS test files: **31/31 PASS**
- Core JS `node --check`: **24/24 PASS**
- Desktop Chromium interaction smoke: PASS
- Mobile Read/Follow smoke: PASS
- Mobile canvas fit/readability smoke: PASS
- v0.20.38 fast-building regression: PASS
- v0.20.39 safe cleanup preview regression: PASS
- v0.20.40 Follow Process 2 regression: PASS
- v0.20.41 Process Control regression: PASS
- v0.20.42 Version History regression: PASS
- v0.20.44 first-process regression: PASS
- v0.20.46 paste-process regression: PASS
- v0.20.48 document interpretation regression: PASS
- v0.20.49 real document flow regression: PASS
- v0.20.50 multi-document browser flow: PASS
- Critical DOM structure checks: PASS via regression suite
- Static HTML IDs: checked, no duplicate literal IDs

## Guardrails
- Documents remain processed in the browser in this release.
- No document contents are persisted to Supabase by this feature.
- Conflicts are explicit review items; Maplini does not decide which source is correct.
- A conflicting sequence is not automatically connected.
- Generated output remains a proposal, not an authoritative process truth.

## Deployment
Release package prepared only. Not pushed and not verified live.
