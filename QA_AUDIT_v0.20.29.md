# QA Audit – Maplini v0.20.29

## Scope
Process Overview & Navigation. No process schema, Supabase, RLS, connector-routing or walkthrough answer semantics changed.

## Intended behavior
- **Översikt** is opt-in and closed by default.
- Miniature nodes are derived from existing node geometry only.
- The overview viewport tracks the currently visible canvas area.
- Clicking a miniature node selects and centers the corresponding real node.
- Clicking empty overview space pans the canvas.
- Overview refresh follows process changes, selection, zoom and scrolling.
- Mobile editor does not expose the overview control.

## Verification
- `python -m py_compile app.py`: PASS
- Python pytest: 312/312 PASS
- JS test files: 27/27 PASS
- Core JS `node --check`: 22/22 PASS
- Chromium interaction smoke, including overview open/jump/close: PASS
- Critical DOM structure: PASS
- Duplicate literal HTML/DOM IDs: 0
- No Supabase migration required
