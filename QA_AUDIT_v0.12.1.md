# QA Audit – Maplini v0.12.1

## Scope
Smart Layout refinement: decision branch semantics, crossing reduction and directed-loop handling.

## Verification
- `python -m py_compile app.py google_docs.py maplini_google_ui.py` – PASS
- `pytest -q` – **163/163 PASS**
- All `tests/test_*.js` – **22/22 PASS**
- `node --check maplini_layout_core.js` – PASS
- `node --check maplini_connector_core.js` – PASS
- `node --check maplini_editing_core.js` – PASS
- Longest embedded editor `<script>` after core injection – PASS
- Critical desktop DOM contract – PASS
- ZIP integrity – PASS (completed during release packaging)

## Smart Layout behavior checked
- Ja branch sorts before/above Nej in horizontal mode even when original node coordinates are reversed.
- Ja branch sorts left of Nej in vertical mode.
- Feedback edges in directed cycles are excluded from forward rank calculation, preventing runaway ranks.
- Main loop path remains compact and forward-progressing.
- Barycentric ordering follows connected parent/child order to reduce avoidable crossings.
- Existing branch/merge rank behavior still passes.
- Selected-only layout continues to use only internal selected links.
- One Undo checkpoint per layout operation through the existing `applyNodePositions` path.
- Node dimensions and selection are preserved; connectors are fully redrawn.
- No database, Supabase, OAuth, secret or dependency changes.

## Known limitation
Smart Layout remains deterministic and graph-aware rather than a full constraint solver. Very dense graphs with several overlapping loops can still benefit from a manual final adjustment.
