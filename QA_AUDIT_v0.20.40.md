# QA Audit – Maplini v0.20.40

## Scope
Release focused on **Följ processen 2.0** only: clearer current action, operational wording, route consequence preview, subprocess continuity and mobile follow positioning. No new database schema, Supabase, RLS, OAuth or dependency changes.

## Functional checks
- Current step has explicit **Gör nu** hierarchy.
- Default quick checks render **Klart / Inte klart** while preserving yes/no state semantics and J/N keyboard compatibility.
- Route questions preview the unique Ja/Nej destination when labels are unambiguous.
- Single-path navigation uses **Fortsätt: [step]**.
- Subprocess completion explicitly returns to the parent flow and renders a one-step continuity notice.
- Mobile Follow resets the run panel to the current step after transitions.
- Existing deviation behavior is unchanged; no new deviation workflow was added.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **364/364 PASS**
- JavaScript test files: **27/27 PASS**
- Core JavaScript syntax (`node --check`): **22/22 PASS**
- Desktop Chromium interaction smoke: PASS
- Mobile Read/Follow Chromium smoke: PASS
- Mobile canvas fit/readability Chromium smoke: PASS
- v0.20.38 fast-building regression smoke: PASS
- v0.20.39 safe-cleanup regression smoke: PASS
- v0.20.40 dedicated Follow Process 2.0 mobile smoke: PASS

## Release integrity
- Critical editor DOM structure preserved.
- Static HTML IDs: **312**, duplicates: **0** (semantic BeautifulSoup check).
- Release ZIP integrity: PASS after packaging.
- Cache, pyc, venv, secrets and transient screenshots excluded from release package.

## Deployment status
Release candidate prepared only. **Not verified live and not pushed/deployed.**
