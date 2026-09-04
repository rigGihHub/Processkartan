## Senaste release: v0.20.34 – Large Process Performance

Maplini har nu en reproducerbar prestandabaslinje för stora processkartor. Connector-routing begränsar dyr korsningsanalys på mycket stora kartor men behåller hinderundvikande, och persist-flödet gör mindre duplicerat arbete. Resultatet är snabbare öppning av stora kartor utan ändring av processdata eller molnmodell.

## Senaste release: v0.20.33 – Mobile Read & Follow

På mobil prioriterar Maplini nu **läsa och följa** framför full redigering. Processen öppnas i en ren mobil Läsvy med direktknappar för Följ processen och Anpassa. Användare med redigeringsrätt kan fortfarande gå till redigeringsläget via ✎. Stegdetaljer och Följ-processen använder större touchvänliga bottom sheets så att canvasen förblir begriplig även på liten skärm.

## Senaste release: v0.20.32 – Read / Presentation Mode

Maplini har nu en ren **Läsvy** för personer som ska förstå en process utan att redigera den. Redigeringspanelen och muterande verktyg döljs, canvasen får hela fokusytan och ett klick på ett steg visar befintlig processinformation som beskrivning, ansvar, system, instruktion, tid, KPI, risk, kontroll samt input/output.

Läsvyn ändrar ingen processdata och är helt reversibel via **Redigera** eller Escape. **Följ processen**, zoom, Anpassa och Översikt finns kvar så att läsaren kan orientera sig och vid behov gå vidare till den interaktiva genomgången. Ingen Supabase-migrering krävs.

---

## Senaste release: v0.20.31 – Follow Process Through Subprocesses

**Följ processen** kan nu fortsätta genom länkade delprocesser. När genomgången når en Delprocess går Maplini in i den underliggande kartan, följer dess steg och återvänder sedan till rätt fortsättning i huvudprocessen. Flera möjliga startpunkter kräver ett tydligt val; Maplini gissar inte.

Genomgången fortsätter att sparas som en sammanhängande körning på huvudprocessen, samtidigt som varje historiksteg bär sin processkontext. Ingen ny databasstruktur eller BPMN-hierarki behövs.

---

## Senaste release: v0.20.30 – Linked Subprocess Navigation

Maplini kan nu använda en **Delprocess** som en riktig navigerbar nivå i processkartan. När en delprocess markeras visas **Öppna delprocess**. Första gången skapas en egen fokuserad processkarta och därefter återanvänds samma länk. En enkel breadcrumb visar vägen tillbaka till huvudprocessen.

Lösningen är medvetet lättviktig: inga BPMN-gateways, ingen separat hierarkiadministration och ingen ny Supabase-tabell. Duplicerade delprocessrutor är dessutom olänkade som standard så att en kopia inte av misstag delar samma underprocess.

---

## Senaste release: v0.20.29 – Process Overview & Navigation

Maplini har nu en frivillig **Processöversikt** för större kartor. Översikten visar hela processens struktur i miniatyr, markerar den del av canvasen som är synlig och låter användaren hoppa direkt till ett steg eller ett område utan att zooma ut hela arbetsytan. Funktionen använder befintlig nodgeometri och förändrar inte processdatan.

Översikten är medvetet inte en ny permanent sidopanel, swimlane-funktion eller BPMN-navigator. Den öppnas vid behov från huvudradens **Översikt** och hålls borta från mobilens redigeringsyta för att behålla enkelheten. Ingen Supabase-migrering krävs.

---

## Senaste release: v0.20.28 – Deviation to Improvement Loop

Maplini knyter nu ihop processgenomgången med faktisk processförbättring. En öppen avvikelse kan öppnas via **Förbättra steg**, vilket tar användaren till exakt det steg där avvikelsen uppstod och håller observationen synlig medan processen justeras. Därefter kan samma avvikelse markeras som hanterad.

Detta är medvetet inte ett separat ärendehanteringssystem. Maplini återanvänder befintlig genomgångshistorik och avvikelsestatus för att stärka kärnloopen **Rita → Följ → Upptäck → Förbättra**. Ingen Supabase-migrering krävs.

---

## v0.20.27 – Safe Sharing & Revoke

