# QA audit – Maplini v0.20.58

## Scope
Export Preview: actual PDF/DOCX page composition is previewed before download, with conservative warnings for nodes near page boundaries.

## Results
- `python -m py_compile app.py`: PASS
- `pytest -q`: **427 passed**
- `node --check maplini_*_core.js`: PASS
- Core JavaScript tests + background state: PASS
- Chromium `browser_interaction_smoke.py`: PASS
- Chromium source-change regression: PASS
- Chromium source-support regression: PASS
- Chromium export-fidelity regression: PASS
- Chromium `browser_v02058_export_preview.py`: PASS
- Critical DOM ancestry: PASS
- Duplicate static editor IDs: none
- Release ZIP integrity: checked after packaging

## Product safeguards
- Preview uses `renderMapSnapshot()` + `composeExportPageCanvases()` — the same page composition used by PDF/DOCX.
- Preview does not rewrite nodes, links, source traces, or process data.
- Boundary warning is deliberately conservative; it says to check the boundary rather than claiming content is invalid.
- No Supabase schema, RLS, OAuth, or workspace changes.
- Not deployed/live-verified in this release preparation.

## Defect caught during QA
Chromium exposed the Swedish status typo `2 sidaor`; corrected to `2 sidor` before packaging.
