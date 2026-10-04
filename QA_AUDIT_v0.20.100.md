# Maplini v0.20.100 – Mobil läsvy

Utgångspunkt: rigGihHub/Processkartan main, 780e59a589fe5b13888adc9289a9d6e5521a8f1d.

## Ändringar

- Återanvänder den befintliga grafbaserade steglistan även på mobil.
- Kompakt kartvy ovanför listan; långa namn radbryts.
- Tydliga Följ / Visa hela / Redigera-knappar med minst 44 px höjd.
- Listval återställer läsbar zoom och fokuserar valt steg; fönsterändring behåller markerat steg.
- Aktivt steg har aria-current="step".
- Versionsetiketten uppdaterad från kvarvarande 0.20.93 till 0.20.100. Äldre regressionstester låser inte längre alla framtida versioner till 0.20.93.

## Verifierat

- 516 Python-tester passerar.
- 38 JavaScript-testsviter passerar.
- Inbäddade JavaScript-program klarar node --check.
- git diff --check utan fel.

## Återstår

Visuell och interaktiv kontroll i Chromium vid 375, 390, 768 och 1440 px, inklusive långa processnamn, samtliga listval, Visa hela → listval, rotation, Redigera och Följ. Testmiljön saknar webbläsare och installationsförsöken gav ogiltiga nedladdningsfiler. Utseende och pekinteraktion är därför inte verifierade.

Ingen push eller publicering genomförd, enligt tidigare instruktion.
