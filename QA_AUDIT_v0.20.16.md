# QA Audit – Maplini v0.20.16

## Release
- Version: `0.20.16`
- Name: **Smart Connector Routing**
- Base: v0.20.15 Flow Collision Prevention
- Supabase migration: **No**

## Scope verified
- Auto-managed orthogonal connectors can evaluate nearby process nodes as routing obstacles.
- The normal short orthogonal route remains preferred when it is clear.
- When blocked, the connector can choose an alternate corridor above, below or around the obstacle.
- Detours keep a short outward stub from source/target anchors so the connector leaves each node in the expected direction.
- Route scoring strongly penalizes obstacle intersections while still preferring shorter, simpler clean routes.
- Manual routing, free routing and manually controlled anchors are not rerouted by the feature.
- No existing node positions are changed.

## Automated QA
- `python -m py_compile app.py`: PASS
- `python -m pytest -q`: **261/261 PASS**
- JavaScript test files: **27/27 PASS**
- `node --check` core JS files: **22/22 PASS**
- `python tests/browser_interaction_smoke.py`: PASS
- Critical canvas DOM contract: PASS
- Duplicate literal HTML IDs in `app.py`: **0**

## Packaging
- ZIP excludes Python caches, `.pyc`, virtual environments and secret/env files.
- ZIP integrity checked after creation.
