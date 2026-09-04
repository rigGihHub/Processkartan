# QA Audit – Maplini v0.20.31

## Scope
Follow Process Through Subprocesses, built from v0.20.30.

## Product constraints
- Keeps subprocess navigation lightweight.
- No BPMN gateway semantics, task management, new database tables or deviation expansion.
- Unlinked subprocess nodes continue to behave as ordinary walkthrough steps.

## Functional checks
- Linked subprocess is entered from Follow Process.
- Unique child start auto-opens.
- Multiple child starts require explicit user choice.
- Empty child returns safely to parent.
- Child completion resumes the stored parent continuation.
- Nested stack can unwind across multiple levels.
- History stores process context per step.
- Completed run remains associated with the root process.
- Closing a nested walkthrough returns editor to root process.

## Automated QA
- Python compile: PASS
- Python tests: 327/327 PASS
- JavaScript test files: 27/27 PASS
- Core JavaScript syntax checks: 22/22 PASS
- Chromium general interaction smoke: PASS
- Chromium subprocess walkthrough smoke: PASS
- Critical DOM hierarchy: PASS
- Duplicate literal HTML IDs: 0
- ZIP integrity: PASS

## Schema / security
No Supabase migration, RLS, OAuth, secrets or dependency changes.

## Release status
Release candidate generated in ChatGPT workspace. Not verified live and not pushed/deployed.
