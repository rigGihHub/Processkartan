# Maplini v0.10.26 — Save/Cloud Consistency & Recovery Audit

## Fixat
- Backup recovery promotion fungerade inte: backupen laddades men kunde hoppas över vid write-back eftersom `lastLocalPayload` redan matchade. Recovery tvingar nu primary-write.
- `maplini_pre_delete_snapshot` skapades men användes inte. Den är nu sista recovery-fallback efter primary, backup, emergency och legacy.
- `saveLocal(true)` returnerar nu verifierad success/failure och lämnar dirty-state kvar efter write-fel.
- Cloud load hämtar `updated_at` och får inte skriva över en lokalt nyare process med samma id.
- Cloud save använder en enda stabil snapshot i stället för flera `state()`-anrop.
- Save-knappens statusmeddelanden skiljer mellan lokal success, cloud success och respektive fel.
- Sign-out tar bort oförändrade cloud-loadade browserkopior men behåller lokalt nyare arbete.

## Ny modul
`maplini_sync_core.js` kapslar content-change, tidsjämförelse, cloud merge och signout-plan.

## Ej gjort
Ingen Supabase-migrering, RLS-ändring, OAuth/secrets-ändring eller live cloud-I/O görs i denna offline-release.
v0.10.14 SECURITY är fortfarande parkerad.
