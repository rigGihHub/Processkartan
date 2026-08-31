# QA Audit – Maplini v0.13.1

## Scope
Autosave status, staged recovery snapshot and interrupted-session recovery.

## Functional verification
- Autosave state displays Saving / Autosaved with local time / Save error.
- A recovery snapshot is staged immediately when editable process content changes.
- The staged snapshot is removed only after the primary localStorage payload has been written and verified.
- A leftover recovery snapshot is offered as an explicit Restore / Ignore choice on next startup when it differs from primary data.
- Shared read-only links remain excluded from local persistence.
- Lifecycle flush covers visibilitychange, pagehide, freeze and beforeunload.

## Automated QA
- Python: 165/165 pytest passed.
- JavaScript: 23/23 test suites passed.
- `python -m py_compile app.py google_docs.py maplini_google_ui.py`: passed.
- `node --check maplini_*_core.js`: passed.
- Longest rendered embedded editor script: `node --check` passed.
- Desktop DOM contract: `.p48-body`, `.p48-side`, `#p48-scroll`, `#p48-controls`, `#p48-canvas` nesting verified.

## Release notes
- No database/Supabase schema changes.
- No new runtime dependencies.
- This package is a local push candidate and is not verified live until deployed.
