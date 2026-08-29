# Maplini v0.10.32 — Final Pre-Push Audit & Cleanup

## Verkliga problem som hittades och fixades

1. **Shared privacy hade fortfarande en defense-in-depth-lucka**
   v0.10.31 gjorde `persist()` ephemeral i shared-view, men flera exportflöden kallade därefter
   `saveLocal(true)` direkt. Eftersom `processes` fortfarande innehåller shared-processen kunde den
   ändå skrivas till normal localStorage. `saveLocal()` har nu själv en privacy-guard.

2. **Shared-view använde gammal partiell UI-låsning**
   `loadShared()` satte manuellt vissa sidebar-kontroller och New/Save till read-only, men körde inte
   den centrala `applyRoleUi()` från v0.10.30. Därför kunde toolbar/processyta visuellt se redigerbara ut
   trots hårda guards. Shared startup använder nu hela centrala read-only-UI:n.

3. **Inline-edit muterade state före commit**
   label `input` skrev direkt till `item.data.text`. Därmed kunde en rollförlust mitt under redigering
   inte verkligen återställa originaltexten. Nu ändras DOM live men process-state commit sker först i
   `finishInlineEdit()`.

4. **Asynkron logouppladdning kunde slutföras efter rollförlust**
   FileReader callback kontrollerar nu `canEdit()` igen innan processloggan skrivs.

5. **Export preflight var duplicerad**
   PDF/DOCX/XLSX använder nu en gemensam `prepareExport()` med verifierad lokal pre-save.
   Shared-view förblir ephemeral genom `saveLocal()` privacy-guarden.

6. **Google Sheets direct-export loggade bara fel till console**
   Felet går nu även via centralt runtime error reporting.

## Pre-push status
Ingen ny produktfunktion. Fokus är release correctness, privacy, role consistency och minskad duplicering.
