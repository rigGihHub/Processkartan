# Maplini v0.11.2

Byggd vidare från v0.11.0.

`Processyta ▾` innehåller nu ett komplett bakgrundsbibliotek:
mönster, solid färg, gradient, uppladdad bild, vattenstämpel och materialtexturer.

Inställningarna sparas i processens befintliga state och kräver ingen databasändring.



### v0.10.44
- Kopplingar kan ha redigerbar textetikett, t.ex. Ja/Nej/Godkänd/Avslag.
- De två första nya utgående kopplingarna från en Beslut-nod får automatiska, redigerbara Ja/Nej-förslag.
- Etiketter följer connectorns geometri och exporteras till processbild samt Excel/Google Sheets.

### v0.10.43
- Kopplingar som sitter i en ruta uppdateras kontinuerligt när rutan flyttas eller storleksändras.
- Geometriändringar från text och formatering markerar också berörda kopplingar för omritning.
- Pilar har fått renare visuellt uttryck: mindre proportionerliga pilspetsar/markörer, rundare linjeändar, diskretare markeringshalo och mindre desktop-draghandtag.
- Nya kopplingar använder en något mjukare neutral standardfärg.

### v0.10.41
- Dokumentlänkar läggs nu in direkt i dokumentrutan på canvasen via ett inline-fält med Spara/Enter.
- Markerad ruta behåller aktivt redigeringsläge när rutstil eller annan nodformatering ändras.
- Vertikal scroll har förenklats: iframe-scrollen är borttagen, sidopanelens dubbla scrollbar är dold men wheel/touch fungerar, och scroll chaining begränsas.

### v0.10.40
- Dropdown menus auto-close on outside click.
- Visual node styles: Standard, 3D, Raised, Glass and Flat, individually or globally.


### v0.10.45
Markerad pil kan nu delas med **＋ Infoga steg**, vilket skapar en ny aktivitet direkt i flödet och öppnar textredigering.

### v0.10.46
Markerad pil → **＋ Infoga steg** → välj Aktivitet, Beslut, Dokument eller Slut. Det nya steget placeras direkt i flödet och öppnas för redigering.

## Faster Editing v0.11.1

- Multi-select kan nu dras som en grupp.
- Interna och externa pilar följer gruppen korrekt under flytt.
- Gruppflytt är en Undo-operation och markeringen ligger kvar efter dragning.

## Faster Editing v0.11.0
- Duplicera markerade rutor via knapp eller Ctrl/Cmd+D.
- Kopiera/klistra in via Ctrl/Cmd+C/V.
- Flera markerade rutor kopieras som grupp och behåller interna pilar.
- Externa pilar till objekt utanför markeringen kopieras inte.


## Faster Editing v0.11.2
- Markerad flödesruta visar en kompakt **＋ Nästa steg**-knapp direkt vid rutan.
- Välj Aktivitet, Beslut, Dokument eller Slut; Maplini placerar steget på en ledig närliggande yta och kopplar det automatiskt.
- Beslut behåller smarta Ja/Nej-förslag på nya grenar.
- Det nya steget markeras och öppnas direkt för textredigering. Enter avslutar snabb textredigering; Shift+Enter kan användas för radbrytning.
- Skapande + koppling är en enda Undo-operation.


## v0.11.3 – snabbare layout
Toolbaren har nu **⊡ Anpassa** för fit-to-screen och **Ordna ▾** för justering/fördelning av flera markerade rutor. Funktionerna ändrar inte nodstorlekar och pilar uppdateras tillsammans med rutorna.
