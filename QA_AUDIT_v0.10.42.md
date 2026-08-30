# QA Audit v0.10.42

## Scope
Connector-focused release built directly from v0.10.41.

## Root cause fixed
Node drag/resize called `drawLinks()` but did not mark connected links as dirty. The optimized renderer therefore had no work to perform and a connector could visually remain at its previous geometry until a later full render. v0.10.42 invalidates node geometry and marks only the affected connectors dirty during move/resize and other geometry-affecting node edits.

## Connector UX audit
### P0 implemented now
- Connected arrows follow nodes continuously while a node moves.
- Connected arrows update during node resize and after text/format changes that can affect geometry.

### Visual polish implemented now
- Smaller, better-proportioned arrow/circle/diamond end markers.
- Rounded visible strokes and joins.
- Less intrusive hover and selected-link halo.
- Smaller visible midpoint drag handle on desktop while coarse-pointer/mobile keeps a larger touch target.
- New links use a softer neutral default color without rewriting persisted user styling.

### Recommended next connector work
1. **Smart endpoints (P1):** optional Auto source/target side so connectors reattach to the nearest sensible side after major layout changes.
2. **Orthogonal routing (P1):** Straight / Elbow / Curved route modes, with Elbow as the professional process-map default candidate.
3. **Decision labels (P1):** lightweight Ja/Nej or custom labels anchored to connector segments.
4. **Insert-on-connector (P1 / v0.11):** select connector → `+ Infoga steg`, replacing A→B with A→new→B in one Undo action.
5. **Better bend editing (P2):** multiple bend points and segment-level dragging instead of one global midpoint/via point.
6. **Collision-aware routing (P2 / Smart Layout):** avoid routing through nodes and reduce line crossings.
7. **Global connector theme (P2):** apply color/width/route/marker defaults to all links without overwriting them accidentally one-by-one.

## Verification targets
- Python compile.
- All pytest regressions.
- All Node JS suites.
- Extracted embedded JS syntax.
- Desktop DOM contract.
- ZIP integrity.

## External changes
None. No Supabase migration, OAuth change, secrets change or dependency change.

## Verification result
- `python -m py_compile app.py google_docs.py maplini_google_ui.py` — passed.
- `pytest -q` — **149 passed**.
- All Node JS suites in `tests/*.js` — passed.
- Extracted main embedded JavaScript `node --check` — passed.
- BeautifulSoup desktop DOM contract — passed.