Maplini visar nu tydligt när en publik läslänk är aktiv och låter användaren återkalla den på riktigt genom att rensa både delningstoken och delningsläge.

## v0.20.25 – Safe Cloud Editing
Maplini skyddar nu mot tyst överskrivning när två personer arbetar med samma molnprocess. En redan sparad process får bara uppdateras om molnversionen fortfarande är exakt den version som användaren öppnade. Om någon annan har hunnit spara stoppas molnuppdateringen och den lokala versionen behålls.

Detta är en säkerhetsmekanism för redigering, inte realtidssamarbete. Ingen Supabase-migrering eller ny processdata krävs.

---

## v0.20.23 – Trustworthy Process Analysis
Processkontrollen visar inte längre ett artificiellt hälsobetyg. Den redovisar i stället konkreta strukturfynd, skiljer fakta från bedömningar och förklarar vilken regel som utlöst varje fynd.

# Maplini v0.20.22 – Core Workflow Simplification

Den här releasen minskar konkurrensen mellan kärnuppgiften och sekundära verktyg. Huvudraden prioriterar nu processnamn, skapande, sparning, **Följ processen**, ångra/gör om, orientering, layout och export. Funktioner som främst behövs efteråt eller mer sällan ligger kvar under **Mer**.

**Dela process**, **Avvikelser** och **Skala process** är alltså inte borttagna. De har flyttats till en progressivt fördjupad meny tillsammans med kvalitets- och avancerade verktyg. Detta gör den första arbetsytan lugnare utan att begränsa professionella användare.

Ingen processdata, routing eller Supabase-konfiguration ändras.

---

# Maplini v0.20.21 – Follow Process Continuity

Den här releasen putsar den visuella hierarkin i processflödet utan att lägga till nya funktioner. Automatiska huvudflöden behåller högre visuell närvaro, medan Ja/Nej-grenar och deras fortsättning tonas ned något. Färgvalet ändras inte, så användarens egna connector-färger bevaras.

När exakt en ruta markeras blir dess anslutna automatiska pilar tydligare samtidigt som övriga automatiska flöden lugnas tillfälligt. Det gör det enklare att snabbt se vad som leder in i och ut ur den ruta man arbetar med. Manuellt hanterade kopplingar lämnas utanför hierarkin. Ingen routing, datamodell eller Supabase-konfiguration ändras.

---

# Maplini v0.20.19 – Connector Label Clarity

Den här releasen förbättrar läsbarheten på piltexter. Ja/Nej och andra explicita connector-etiketter behöver inte längre ligga vid pilens geometriska mittpunkt. Maplini provar flera lägen på raka delar av kopplingen och föredrar en plats med luft till processrutor, böjar och redan placerade piltexter.

Om standardläget är blockerat kan etiketten byta sida om pilen. När en markerad pils etikett flyttas följer snabbverktyget med logiken och hamnar på motsatt sida, så text, draghandtag och verktyg inte staplas. Själva pilrutten ändras inte av etikettplaceringen och ingen Supabase-migrering krävs.

---

# Maplini v0.20.18 – Connector Lane Separation

Den här releasen gör parallella automatiska kopplingar lättare att läsa. Om en ny vinkelrät auto-pil skulle ligga ovanpå eller mycket nära en längre del av en befintlig pil väger Maplini in överlappningen och väljer hellre en närliggande separat korridor när det finns en rimlig sådan.

En kort gemensam stam direkt vid samma beslut eller återförening är fortfarande tillåten. Hindrande processrutor och riktiga korsningar väger dessutom tyngre än lane-separation, så routingmotorn väljer inte onödigt långa omvägar bara för att skapa luft mellan linjer. Manuella pilar lämnas helt orörda. Ingen Supabase-migrering krävs.

---

# Maplini v0.20.17 – Connector Crossing Reduction

Den här releasen gör automatisk routing mer medveten om andra flöden. Om två möjliga vinkelräta pilbanor båda är fria från processrutor föredrar Maplini den som ger färre riktiga korsningar mot orelaterade kopplingar. Rutkollisioner är fortfarande mycket dyrare än pilkorsningar, så appen skapar inte stora omvägar bara för att undvika en linje.

