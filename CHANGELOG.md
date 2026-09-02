# Changelog

## v0.20.9 – Walkthrough Transition Polish
- Ja/Nej-vägval läses nu direkt på canvasen genom små grenetiketter vid möjliga nästa rutor när pilarna har vägvalsetiketter.
- När ett svar entydigt väljer en gren tonas övriga alternativ bort och vald nästa ruta får en tydligare men kortvarigt lugn fokusmarkering.
- Den valda pilen förstärks mer än övriga möjliga pilar så riktningen blir självklar innan nästa steg öppnas.
- Grenetiketter och valmarkeringar rensas alltid när genomgången går vidare, stängs eller avslutas.
- Befintlig auto-vidare, avvikelsehantering, canvasföljning och manuell routing är bevarad.
- Ingen gamification, ingen datamodellsändring och ingen Supabase-migrering.

## v0.20.8 – Visual Walkthrough Position
- Följ processen visar nu själva positionen direkt på canvasen: aktuell ruta får tydligt fokus utan att resten av processen försvinner.
- Redan passerade steg tonas ned diskret så att användaren ser varifrån genomgången kommer.
- Möjliga nästa steg markeras subtilt direkt i flödet.
- Den eller de relevanta utgående pilarna förstärks; efter ett entydigt Ja/Nej-vägval framhävs bara vald gren.
- Canvasen följer mjukt med när nästa steg hamnar utanför den centrala läszonen, utan automatisk zoom.
- Walkthrough-bakgrunden är mindre dimmad så processkartan fortsätter vara en aktiv del av upplevelsen.
- Ingen gamification, ingen datamodellsändring och ingen Supabase-migrering.

## v0.20.7 – Focused Follow Process
- Förenklade introduktionen till Följ processen: en fråga i taget, Ja/Nej och vidare längs rätt väg.
- En ensam fråga visas utan onödig numrering och får tydligare fokus.
- **J** och **N** fungerar som tangentbordsgenvägar för Ja respektive Nej när exakt en fråga visas.
- Snabba standardfrågor fortsätter automatiskt efter Ja/Nej när det bara finns en möjlig väg.
- En ensam explicit kontrollfråga med **Ja** fortsätter automatiskt när nästa steg är entydigt.
- En styrfråga/vägvalsfråga fortsätter automatiskt på unik Ja/Nej-gren när svaret räcker för att avgöra vägen.
- Explicit kontrollfråga med **Nej** stannar kvar när uppföljningsdetaljer krävs.
- Noll avvikelser visas inte längre som en ständig administrativ räknare under genomgången.
- Ingen gamification, ingen datamodellsändring och ingen Supabase-migrering.

## v0.20.7 – Direct Follow Process
- Standardfrågan **Har du gjort detta?** är nu den visuellt primära handlingen.
- Större och tydligare Ja/Nej-knappar.
- Vid exakt en möjlig nästa väg går snabbfrågan automatiskt vidare efter svaret.
- Auto-vidare används inte vid verkliga vägval, flera utgående vägar eller explicita kontrollfrågor.
- Nej på snabbfrågan registreras fortsatt utan att kräva extra administration före nästa steg.
- Ingen Supabase-migrering.

## v0.20.6 – Visual Flow Rhythm
- Förfinade avstånden när nya steg skapas så att flödet ser mer genomarbetat ut direkt.
- Objekt ↔ Aktivitet får något tätare rytm för att tydligare kännas som en sammanhängande arbetssekvens.
- Beslut får mer luft både framåt och mellan Ja/Nej-grenar för bättre läsbarhet.
- Slutsteg får lite extra avstånd så att avslut visuellt separeras från arbetsstegen.
- `smartNextStepPosition` stödjer nu konfigurerbart tväravstånd (`crossGap`) i stället för ett fast värde.
- En markerad ruta tonar subtilt fram sina automatiskt hanterade in- och utgående pilar för att göra den lokala flödesrelationen lättare att läsa.
- Manuellt placerade rutor och manuellt redigerade pilar påverkas inte av den nya rytmlogiken.
- Ingen gamification och ingen Supabase-migrering.

## v0.20.5 – Smart Connector Flow
- Automatiskt skapade pilar får nu ett eget internt läge, **autoManaged**, så Maplini kan hålla dem snygga utan att skriva över manuellt pilarbete.
- När en auto-pil följer en ruta under dragning växlar den live mellan rak och vinkelrät geometri beroende på hur rutorna ligger.
- Nästan horisontella eller vertikala flöden får en rak pil redan inom 10 px tolerans.
- När rutorna lämnar samma axel går auto-pilen tillbaka till en ren vinkelrät bana.
- Om användaren själv väljer Rak, Vinkelrät, Fri eller ändrar fästpunkter lämnas pilen därefter i fred av auto-poleringen.
- Ingen gamification och ingen Supabase-migrering.

## v0.20.4 – Formation Selection
- Flera markerade rutor visas nu som en tydlig sammanhållen **formation** med en diskret gemensam ram.
- Formationens ram följer med live när gruppen dras.
- Alla rutor i gruppen får en lätt gemensam dragrespons medan de flyttas.
- Ny kompakt **Ordna**-meny i snabbverktyget för fler-markering:
  - justera överkant
  - justera vänsterkant
  - fördela jämnt horisontellt
  - fördela jämnt vertikalt
  - Snygga till markerade horisontellt/vertikalt
- Pilarna flyttas fortsatt tillsammans med gruppens interna kopplingsgeometri.
- Markerade rutor kan finjusteras med piltangenter:
  - pil = 2 px
  - Shift + pil = 20 px
- Ingen permanent gruppering skapas; detta är endast ett snabbare sätt att manipulera en tillfällig markering.
- Ingen gamification, ingen datamodellsändring och ingen Supabase-migrering.

## v0.20.3 – Canvas Build Rhythm
- Gjorde det möjligt att bygga fler delar av processen utan att lämna canvasen.
- **Tab** på en markerad ruta skapar direkt Maplinis rekommenderade nästa steg.
- På ett Beslut skapar **Tab** Ja- och Nej-grenarna.
- **Shift+Tab** öppnar rutans befintliga meny för alternativa nästa steg.
- **Enter** på en markerad ruta startar direkt textredigering.
- **Ctrl/Cmd+D** och snabbknappen Duplicera behåller befintlig funktion men duplicerade rutor får nu direkt visuell feedback och förs in i vyn.
- När användaren drar en koppling från en kopplingspunkt till **tom canvas** längre än en liten säkerhetsmarginal skapas automatiskt rekommenderad nästa ruttyp där pilen släpps och kopplas direkt.
- Kopplingslinjen visar ett separat visuellt läge när släpp på tom canvas kommer skapa ett nytt steg.
- Släpp på en befintlig ruta fungerar som tidigare.
- Ingen gamification, ingen datamodellsändring och ingen Supabase-migrering.

## v0.20.2 – Navigation Feel
- Gjorde navigeringen i större processer mer direkt och spel-lik utan gamification.
- **Ctrl/Cmd + mushjul** zoomar nu mot muspekaren i stället för mot mitten av canvasen.
- **Mellanslag + dra** ger tillfällig panorering även när markeringsläget är aktivt.
- **Mittenknapp + dra** panorerar canvasen direkt.
- Markeringsramen har fått tydligare men diskret visuell feedback.
- Rutor som ligger inom markeringsramen förhandsmarkeras medan ramen dras.
- Markera område visar nu ett tydligare tips om att Mellanslag tillfälligt växlar till panorering.
- Befintlig mobil pinch-zoom och en-finger-pan lämnas oförändrad.
- Ingen datamodellsändring och ingen Supabase-migrering.

## v0.20.1 – Canvas Feel, No Rewards
- Tog bort FLOW-streaken och den belöningsliknande avslutningsanimationen från v0.20.0.
- Behöll den responsiva känslan men flyttade fokus till själva interaktionen.
- Rutor lyfter visuellt när de dras.
- När en ruta magnetiskt linjerar med en annan blir snap-guiden tydligare och rutan får en subtil snap-respons.
- Vid ritning av en ny koppling markeras giltig målruta direkt.
- Den tillfälliga pilen byter visuellt läge när den ligger över ett giltigt mål.
- När kopplingen släpps får målrutan en mycket kort bekräftelsepuls.
- Följ processen använder nu samma neutrala knapprespons för både Ja och Nej.
- Nya steg får fortsatt en kort spawn-animation eftersom den ger direkt input-feedback, inte belöning.
- `prefers-reduced-motion` respekteras.
- Ingen datamodellsändring och ingen Supabase-migrering.

