# QA AUDIT — Maplini v0.20.33

## Scope
Mobile Read & Follow built incrementally from v0.20.32. No schema/RLS/OAuth/dependency changes.

## Product checks
- Mobile defaults to a consumption-first read mode after process restore.
- Explicit edit escape hatch remains for users with edit permission.
- Reader toolbar exposes Follow, Fit and Edit without exposing the full editing chrome.
- Read details use a touch-friendly bottom sheet.
- Follow Process uses a mobile bottom sheet with larger controls while keeping part of the canvas visible.
- Follow launched from mobile edit temporarily enables read mode and restores edit mode on close.
- Follow launched from read mode preserves read mode on close.

## Automated QA
- `python -m py_compile app.py` — PASS
- `pytest -q` — 335 passed
- JS test files — 27/27 PASS
- `node --check maplini_*_core.js` — 22/22 PASS
- Desktop Chromium interaction smoke — PASS
- Mobile Chromium read/follow smoke (390×844, touch/mobile context) — PASS
- Critical DOM / duplicate ID regression suite — PASS via pytest and explicit duplicate-ID check
- ZIP integrity — PASS

## Known limitations
- Mobile remains intentionally secondary for complex editing; desktop is still the primary authoring environment.
- Large-process mobile performance is not yet benchmarked separately.
- No background/offline installable PWA behavior was added.
