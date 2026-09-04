# QA Audit – Maplini v0.20.28

## Scope
Deviation to Improvement Loop. No database schema, RLS, routing engine or walkthrough answer semantics changed.

## Intended behavior
- Open deviations expose **Förbättra steg**.
- The originating process and node are opened and focused.
- The deviation observation stays visible while the user edits the process.
- Node properties are reachable directly from the improvement context.
- Resolution reuses the existing walkthrough deviation status update path.
- Restoring another process clears the active improvement context.

## Verification
- `python -m py_compile app.py`: PASS
- Python pytest: 307/307 PASS.
- JS test files: 27/27 PASS.
- Core JS `node --check`: 22/22 PASS.
- Chromium interaction smoke: PASS.
- No Supabase migration required.

- Critical DOM structure: PASS.
- Duplicate HTML/DOM IDs: 0.
- Improvement context clears on process restore: verified by source regression contract.