## v0.20.0 – Game Feel / Flow Streak
- Gjorde Maplini mer responsivt och roligare att använda utan att göra gränssnittet barnsligt.
- Nya steg som skapas via **+ Nästa** får en snabb, mjuk spawn-animation.
- När användaren bygger flera steg i följd inom 12 sekunder visas en faktisk **FLOW ×N**-streak i snabbverktyget.
- Ja/Nej-grenar räknas in i samma bygg-flow och ger direkt visuell respons när de skapas.
- Följ processen har fått tydligare mikrofeedback:
  - Ja får en kort positiv pulseffekt.
  - Nej får en diskret respons utan att framställas som ett “fel”.
  - Varje nytt steg glider in mjukt.
  - En helt godkänd genomgång får en kort avslutningsanimation.
- Animationer respekterar `prefers-reduced-motion`.
- Ingen poäng eller kvalitetsrating hittas på – FLOW räknar bara faktiska byggsteg.
- Ingen datamodellsändring eller Supabase-migrering.

## v0.19.9 – Quick Shape Picker
- Lade till **Form** direkt i snabbverktyget ovanför markerad ruta.
- Ett klick öppnar fyra visuella standardval: Typstandard, Rektangel, Rundad och Kapsel.
- Aktuell form visas direkt i snabbverktygets ikon.
- Vid flera markerade rutor visar snabbvalet gemensam form när alla matchar; ett val appliceras på hela markeringen.
- Formbytet använder samma befintliga undo/persist/style-väg som Utseende-panelen.
- Den fullständiga Form-inställningen under Utseende finns kvar.
- Ingen ny panel, ingen datamodellsändring och ingen Supabase-migrering.

## v0.19.8 – Shape Presets + Better Flow Rhythm
- Lade till ett nytt **Form**-val i befintliga Utseende-inställningar för rutor.
- Standardformer:
  - Typstandard
  - Rektangel
  - Rundad
  - Kapsel
- Formvalet fungerar på markerad ruta och på flera markerade rutor samtidigt.
- Beslutspunkter kan också byta från diamant till de valbara standardformerna när användaren vill frångå typstandarden.
- Formvalet sparas med noden och följer med i lokalt sparande, molnlagring och export via den befintliga processdatan.
- Ogiltiga/äldre formvärden normaliseras säkert till Typstandard.
- **Snygga till** har fått luftigare grundspacing: större avstånd i huvudflödet och mellan parallella grenar.
- Ingen ny panel eller extra arbetsyta har lagts till.
- Ingen Supabase-migrering krävs.

## v0.19.7 – Clearer Node Hierarchy
- Förtydligade de tre viktigaste byggstenarna visuellt utan att lägga till fler inställningar.
- **Objekt** är nu kompaktare och känns mer som input/output/resultat än som en aktivitet.
- **Aktivitet** har fått starkare visuell tyngd som processens primära arbetssteg, med diskret vänsteraccent och något tydligare kortkänsla.
- **Beslut** behåller diamantformen men har fått lugnare, mer professionell kontrast och subtilt djup.
- Textvikter och spacing har justerats så att Objekt → Aktivitet → Beslut går snabbare att skanna visuellt.
- Start/Slut, routing, Följ processen och processlogik är oförändrade.
- Ingen ny Supabase-migrering.

## v0.19.6 – Cleaner Decision Flows
- Förfinade pilarnas visuella uttryck utan att lägga till nya inställningar.
- Vinkelräta automatiska pilar får nu mjukt rundade hörn i stället för hårda 90°-knäckar.
- Ja/Nej-etiketter får diskret semantisk styling: Ja i grön ton och Nej i röd ton, medan själva pilen behåller processens neutrala linjestil.
- Ja/Nej-kopplingar får semantiska SVG-klasser för konsekvent rendering och framtida finjusteringar.
- Rak och fri routing påverkas inte.
- Befintlig connector-logik, manuell routing, markering, dragning och Följ processen-routing är bevarad.
- Ingen ny Supabase-migrering.

## v0.19.5 – Guided Follow Process
- Gjorde **Följ processen** mer fokuserad och lättare att använda som ett guidat arbetsflöde.
- Aktuell aktivitet visas större och tydligare.
- Ja/Nej-knapparna är större och mer lätttryckta på både desktop och mobil.
- Ny positionsrad visar de senaste stegen och vilket steg som är aktuellt.
- Aktiviteter/delprocesser utan egna kontrollfrågor får automatiskt den enkla frågan **”Har du gjort detta?”**.
- Ett Nej på den automatiska snabbfrågan registreras som avvikelse utan att tvinga fram ett administrativt formulär direkt.
- Egna konfigurerade kontrollfrågor behåller befintlig avvikelseuppföljning med förklaring, ansvarig och datum.
- Befintlig Ja/Nej-routing, historik, molnsynk och avvikelselogik är bevarad.
- Ingen ny Supabase-migrering.

# v0.19.4 – Smart decision branches

- Beslutspunkter kan skapa Ja- och Nej-grenar i ett klick.
- Grenarna placeras automatiskt på varsin sida om huvudflödet och märks Ja/Nej.
- Ctrl/Cmd+Enter från ett beslut skapar båda grenarna direkt.
- Om en Ja- eller Nej-gren redan finns skapas bara den saknade grenen.

# Changelog

## 0.19.3 – Smart Next Build
- `+ Nästa` fortsätter nu i samma riktning som det befintliga processflödet.
- Nya steg placeras på samma baslinje när det finns plats och i parallell körlinje vid kollision, i stället för att hoppa slumpmässigt nedåt.
- Beslutsgrenar sprids automatiskt ovanför/under beslutet.
- Nya steg snappas till 20 px-grid och kopplingen använder rätt sida för flödesriktningen.
- Följ processen och befintlig processlogik är oförändrade.

## v0.19.2 – Visual Flow Polish
- `✨ Snygga till` is now a true one-click action in the top toolbar instead of requiring the user to open a menu first.
- The small adjacent dropdown keeps manual horizontal/vertical and selected-node layout options.
- Smart layout now centers every rank on the actual connected flow rather than only on the old drawing's overall bounding box.
- Decision branches are visually balanced around their source step; merge steps are centered between their incoming branches.
- Long straight chains are gently aligned in a reverse pass, reducing unnecessary zig-zag connector routes.
- Default automatic spacing is slightly tighter (`mainGap 118`, `crossGap 52`) for a cleaner professional rhythm without changing process logic.
- Existing connector cleanup still runs in the same atomic Undo operation.
- No Supabase/database migration is required.

## v0.19.1 – Individual deviation status
- Each deviation now has its own `open` / `resolved` status instead of inheriting one status for the entire walkthrough run.
- The deviation dashboard action now updates only the selected deviation: `Markera avvikelse hanterad` / `Öppna avvikelse igen`.
- Walkthrough history shows a status badge and individual follow-up button per deviation.
- Run-level follow-up status is derived automatically: the run is resolved only when all deviations are resolved.
- Reopening one deviation leaves other resolved deviations unchanged.
- Backward compatibility: older runs that only have run-level follow-up status are materialized safely into per-deviation statuses when first edited.
- Cloud PATCH now persists the updated `result` and `history`, so individual deviation statuses sync through the existing `walkthrough_runs` table.
- No new Supabase migration is required beyond v0.18.9.

## v0.19.0 – Avvikelseöversikt
- Added a dedicated **⚠ Avvikelser** dashboard in the top toolbar.
- Aggregates deviations from walkthrough history across all processes currently available in the active personal/workspace scope.
- Summary counters show open, overdue and resolved deviations.
- Filters: open/all/resolved status, responsible owner search and overdue-only.
- Open deviations are sorted with overdue items first, then by due date.
- Overdue actions are visually highlighted and based on the saved deviation due date.
- Each row shows process, walkthrough date, process step/question, explanation, responsible owner, due date, status and cloud marker.
- `Visa i process` opens the source process and selects the affected node when the process is loaded.
- Follow-up can be marked handled/reopened directly from the dashboard; the existing run-level status is reused and cloud-synced through v0.18.9.
- When signed in, the dashboard loads walkthrough runs for the active personal/workspace scope from Supabase and merges them with local-first history.
- No new database migration is required for v0.19.0; `supabase_schema_v0189.sql` remains the prerequisite for cloud history.
- The current data model tracks follow-up status per walkthrough run. If one run contains several deviations, marking the run handled resolves that run's deviations together.

