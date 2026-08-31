# QA Audit – Maplini v0.12.0

## Scope
Smart Layout: automatic graph-aware horizontal/vertical layout for the full process or selected nodes.

## Verification
- `python -m py_compile app.py google_docs.py maplini_google_ui.py` – PASS
- `pytest -q` – **163/163 PASS**
- All `tests/test_*.js` – **22/22 PASS**
- `node --check maplini_layout_core.js` – PASS
- `node --check maplini_connector_core.js` – PASS
- `node --check maplini_editing_core.js` – PASS
- Longest embedded editor `<script>` extracted after core injection and checked with `node --check` – PASS
- BeautifulSoup desktop DOM contract – PASS:
  - `.p48-body` exists
  - `.p48-side` is inside `.p48-body`
  - `#p48-scroll` is inside `.p48-body`
  - `#p48-controls` is inside `.p48-side`
  - `#p48-canvas` is inside `#p48-scroll`

## Smart Layout behavior checked
- Horizontal rank progression follows connectors.
- Vertical rank progression follows connectors.
- Branch siblings share the same rank and are spread on the cross-axis.
- Merge nodes are placed later in the flow.
- Selected-only layout uses only internal links and does not move unselected nodes.
- One Undo checkpoint per layout operation through the existing `applyNodePositions` path.
- Selection and node dimensions are preserved.
- Connector redraw is forced after layout.
- Layout spacing adapts to the fixed 2400×1400 canvas bounds.
- No database, Supabase, OAuth, secrets or dependency changes.

## Known limitation
This first Smart Layout release is deterministic and graph-aware but is not yet a full constraint solver. Highly cyclic or unusually dense graphs can still benefit from a manual final adjustment after automatic layout.
