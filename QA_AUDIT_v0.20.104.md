# v0.20.104 – tomrad i mobilfältet

Användarbilden från v0.20.103 visar Ny ensam till höger, följt av Verktyg och Spara på nästa rad. Knapparna hade samma CSS-order men olika kolumner; Ny förekom först i HTML och gridens placeringsmarkör fyllde nästa rad för de övriga.

## Ändring

- Tre explicita rader: namn, arbetssätt, sedan Spara/Ny/Exportera/Mer i fyra olika kolumner.
- Mobilens Start och Hitta flyttas till Mer. Samma DOM-element och händelsehanterare används; datorläget återställer originalplaceringen.
- Autosparstatus flyttas till logotypraden på mobilen.
- Dubblerad Verktyg-knapp i överfältet döljs. Snabbmenyns Verktyg finns kvar och verktygspanelen har en egen stängknapp.
- Standardmarkörerna före huvudmenyernas rubriker tas bort på mobilen. Inbäddad sökning öppnas inom Mer-panelens bredd.

## Kontroller

- 516 Python-tester och 39 JavaScript-sviter godkända.
- DOM-test med den faktiska mobil-CSS: de fyra processåtgärderna har samma uttryckliga grid-rad, olika kolumner och ingen dubblerad Verktyg-knapp i överfältet.
- Flyttad sökning behåller Mer öppet, visar riktiga träffar och markerar ett processsteg. Mobilens stängknapp stänger panelen. Flyttade kontroller återställs till datorfältet och tillbaka utan duplicering.
- Befintliga tester för läsa, redigera, lägga till, exportplacering, beslutsvägar och sparad data godkända.
- Python-kompilering och diffkontroll godkända.

DOM-testet aktiverar mobilregler explicit eftersom jsdom inte matchar skärmbredd. Det verifierar deklarationer och kontroller, men inte fysisk CSS-grid-layout eller touch på en telefon.