## v0.18.9 – Cloud walkthrough history
- Added a dedicated Supabase-backed `walkthrough_runs` model for cross-device walkthrough history.
- Completed walkthroughs still save locally first, then sync to Supabase when the user is signed in and the v0.18.9 migration is installed.
- Opening `Följ processen` now loads cloud history for the current process and merges it with local history by run ID.
- Cloud-synced runs are marked `Moln` in the history UI.
- Follow-up status changes (`Hanterad` / `Öppna igen`) are synced back to the cloud.
- Cloud payload preserves process, creator, workspace, person, timestamps, result, detailed deviations and the traversed walkthrough history.
- Workspace members can read and create walkthrough runs; run creator, process owner and workspace owner/editor can update follow-up status.
- Local fallback is explicit: if the table/migration is unavailable, Maplini continues to work and explains that history is local.
- Added `supabase_schema_v0189.sql` with table, indexes, RLS and workspace-aware policies.
- No existing process table is altered by this migration.

## v0.18.8 – Deviation follow-up
- `Följ processen` now opens a structured deviation form immediately when a user answers `Nej` on a **Kontrollfråga**.
- Every control deviation now requires three follow-up fields before the walkthrough can continue:
  - explanation of what deviated,
  - responsible person/role/function,
  - due date.
- Route-question `Nej` answers remain normal process routing and never open a deviation form.
- Deviation details are stored with the walkthrough answer and preserved in the saved run history.
- The completion summary now shows explanation, responsible owner and due date for each deviation.
- Copied walkthrough results include the same follow-up information.
- Previous-run history shows responsible owner and due date for open deviations, making the history useful as a lightweight action list.
- The existing run-level `Markera hanterad` / `Öppna igen` follow-up state remains available.
- No database/Supabase migration required; history remains browser-local in this release.

## v0.18.7 – Control questions vs route questions
- Walkthrough questions now have an explicit type: **Kontrollfråga** or **Vägvalsfråga**.
- A `Kontrollfråga` keeps the compliance meaning: `Nej` is counted as an actionable deviation.
- A `Vägvalsfråga` treats both `Ja` and `Nej` as normal process outcomes; neither answer is a deviation.
- Vägvalsfrågor automatically drive a unique outgoing `Ja` or `Nej` connector when available.
- Only one route question is kept per step in the editor; selecting a new route question returns the previous one to control type.
- Walkthrough question cards now show `KONTROLL` or `VÄGVAL` so users understand why an answer affects compliance or routing.
- The live deviation counter now ignores neutral `Nej` answers from route questions.
- Completion status, saved walkthrough history and follow-up state are now based on actual deviations rather than the raw number of `Nej` answers.
- Summary shows separate counts for steps, Ja, Nej and deviations.
- Saved run data now preserves question kind and separate control/route counts for future reporting.
- Backward compatibility: old questions marked `route:true` are normalized as `Vägvalsfråga`; questions without a type remain `Kontrollfråga`.
- No database/Supabase migration required.

## v0.18.6 – Smart Ja/Nej routing
- Added explicit **Styr Ja/Nej-väg** on walkthrough control questions.
- Only one question per step can be designated as the routing question in the editor; choosing another automatically replaces the previous routing question.
- During `Följ processen`, a routing question now resolves the next branch automatically when the current step has one outgoing `Ja` edge and one outgoing `Nej` edge.
- Before the routing question is answered, manual branch buttons are hidden and Maplini explains that the answer will choose the path.
- After answering, the user gets one clear continuation action such as `Fortsätt på Ja: ...` instead of manually choosing a branch.
- Branch labels are matched case-insensitively and support common equivalents such as Yes/No.
- If Ja/Nej labels are missing or ambiguous, Maplini does not guess: it explains the issue and falls back to manual branch selection.
- Single-path steps and end steps continue to behave exactly as before.
- Routing metadata is stored with the existing walkthrough question data; no database/Supabase migration is required.

## v0.18.5 – Walkthrough history & follow-up
- `Följ processen` now stores completed walkthroughs locally per process in the browser.
- Name or initials are required before a walkthrough starts so completed checks can be traced to a person.
- Each saved run includes process, person, start/completion time, step count, yes/no totals and detailed deviations.
- Up to 50 recent runs are kept per process (500 total locally) to avoid unbounded browser storage growth.
- The start view now shows `Tidigare genomgångar` with date/time, person, result and follow-up state.
- Runs with no deviations are shown as approved.
- Runs with deviations are shown as `Kräver uppföljning` and can be marked `Hanterad` or reopened.
- Stored run summaries can be copied directly for follow-up/documentation.
- The completion screen confirms whether the run was saved successfully.
- This release deliberately uses browser-local history only; workspace/cloud-synced audit history is the next architectural step and requires a deliberate backend model.
- No Supabase/database migration required.

## v0.18.4 – Follow the process + workflow polish
- Added a new top-level **Följ processen** mode for interactive, step-by-step process walkthroughs.
- Process owners can add reusable **Ja/Nej control questions** to Activity, Decision and Subprocess nodes from the properties panel.
- Walkthrough mode starts from explicit Start nodes when present, otherwise from graph roots, and follows the actual process connectors.
- Branches with multiple outgoing connectors are presented as explicit next-step choices using connector labels when available.
- Required questions must be answered before the walkthrough can continue.
- `Nej` answers are tracked as deviations and surfaced in a final summary with step/question context.
- The current walkthrough result can be copied for follow-up. This first release keeps run results in the current browser session only; permanent run history is deliberately deferred.
- Added a dedicated `maplini_walkthrough_core.js` with question normalization, graph traversal helpers and deterministic result summaries.
- `walkthroughQuestions` are normalized/preserved in the existing process JSON; no database migration is required.
- **Snygga till** is now safer and more predictable: automatic cleanup only rearranges nodes that participate in the connected flow, leaves isolated draft nodes untouched, uses tighter spacing, and no longer changes canvas zoom automatically.
- If no connected flow exists, Snygga till now explains that at least two connected nodes are required instead of arbitrarily rearranging loose nodes.
- Fixed a Ctrl/Cmd multi-select regression introduced by direct label dragging.
- Hardened the desktop sidebar in Chrome with additional scroll end-space and scroll padding so the final controls can be reached reliably.
- Updated browser smoke coverage to the current Objekt → Aktivitet methodology.
- No Supabase/database migration required.

## v0.18.3 – Direct page settings
- Added a compact sticky page control directly over the canvas: `A4 stående · Auto ▾`.
- Paper format and orientation can now be changed without opening Export or More.
- Direct options: no page area, A4 portrait, A4 landscape, A3 portrait and A3 landscape.
- Page count can be set to automatic or manually from 1–8 pages.
- The quick control stays synchronized with the existing Export page settings in both directions.
- The control explains that page borders represent the export split.
- Mobile sizing was tightened so the page control remains usable without dominating the canvas.
- No data-model, Supabase or database migration changes.

## v0.18.2 – Direct drag & cleaner objects
- Nodes can now be grabbed and dragged directly from their visible text area without being selected first.
- The same pointer gesture automatically selects the node and starts movement; no separate preselection click is required.
- Inline text editing remains protected: when the label is content-editable, dragging does not steal the text interaction.
- Object type badges (`OBJEKT`, `OBJEKT IN`, `OBJEKT UT`) have been removed from the canvas to reduce visual noise.
- `objectRole` remains fully preserved in node data and continues to drive methodology, analysis and property-panel context.
- Node labels use grab/grabbing cursor feedback when not editing.
- No data-model, Supabase or database migration changes.

## v0.18.1 – Egenskapspanel UX
- Reworked Processinformation into a lighter, task-oriented panel: `Vad händer?`, `Vem ansvarar?`, `Vilket system?` and `Tidsåtgång` are immediately visible.
- Advanced fields (instruction, risk, control and KPI) now live under a collapsible `Fördjupa beskrivningen` section instead of forming a long permanent form.
- Responsible role and system fields now reuse values already present in the current process through native suggestion lists.
- Suggestions are deduplicated case-insensitively, alphabetized and capped to keep the UI light.
- Completion feedback is now phrased as `x av 8` and explicitly remains optional rather than implying every field must be filled.
- Advanced-section summary shows how many of its four fields are populated.
- Ctrl/Cmd+Enter saves the active process-information field and returns keyboard focus to the selected canvas node.
- Read-only permissions now also disable textareas, not only inputs/selects/buttons.
- No data-model, Supabase or database migration changes.

