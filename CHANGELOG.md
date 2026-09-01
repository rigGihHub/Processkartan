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
