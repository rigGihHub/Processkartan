# Maplini v0.10.27 — Startup, Session & Workspace State Hardening

## Verkliga problem som åtgärdats
- Login fortsatte tidigare med “Inloggad” och cloud-load även om `validateSession()` returnerade false.
- En ogiltig/utgången session rensade auth-token men återställde inte workspace/role-state.
- Vald workspace sparades inte per användare och kunde därför inte återställas deterministiskt vid startup.
- Om en tidigare vald workspace inte längre fanns bland användarens memberships kunde ett stale workspace-id ligga kvar.
- Byte mellan workspace/personligt kunde lämna cloud-loadade processer från föregående scope i samma lokala lista.
- Workspace change startade cloud-load utan await/rollback.

## Genomfört
- Ny `maplini_session_core.js` för user-scoped workspace preference, scope keys och validerad workspace selection.
- Login/signup kräver lyckad session-verifiering innan cloud-data hämtas.
- Invalid session återgår explicit till local-only + owner/personal UI.
- Workspace preference lagras per Supabase-user-id och används bara om membership fortfarande finns.
- Cloud-loadade processer scope-taggas; oförändrade kopior från föregående workspace tas bort vid scope-byte, medan lokalt nyare data skyddas av sync-reglerna.
- Workspace byte är async, sparar valet och har rollback vid exception.
- Startup kör local restore först, därefter validerad session/workspace/cloud-sekvens.

## Ej gjort
Ingen Supabase schema/RLS/OAuth/secrets-ändring och ingen live cloud-I/O i denna offline-release.