## v0.18.0 – Processinformation
- Added structured business information for Activity, Subprocess and Decision nodes.
- New fields: description, responsible role, system, instruction, risk, control, KPI/measure and duration.
- Process information lives in the properties panel and does not clutter the canvas.
- Visual formatting is now grouped under a collapsible `Utseende` section so business information gets priority.
- Added a small completeness indicator (0/8–8/8) for the selected process step.
- Existing Input/Output lists remain part of the step and continue to work unchanged.
- Added `maplini_process_info_core.js` for safe normalization, field length limits and completeness calculation.
- `maplini_state_core.js` now preserves and normalizes `processInfo`; older saved processes without the field open with empty metadata.
- New nodes initialize an empty process information object.
- No Supabase/database migration is required because metadata is stored inside the existing process payload.

## v0.17.4 – Build Flow UX Polish
- Added a compact contextual flow cue next to the selected node, e.g. `Aktivitet → Objekt ut` or `Objekt → Aktivitet`.
- The flow cue mirrors the same methodology used by the one-click Next action, reducing ambiguity between the canvas and toolbar.
- The node-side alternative Next menu now highlights the recommended choice while keeping all alternate step types available.
- Newly created next steps are automatically kept inside the visible viewport before inline editing begins.
- Add-next feedback now explains the fastest continuation: write the name, then use `Ctrl/Cmd+Enter` to continue.
- Palette-created core steps now give consistent guidance to continue with `Nästa`.
- No process logic, schema, database or Supabase migration changes.

## v0.17.3 – Canvas Performance
- Node geometry caching is now invalidated per node instead of globally; moving one box no longer makes every cached node geometry stale.
- Added a node-to-connector adjacency cache so dragging a node can find its connected arrows without scanning the entire connector list every frame.
- Full connector renders rebuild the adjacency cache automatically after graph changes.
- Node drag and resize now use a fast geometry mode: visible connector paths update live, while expensive hit-segment, marker and label DOM rebuilding is deferred until the gesture ends.
- A complete connector render is forced at gesture end, so final arrows, labels and click targets remain fully accurate.
- Contextual node toolbar refresh is skipped on connector-only redraw frames when no node selection exists.
- No process data model, database or Supabase migration changes.

## v0.17.2 – Undo Safety
- Added atomic undo transactions for large operations so one user action maps to one Undo checkpoint.
- `Rensa hela canvasen` now records the entire clear as one atomic operation and restores all nodes/connectors with one Undo.
- Smart Layout and `Ordna processen automatiskt` now group node movement plus connector cleanup into the same Undo checkpoint.
- Nested internal history writes are suppressed while an atomic operation is running, preventing duplicate Undo steps.
- Process-scale slider gestures now create a checkpoint only if the slider actually changes the process.
- Multiple slider `input` events during one drag/keyboard gesture still collapse into one Undo step.
- Cancelled/no-op large actions no longer pollute Undo history.
- No database or Supabase migration changes.

## v0.17.1 – Automatic Cleanup
- Added a one-click `Ordna processen automatiskt` action at the top of `Snygga till`.
- Maplini automatically chooses horizontal or vertical layout based on the direction of the process's existing connected flow.
- If there are too few usable links, Maplini falls back to the current process shape to choose the most natural orientation.
- The action reuses Smart Layout to align nodes, equalize spacing and reduce crossings.
- Connectors are normalized after cleanup: aligned nodes use straight routes, other automatic routes use orthogonal geometry.
- The process graph itself is not changed: no nodes or connections are added, removed or reordered logically.
- The whole cleanup is undoable as one layout operation.
- Manual horizontal/vertical Smart Layout controls remain available below the automatic action.
- No database or Supabase migration changes.

## v0.17.0 – Process Flow Assistant
- Direct Activity → Activity links now open a focused methodology coach instead of only a generic insert-step menu.
- The coach asks what result from the first Activity enables the next one.
- One click on `Infoga Objekt / resultat` splits the connector and inserts an Object between the Activities.
- The inserted Object is a normal technical `object` node with intermediate/result semantics.
- Users can explicitly choose `Behåll direktkoppling`; Maplini stores that as an intentional methodology override.
- Intentional direct Activity links are no longer repeatedly flagged by Process Analysis.
- Process Analysis findings for unacknowledged direct Activity links now include a one-click `Infoga Objekt / resultat` fix.
- No database or Supabase migration changes.

## v0.16.9 – Faster Process Building
- The contextual quick action no longer opens a menu for the normal path; it adds the recommended next step immediately.
- After an Activity, the primary action becomes `＋ Objekt ut`.
- After an Object, Start, Decision, Document or Subprocess, the primary action becomes `＋ Aktivitet`.
- A separate small dropdown button keeps access to all alternative next-step types.
- Mobile uses the same dynamic recommended-next label and direct action.
- `Ctrl/Cmd + Enter` while editing a node finishes the text and immediately creates the recommended next step.
- The new step remains selected and enters inline editing, supporting a fast write → continue → write workflow.
- Existing node-side `+` remains available as the explicit chooser for alternate step types.
- No database, Supabase or process-schema migration changes.

## v0.16.8 – Object UX
- Kept `Objekt in` and `Objekt ut` as the same underlying `object` node type.
- Added lightweight semantic role metadata (`input`, `output`, `intermediate`) only as a UX hint; it does not change graph logic.
- Palette-created `Objekt in` and `Objekt ut` now retain the intended role after click/drag creation.
- Object nodes show a compact role chip (`OBJEKT IN`, `OBJEKT UT`, or `OBJEKT`) above the node.
- `+ Nästa` from an Activity creates an Object with output/result semantics.
- Generic/intermediate Objects remain valid as both a prior result and the next Activity's input.
- Object selection now explains the role directly in the properties panel.
- State normalization preserves object-role hints while older object nodes safely default to `intermediate`.
- No database or Supabase migration changes.

## v0.16.7 – Smart Connector Polish
- Automatic connectors now choose the cleanest route after node movement: straight when connected node centers share an axis, otherwise orthogonal.
- Newly created connectors are polished immediately instead of inheriting avoidable diagonal geometry.
- `+ Nästa` connectors receive the same route cleanup automatically.
- Smart Layout now chooses straight routes for aligned pairs instead of forcing every connector to orthogonal.
- Stale automatic via/free offsets are cleared when geometry is normalized.
- Deliberately manual connector work is protected: free-routing and fixed-anchor connectors are not auto-polished during ordinary node dragging.
- Smart Layout may still normalize manual connector geometry because the user explicitly asked it to reorganize the layout.
- No process logic, node data, database schema or Supabase migration changes.

## v0.16.6 – Clear Canvas
- Added `Rensa hela canvasen` under `Mer`.
- The action always asks `Är du säker på att du vill rensa hela canvasen?` before deleting anything.
- Confirming removes all nodes and connectors but keeps the current process itself.
- Clearing creates an undo checkpoint, so `Ångra` can restore the canvas contents.
- Empty canvases are left untouched and show a short status message instead.
- No data-schema, Supabase or migration changes.

## v0.16.5 – Magnetic Alignment
- Added an invisible 10 px base grid for node movement.
- Added magnetic alignment against other nodes' left/center/right and top/center/bottom lines within an 8 px snap tolerance.
- While snapping to another node, a temporary subtle alignment guide is shown; the grid itself remains invisible.
- Multi-node moves preserve relative geometry and snap the group using the dragged reference node.
- When connected nodes end up with exactly aligned centers horizontally or vertically, their connector is normalized to a straight automatic route.
- Manual connector via/free offsets are cleared only for those newly aligned connected links.
- Renamed the quick-toolbar button `Formatera` to `Egenskaper` and clarified its tooltip.
- Mobile context wording was aligned to `Egenskaper`.
- No data-schema, Supabase or migration changes.

## v0.16.4 – Click Outside to Deselect
- Clicking blank canvas now always clears the selected node or connector.
- Desktop drag-to-pan is preserved: a real drag pans the canvas and does not clear selection mid-gesture.
- The deselection is handled at the end of a non-moving blank-canvas pointer gesture, which avoids pointer-capture retargeting from swallowing the normal click.
- Broadened blank-canvas click recognition to canvas, scroll surface, SVG/link background and page background.
- No data-schema, Supabase or migration changes.

