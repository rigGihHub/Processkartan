# QA Audit v0.10.41

## Scope
Three focused UX fixes built directly from v0.10.40:
1. Inline document-link entry inside document nodes on the canvas.
2. Preserve active node selection after visual-style/format edits.
3. Reduce redundant vertical scrolling surfaces.

## Regression focus
- Existing valid document links still open in a new tab.
- Invalid non-http(s) inline URLs are rejected without changing state.
- Inline link save remains one undoable data change.
- Node selection remains active after styling.
- Sidebar remains wheel/touch scrollable even though its visual scrollbar is hidden.
- Canvas keeps its main vertical/horizontal scrolling.
- Desktop DOM contract remains two columns: sidebar + canvas.

## External changes
None. No Supabase migration, OAuth change, secret change or dependency change.

## Verification
- `python -m py_compile app.py google_docs.py maplini_google_ui.py` — passed.
- `pytest -q` — **147 passed**.
- All Node JS test suites in `tests/*.js` — passed.
- Extracted embedded JavaScript `node --check` — passed.
- BeautifulSoup desktop DOM contract — passed.
- ZIP integrity — verified after packaging.
