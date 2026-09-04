# QA Audit – Maplini v0.20.11

Release: **Direct Manipulation Polish**

## Scope
- Single-node contextual toolbar no longer duplicates the primary next-step action.
- Direct `+` next-step control polished and kept as the main flow-building interaction.
- Selected-node connection points and selection emphasis visually calmed without removing functionality.
- Mobile touch sizing retained.

## Executed QA
- `python -m py_compile app.py`: PASS
- Python pytest: **252/252 PASS**
- JavaScript test files: **27/27 PASS**
- `node --check` on core JS files: **22/22 PASS**
- Chromium `browser_interaction_smoke.py`: **PASS**
- Critical DOM hierarchy: **PASS via regression/desktop contract suite**
- Literal HTML ID duplicate scan: **0 duplicates**
- ZIP integrity: checked after packaging

## Data / migration
No Supabase migration required. No data model, OAuth, RLS, secret or dependency change.