Kopplingar som delar källa eller mål får fortsatt förgrenas och mötas naturligt. Manuellt redigerade pilar, fri routing och manuella fästpunkter lämnas orörda. Ingen datamodell ändras och ingen Supabase-migrering krävs.

---

# Maplini v0.20.16 – Smart Connector Routing

Den här releasen förbättrar själva pilbanan i tätare processkartor. Automatiskt hanterade vinkelräta pilar kontrollerar nu om den normala vägen passerar genom andra processrutor. Om den gör det provar Maplini alternativa vägar runt hindret och väljer den kortaste rena rutten.

Om en riktig omväg behövs lämnar pilen först källrutan med en kort rak sträcka i rätt riktning, går runt hindret och ansluter sedan naturligt till målrutan. Manuellt redigerade pilar, fria pilar och manuella fästpunkter lämnas helt orörda.

Ingen datamodell ändras och ingen Supabase-migrering krävs.

---

# Maplini v0.20.15 – Smart Flow Continuation

Den här releasen förbättrar automatisk placering av beslutets Ja/Nej-grenar. När båda grenarna skapas tillsammans planeras de som ett visuellt par: samma framåtrank, balanserade runt beslutet och med symmetrisk undanmanöver när standardläget är upptaget. Manuellt placerade objekt flyttas inte.


Canvasens direktmanipulation är renare. När en enda ruta är markerad används den lilla **+**-kontrollen vid själva rutan som den primära vägen för att bygga vidare. Den flytande snabbmenyn duplicerar därför inte längre nästa-steg-kommandot utan fokuserar på **Form, Egenskaper, Duplicera och Ta bort**.

Den direkta +‑kontrollen ligger närmare rutan och får tydligare hover/fokusrespons. Kopplingspunkterna är fortsatt tillgängliga på markerad ruta men visuellt lugnare tills användaren för musen över dem. Markeringen runt en vald ruta har också tonats ned något.

Ingen datamodell ändras och ingen Supabase-migrering krävs.

---

# Maplini v0.20.10 – Walkthrough Transition Polish

Följ processen visar nu vägval tydligare direkt i processkartan. När ett steg har märkta Ja/Nej-grenar visas diskreta etiketter vid de möjliga nästa rutorna. När användaren svarar och vägen blir entydig tonas de andra alternativen bort, medan den valda rutan och pilen förstärks innan genomgången går vidare.

Det gör att övergången känns mer som att faktiskt följa ett flöde: **jag är här → jag svarar → jag ser exakt vart processen går**. Ingen extra panel, HUD eller administration har lagts till. Befintlig avvikelsehantering och automatisk fortsättning är oförändrad.

Ingen gamification och ingen Supabase-migrering krävs.

---

# Maplini v0.20.8 – Visual Walkthrough Position

Följ processen är nu tydligare kopplat till själva processkartan. Den aktuella rutan markeras direkt på canvasen, tidigare passerade steg tonas ned och nästa möjliga steg samt relevanta pilar framhävs diskret. Vid ett entydigt Ja/Nej-vägval visas den valda grenen tydligare redan innan nästa steg öppnas.

När genomgången flyttar vidare följer canvasen mjukt med om nästa steg ligger utanför den centrala läszonen. Maplini zoomar inte automatiskt och lägger inte till någon permanent HUD eller extra administrationspanel.

Ingen gamification och ingen Supabase-migrering krävs.

---

# Maplini v0.20.7 – Direct Follow Process

Följ processen är nu mer direkt. På vanliga aktivitetssteg står **Har du gjort detta?** i centrum med större Ja/Nej-knappar. När det bara finns en möjlig nästa väg tar Ja eller Nej dig automatiskt vidare efter en kort knapprespons.

Maplini auto-fortsätter inte när det finns ett verkligt vägval eller flera möjliga nästa steg. Explicita kontrollfrågor behåller sin detaljerade hantering.

Ingen Supabase-migrering krävs.

---

# Maplini v0.20.6 – Visual Flow Rhythm

Den här releasen putsar själva rytmen i processflödet. Nya steg får nu mer genomtänkta avstånd beroende på vad som byggs: Objekt och Aktivitet hålls relativt nära varandra, Beslut får mer luft och Ja/Nej-grenar separeras tydligare.

