# QA Audit – Maplini v0.20.12

Release: **Smart Branch Layout**

## Scope
- Ja/Nej-grenar som skapas tillsammans planeras som ett par.
- Grenarna delar framåtrank och balanseras runt beslutets mittlinje.
- Vid upptagna standardlägen expanderar paret symmetriskt eller flyttas framåt.
- Ja/Nej-semantiken behålls i både horisontellt och vertikalt flöde.
- En ensam saknad gren använder befintlig smart placering.
- Inga redan manuellt placerade rutor flyttas av funktionen.

## Executed QA
- `python -m py_compile app.py`: **PASS**
- Python pytest: **253/253 PASS**
- JavaScript test files: **27/27 PASS**
- `node --check` on core JS files: **22/22 PASS**
- Chromium `browser_interaction_smoke.py`: **PASS**
- Browser smoke verifies paired decision geometry: **PASS**
- Critical DOM hierarchy: **PASS**
- Literal HTML ID duplicate scan: **0 duplicates**
- ZIP integrity: checked after packaging

## Data / migration
No Supabase migration required. No data model, OAuth, RLS, secret or dependency change.
