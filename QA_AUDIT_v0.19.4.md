# QA Audit v0.19.4

## Scope
Smart Ja/Nej branching from decision nodes.

## Verified behavior
- A decision node exposes a dedicated `Ja + Nej` action in its next-step menu.
- The action creates two activity nodes in one undoable operation.
- The branches use the existing smart-next positioning engine with deterministic branch slots 0/1.
- Connector labels are explicitly stored as `Ja` and `Nej`.
- If one labeled branch already exists, only the missing branch is created.
- If both already exist, no duplicate pair is created.
- Ctrl/Cmd+Enter while editing a decision creates the Ja/Nej pair instead of a single unlabeled next activity.
- Existing Follow Process routing remains based on connector labels and was not rewritten.

## QA executed
- `python -m py_compile app.py`: passed.
- Python pytest: 228/228 passed.
- JavaScript suites: 27/27 passed.
- `node --check` on all `maplini_*_core.js`: passed.
- Full `tests/browser_interaction_smoke.py`: passed.
- Browser smoke includes a focused v0.19.4 assertion: decision `n3` creates exactly two new nodes and outgoing connector labels include both `Ja` and `Nej`.
- Critical editor DOM ids/hierarchy presence check: passed.
- Duplicate literal HTML id check: passed.

## Migration
No new Supabase migration is required for v0.19.4.
