# QA Audit – Maplini v0.20.60

Release: **Förstå steget direkt**

## Scope
- Ny kompakt snabböverblick när aktivitet, delprocess eller beslut markeras.
- Visar **Vad? Vem? Input? Output? Sedan?**.
- Bygger endast på sparad stegdata och faktiska utgående kopplingar.
- Väglabels på kopplingar bevaras i "Sedan".
- Saknad information markeras explicit; ingen ny processinformation uppfinns.
- Ingen ändring av Supabase-schema, RLS, OAuth eller processdatastruktur.

## Automated QA
- `python -m py_compile app.py`: PASS
- `pytest -q`: **430 passed**
- Node JS test suite (`tests/*.js`, 36 filer): PASS
- `node --check maplini_*_core.js` (28 core-filer): PASS
- `tests/browser_interaction_smoke.py`: PASS
- `tests/browser_v02059_walkthrough_first_use.py`: PASS
- `tests/browser_v02060_step_understanding.py`: PASS

## Browser / DOM integrity
Rendered Chromium DOM verified:
- `.p48-body aside.p48-side`: 1
- `.p48-body main#p48-scroll`: 1
- `aside.p48-side #p48-controls`: 1
- `main#p48-scroll #p48-canvas`: 1
- Duplicate rendered IDs: none

## Product guardrails
- Canvas remains dominant.
- No separate analysis dashboard added.
- Existing detailed process-info editor remains available beneath the summary.
- "Sedan" reads the actual graph rather than inferring hidden process logic.
