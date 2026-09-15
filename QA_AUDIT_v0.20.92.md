# QA audit – Maplini v0.20.92

## Fokus

Förstå ska byta innehåll, inte få hela vänsterflanken att försvinna. Desktop får därför en stabil navigationspanel medan mobil fortsätter prioritera canvasen.

## Verifierat

- Vänsterkolumnens bredd och arbetsytans grundstruktur består vid byte mellan Rita och Förstå.
- Rit- och formateringsverktyg visas inte i Förstå.
- Steglistan är klickbar, markerar aktuellt steg och centrerar valet på canvasen.
- Början använder den befintliga kopplingsbaserade navigatorn och gissar inte en gren.
- Visa hela använder samma beprövade fit-funktion som övriga gränssnittet.
- Mobil behåller fullbreddsläget.

## Automatiska kontroller

- `pytest`: 513 godkända
- JavaScript: 38 testfiler godkända
- Core JavaScript: 30 filer syntaxkontrollerade
- Python-kompilering och `git diff --check`: godkända
