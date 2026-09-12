# QA Audit – Maplini v0.20.77 Secondary Tools Cleanup

## Scope
UI-only cleanup of the existing **Mer** panel. No process schema, Supabase, RLS or OAuth changes.

## Automated verification
- `python -m py_compile app.py`: PASS
- `pytest -q`: **477/477 PASS**
- Core JavaScript syntax (`node --check`): **30/30 PASS**
- JavaScript test files: **38/38 PASS**
- `browser_interaction_smoke.py`: PASS after updating the smoke path to the intentional new nested UI hierarchy.
- `browser_v02076_command_bar.py`: PASS
- `browser_v02075_calm_neutral_sidebar.py`: PASS
- `browser_v02066_contextual_sidebar.py`: PASS
- `browser_v02077_secondary_tools_cleanup.py`: PASS
- Static duplicate DOM IDs: PASS

## v0.20.77 browser contract
When **Mer** is opened on desktop:
- `Källa → processförslag`, `Klistra in steg` and `Processkontroll` are immediately visible.
- Share and version history are immediately visible but visually secondary.
- `Redigering & struktur`, `Utseende, layout & export`, and `Övrigt` are collapsed groups.
- Opening each group reveals the original existing controls without duplicate IDs.
- The floating panel remains bounded and does not become a long page-like toolbar.

## Notes
An older v0.20.65 regression asserted the previous implementation detail `more.appendChild(el)`. It was updated to assert the new intentional presentation-group relocation instead. The main Chromium smoke likewise now opens the new presentation group before using View/Export/Processyta. These are test-maintenance changes caused by the deliberate UI hierarchy change, not product defects.