När en ensam ruta markeras förstärks dess automatiskt hanterade in- och utgående pilar mycket subtilt, så det blir lättare att se exakt var steget hör hemma utan extra paneler eller markeringar.

Ingen Supabase-migrering krävs.

---

# Maplini v0.20.5 – Smart Connector Flow

Automatiskt skapade pilar beter sig nu mer intelligent när du flyttar rutor. De följer relationen mellan rutorna live och växlar mellan rak och vinkelrät form när det ger ett renare flöde.

Manuellt pilarbete skyddas samtidigt bättre. Så fort du själv väljer piltyp eller ändrar fästpunkter slutar Maplini auto-styra just den pilen.

Ingen Supabase-migrering krävs.

---

# Maplini v0.20.4 – Formation Selection

Flera markerade rutor känns nu mer som en sammanhållen formation. En diskret ram omsluter markeringen och följer med medan du drar hela gruppen.

Snabbverktyget får samtidigt **Ordna** när flera rutor är markerade. Där kan du justera kanter, fördela rutor jämnt eller köra Snygga till bara på markeringen. För små korrigeringar fungerar piltangenterna direkt; håll Shift för större steg.

Det här skapar ingen permanent grupp i processdata. Det är bara snabbare och tydligare manipulation av en tillfällig markering. Ingen Supabase-migrering krävs.

---

# Maplini v0.20.3 – Canvas Build Rhythm

Nu går det snabbare att bygga processen direkt på canvasen. Markera ett steg och tryck **Tab** för att skapa rekommenderat nästa steg. På ett Beslut skapar Tab Ja/Nej-grenarna, medan **Shift+Tab** öppnar valet av alternativa nästa steg. **Enter** går direkt in i textredigering.

Det går också att dra en pil från en kopplingspunkt och släppa den på tom canvas. Om draget är tydligt nog skapar Maplini då automatiskt den rekommenderade nästa ruttypen där du släpper och kopplar den direkt. Det går fortfarande att släppa pilen på en befintlig ruta precis som tidigare.

Ingen gamification och ingen Supabase-migrering krävs.

---

# Maplini v0.20.2 – Navigation Feel

Den här releasen fortsätter på samma spår: mer känsla av ett välkontrollerat bygg-/strategiverktyg utan poäng eller belöningar.

På desktop kan du nu zooma mot den punkt du faktiskt tittar på med **Ctrl/Cmd + mushjul**. Håll **Mellanslag** och dra för att panorera tillfälligt, även när du står i markeringsläge. Mittenknappen kan också användas för snabb panorering. Markeringsramen visar dessutom direkt vilka rutor som kommer att följa med innan du släpper.

Mobilens befintliga pan och pinch-zoom är oförändrade. Ingen Supabase-migrering krävs.

---

# Maplini v0.20.1 – Canvas Feel, No Rewards

Den här releasen justerar “dataspelskänslan” bort från gamification och mot **responsiv interaktion**. FLOW-streaken är borttagen. I stället känns canvasen mer fysisk och direkt: rutor lyfter när de dras, snap blir tydligare när något linjerar och kopplingsmål markeras medan man drar en pil.

Ja och Nej i Följ processen får samma neutrala tryckrespons. Nya steg får fortfarande en kort spawn-rörelse eftersom den fungerar som omedelbar feedback på att kommandot genomförts, inte som belöning.

Ingen Supabase-migrering krävs.

---

# Maplini v0.20.0 – Game Feel / Flow Streak

Maplini ska inte bara vara effektivt utan också kännas bra att använda. Den här releasen lägger därför till diskret **game feel** i kärnflödet.

När du bygger vidare med **+ Nästa** poppar nya steg in mjukt. Fortsätter du bygga inom kort tid visas en **FLOW ×N**-streak som räknar faktiska skapade steg. Den är bara visuell och påverkar varken processdata eller någon påhittad kvalitetspoäng.

Även **Följ processen** har fått mer taktil respons med korta Ja/Nej-animationer, mjuk övergång mellan steg och en liten avslutningspuls när en genomgång klaras utan avvikelser. All rörelse stängs av automatiskt för användare som föredrar reducerad animation.

Ingen Supabase-migrering krävs.

---

# Maplini v0.19.9 – Quick Shape Picker

