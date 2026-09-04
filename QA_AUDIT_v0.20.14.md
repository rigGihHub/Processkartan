# QA Audit – Maplini v0.20.14 Branch Rejoin

## Scope
- Explicit branch rejoin for simple, unambiguous Ja/Nej flows.
- Shared next node is created from both terminal branch tips.
- Rejoin placement is centered between branch lanes and placed beyond the furthest tip.
- If blocked, placement prefers additional forward distance before cross-lane drift.
- Existing/manual node positions are never changed by the rejoin action.
- No schema or Supabase migration.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: 257/257 PASS
- JavaScript test files: 27/27 PASS
- `node --check` core JavaScript files: 22/22 PASS
- Chromium browser interaction smoke: PASS
- Critical DOM contract: PASS
- Duplicate static HTML IDs: 0
- ZIP integrity: PASS

## Release notes
- APP_VERSION: 0.20.14
- Release name: Branch Rejoin
- Live deployment was not performed or verified as part of this build.