## v0.16.3 – Canvas Pan & Scale Slider
- Added desktop mouse navigation: press and drag on blank canvas to pan horizontally and vertically.
- Panning ignores nodes, connectors, controls and other interactive elements so normal editing gestures remain intact.
- Replaced the whole-process `+10 % / −10 %` controls with a 50–150% slider and live percentage readout.
- Slider interaction keeps the scale menu open and scales continuously while dragging.
- Fixed whole-process scaling so node CSS minimum/maximum dimensions no longer block visible shrinking or growing.
- Scaled nodes now use border-box dimensions and explicit min/max overrides, so the visible rectangle follows the scale together with text and spacing.
- Stored scaled width/height are restored with the same sizing rules when a process is reopened.
- Fit-to-page remains available as a separate one-shot action.
- No database, Supabase or migration changes.

## v0.16.2 – Process Scale Quick Access
- Moved `Skala process` out of the `Mer` menu and into the main top toolbar, directly beside the primary process tools.
- The scale control is now visible without first opening a secondary menu.
- `−10 %` and `+10 %` keep the scale menu open after each press, allowing repeated scaling in one continuous interaction.
- Added event isolation so scale-button clicks do not collapse the surrounding details menu.
- `Passa till vald sida` still closes the menu after completing its one-shot action.
- Existing process scaling behavior remains proportional across nodes, text, spacing and connector geometry.
- No data-schema, Supabase or migration changes.

## v0.16.1 – Dependency Coach
- Added a process-method warning for direct Activity → Activity links.
- When a user manually connects two activities directly, Maplini selects the new connector, opens `Infoga steg`, and asks what result from the first activity enables the next.
- Added `Objekt / resultat` as the first insert-on-connector option.
- `Infoga steg` can now insert the new Object node type and split the existing connector automatically.
- Process Check now flags each direct Activity → Activity link as a warning with concrete guidance to identify the missing result/input.
- Findings include the affected node IDs and connector index for future one-click fixes.
- Object-based flows are not flagged.
- No database, Supabase or migration changes.

## v0.16.0 – Object → Activity → Object
- Introduced `Objekt` as a first-class process node alongside Activity.
- Reframed the main palette around the process method `Objekt → Aktivitet → Objekt`.
- Added clear beginner-facing choices for `Objekt in`, `Aktivitet` and `Objekt ut`; input/output are the same underlying object type so an activity result can naturally become the next activity's input.
- Moved Start, Decision, End, Subprocess, Note and Document under `Fler typer`.
- Added a compact visual method guide directly in the palette.
- Empty processes now ask `Vad startar processen?` and lead with `Objekt in`.
- Object nodes use a distinct compact visual language from activities.
- `+ Nästa` is context-aware: after an Activity it prioritizes an Object/result; after an Object it prioritizes an Activity.
- State normalization now preserves the new `object` node type.
- Existing process node types and saved processes remain backward compatible.
- No database, Supabase or migration changes.

## v0.15.11 – First View & A4 Portrait Default
- Fixed the empty-process onboarding so its card styling is present inside the embedded editor iframe instead of only in Streamlit's parent document.
- New/empty processes now show a centered, clearly designed start card rather than raw text at the top-left of the canvas.
- A4 portrait is now the default PDF/page format throughout the editor.
- Updated the page-spec fallback from A3 landscape to A4 portrait.
- Hardened runtime warnings: incidental browser/iframe errors are still logged for diagnostics but no longer trigger the red data-safety banner.
- Explicit Maplini operation failures still display the red banner.
- A successful process restore clears a stale runtime banner.
- No database, Supabase or migration changes.

## v0.15.10 – Full Canvas Zoom & Ctrl Multi-Select
- Fixed top-bar zoom so the scaling rule now lives inside the embedded editor iframe. `+` / `−` therefore scale the complete canvas contents: nodes, node text, connectors, connector labels, process logo and canvas guides together.
- Kept logical canvas coordinates unchanged, so zoom remains visual and does not rewrite process data.
- Added Ctrl-click / Cmd-click toggle selection for nodes. Existing selections remain active while additional nodes are added or removed.
- Ctrl-click works both on the node body and its text label.
- Multi-selected nodes can continue to be moved/formatted as a group using the existing multi-selection workflow.
- Hardened selection context: connector controls are explicitly hidden whenever no connector is selected.
- No database, Supabase or migration changes.

## v0.15.9 – Node Style Cleanup
- Reduced the standard node-style picker from five variants to three clear choices: Standard, Upphöjd and Minimal.
- Removed 3D and Glass from the normal picker because they add decorative complexity without improving process readability.
- Preserved backward compatibility: existing nodes using 3D or Glass keep their visual rendering and receive a temporary `Tidigare rutstil: …` option when selected.
- Returning to a current node style removes the temporary legacy option.
- Existing process data is not silently migrated.
- No database, Supabase or deployment changes.

## v0.15.8 – Canvas Appearance Cleanup
- Reduced Processyta background choices to five focused options: Enfärgad, Prickar, Rutnät, Bild and Vattenstämpel.
- Removed decorative/advanced backgrounds from the standard picker: gradients, lined/crosshatched/technical patterns, parchment, canvas, concrete and similar textures.
- Preserved backward compatibility: an older saved background is shown temporarily as `Tidigare bakgrund: …` rather than being silently changed.
- Returning to a current background removes the temporary legacy option.
- Existing rendering support for older background types remains in place so old processes retain their appearance.
- No database, Supabase or deployment changes.

## v0.15.7 – Typography Cleanup
- Reduced the font picker from 27 choices to 7 focused options suitable for process documentation: Inter, DM Sans, Poppins, Montserrat, Roboto, Georgia and System.
- Removed decorative and overlapping font choices that added noise without improving process readability.
- Added backward compatibility for saved processes using an older font: the existing font is shown temporarily as `Tidigare typsnitt: …` instead of being silently replaced.
- Choosing a current font removes the temporary legacy option again.
- Existing process data is never rewritten merely because its font is no longer in the standard picker.
- No database, Supabase or deployment changes.

## v0.15.6 – Context Panel Polish
- The formatting panel now changes its heading based on selection: `Pil`, `Ruta`, `Flera rutor` or `Formatering`.
- Help text is contextual instead of generic, so users immediately understand what the visible controls affect.
- Removed the redundant inner `Pil / koppling` heading from connector formatting.
- Added a concise note inside connector settings clarifying that changes affect only the selected connector.
- Added subtle visual differentiation between connector and node formatting contexts.
- Existing formatting controls, connector behavior and saved process data remain unchanged.
- No database, Supabase or deployment changes.

## v0.15.5 – Connector Formatting Cleanup
- Made the connector formatting panel self-contained: connector color, width, line type, shape, end marker, anchoring and label now live together.
- Added a dedicated connector width control instead of reusing the node border-width control.
- Node border color and border width are now explicitly hidden whenever a connector is selected.
- Connector color no longer writes into the node border-color control.
- Replaced technical wording such as `Routing` with clearer Swedish labels such as `Pilform` and `Fästning`.
- Clarified that connector text is custom for the currently selected connector.
- No connector data format, database, Supabase or deployment changes.

## v0.15.4 – Connector Interaction Polish
- Separated the selected connector's three visual affordances: text label, drag handle and routing quick toolbar.
- When a connector has text, the label sits on one side of the route and the routing toolbar is deliberately placed on the opposite side.
- When there is no label, the routing toolbar still receives a clean offset from the drag handle.
- Reused one placement helper in both full and incremental connector redraws so the UI stays stable while dragging and editing.
- Kept connector data, routing logic and saved labels unchanged.
- No database, Supabase or process-data schema changes.

## v0.15.3 – Connector Labels & Selection UX
- Reworked connector labels into professional white badges with stronger typography, spacing, contrast and subtle shadow.
- Labels are positioned offset from the connector path so the connector drag handle no longer obscures the text.
- Connector text updates live while typing instead of appearing only after the input loses focus.
- Every connector keeps its own label value; editing one connector does not change any other connector.
- New connectors no longer receive automatic standard Ja/Nej text. Connector text is explicit and user-defined.
- Existing saved connector labels are preserved.
- `Ta bort markerad ruta` is now explicitly hidden unless exactly one node is selected.
- The node-delete action stays hidden when a connector or nothing is selected.
- No database, Supabase or process-data schema changes.

## v0.15.2 – New Process UX
- Replaced the browser-native `prompt()` used by New Process with a Maplini-styled modal dialog.
- New Process now keeps the current process safe until the user explicitly creates the new one.
- Process name field is focused and selected automatically for fast keyboard use.
- Enter creates the process; Escape, backdrop click or Avbryt closes the dialog without creating anything.
- Empty names are blocked with inline validation rather than silently creating a fallback.
- Successful creation lands directly in the v0.15.1 empty-canvas first-step experience.
- Mobile uses a bottom-positioned dialog with large touch targets.
- No database, Supabase, dependency or process-data changes.

