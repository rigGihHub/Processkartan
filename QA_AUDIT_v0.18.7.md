# QA Audit v0.18.7

## Scope
Separate compliance questions from neutral process-routing questions.

## Verified
- New questions default to `Kontrollfråga`.
- A question can be changed to `Vägvalsfråga`.
- Legacy `route:true` questions remain route questions after normalization.
- `Nej` on a control question is an actionable deviation.
- `Nej` on a route question is a normal route answer and is not a deviation.
- Route questions still automatically select unique Ja/Nej connectors.
- Walkthrough UI labels each question as KONTROLL or VÄGVAL.
- Live deviation count reflects only control deviations.
- Final completion status and stored follow-up state use actual deviation count, not raw No count.
- Focused Chromium smoke completed two runs:
  1. Control=Ja + Route=Nej -> 0 deviations, automatic Nej branch, approved result.
  2. Control=Nej + Route=Ja -> 1 deviation, automatic Ja branch, follow-up required.
- Existing full browser interaction smoke remains green.

## Gates
- py_compile: passed.
- pytest: 220/220 passed.
- JavaScript suites: 27/27 passed.
- Full Chromium browser interaction smoke: passed.
- Focused Chromium control-vs-route smoke: passed.
- Core JavaScript syntax: passed.
- Embedded JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Compatibility note
Previously saved local v0.18.6 walkthrough runs did not persist question kind per answer. They remain readable; new v0.18.7 runs contain the richer semantics needed for accurate control-vs-route reporting.

## Deployment
Not pushed or deployed.
