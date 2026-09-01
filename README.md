## UI Regression Fix v0.13.4

- Fixar regressionen där canvasens kontextverktyg (`Rak/Vinkelrät` och nodens snabbmeny) renderades som vanliga HTML-kontroller uppe till vänster trots att inget var markerat.
- Grundorsak: toolbar-CSS låg i Streamlit-förälderns stylesheet medan editorn körs i ett separat `components.html`-iframe. CSS kan inte korsa iframe-gränsen.
- Flyttar/duplicerar därför toolbarernas visibility-, layout-, hover-, active- och touch-regler till editorns eget iframe-stylesheet.
- Båda toolbarerna är nu `display:none` som standard och visas endast när JavaScript sätter `.on` efter korrekt nod-/pilmarkering.
- Ingen databas-, Supabase- eller dependencyändring.

# Maplini v0.18.2

## Process Intelligence v0.18.2

- **🔍 Analysera** öppnar Processkontroll med en deterministisk strukturanalys av aktuell process.
- Visar processhälsa, fel, kontrollpunkter och insikter.
- Kontrollerar Start/Slut, isolerade rutor, inkommande/utgående flöden, beslut, loopar, långa sekvenser samt flödeskoncentrationer.
- Klick på ett fynd markerar och centrerar berörda rutor på canvasen.
- V0.14.1 ändrar inte processdata, Supabase-schema eller dependencies.


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


### v0.13.4
- Desktop sidebar scroll fix: persistent vertical scrolling, stable scrollbar gutter and bottom clearance so the final connector controls remain reachable.


### v0.18.2
Connector drag, multi-page horizontal scrolling and verified zoom direction.


### v0.18.2
Förfinar Smart Layout-pilarnas centrering, desktop-sidebarens åtkomlighet, rutstilar och den samlade textformateringen.


### v0.18.2
UI simplified: Ordna removed, compact account panel, dedicated Logotyp menu, and whole-process scaling including fit to selected A4/A3 page.


### v0.18.2
Connector dragging fixed: click-drag works directly on the connector hit area without a separate pre-selection click.


### v0.18.2
Stability/UX cleanup: dynamic multi-page layout bounds, resilient toolbar positioning, resize recalculation and centralized popover cleanup.


### v0.18.2
Free connector routing: drag the arrow body independently while endpoints remain attached and continue following moved nodes. Includes a small visual/UX polish pass.


### v0.18.2 – Integrity & Core Interaction
This release fixes workspace ownership integrity, connector one-gesture/free-drag behavior and Google Sheets column alignment.

**Supabase:** deployments using workspaces must run `supabase_schema_v0147.sql` after updating the app. The migration preserves editor access but enforces the workspace owner as canonical `processes.owner_id`.

**Browser smoke QA:** `python tests/browser_interaction_smoke.py` runs the embedded editor in Chromium and verifies one-gesture connector drag, attached endpoint behavior after moving a node, and Undo.


### v0.18.2
30% Simpler: the main toolbar now exposes only core commands. Export/page settings are grouped under Export, secondary tools under More, and the normal mobile bar is reduced to four actions.


### v0.18.2
Stability/polish pass for the simplified command surface. Nested menus now remain open correctly, mobile keeps four primary actions while Redo/Fullscreen remain available secondarily, and browser smoke coverage validates these flows together with free connector dragging.


### v0.18.2
Actionable Process Check: structural findings now explain what to do next, are prioritized, and can focus affected nodes directly on the canvas. The analysis remains deterministic/local and does not add an AI dependency.


### v0.18.2
First-Time User UX: empty editable processes now present a clear first-step card on the canvas with direct Start/Activity actions and guidance to continue with `＋ Nästa`.


### v0.18.2
New Process UX: browser `prompt()` has been replaced by a Maplini-native naming dialog with Enter/Escape support, inline validation, cancel/backdrop behavior and direct continuation into the empty-canvas first-step flow.


### v0.18.2
Connector Labels & Selection UX: connector text is now per-connector, live-updating, visually offset from the drag handle and rendered as a readable badge. New connectors have no automatic Ja/Nej label. The node-delete action only appears for a single selected node.


### v0.18.2
Connector Interaction Polish: selected connector text, drag handle and routing quick toolbar are now spatially separated so they no longer stack on top of one another during editing.


