# QA AUDIT – Maplini v0.11.5

## Scope
- Contextual connector quick routing
- Straight/orthogonal switching on selected connector
- Undo/read-only/mobile touch regression guard

## Implementation verified
- Selected connector shows an on-canvas quick toolbar with **Rak** and **Vinkelrät**.
- Current routing is visually marked as active.
- Quick toolbar follows the selected connector midpoint during full and dirty-link renders.
- Quick toolbar and sidebar routing both call the same `applySelectedLinkRouting` function.
- Switching to straight clears stale `viaX`/`viaY`.
- A routing change creates one Undo checkpoint; selecting the already active routing creates none.
- Quick toolbar is hidden when editing is not allowed.
- Coarse-pointer/mobile controls use larger touch targets.

## Automated QA
- `python -m py_compile app.py google_docs.py maplini_google_ui.py`: PASS
- `pytest -q`: **160 passed**
- JavaScript suites `tests/test_*.js`: **21/21 passed**
- `node --check maplini_*_core.js`: PASS
- longest embedded `<script>` syntax check: PASS
- critical DOM nesting including `#p48-link-quick` inside `#p48-canvas`: PASS

## Release status
GitHub-ready local push candidate. Not verified live until pushed/deployed.