Formvalet från v0.19.8 finns nu även direkt i snabbverktyget ovanför markerad ruta. **Form** öppnar fyra visuella ikoner för Typstandard, Rektangel, Rundad och Kapsel. Det gör att formen kan bytas utan att öppna Utseende-panelen.

Snabbvalet fungerar även på flera markerade rutor och använder samma sparning, undo och `shapePreset`-data som det befintliga formvalet. Ingen Supabase-migrering krävs.

---

# Maplini v0.19.8 – Shape Presets + Better Flow Rhythm

Den här releasen kombinerar två förbättringar i processritningen. För det första får **Snygga till** lite mer luft mellan steg och grenar så att flöden med olika stora Objekt, Aktiviteter och Beslut blir lättare att läsa. För det andra går det nu att ändra en rutas **Form** direkt under Utseende.

Tillgängliga standardformer är **Typstandard**, **Rektangel**, **Rundad** och **Kapsel**. Typstandard behåller Maplinis metodikform för nodtypen, medan de andra alternativen låter användaren göra en avvikande visuell form när det behövs. Formvalet lagras tillsammans med noden och kräver ingen databasändring.

---

# Maplini v0.19.7 – Clearer Node Hierarchy

Den här releasen gör kärnflödet lättare att läsa redan vid första ögonkastet. Objekt, Aktivitet och Beslut har nu tydligare roller i samma visuella designsystem: Objekt är kompakt och statiskt, Aktivitet är processens primära arbetskort och Beslut är ett tydligt vägval. Förändringen är medvetet återhållsam och lägger inte till nya reglage eller dekorativa teman.

Ingen ny Supabase-migrering krävs.

---

# Maplini v0.19.6 – Cleaner Decision Flows

Den här releasen fokuserar på att göra processflödet mer lättläst och professionellt utan fler reglage. Automatiska vinkelräta pilar får mjukt rundade hörn, och Ja/Nej-grenar får diskret färgkodade etiketter så att vägval kan avläsas snabbare. Själva pilarna behåller sin neutrala stil för att processkartan inte ska bli visuellt stökig.

Rak routing, fri/manuell routing och befintlig Ja/Nej-logik är oförändrade. Ingen ny Supabase-migrering krävs.

---

# Maplini v0.19.5 – Guided Follow Process

Den här releasen fokuserar på Maplinis två kärnor: ett tydligt processflöde och en enkel interaktiv genomgång. **Följ processen** visar nu aktuell aktivitet tydligare, större Ja/Nej-knappar och en enkel positionsrad. Aktiviteter utan egna frågor får automatiskt frågan **”Har du gjort detta?”**, så ett vanligt processflöde kan följas direkt utan extra konfigurering.

Nej på den automatiska snabbfrågan registreras som en avvikelse men kräver inte att användaren fyller i uppföljningsformuläret direkt. Egna kontrollfrågor fortsätter däremot att använda den mer strukturerade avvikelseuppföljningen.

Ingen ny Supabase-migrering krävs.

---

## Snyggare processflöden v0.19.4

`✨ Snygga till` i toppraden är nu en direkt en-klicksfunktion. Maplini rätar upp det sammanhängande flödet, balanserar grenar, centrerar återföreningar, jämnar avstånd och snyggar till automatiska pilar utan att ändra processens logik. Den lilla pilen bredvid öppnar fortfarande manuella layoutval. Ingen ny databas- eller Supabase-migrering krävs.

## Individual avvikelsestatus v0.19.1

Varje avvikelse kan nu följas upp separat. En genomgång med flera avvikelser kan därför ha både öppna och hanterade åtgärder samtidigt. Genomgången räknas som helt hanterad först när alla dess avvikelser är hanterade. Statusen synkas via den befintliga `walkthrough_runs`-tabellen från v0.18.9; ingen ny SQL-migrering behövs.

## UI Regression Fix v0.13.4

