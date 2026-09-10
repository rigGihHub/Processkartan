# Produktgranskning – Maplini v0.20.43

## Frågan
Gör Maplini användaren snabbare i kärnflödet **Rita → Förstå → Följ**, eller har gränssnittet börjat visa för mycket på samma gång?

## 1. Processägare som ritar från noll
**Friktion:** toppfältet visade både zoom, Anpassa, Översikt och Ansvar samtidigt som Spara, Följ, Läsvy, Snygga till, Exportera och Mer. Funktionerna är bra, men de konkurrerade visuellt med själva ritandet.

**Åtgärd:** zoom, Anpassa, Översikt och Ansvar grupperas under **Visa ▾**. Funktionerna är kvar och deras befintliga ID:n/beteenden bevaras.

## 2. Chef eller kollega som ska förstå processen
**Behov:** kunna läsa och orientera sig utan redigeringsbrus.

**Beslut:** **Läsvy** och **Följ processen** ligger kvar som tydliga huvudhandlingar. Översikt och Ansvar är sekundära vyer och flyttas därför till Visa-menyn, inte bort.

## 3. Medarbetare som faktiskt följer processen
**Behov:** aktuell handling ska dominera, inte administrationsfunktioner.

**Beslut:** Follow-flödet ändras inte i denna release. **Följ processen** är fortsatt den starkaste primära knappen i desktopflödet och mobilens Read/Follow-prioritering lämnas intakt.

## 4. Verksamhetsutvecklare / kvalitetsansvarig
**Friktion:** funktionen hette `Analysera process` i menyn men panelen och produktlogiken heter `Processkontroll`.

**Åtgärd:** samma begrepp används nu överallt: **Processkontroll**. Det beskriver bättre att Maplini visar konkreta strukturkontroller och inte en AI-analys eller ett syntetiskt betyg.

## 5. Sällananvändare
**Friktion:** avvikelser låg för högt i Mer-menyn i relation till produktens kärna.

**Åtgärd:** avvikelser finns kvar men flyttas till **Övrigt** längst ned i Mer-menyn. Ingen avvikelsefunktion tas bort eller byggs ut.

## 6. Power user
**Behov:** avancerade verktyg, export, skalning, bakgrund och logotyp måste fortfarande gå att nå.

**Beslut:** inget av detta tas bort. Granskningen förenklar den omedelbara ytan i stället för att göra en riskfylld funktionsrensning.

## Övrigt fynd
`Processyta` visades dubbelt som rubrik i samma meny. Dubbletten är borttagen.

## Produktbeslut
Maplini ska inte vinna på flest synliga kontroller. Det ska kännas som att huvudytan säger:

**Rita processen → Snygga till → Följ den.**

Sekundära vyer och administration ska finnas nära till hands, men inte konkurrera med kärnan.
