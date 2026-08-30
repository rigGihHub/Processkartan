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