- Fixar regressionen där canvasens kontextverktyg (`Rak/Vinkelrät` och nodens snabbmeny) renderades som vanliga HTML-kontroller uppe till vänster trots att inget var markerat.
- Grundorsak: toolbar-CSS låg i Streamlit-förälderns stylesheet medan editorn körs i ett separat `components.html`-iframe. CSS kan inte korsa iframe-gränsen.
- Flyttar/duplicerar därför toolbarernas visibility-, layout-, hover-, active- och touch-regler till editorns eget iframe-stylesheet.
- Båda toolbarerna är nu `display:none` som standard och visas endast när JavaScript sätter `.on` efter korrekt nod-/pilmarkering.
- Ingen databas-, Supabase- eller dependencyändring.

# Maplini v0.19.0

## Avvikelseöversikt v0.19.0

Toppraden har nu **⚠ Avvikelser**, en samlad uppföljningsvy över genomgångar i aktuell personlig/workspace-vy. Den visar öppna, försenade och hanterade avvikelser och kan filtreras på status, ansvarig och endast försenade. Varje rad visar process, fråga/steg, förklaring, ansvarig och deadline. Från raden kan användaren öppna källprocessen eller markera hela genomgångens uppföljning som hanterad/öppen. Molndata använder tabellen `walkthrough_runs` från `supabase_schema_v0189.sql`; v0.19.0 kräver ingen ny migrering.


## Molnsynkad genomgångshistorik v0.18.9

Genomgångar sparas fortfarande lokalt först, men när användaren är inloggad synkas de även till Supabase. Historiken kan därmed följa processen mellan datorer och workspace-användare. Uppföljningsstatus på avvikelser synkas också. Installera `supabase_schema_v0189.sql` efter de tidigare workspace-/integritetsmigreringarna. Om migreringen inte är installerad fortsätter `Följ processen` att fungera lokalt och visar tydligt att molnsynk saknas.


## Avvikelseuppföljning v0.18.8

När användaren svarar **Nej** på en Kontrollfråga öppnas nu direkt en avvikelsepanel. Innan användaren får gå vidare måste avvikelsen beskrivas, en ansvarig anges och ett förfallodatum sättas. Informationen följer med in i sammanfattningen, kopierat resultat och den lokala genomgångshistoriken. Nej på en Vägvalsfråga påverkas inte och fortsätter vara ett normalt processutfall.


## Kontrollfråga eller vägvalsfråga v0.18.7

Kontrollfrågor och vägval är nu separerade. **Kontrollfråga** används när ett Nej betyder att processen inte har följts och ska registreras som avvikelse. **Vägvalsfråga** används när både Ja och Nej är normala affärsutfall; svaret styr då automatiskt en pil märkt Ja eller Nej utan att skapa en avvikelse. Detta gör att `Följ processen` kan användas både för regelefterlevnad och verkliga processförgreningar utan att blanda ihop de två.


## Smart Ja/Nej-väg v0.18.6

En kontrollfråga kan nu markeras **Styr Ja/Nej-väg**. Om steget har en unik pil märkt **Ja** och en unik pil märkt **Nej** använder `Följ processen` svaret för att välja nästa väg automatiskt. Användaren behöver alltså inte svara Ja och sedan manuellt välja Ja-grenen. Om märkningen saknas eller är tvetydig gissar Maplini inte utan faller tillbaka till ett manuellt vägval med tydlig förklaring.


## Walkthrough history v0.18.5

`Följ processen` har nu lokal historik per process. Utföraren måste ange namn eller initialer innan genomgången startar. När genomgången slutförs sparas datum/tid, utförare, antal steg, Ja/Nej och avvikelser i webbläsaren. Avvikelser kan markeras som **Hanterad** och öppnas igen. Resultatet kan kopieras från historiken. Historiken är ännu inte molnsynkad mellan datorer; det kräver ett separat backend-/behörighetslager och är avsiktligt inte smygimplementerat i denna release.


## Följ processen v0.18.4

Maplini kan nu användas efter själva kartläggningen. Lägg kontrollfrågor på ett processteg och välj **▶ Följ processen** för att gå igenom den faktiska processgrafen steg för steg. Ja/Nej-svar måste fyllas i innan användaren går vidare och Nej samlas som avvikelser i en avslutande sammanfattning. Förgrenade flöden använder befintliga pilar och piltexter för att välja nästa väg. Den första versionen sparar inte körhistorik permanent; den delen är avsiktligt separerad från kartans processdata.

