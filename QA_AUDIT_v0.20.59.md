# QA Audit – Maplini v0.20.59

## Scope
Novice-first improvements to **Följ processen** without adding case-management behavior.

## Product checks
- Start copy explains **what to do now** and **what comes next**.
- Name/initials are optional; empty input is stored as `Anonym` instead of blocking the walkthrough.
- Every current step shows a compact **DÄREFTER** cue.
- One outgoing edge shows the actual next step.
- Multiple outgoing edges are described conservatively as multiple possible paths; Maplini does not guess the route.
- End state says that the process is complete (or returns from a subprocess).
- Existing yes/no routing, subprocess behavior and history remain intact.

## Automated QA
- `python -m py_compile app.py`: PASS
- `pytest -q`: **427 passed**
- all `tests/*.js`: PASS
- `node --check maplini_walkthrough_core.js`: PASS
- `tests/browser_v02059_walkthrough_first_use.py`: PASS
- `tests/browser_v02040_follow_process_2.py`: PASS
- `tests/browser_mobile_read_follow_smoke.py`: PASS
- `tests/browser_interaction_smoke.py`: PASS

## Release status
Push-ready candidate. Not deployed or live-verified.