## v0.15.1 – First-Time User UX
- Added a focused empty-canvas start state for genuinely empty editable processes.
- New users can create the first Start or Activity directly from the canvas without hunting through the sidebar.
- The first created node is selected and opened for inline text editing immediately.
- Added a concise hint that `＋ Nästa` is the fastest way to continue building the flow.
- The empty-state guide disappears as soon as the first node exists and stays hidden in shared read-only views.
- Mobile uses the same first-step model with larger, stacked actions.
- Existing palette, drag/drop, mobile add sheet and process data format remain unchanged.
- No database, Supabase or dependency changes.

## v0.15.0 – Actionable Process Check
- Reworked Processkontroll around the user's next action instead of technical findings.
- Every deterministic structural finding now includes a concrete Swedish "Gör så här" recommendation.
- Added clear priority labels: Åtgärda först, Kontrollera and Förbättring.
- Added a "Börja här" card that surfaces the highest-priority finding and can jump directly to affected nodes.
- Replaced disabled finding buttons with readable finding cards plus explicit "Visa berörd ruta" actions.
- Improved the empty state so a clean structural check is easier to understand.
- Renamed summary categories from Fel/Insikter to the more actionable Åtgärda/Kontrollera/Förbättra.
- Kept the analysis deterministic and local; no AI, external API or new data collection was added.
- No database, Supabase or data-format changes.

## v0.14.9 – Simplified UI Stability & Browser Polish
- Fixed a real v0.14.8 nested-menu regression: opening Excel/Google Sheets inside Export no longer closes Export, and opening Processyta/Logotyp/Skala inside More no longer closes More.
- Preserved the four-button mobile bottom bar while restoring mobile access to Redo and Fullscreen as secondary actions in the Add sheet.
- Fullscreen state now updates the secondary mobile button label as well.
- Export actions close the Export menu after the action is started, reducing stale overlay states.
- Expanded Chromium interaction smoke coverage to verify nested Export/More menus, four-button mobile navigation, secondary Redo/Fullscreen access, and the existing free-connector drag/node-follow/Undo flow.
- No database, Supabase or data-format changes.

## v0.14.8 – 30% Simpler
- Reduced the permanent desktop command surface to the core actions: New, Save, Share, Undo/Redo, Zoom/Fit, Smart Layout, Export and More.
- Grouped PDF, DOCX, Excel/Google Sheets and page-format controls under one Export menu.
- Moved Process Analysis, area selection, duplicate/delete, canvas appearance, logo and process scaling under one More menu.
- Simplified Undo/Redo labels to compact icon actions while preserving tooltips and keyboard shortcuts.
- Reduced the normal mobile bottom bar to four actions: Add, Undo, Fit and Tools.
- Secondary mobile actions remain accessible through contextual tools rather than competing permanently for space.
- Existing feature IDs and data formats are preserved; this is an information-architecture simplification, not a feature removal.
- No database or Supabase migration changes.

## v0.14.7 – Integrity & Core Interaction
- Fixed a verified workspace ownership bug: workspace process saves now use the workspace owner's canonical user id instead of the current editor's id.
- Added `supabase_schema_v0147.sql` to harden RLS so editors may edit workspace process content but cannot claim ownership.
- Rebuilt free connector dragging around pointer delta from pointerdown, eliminating jumps when grabbing near an endpoint.
- Fixed the actual one-gesture connector blocker: the document capture listener now arms drag instead of consuming the first pointerdown as selection-only.
- Removed a stale call to nonexistent `refreshLinkQuickToolbar()` and made early resize refreshes safe while the editor is initializing.
- Fixed Google Sheets Processsteg columns by adding the missing `Dokumentlänk` header and adjusting formatting/filter range to 13 columns.
- Added a real Chromium browser interaction smoke test for connector drag, node-follow behavior and Undo.
- No new product features.

## v0.14.6 – Free Connector Routing & Visual UX Polish
- Added true free connector routing. Dragging a connector moves its middle body independently while both endpoints remain attached to their nodes.
- Free routing stores offsets relative to the attached endpoints; moving nodes therefore keeps the manual connector shape following the process.
- Added explicit "Fri" routing in both connector controls and contextual connector toolbar.
- Smart Layout intentionally resets internal connectors to centered automatic orthogonal routing.
- Whole-process scaling also scales free-route offsets.
- Small visual polish pass: clearer sidebar section hierarchy, focus states and drag cursors.
- No database, Supabase or dependency changes.

## v0.14.5 – Editing Stability & UX Cleanup
- Removed remaining live event wiring for the retired Align/Distribute UI.
- Smart Layout now uses the actual logical canvas size instead of fixed 2400×1400 bounds.
- Contextual node toolbar positioning now respects multi-page canvas width.
- Resizing the browser recalculates page extents, horizontal navigation and contextual toolbars.
- Added centralized transient-menu cleanup so popovers do not stack; Escape or blank-canvas interaction closes them.
- No database, Supabase or dependency changes.

## v0.14.4 – Connector Drag Fix
- Connector click-drag now works in one gesture; pre-selection is no longer required.
- Both SVG and HTML connector hit targets start the same drag path.
- Pointer capture reduces lost drags inside the editor iframe.
- A simple click still only selects because geometry is not changed until the movement threshold is crossed.

## v0.14.3 – UI Simplification & Process Scaling
- Removed the Align/Distribute "Ordna" UI from the top toolbar and contextual toolbar.
- Added "Skala process" with −10 %, +10 % and "Passa till vald sida".
- Scaling changes node position, dimensions, text size and manual connector bend coordinates proportionally; one Undo checkpoint.
- Account/login UI is collapsed behind a compact Konto control.
- Process logo controls moved to a dedicated top-toolbar "Logotyp" menu.
- Existing process data remains compatible; removed UI helpers remain internal only.

## v0.14.2 – Layout & Formatting Polish
- Vertikal Smart Layout återställer interna kopplingar till Auto-fästpunkter och rensar gamla brytpunkter så pilar centreras botten→topp.
- Desktop-editorns höjd anpassas efter skärmens tillgängliga höjd så hela vänsterpanelens scrollbar kan nås.
- Rutstilarna 3D, Upphöjd skugga, Glas och Minimal/platt har fått tydligare visuella skillnader.
- Typsnitt, textstorlek, fet/kursiv/understruken och textjustering ligger nu i ett sammanhållet textformateringsblock.

## v0.14.1 – Editing Stability
- Restores drag-to-adjust for selected connectors by starting drag directly from the connector hit target.
- Dragging a strict straight connector switches it to manually routed orthogonal mode so its path can actually be moved; endpoints remain attached to nodes.
- Canvas width now expands dynamically for multi-page print layouts and nodes beyond the default 2400 px workspace, restoring horizontal scrolling to later pages.
- Zoom −/+ now share a tested zoomStep contract: minus always zooms out, plus always zooms in.

## v0.14.0 – Process Intelligence: Processkontroll
- Ny **🔍 Analysera**-funktion i toppmenyn med strukturell processkontroll.
- Processhälsa visas som 1,5–10,0/10 tillsammans med antal fel, kontrollpunkter och insikter.
- Identifierar saknad Start/Slut, isolerade rutor, saknade inkommande flöden, döda ändar och beslut med färre än två utgående grenar.
- Identifierar dessutom loopar/återkopplingar, långa sekvenser och noder där många flöden samlas eller förgrenas.
- Fynd kopplade till rutor är klickbara: Maplini markerar berörda rutor och centrerar dem på canvasen.
- Anteckningar/gruppytor behandlas som annotationer och ger inte falska strukturfel.
- Analysen är deterministisk och regelbaserad; inga AI-gissningar, databasändringar eller nya dependencies.

## v0.13.4 – Sidebar Scroll Reachability
- Fixes desktop left sidebar so the bottom-most controls can always be reached.
- Adds stable vertical scrollbar, contained overscroll and bottom clearance without changing canvas/body DOM structure.

## v0.13.3 – UI Regression Fix
- Rättar kontextverktyg som syntes ostylade uppe till vänster i canvasen utan markering.
- Flyttar kritisk CSS för `.p48-link-quick` och `.p48-node-quick` till editor-iframens eget stylesheet.
- Återställer `display:none` som default och `.on { display:flex }` endast vid giltig markering.
- Återställer korrekt styling, hover/active-lägen, multi-select-visning och touchstorlekar.
- Ny regressionstestning verifierar uttryckligen att toolbar-CSS finns inne i raw editor HTML/iframe.