### v0.18.2
Connector Formatting Cleanup: connector formatting is now fully self-contained, with its own width control and clearer Swedish terminology. Node border controls stay hidden during connector editing.


### v0.18.2
Context Panel Polish: the left formatting panel now clearly switches between Pil, Ruta, Flera rutor and an unselected state, with contextual guidance instead of mixed generic copy.


### v0.18.2
Typography Cleanup: the font picker is reduced from 27 options to 7 clear choices. Older saved fonts remain supported through a temporary legacy option rather than being silently changed.


### v0.18.2
Canvas Appearance Cleanup: Processyta now offers five focused background choices. Older saved backgrounds remain supported through a temporary legacy option instead of being silently changed.


### v0.18.2
Node Style Cleanup: the standard node-style picker is reduced to Standard, Upphöjd and Minimal. Older 3D/Glass styles remain fully supported when opening existing processes.


### v0.18.2
Full Canvas Zoom & Ctrl Multi-Select: top-bar zoom now scales every visible object and text element in the embedded canvas, and Ctrl/Cmd-click toggles multiple node selection.


### v0.18.2
First View & A4 Portrait Default: empty processes now present a proper centered start card inside the editor iframe, A4 portrait is the default page format, and generic browser/iframe noise no longer raises the red data-safety banner.


### v0.18.2
Maplini's core process model is now Object → Activity → Object. Object in/out are two user-facing roles for the same underlying object type, allowing results to become inputs to later activities.


### v0.18.2
Dependency Coach: direct Activity → Activity connections are now challenged in context, and Process Check explains that a missing result/object may be hiding the real dependency.


### v0.18.2
Process Scale Quick Access: `Skala process` is now a main-toolbar control, and its +10% / −10% actions keep the menu open for repeated presses.


### v0.18.2
Canvas Pan & Scale Slider: desktop users can drag blank canvas to navigate, and whole-process scaling uses a 50–150% slider that changes actual node dimensions as well as text and spacing.


### v0.18.2
Blank canvas click now clears the current selection while drag-to-pan remains intact.


### v0.18.2
Magnetic Alignment: node dragging snaps to an invisible grid and to other nodes' edges/centers. Connected nodes aligned on the same axis receive a straight connector. The quick `Formatera` action is now called `Egenskaper`.


### v0.18.2
`Mer → Rensa hela canvasen` removes all nodes/connectors only after an explicit confirmation. The operation is undoable.


### v0.18.2
Smart Connector Polish automatically keeps ordinary connectors straight when nodes share an axis and orthogonal otherwise, while preserving user-created free/manual routes during normal dragging.


### v0.18.2
Object UX keeps one technical Object type but adds clear input/output/intermediate role hints in creation, node labels and properties guidance.


### v0.18.2
Faster Process Building turns the contextual Next action into a one-click recommended continuation, while a separate dropdown preserves alternate step types. Ctrl/Cmd+Enter continues the flow directly from inline editing.


### v0.18.2
Process Flow Assistant gives contextual methodology help for direct Activity-to-Activity links, with one-click insertion of an Object/result or an explicit intentional override.


### v0.18.2
Automatic Cleanup adds a one-click process tidy action that chooses layout direction from the existing flow, aligns nodes, evens spacing and cleans connector geometry without changing graph logic.


### v0.18.2
Undo Safety introduces atomic history transactions for clear, layout/automatic cleanup and scale gestures, ensuring one user action restores with one Undo and no-op gestures create no history noise.


### v0.18.2
Canvas Performance reduces per-frame work on large maps with local geometry invalidation, cached node-to-link adjacency and path-only connector updates during drag/resize gestures.


### v0.18.2
Build Flow UX Polish unifies the recent methodology features with a contextual flow cue, highlighted recommended alternatives, better next-step feedback and automatic viewport follow when extending a process.


### v0.18.2
Processinformation adds structured business metadata to process steps: description, responsible role, system, instruction, risk, control, KPI and duration. The data is kept off-canvas in the properties panel and is backward compatible with older saved maps.


### v0.18.2
Egenskapspanel UX makes process information faster to enter: essentials first, advanced details collapsed, reusable role/system suggestions, clearer optional completeness feedback and keyboard save/focus behavior.


### v0.18.2
Direct drag removes the preselection step for moving nodes. Object-role badges are no longer rendered above object nodes; role metadata remains preserved in the process data.
