# Maplini v0.10.28 — Final Stabilization & Release Candidate Audit

## RC-audit
Den aktiva kedjan v0.10.13 → v0.10.27 granskades med fokus på startup, session/workspace,
local/cloud save, recovery, destruktiva flöden, mobile/desktop-kontrakt, connector/state,
export och runtime error reporting.

## Verkliga problem fixade
1. `loadCloudProcesses()` fångade sina egna exceptions och returnerade inget.
   Workspace-handlerns try/catch från v0.10.27 kunde därför **inte faktiskt rollbacka ett misslyckat workspacebyte**.
2. Cloud scope-cleanup gjordes före network fetch. Om fetchen sedan misslyckades kunde UI/state redan ha
   ändrats trots att cloud-load misslyckats. Scope/process-state snapshotas nu och återställs på fel.
3. `createWorkspace()` kunde alltid säga “Workspace skapat” även om efterföljande cloud-load misslyckades.
4. Share-fel gick inte genom det centrala runtime-errorflödet.
5. visibility/beforeunload-save svalde fel helt. Lifecycle save använder nu verifierad save-status och error reporting.

## Ny modul
`maplini_rc_core.js` innehåller testbara release-invariants och scope snapshot/rollback.

## RC-status
Automatiserad syntax, DOM, unit/regression och cross-module E2E körs på hela paketet.
Ingen live deployment, fysisk Android/iPhone-session, riktig Supabase I/O eller Google Drive-write påstås verifierad.

## Parkerat
v0.10.14 SECURITY / Supabase-migreringen är fortsatt parkerad eftersom den kräver extern manuell åtgärd.
