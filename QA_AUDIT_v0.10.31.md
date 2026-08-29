# Maplini v0.10.31 — Shared Privacy & Editor State Hardening

## Verkliga problem
1. Public shared-view kunde exporteras eller sidan kunde döljas/stängas efter att `persist()` körts.
   `persist()` skrev då den delade processens payload till Maplinis vanliga localStorage-store.
   Det innebar att en process öppnad via en publik read-only-länk kunde lämnas kvar i webbläsarens
   lokala processdata och dyka upp i senare sessioner.
2. `refreshControls()` → `setFormatEnabled()` kunde återställa `disabled=false` på formatkontroller
   efter att roll-UI tidigare satt viewer/shared till read-only.
3. Några mutationsvägar saknade fortfarande hårda guards: Input/Output-editor samt border color/width
   när en connector var vald.
4. Ett inline-edit som redan var öppet när rollen växlade till read-only kunde avslutas och persista texten.

## Fix
- Ny `maplini_privacy_core.js`.
- Shared-view är ephemeral och skrivs aldrig till den vanliga lokala process-store:n.
- visibility/beforeunload skippar lokal process-save för shared-view.
- Formatkontroller respekterar `canEdit()` även vid selection refresh.
- IO och connector-border mutationsvägar har `requireEdit()` guards.
- Pågående inline-edit avbryts och återställs om editbehörigheten har försvunnit.

## Ej ändrat
Vanliga personliga/workspace-processer fortsätter använda lokal cache/recovery enligt tidigare releases.
Export från shared-view är fortfarande tillåtet men skapar ingen lokal Maplini-processkopia.
