# QA Audit v0.18.9

## Scope
Cross-device/cloud walkthrough history with local-first fallback.

## Verified
- Completed walkthroughs remain locally durable even if cloud sync fails.
- Signed-in cloud mode can GET walkthrough history for the current process.
- Cloud rows normalize into local history format and merge by run ID.
- Cloud save POST includes creator, canonical process owner, workspace scope, timestamps, result and detailed history.
- Follow-up status PATCH synchronizes handled/reopened state.
- A browser-level fake Supabase test verified GET, POST and PATCH request contracts and payload ownership fields.
- Existing full Chromium editor interaction smoke remains green.
- RLS migration defines workspace-aware read/create/update policies.

## Gates
- py_compile: passed.
- pytest: 223/223 passed.
- JavaScript suites: 27/27 passed.
- Full Chromium browser interaction smoke: passed.
- Focused Chromium fake-Supabase walkthrough API smoke: passed.
- Core JavaScript syntax: passed.
- Embedded JavaScript syntax: passed.
- Critical DOM hierarchy: passed.
- Duplicate HTML IDs: none detected.
- ZIP integrity: passed.

## Important deployment step
Run `supabase_schema_v0189.sql` in the Maplini Supabase project after the previous workspace/integrity migrations. Until then, the new release intentionally falls back to browser-local walkthrough history.

## Limitation
The cloud contract was browser-tested against a deterministic fake Supabase endpoint, not against the user's live Supabase project in this build environment.

## Deployment
Not pushed or deployed.
