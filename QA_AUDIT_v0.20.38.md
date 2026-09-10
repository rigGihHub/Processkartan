# QA AUDIT – Maplini v0.20.38

## Scope
Fast process building on top of the existing direct-manipulation flow. The release reduces keystrokes between newly created steps, adds deterministic text-to-step inference for quick-build nodes, and guides Ja/Nej branch naming without generative AI.

## Product guardrails
- User-authored process content remains authoritative; Maplini does not generate or invent steps.
- Text inference is deterministic and limited to obvious patterns such as questions, action phrases and explicit end phrases.
- Existing Tab, explicit node-type menu and Ctrl/Cmd+Enter paths remain available.
- Existing Objekt → Aktivitet → Objekt methodology remains available; fast build is an additional low-friction path.
- No deviation/admin expansion.
- No Supabase migration, RLS, OAuth, dependency or persisted-schema change.

## QA results
- Python compile: PASS
- Python/pytest: **355/355 PASS**
- JavaScript test files: **27/27 PASS**
- Core JavaScript syntax (`node --check`): **22/22 PASS**
- Chromium desktop interaction smoke: PASS
- Chromium targeted fast-building smoke: PASS
  - Tab creates a quick-build step
  - `Godkänd?` becomes a Decision
  - Ja/Nej links are created
  - both branch labels are entered sequentially
- Chromium mobile Read/Follow smoke: PASS
- Chromium mobile canvas fit/readability smoke: PASS
- Critical desktop DOM/test contract: PASS via pytest suite
- Static HTML IDs: **307**, duplicates: **0**
- ZIP integrity: PASS

## Known limitations
- Text inference intentionally recognizes only clear wording; ambiguous wording keeps the chosen/current step type rather than guessing.
- After both decision branches are named, Maplini stops and leaves the user on the selected branch; it does not guess which branch should continue or whether branches should rejoin.
- Full automatic process generation is explicitly out of scope.
