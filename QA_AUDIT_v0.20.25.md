# QA Audit – Maplini v0.20.25 Safe Cloud Editing

## Scope
Optimistic concurrency protection for process cloud saves. No realtime collaboration, no schema migration, no RLS change.

## Verified behavior
- Existing cloud row uses conditional PATCH filtered by both process id and the previously loaded `updated_at`.
- Conditional PATCH must update exactly one row; zero rows becomes `CLOUD_CONFLICT`.
- Unknown cloud base checks for an existing row before insert.
- Insert race HTTP 409 becomes `CLOUD_CONFLICT`.
- Conflict path leaves the current process in local storage and does not perform a fallback overwrite.
- Persistent account status communicates that cloud saving was stopped because another cloud version exists.

## Regression QA
- `python -m py_compile app.py`: PASS
- Python pytest: 291/291 PASS
- JS test files: 27/27 PASS
- Core JS `node --check`: 22/22 PASS
- Chromium browser interaction smoke: PASS
- Critical DOM hierarchy: PASS
- Duplicate literal DOM IDs: 0
- ZIP integrity: PASS

## Data / security impact
- No Supabase migration.
- No database schema change.
- No RLS/OAuth/secret/dependency change.
- Cloud write semantics are stricter: conflicts stop writes instead of silently overwriting.

## Known limitation
This release detects and blocks conflicts. It does not yet provide a dedicated merge UI; the user's edited copy remains local when a conflict is detected.
