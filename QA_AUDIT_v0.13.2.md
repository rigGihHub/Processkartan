# QA Audit – Maplini v0.13.2

## Scope
Mobile contextual editing sheet and fullscreen canvas mode.

## Functional verification
- Mobile Add opens a dedicated bottom-sheet with Start, Aktivitet, Beslut, Dokument, Delprocess, Anteckning and Slut.
- Selected-node mobile context exposes copy, formatting, selected Smart Layout and delete without requiring the sidebar for common actions.
- Fullscreen hides brand/top toolbar, expands the canvas viewport and keeps the fixed mobile action bar available.
- Browser Fullscreen API is requested from the user gesture when available; CSS fullscreen remains the fallback.
- Fullscreen exit via browser/system event restores Maplini state without leaving body scrolling locked.
- Sidebar remains available for advanced properties and is closed when fullscreen starts.

## Automated QA
- Python: 166/166 pytest passed.
- JavaScript: 23/23 test suites passed.
- `python -m py_compile app.py google_docs.py maplini_google_ui.py`: passed.
- `node --check maplini_*_core.js`: passed.
- Longest rendered embedded editor script: `node --check` passed.
- Desktop DOM contract verified: `.p48-body`, `.p48-side`, `#p48-scroll`, `#p48-controls`, `#p48-canvas` retain required nesting.

## Release notes
- No database/Supabase schema changes.
- No new runtime dependencies.
- Local push candidate; not verified live until deployed.
