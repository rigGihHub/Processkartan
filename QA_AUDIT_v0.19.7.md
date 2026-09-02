# QA Audit – Maplini v0.19.7

## Scope
Visual hierarchy for the three core process building blocks: Object, Activity and Decision.

## Automated QA
- `python -m py_compile app.py`: PASS
- Python pytest: **231/231 passed**
- JavaScript test files: **27/27 passed**
- Full Chromium `tests/browser_interaction_smoke.py`: PASS
- Regression contract for v0.19.7 node hierarchy: PASS
- No Supabase migration required.

## Behavior preserved
- Node types and persisted process data are unchanged.
- Connector routing and Ja/Nej branch logic are unchanged.
- Follow Process behavior is unchanged.
- Start/End behavior is unchanged.
- No new settings or panels were introduced.

## Visual intent
- Object = compact, static input/output/result token.
- Activity = primary work step with strongest card hierarchy.
- Decision = distinct branch point with retained diamond geometry.
