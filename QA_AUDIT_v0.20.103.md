# v0.20.103 – mobilens redigeringsvy

Användarbilden från v0.20.102 visar en klippt verktygsrad, stor logotyp med dubblerad underrubrik och en karta med mycket tomrum. Den fasta snabbmenyn hamnar nedanför telefonens synliga område eftersom den förankras i en 920 px hög iframe.

## Ändringar

- Verktygsraden använder fyra kolumner och flera rader; processnamnet har en egen rad. Spara, Ny, Verktyg, arbetssätt och huvudmenyer är kvar.
- Mobilens logotyp är 130 px bred, rubrikområdet 44 px högt och den extra underrubriken dold.
- Snabbknapparna ligger ovanför kartan i sidans flöde. Kartan är 280–380 px hög. Fullskärmsläget behåller knappar vid nederkanten.
- Snabbmenyer för tillägg/egenskaper öppnas under knapparna; huvudmenyernas popover begränsas till redigerarens bredd.
- Läsväxling stänger redigeringspanelen och snabbmenyn.
- Testets HTML-extraktor fungerar utan att importera Playwright; webbläsartestet importerar det vid körning.

## Kontroller

- 516 Python-tester och 39 JavaScript-sviter godkända.
- 32 inbäddade skript syntaxkontrollerade.
- DOM-test av faktisk editor: mobil Lägg till skapar ett steg, Egenskaper öppnar panelen, namnändring uppdaterar steget, byte till läsvy stänger panelerna och placerar exportmenyn rätt.
- Befintliga tester av native lässvep, manuell redigeringspanorering, beslutsvägar, sparad data och ångra godkända.
- Python-kompilering och diffkontroll godkända.

DOM-testmiljön utför ingen verklig CSS-layout. Visuell kontroll och fysisk touch på Android/iOS återstår.