**Snygga till** arbetar nu endast med sammanhängande flöden och lämnar okopplade utkast på plats. Funktionen ändrar inte längre zoomnivån automatiskt. Desktop-vänsterpanelen har dessutom extra bottenutrymme för säkrare scrollning i Chrome.


## Process Intelligence v0.18.3

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


### v0.18.3
Connector drag, multi-page horizontal scrolling and verified zoom direction.


### v0.18.3
Förfinar Smart Layout-pilarnas centrering, desktop-sidebarens åtkomlighet, rutstilar och den samlade textformateringen.


### v0.18.3
UI simplified: Ordna removed, compact account panel, dedicated Logotyp menu, and whole-process scaling including fit to selected A4/A3 page.


### v0.18.3
Connector dragging fixed: click-drag works directly on the connector hit area without a separate pre-selection click.


### v0.18.3
Stability/UX cleanup: dynamic multi-page layout bounds, resilient toolbar positioning, resize recalculation and centralized popover cleanup.


### v0.18.3
Free connector routing: drag the arrow body independently while endpoints remain attached and continue following moved nodes. Includes a small visual/UX polish pass.


### v0.18.3 – Integrity & Core Interaction
This release fixes workspace ownership integrity, connector one-gesture/free-drag behavior and Google Sheets column alignment.

**Supabase:** deployments using workspaces must run `supabase_schema_v0147.sql` after updating the app. The migration preserves editor access but enforces the workspace owner as canonical `processes.owner_id`.

**Browser smoke QA:** `python tests/browser_interaction_smoke.py` runs the embedded editor in Chromium and verifies one-gesture connector drag, attached endpoint behavior after moving a node, and Undo.


### v0.18.3
30% Simpler: the main toolbar now exposes only core commands. Export/page settings are grouped under Export, secondary tools under More, and the normal mobile bar is reduced to four actions.


### v0.18.3
Stability/polish pass for the simplified command surface. Nested menus now remain open correctly, mobile keeps four primary actions while Redo/Fullscreen remain available secondarily, and browser smoke coverage validates these flows together with free connector dragging.


### v0.18.3
Actionable Process Check: structural findings now explain what to do next, are prioritized, and can focus affected nodes directly on the canvas. The analysis remains deterministic/local and does not add an AI dependency.


### v0.18.3
First-Time User UX: empty editable processes now present a clear first-step card on the canvas with direct Start/Activity actions and guidance to continue with `＋ Nästa`.


### v0.18.3
New Process UX: browser `prompt()` has been replaced by a Maplini-native naming dialog with Enter/Escape support, inline validation, cancel/backdrop behavior and direct continuation into the empty-canvas first-step flow.


### v0.18.3
Connector Labels & Selection UX: connector text is now per-connector, live-updating, visually offset from the drag handle and rendered as a readable badge. New connectors have no automatic Ja/Nej label. The node-delete action only appears for a single selected node.


### v0.18.3
Connector Interaction Polish: selected connector text, drag handle and routing quick toolbar are now spatially separated so they no longer stack on top of one another during editing.


### v0.18.3
Connector Formatting Cleanup: connector formatting is now fully self-contained, with its own width control and clearer Swedish terminology. Node border controls stay hidden during connector editing.


### v0.18.3
Context Panel Polish: the left formatting panel now clearly switches between Pil, Ruta, Flera rutor and an unselected state, with contextual guidance instead of mixed generic copy.


### v0.18.3
Typography Cleanup: the font picker is reduced from 27 options to 7 clear choices. Older saved fonts remain supported through a temporary legacy option rather than being silently changed.


### v0.18.3
Canvas Appearance Cleanup: Processyta now offers five focused background choices. Older saved backgrounds remain supported through a temporary legacy option instead of being silently changed.


### v0.18.3
Node Style Cleanup: the standard node-style picker is reduced to Standard, Upphöjd and Minimal. Older 3D/Glass styles remain fully supported when opening existing processes.


### v0.18.3
Full Canvas Zoom & Ctrl Multi-Select: top-bar zoom now scales every visible object and text element in the embedded canvas, and Ctrl/Cmd-click toggles multiple node selection.


### v0.18.3
First View & A4 Portrait Default: empty processes now present a proper centered start card inside the editor iframe, A4 portrait is the default page format, and generic browser/iframe noise no longer raises the red data-safety banner.


