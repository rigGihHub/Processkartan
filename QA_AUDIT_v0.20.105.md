# v0.20.105 – startrutan på mobil

Användarbilden visar en mycket liten startruta långt åt höger i en i övrigt tom karta. Den låg under den 2400 px breda, skalade kartan, så både position och innehåll ärvde kartzoom.

## Ändring

- Flyttad startvy till arbetsytan, utanför den transformerade kartan.
- Tom redigerbar process döljer kartwrapper, sidnavigator och bottenutfyllnad. Mobilens tomma arbetsyta har plats för startformuläret; vid behov går själva formuläret att scrolla.
- Inmatning 16 px, primär knapp 46 px och övriga mobilknappar minst 44 px.
- Första manuellt tillagda steget återställer kartzoom till 100 %.
- Efter första aktiviteten uppdateras även egenskapspanelens namn direkt. Felet upptäcktes vid prov i den publicerade webbläsaren.
- Lägesväxling uppdaterar startvyn direkt.
- Startvalen kan gå från läsläge till redigering när användaren har redigeringsbehörighet; delade läsvyer behåller samma behörighetskontroll.
- Svep i startvyn fångas inte av kartans gesthantering.

## Kontroller

516 Python-tester, 39 JavaScript-sviter och funktionella DOM-tester godkända. Startflödet kontrolleras i mobil- och datorläge, inklusive 25 % kartzoom, obligatorisk första aktivitet, skapande, 100 % första steg, ångra samt Rita/Förstå. Befintlig sökning, export, båda beslutsvägarna och mobilredigering täcks också. 32 inbäddade skript syntaxkontrollerade.

DOM-testet aktiverar de faktiska mobilreglerna i deras ursprungliga ordning. Det kontrollerar struktur, deklarationer och funktion men utför inte webbläsarlayout eller fysisk touch. Visuell kontroll av publicerad datorvy görs separat. Ingen fysisk telefonkontroll har utförts.
