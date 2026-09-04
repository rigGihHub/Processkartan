# QA Audit – Maplini v0.20.15

## Release
- Version: `0.20.15`
- Name: **Flow Collision Prevention**
- Base: v0.20.14 Branch Rejoin
- Supabase migration: **No**

## Scope verified
- Automatic next-step placement can consume existing connector segments as layout obstacles.
- Candidate nodes are penalized when they overlap or sit too close to an existing connector.
- Candidate routes are also penalized when their preliminary source-to-target path crosses an existing connector.
- Source-connected links are excluded from obstacle collection to avoid false conflicts at legitimate attachment points.
- Collision-aware placement is wired into normal next steps, decision branches, branch continuation and branch rejoin.
- Existing/manual node positions are not changed by the feature.

## Automated QA
- `python -m py_compile app.py`: PASS
- `python -m pytest -q`: **259/259 PASS**
- JavaScript test files: **27/27 PASS**
- `node --check` core JS files: **22/22 PASS**
- `python tests/browser_interaction_smoke.py`: PASS
- Critical canvas DOM contract: PASS
- Duplicate literal HTML IDs in `app.py`: **0**

## Packaging
- ZIP excludes Python caches, `.pyc`, virtual environments and secret/env files.
- ZIP integrity checked after creation.
