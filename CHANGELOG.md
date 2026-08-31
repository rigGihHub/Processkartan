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

# Changelog

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
