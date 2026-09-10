# QA Audit – Maplini v0.20.41

## Scope
Release focused on **Processkontroll**: concrete rule-based process checks, decision-route clarity, reachability from Start, start/end flow sanity, responsibility coverage and faster re-checking. No new database schema, Supabase, RLS, OAuth or dependency changes.

## Functional checks
- No synthetic process-health score is introduced; the UI still reports structural findings only.
- Decision with one explicit Ja/Nej route and no counterpart is flagged.
- Multi-route decision with no labels is flagged separately without assuming Ja/Nej semantics.
- Nodes unreachable from every Start are found even when they form their own connected island.
- Incoming flow to Start and outgoing flow from Slut are flagged as structural facts.
- Responsibility gaps reuse existing `processInfo.responsibleRole`; responsibility remains advisory, not mandatory.
- Every node-backed finding remains clickable on the canvas.
- Mobile closes the analysis panel after a canvas jump so the selected problem is visible.
- **↻ Igen** reruns the process check after changes.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **368/368 PASS**
- JavaScript test files: **27/27 PASS**
- Core JavaScript syntax (`node --check`): **22/22 PASS**
- Desktop Chromium interaction smoke: PASS
- Mobile Read/Follow Chromium smoke: PASS
- Mobile canvas fit/readability Chromium smoke: PASS
- v0.20.38 fast-building regression smoke: PASS
- v0.20.39 safe-cleanup regression smoke: PASS
- v0.20.40 Follow Process 2.0 regression smoke: PASS
- v0.20.41 dedicated Processkontroll browser smoke: PASS

## Release integrity
- Critical editor DOM structure preserved.
- Static HTML IDs: **313**, duplicates: **0** (semantic BeautifulSoup check).
- Release ZIP integrity: PASS after packaging.
- Cache, pyc, venv, secrets and transient screenshots are excluded from the release package.

## Deployment status
Release candidate prepared only. **Not verified live and not pushed/deployed.**
