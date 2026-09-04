# QA Audit – Maplini v0.20.30

## Scope
Linked subprocess hierarchy and breadcrumb navigation. No Supabase migration, RLS change or new table.

## Intended behavior
- Selecting a Delprocess exposes **Öppna delprocess** in the contextual toolbar.
- First open creates a separate child process and links it to the selected subprocess node.
- Reopening the same node reuses the existing child process.
- Breadcrumb navigation appears only when inside a child process.
- Returning to a parent reselects the subprocess node that leads to the child.
- Pasted/duplicated subprocess nodes do not inherit the original child link.
- Existing overview, Follow Process and canvas editing behavior remain unchanged.

## Verification
- `python -m py_compile app.py`: PASS
- Python pytest: 318/318 PASS
- JS test files: 27/27 PASS
- Core JS `node --check`: 22/22 PASS
- Chromium interaction smoke: PASS
- Critical DOM structure: PASS
- Duplicate literal HTML/DOM IDs: 0
- No Supabase migration required
