# QA AUDIT – Maplini v0.11.4

## Scope
- Straight connector routing regression
- Left sidebar full-height scrolling regression
- Desktop/mobile layout guard

## Implementation verified
- `Routing → Rak` clears stale `viaX`/`viaY` breakpoints.
- Connector core renders `straight` as exactly one direct segment even for legacy links with saved via coordinates.
- Sidebar uses `box-sizing:border-box` in base, desktop guard and mobile drawer, preventing bottom clipping from height + padding.
- Desktop sidebar exposes a slim scrollbar; mobile retains touch scrolling with hidden scrollbar.

## Automated QA
- `python -m py_compile app.py google_docs.py maplini_google_ui.py`: PASS
- `pytest -q`: **159 passed**
- JavaScript suites `tests/test_*.js`: **21/21 passed**
- `node --check maplini_connector_core.js`: PASS
- `node --check maplini_editing_core.js`: PASS
- `node --check maplini_canvas_core.js`: PASS
- longest fully substituted embedded `<script>` syntax check: PASS
- critical DOM: `.p48-body`, `.p48-side`, `#p48-scroll`, `#p48-controls`, `#p48-canvas`: PASS

## Release status
GitHub-ready local push candidate. Not verified live until pushed/deployed.