## v0.13.2 – Mobile Context & Fullscreen
- Mobilens **＋ Lägg till** öppnar nu en egen bottom-sheet med Start, Aktivitet, Beslut, Dokument, Delprocess, Anteckning och Slut utan att vänsterpanelen behöver öppnas.
- Markerade rutor får **••• Mer** med Kopiera, Formatering, Smart Layout horisontellt/vertikalt, fler egenskaper och borttagning.
- Ny **⛶ Helskärm** i mobilens nederkant. Header och toppverktygsfält döljs och canvasen använder hela mobilens viewport.
- Helskärmsläget försöker använda webbläsarens Fullscreen API när det stöds och har CSS-fallback när det inte gör det. Escape/system-exit synkroniserar tillbaka Maplinis UI.
- Mobilens Add/context-menyer använder 44–48 px touchmål, safe-area och backdrop för stabil användning med en hand.
- Vanliga mobilåtgärder kan nu utföras utan att sidopanelen är framme; avancerad formatering och alla verktyg finns fortfarande ett tryck bort.
- Desktop-layout, databas/Supabase och dependencies är oförändrade.

## v0.13.1 – Autosave & Recovery
- Tydlig autosave-status i verktygsraden: Sparar…, Autosparad med klockslag eller Sparfel.
- Tvåstegssparning: en recovery-snapshot skrivs direkt när innehåll ändras och rensas först när ordinarie lokal lagring verifierats.
- Vid avbruten session kan Maplini erbjuda Återställ eller Ignorera utan att skriva över den ordinarie processen automatiskt.
- Lifecycle-save förstärkt med visibilitychange, pagehide, freeze och beforeunload för mobil/appväxling.
- Delade read-only-vyer fortsätter att vara helt utan lokal persistens.

# v0.13.0 – Mobile UX

- Ny fast mobil snabbmeny i nederkant som växlar efter kontext. Normalläge: **＋ Lägg till**, **↶ Ångra**, **↷ Gör om**, **⊡ Anpassa**, **☰ Verktyg**. Markerad ruta: **＋ Nästa**, **Egenskaper**, **Duplicera**, **Ta bort**.
- Mobil canvas använder nu egen touch-gesthantering: dra på tom processyta för att panorera både horisontellt och vertikalt.
- Två fingrar ger pinch-zoom mellan befintliga 25–150 %, centrerad kring fingrarnas mittpunkt.
- Mobilens canvasviewport är begränsad till en användbar skärmhöjd så panorering sker i editorn i stället för genom hela sidan.
- Kopplingarnas touchmål är 44 px och pilens draghandtag har större osynlig träffyta.
- Noddragning, resize, connectorinteraktion och områdesmarkering undantas från canvasens pan-gest för att undvika konkurrerande touchbeteenden.
- Nederkanten tar hänsyn till safe-area på telefoner med gestfält/notch.
- Desktop-DOM och desktop-layout lämnas oförändrade. Ingen databas-, Supabase-, OAuth-, secret- eller dependency-ändring.

# v0.12.1 – Smart Layout refinement

- **Ja/Nej-aware decision layout:** connector labels are used as semantic ordering signals. In horizontal layout Ja is placed above Nej; in vertical layout Ja is placed left of Nej.
- **Fewer connector crossings:** three deterministic barycentric down/up sweeps reorder siblings based on connected neighbors rather than only original coordinates.
- **Better loop handling:** DFS detects feedback edges before rank calculation so a loop such as `X → Y → Z → X` no longer pushes ranks forward repeatedly. The main path remains compact and the feedback connector returns visually.
- Merge behavior, selected-only layout, node dimensions, selection state, Fit-to-screen and one-Undo-per-layout remain unchanged.
- Added Smart Layout regression coverage for reversed Ja/Nej source order, vertical branch semantics, feedback loops and crossing reduction.
- No database, Supabase, OAuth, secret or dependency changes.

# v0.12.0 – Smart Layout

- Ny **✨ Snygga till ▾**-meny i toppverktygsfältet.
- Hela processen kan ordnas automatiskt **horisontellt** eller **vertikalt**.
- Minst två markerade rutor kan snyggas till separat utan att övriga rutor flyttas.
- Layoutmotorn använder interna kopplingar för att skapa flödesnivåer: grenar sprids, syskon delar nivå och sammanslagningar placeras längre fram.
- Befintlig visuell ordning används som tie-breaker för stabilare resultat och cykler/disconnected delar hanteras defensivt.
- Layouten anpassar mellanrum till canvasens 2400×1400-gränser och försöker hålla alla rutor inom arbetsytan.
- Varje Smart Layout-körning är en enda Undo-operation. Markering och nodstorlekar bevaras och pilar ritas om efter flytten.
- Efter hel/processlayout används befintlig Fit-to-screen för att visa resultatet utan extra Undo-steg.
- Ny fristående `maplini_layout_core.js` med egna JS-regressionstester.
- Ingen databas-, Supabase-, OAuth-, secret- eller dependency-ändring.

# v0.11.7 – Contextual node toolbar

- Markerade rutor får nu en kontextuell snabbmeny direkt på canvasen.
- Enkel ruta: **＋ Nästa**, **Formatera**, **Duplicera**, **Ta bort**.
- Flera rutor: **Formatera**, **Färg**, **Duplicera**, **Ordna**, **Ta bort**.
- Multi-select-menyn innehåller befintliga Align/Distribute-kommandon och använder samma Undo-logik som toppmenyn.
- Snabbmenyn följer urvalets bounding box vid flytt/storleksändring och kompenserar för canvaszoom så knapparna förblir läsbara.
- Formatera återanvänder den befintliga sidopanelen och öppnar mobilens verktygspanel vid behov.
- Toolbar-interaktion undantas från connector hit-testing och dess Ordna-meny stängs vid klick utanför.
- Ingen databas-, Supabase-, OAuth-, secret- eller dependency-ändring.

# v0.11.6 – Multi-select formatting

- Formateringspanelen fungerar nu även när flera rutor är markerade.
- Typsnitt, textstorlek, textfärg, bakgrund, kantfärg, kanttjocklek, rutstil, fet/kursiv/understruken text och textjustering kan appliceras på hela markeringen samtidigt.
- Multi-select ligger kvar efter formatering och kopplade pilar ritas om när nodernas geometri påverkas.
- Varje formateringsändring skapar en enda Undo-checkpoint för hela markeringen.
- Enkelrute-funktioner som dokumentlänk och Inputs/Outputs döljs/inaktiveras vid multi-select för att undvika otydlig massredigering.
- Blandade formatvärden ändras inte förrän användaren aktivt väljer ett nytt värde.

# v0.11.5 – Connector quick routing

- Markerad pil visar nu ett kompakt snabbval direkt vid pilen: **Rak** eller **Vinkelrät**.
- Aktiv routing markeras visuellt så det syns direkt hur pilen är inställd.
- Snabbvalet återanvänder samma routinglogik som sidopanelen: byte till Rak rensar gamla brytpunkter (`viaX`/`viaY`).
- Routingbyte är en enda Undo-operation och respekterar read-only-läge.
- Snabbvalet följer den markerade pilens mittpunkt när pilens geometri ändras och har större touchytor på mobil.

# v0.11.4 – Straight connectors + sidebar scroll fix

- **Rak routing är nu verkligen rak:** byte från vinkelrät till Rak tar bort gamla brytpunkter (`viaX`/`viaY`) och renderar en direkt linje mellan fästpunkterna.
- Connector-kärnan ignorerar även gamla sparade brytpunkter när routing är `straight`, så äldre processer kan rätas ut korrekt.
- **Vänsterflanken kan scrollas hela vägen ned:** sidopanelen använder nu `box-sizing:border-box`, så dess padding räknas in i den fasta editorhöjden i stället för att klippas av.
- En smal scrollbar visas på desktop för tydligare återkoppling; mobil behåller dold scrollbar men full touch-scroll.

# v0.11.3 – Fit-to-screen + Align/Distribute

- Ny **⊡ Anpassa**-knapp zoomar och centrerar hela processen utan att ändra nodernas koordinater.
- Ny **Ordna ▾**-meny för vänster/center/höger, topp/center/botten och jämn horisontell/vertikal fördelning.
- Align/Distribute bevarar multi-select, nodstorlekar och kopplade pilar samt skapar en Undo-checkpoint per operation.
- Fit-to-screen kan zooma ned till 25% för stora processkartor.


