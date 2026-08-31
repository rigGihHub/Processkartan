# Maplini v0.13.0

## Mobile Context & Fullscreen v0.13.2

- **Lägg till** använder en mobil bottom-sheet för de vanligaste nodtyperna; vänsterpanelen behöver inte öppnas för att bygga flödet.
- Markerade rutor har en mobil kontextmeny för kopiera, formatering, Smart Layout och borttagning.
- **Helskärm** maximerar canvasen på telefon och använder Fullscreen API där webbläsaren tillåter det, annars en CSS-baserad fallback.
- Fullskärmsläget kan lämnas med knappen **Avsluta**, Escape eller webbläsarens/systemets fullscreen-exit.
- Avancerade inställningar finns kvar via **Alla verktyg och inställningar/Fler egenskaper**.


## Mobile UX v0.13.0

- Fast kontextuell nederkantstoolbar på mobil för de vanligaste kommandona.
- Dra på tom canvas för att panorera; två fingrar för pinch-zoom.
- Större touchmål för kopplingar och handtag.
- Mobil processyta har egen scroll/pan-viewport så editorinteraktion inte konkurrerar med sidscroll.
- Befintlig verktygspanel öppnas fortfarande från **Verktyg** eller **Egenskaper** när mer avancerade inställningar behövs.


## Smart Layout v0.12.1

### Smart Layout refinement v0.12.1
- Decision branches use connector labels as layout semantics: **Ja** is placed before/above (or left in vertical layout) and **Nej** after/below (or right).
- Iterative barycentric ordering reduces avoidable connector crossings between adjacent flow levels.
- Directed cycles are detected as feedback edges before rank calculation, preventing loop rank explosion while keeping the main flow compact.
- Full-process and selected-only layout keep the existing single-Undo, node-size, selection and connector redraw behavior.


- **✨ Snygga till ▾** ordnar hela processen eller endast markerade rutor.
- Välj horisontellt eller vertikalt flöde.
- Kopplingarna används för att förstå ordningen i flödet; grenar placeras bredvid varandra och merges senare i flödet.
- Layouten bevarar nodstorlek och urval, ritar om pilar och skapar en Undo-checkpoint per körning.
- Layoutlogiken ligger i `maplini_layout_core.js` och kräver ingen ny dependency eller databasändring.


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


## v0.11.4 – raka kopplingar och komplett sidscroll

- Markerad koppling kan växlas till **Routing → Rak** och blir då en verklig rak linje även om den tidigare haft en manuell brytpunkt.
- Vänster verktygs-/formateringspanel kan scrollas hela vägen till sista kontrollen på desktop och mobil.

## v0.11.3 – snabbare layout
Toolbaren har nu **⊡ Anpassa** för fit-to-screen och **Ordna ▾** för justering/fördelning av flera markerade rutor. Funktionerna ändrar inte nodstorlekar och pilar uppdateras tillsammans med rutorna.

## v0.11.5 – snabbval direkt på pil

- Markera en pil på canvasen för att få direktvalen **Rak** och **Vinkelrät** intill pilen.
- Aktivt val visas markerat.
- Byte till Rak tar bort äldre brytpunkter och skapar en verkligt rak koppling.
- Funktionen fungerar med Undo och döljs i read-only-läge.



## v0.11.7 – contextual toolbar
- Markerad ruta visar en kompakt snabbmeny direkt vid urvalet.
- Enkelmarkering: **＋ Nästa**, **Formatera**, **Duplicera**, **Ta bort**.
- Multi-select: **Formatera**, **Färg**, **Duplicera**, **Ordna**, **Ta bort**.
- **Ordna** ger snabb åtkomst till justering och jämn fördelning utan att gå via toppmenyn.
- Snabbmenyn följer urvalet vid flytt och behåller samma visuella storlek vid zoom.
- Formatera öppnar/fokuserar den befintliga formateringspanelen; ingen parallell formateringslogik har skapats.
- Alla redigeringskommandon återanvänder befintlig Undo-, selection- och read-only-logik.

## v0.11.6 – formatera flera rutor samtidigt

Markera två eller fler rutor för att använda samma Formatering-panel på hela markeringen. Du kan ändra typsnitt, textstorlek, färger, kant, rutstil, fet/kursiv/understruken text och textjustering i ett moment. Multi-select ligger kvar efter ändringen och varje åtgärd är en Undo-operation. Dokumentlänk och Inputs/Outputs fortsätter vara enkelrute-funktioner.

### Autosave och återställning (v0.13.1)
Maplini visar löpande sparstatus och använder en kortlivad recovery-snapshot mellan redigering och verifierad lokal sparning. Om en session avbryts mitt i detta fönster visas vid nästa start ett val att återställa eller ignorera de avbrutna ändringarna. Mobilens appväxling och sidstängning triggar dessutom omedelbar lifecycle-save.
