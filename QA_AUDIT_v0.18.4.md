# QA Audit v0.18.4

## Scope
- Fix and harden `Snygga till`.
- Fix desktop/Chrome left-panel bottom scroll reachability.
- Add first usable version of `Följ processen` with configurable Ja/Nej control questions.

## Implemented
### Snygga till
- Automatic cleanup only rearranges nodes that are part of a connected flow.
- Isolated draft nodes remain in place.
- Layout spacing is tightened.
- The user's zoom/view is no longer changed automatically after cleanup.
- If no connected flow exists, the user gets a clear message instead of loose nodes being rearranged arbitrarily.

### Chrome sidebar
- Added desktop scroll padding and bottom breathing room to the left sidebar.
- Verified the final properties section can be reached at maximum scroll in Chromium.

### Följ processen
- New top-level `▶ Följ processen` action.
- Activity, Decision and Subprocess nodes can store reusable Ja/Nej control questions.
- Walkthrough follows the actual graph and uses Start nodes or graph roots as entry points.
- Required questions must be answered before proceeding.
- `Nej` answers are counted as deviations.
- Branches with multiple outgoing connectors are shown as explicit choices, using connector labels when present.
- Final summary shows steps, Ja, Nej and each deviation with step/question context.
- Result can be copied.
- Walkthrough run history is session-only in this first version; permanent execution history is not claimed.
- Questions are stored inside existing process JSON; no Supabase/database migration is required.

## Regression fixes
- Fixed Ctrl/Cmd multi-select behavior after the direct-drag change.
- Browser smoke baseline updated to current Objekt → Aktivitet methodology.

## QA gates
- Python compile: passed.
- Pytest: 217/217 passed.
- JavaScript suites: 27/27 passed.
- Full browser interaction smoke: passed.
- Focused Chromium smoke for sidebar reachability, safe auto-clean, question persistence and interactive walkthrough: passed.
- Walkthrough, state and layout core JavaScript syntax: passed.
- Critical editor DOM hierarchy retained.

## Known limitation / deliberate next step
- Walkthrough execution results are not yet stored permanently or tied to authenticated users.
- Branch navigation is explicit when multiple outgoing links exist; a future version can map a Decision question's Ja/Nej answer directly to Ja/Nej connector branches.

## Deployment
Not pushed or deployed by ChatGPT.