## v0.11.1 — Faster Editing: multi-select group move
- Flera markerade rutor kan nu flyttas tillsammans genom att dra i valfri ruta i markeringen.
- Hela gruppen använder samma förflyttningsdelta och behåller sina inbördes positioner även nära canvasens kanter.
- Alla anslutna pilar ritas om kontinuerligt under gruppdragning; externa pilar följer respektive flyttad ruta.
- Manuella brytpunkter på pilar mellan två markerade rutor flyttas med gruppen så att intern routing inte deformeras.
- Gruppmarkeringen ligger kvar efter avslutad dragning och hela gruppflytten är en enda Undo-operation.
- Ingen databas-, OAuth-, secret- eller dependency-ändring.

## v0.11.0 — Faster Editing: duplicate + copy/paste
- Added **Duplicera** for selected node(s).
- Added Ctrl/Cmd+C, Ctrl/Cmd+V and Ctrl/Cmd+D editing shortcuts.
- Multi-node copy preserves only internal connectors between copied nodes.
- Deep copy preserves node content, styling, dimensions, Inputs/Outputs and document links.
- Pasted nodes are offset and selected immediately.
- Manual connector bend coordinates move with duplicated groups.
- Paste/duplicate is a single Undo operation and respects read-only mode.

## 0.10.45 — Insert step on connector
- Added **＋ Infoga steg** for a selected connector.
- Inserting replaces `A → B` with `A → Ny aktivitet → B` in one undoable operation.
- The new activity is positioned at the connector midpoint, selected, and opened for inline text editing.
- Connector color, width, dash, end marker and routing are preserved; manual via-points are cleared and smart auto anchors are used for the two new segments.
- Existing connector label (for example Ja/Nej) stays on the first segment so decision semantics are preserved.

## 0.10.44 – Connector labels & decision branches
- Markerade kopplingar kan nu få egen text direkt i formatpanelen, exempelvis Ja, Nej, Godkänd eller Avslag.
- Piltext visas som en diskret läsbar etikett ovanpå kopplingen och följer med när noder eller pilrouting flyttas.
- Första två nya utgående kopplingarna från en Beslut-nod föreslås automatiskt som **Ja** och **Nej**; texten är fullt redigerbar eller kan tas bort.
- Piltext sparas i befintlig connector-state och följer med vid reload.
- PDF/DOCX-snapshot och Excel/Google Sheets-export inkluderar piltext.
- Routing- och fästpunktskontrollerna är samtidigt korrigerade så att de förblir redigerbara i markerat pil-läge.
- Ingen databas-, OAuth-, secret- eller dependency-ändring.


## 0.10.43 – Smart connector routing
- Nya kopplingar använder vinkelrät routing som standard.
- Nya kopplingar använder smarta automatiska fästpunkter som följer nodernas relativa position.
- Markerad koppling kan växla mellan Vinkelrät/Rak och Auto/Behåll startpunkt.
- Vinkelräta kopplingar följer flyttade noder och behåller redigerbar mittlinje.
- PDF/DOCX-processbilden använder samma routing som canvasen.
- Befintliga äldre kopplingar behåller rak/manuell standard tills de ändras.
# Maplini Changelog

## 0.10.42 - Connector follow & visual polish
- Fixar rotorsaken till att pilar kunde ligga kvar på sin gamla plats när en ansluten ruta flyttades: berörda länkar markeras nu dirty och ritas om kontinuerligt under dragning.
- Samma geometriuppdatering görs vid resize, textändringar och formatering som kan påverka rutans storlek.
- Förfinad connector-rendering med mindre pilspetsar/markörer, rundade linjeändar och linjehörn, diskretare hover/selection samt mindre draghandtag på desktop.
- Nya kopplingar får en mjukare neutral standardfärg; befintligt sparat användarval skrivs inte över.
- Ingen databas-, OAuth-, secret- eller dependency-ändring.

## 0.10.41 - Inline document link, persistent selection & simpler scrolling
- Dokumentnodens `+ Lägg till dokumentlänk` öppnar ett URL-fält direkt i noden på canvasen i stället för att flytta fokus till vänsterpanelen.
- Inline-länken validerar http/https, sparas med Spara eller Enter och håller dokumentnoden markerad efter sparning.
- Nodmarkering bevaras explicit efter formateringsändringar, inklusive 3D/raised/glass/flat, så användaren kan fortsätta redigera utan att markera om noden.
- Tog bort iframe-baserad vertikal scroll, döljer den redundanta sidebar-scrollbaren men behåller wheel/touch-scroll och stoppar scroll chaining mellan panelerna.
- Ingen databas-, OAuth- eller dependency-ändring.

## 0.10.40 - Menu auto-close & node visual styles
- Öppna dropdown-menyer stängs när användaren klickar utanför dem, och en ny dropdown stänger den tidigare.
- Delningspanelen stängs också vid klick utanför.
- Ny inställning **Rutstil** för markerade rutor: Standard, 3D, Upphöjd skugga, Glas och Minimal/platt.
- Ny knapp för att applicera vald rutstil på alla rutor i processen.
- Rutstil sparas per nod, stöds av Undo och återskapas efter reload.
- PDF/DOCX-snapshot återger de nya visuella stilarna med motsvarande skuggbehandling.

## 0.10.39 - Global text typography
- Global formatting action now applies both selected font family and text size to all process nodes at once.
- Inputs/Outputs and document-link text inherit the node typography consistently.
- Global typography change is one Undo operation and persists with the process.

Integrerad bakgrundsväljare i **Processyta ▾**.

## Mönstrade
- Prickar / Dot grid
- Rutor / Graf
- Linjer / Linjerat
- Befintliga korslinjer, diagonal och tekniskt rutnät finns kvar

## Enfärgade och tonade
- Solid färg
- Gradient med startfärg, slutfärg och riktning

## Grafiska
- Uppladdad bakgrundsbild med reglerbar opacitet
- Vattenstämpel som text, t.ex. UTKAST/KONFIDENTIELLT
- Alternativ att använda uppladdad processlogga som vattenstämpel
- Reglerbar vattenstämpelopacitet
- Texturer: gammalt papper, pergament, canvas och betong

## Persistens och export
- Alla nya bakgrundsinställningar sparas per process i befintlig JSON-state
- PDF/DOCX-kartbilden återger gradienter, bilder, vattenstämplar och texturer
- Bakgrundsbilder begränsas till 1,5 MB för att skydda lokal lagring och backup

Ingen Supabase-migrering, OAuth-, secret- eller dependency-ändring.

# v0.10.38 — DOCUMENT LINK ADD FIX

- Fixar **+ Lägg till dokumentlänk** direkt i en Dokument-ruta.
- Klick markerar dokumentrutan, visar Dokument-panelen och fokuserar fältet **Dokumentlänk**.
- Dokumentfältet scrollas fram vid behov så att länken kan klistras in direkt.
- Befintliga giltiga dokumentlänkar fortsätter öppnas i ny flik.
- Ingen databas-, dependency- eller konfigurationsändring.

## 0.10.46 – Insert step type chooser
- **＋ Infoga steg** på en markerad pil öppnar nu ett kompakt val direkt vid pilverktygen.
- Användaren kan infoga **Aktivitet, Beslut, Dokument eller Slut** utan att först skapa en vanlig aktivitet och byta typ efteråt.
- Det valda steget placeras på pilens mittpunkt, kopplingen delas i två och den nya rutan öppnas direkt för textredigering.
- Hela infogningen är fortsatt en enda Undo-operation och befintlig pilstil/piltext hanteras via samma split-link-flöde som tidigare.
- Valmenyn stängs vid val, klick utanför, read-only-läge eller när den markerade kopplingen försvinner.
- Ingen databas-, OAuth-, secret- eller dependency-ändring.


## 0.11.2 – Quick Next Step
- Markerad Start/Aktivitet/Beslut/Dokument/Delprocess får **＋ Nästa steg** direkt på canvasen.
- Aktivitet, Beslut, Dokument eller Slut kan skapas och kopplas i ett klickflöde.
- Placeringen väljer i första hand höger sida men undviker upptagen yta och kan välja under/vänster/över.
- Beslutsgrenar återanvänder automatiska Ja/Nej-förslag.
- Nya steget öppnas direkt för redigering och Enter avslutar redigeringen.
- Hela operationen är en Undo och kräver ingen databas-/dependencyändring.
