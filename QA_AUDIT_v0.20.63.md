# QA Audit – Maplini v0.20.63

## Scope
Process Navigator for large process maps: start/end jumps, previous/next navigation following stored process links, explicit choices when several routes exist, and fit-to-screen from the overview.

## Results
- Python compile: PASS
- pytest: 434 passed
- JavaScript unit tests: 38 test files PASS
- node --check: 30 core files PASS
- Chromium interaction smoke: PASS, including Start → Next → End → Previous navigation
- Branch behavior: PASS in maplini_navigation_core unit test; multiple routes stay explicit and are not auto-selected
- Critical DOM ancestry: PASS
- Static duplicate HTML IDs: PASS
- Supabase/RLS/OAuth/schema changes: none

## Product guardrails
- Navigation uses only existing node/link data.
- No process content is inferred or changed.
- Multiple possible routes are shown as choices rather than guessed.