### v0.18.3
Maplini's core process model is now Object → Activity → Object. Object in/out are two user-facing roles for the same underlying object type, allowing results to become inputs to later activities.


### v0.18.3
Dependency Coach: direct Activity → Activity connections are now challenged in context, and Process Check explains that a missing result/object may be hiding the real dependency.


### v0.18.3
Process Scale Quick Access: `Skala process` is now a main-toolbar control, and its +10% / −10% actions keep the menu open for repeated presses.


### v0.18.3
Canvas Pan & Scale Slider: desktop users can drag blank canvas to navigate, and whole-process scaling uses a 50–150% slider that changes actual node dimensions as well as text and spacing.


### v0.18.3
Blank canvas click now clears the current selection while drag-to-pan remains intact.


### v0.18.3
Magnetic Alignment: node dragging snaps to an invisible grid and to other nodes' edges/centers. Connected nodes aligned on the same axis receive a straight connector. The quick `Formatera` action is now called `Egenskaper`.


### v0.18.3
`Mer → Rensa hela canvasen` removes all nodes/connectors only after an explicit confirmation. The operation is undoable.


### v0.18.3
Smart Connector Polish automatically keeps ordinary connectors straight when nodes share an axis and orthogonal otherwise, while preserving user-created free/manual routes during normal dragging.


### v0.18.3
Object UX keeps one technical Object type but adds clear input/output/intermediate role hints in creation, node labels and properties guidance.


### v0.18.3
Faster Process Building turns the contextual Next action into a one-click recommended continuation, while a separate dropdown preserves alternate step types. Ctrl/Cmd+Enter continues the flow directly from inline editing.


### v0.18.3
Process Flow Assistant gives contextual methodology help for direct Activity-to-Activity links, with one-click insertion of an Object/result or an explicit intentional override.


### v0.18.3
Automatic Cleanup adds a one-click process tidy action that chooses layout direction from the existing flow, aligns nodes, evens spacing and cleans connector geometry without changing graph logic.


### v0.18.3
Undo Safety introduces atomic history transactions for clear, layout/automatic cleanup and scale gestures, ensuring one user action restores with one Undo and no-op gestures create no history noise.


### v0.18.3
Canvas Performance reduces per-frame work on large maps with local geometry invalidation, cached node-to-link adjacency and path-only connector updates during drag/resize gestures.


### v0.18.3
Build Flow UX Polish unifies the recent methodology features with a contextual flow cue, highlighted recommended alternatives, better next-step feedback and automatic viewport follow when extending a process.


### v0.18.3
Processinformation adds structured business metadata to process steps: description, responsible role, system, instruction, risk, control, KPI and duration. The data is kept off-canvas in the properties panel and is backward compatible with older saved maps.


### v0.18.3
Egenskapspanel UX makes process information faster to enter: essentials first, advanced details collapsed, reusable role/system suggestions, clearer optional completeness feedback and keyboard save/focus behavior.


### v0.18.3
Direct drag removes the preselection step for moving nodes. Object-role badges are no longer rendered above object nodes; role metadata remains preserved in the process data.


### v0.18.3
Page setup is now available directly over the canvas through a compact sticky control for A4/A3, portrait/landscape and automatic or 1–8 pages. Existing Export settings remain synchronized.


## v0.19.4 – Smart + Nästa
Bygg vidare på en markerad ruta med `+ Nästa`. Maplini försöker nu hålla samma flödesriktning, baslinje och visuella rytm automatiskt. Beslut får separerade grenar och kollisioner flyttas till parallella körlinjer utan att bryta huvudriktningen.


### v0.20.15 – Branch Rejoin
Enkla Ja/Nej-grenar kan sammanföras explicit till ett gemensamt nästa steg med smart, centrerad placering utan att Maplini flyttar manuellt placerade noder.


### v0.20.15 – Flow Collision Prevention
Automatisk placering väger nu in befintliga kopplingslinjer för att minska överlappande och korsande flöden i större processkartor. Befintlig layout flyttas inte.


### v0.20.27 – Safe Sharing & Revoke
Publik processdelning visar nu aktiv status och kan återkallas direkt. Den gamla länken slutar då fungera eftersom både delningstoken och delningsläge rensas i molnet.
