# QA Audit v0.19.0

## Scope
Cross-process deviation dashboard built on walkthrough history and v0.18.9 cloud sync.

## Verified
- Dashboard opens from the top toolbar and can be closed via button/backdrop/Escape.
- Open, overdue and resolved counters reflect individual deviations.
- Default filter shows open deviations.
- Owner search and overdue-only filtering work.
- Overdue detection compares saved ISO due date with the browser's local current date.
- Rows show process, question/step, explanation, owner, due date and status.
- A focused Chromium smoke used three deterministic runs: one overdue open deviation, one future open deviation and one resolved deviation.
- The focused smoke verified counters, sorting, overdue visual/text state, owner filter, overdue filter, resolving a run from the dashboard and resolved filtering.
- Existing full Chromium editor interaction smoke remains green.
- Cloud scope loader uses the existing v0.18.9 `walkthrough_runs` table and RLS.

## Gates
- py_compile: passed.
- pytest: 224/224 passed.
- JavaScript suites: 27/27 passed.
- Full Chromium browser interaction smoke: passed.
- Focused Chromium deviation-dashboard smoke: passed.
- Core JavaScript syntax: passed.
- Embedded JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Data-model limitation
Follow-up status is currently stored per walkthrough run, not per individual deviation. A walkthrough containing multiple deviations is therefore handled/reopened as one follow-up unit. Per-deviation lifecycle should be a future schema change if finer-grained ownership/status is needed.

## Database
No new migration for v0.19.0. Cloud dashboard data requires the existing `supabase_schema_v0189.sql`.

## Deployment
Not pushed or deployed.
