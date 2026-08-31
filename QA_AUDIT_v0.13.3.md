# QA Audit – Maplini v0.13.3

## Scope
UI regression fix for contextual node/link toolbars in the editor iframe.

## Root cause
The toolbar CSS existed in the Streamlit parent document stylesheet, while the toolbar DOM is rendered inside `components.html` in an iframe. Parent CSS cannot style iframe contents. As a result the toolbar DOM was visible with browser-default styling and default block layout even without selection.

## Fix
- Added `.p48-link-quick` and `.p48-node-quick` base/active/child/mobile rules to the raw editor HTML stylesheet.
- Default visibility is `display:none`; `.on` is the sole display trigger.
- Preserved existing JS selection logic, routing state, multi-select modes and touch sizing.
- No backend, persistence, Supabase or dependency changes.

## Verification
- Python compile: OK (`app.py`, `google_docs.py`, `maplini_google_ui.py`)
- pytest: 167/167 passed
- JavaScript test suites: 23/23 passed
- `node --check` all `maplini_*_core.js`: OK
- longest embedded editor `<script>` syntax: OK
- critical desktop DOM nesting: OK
- regression test confirms toolbar visibility/style CSS exists inside editor iframe source
- ZIP integrity: verified during packaging
