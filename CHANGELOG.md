# v0.10.32 — FINAL PRE-PUSH AUDIT & CLEANUP

- Added a privacy guard directly inside `saveLocal()` so shared-view can never enter the normal local process store through another caller.
- Shared-link startup now uses centralized `applyRoleUi()` and control refresh instead of partial legacy locking.
- Inline editing no longer mutates process text state before commit.
- Async logo upload re-checks edit permission on FileReader completion.
- Centralized PDF/DOCX/XLSX pre-export persistence in `prepareExport()`.
- Direct Google Sheets export failures now use centralized runtime error reporting.
- Added final pre-push regressions.
- No dependency, database, OAuth/secrets, or external configuration changes.

Active chain:
v0.10.13 → v0.10.15 → … → v0.10.31 → v0.10.32.
v0.10.14 remains parked.
