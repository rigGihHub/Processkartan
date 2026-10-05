# v0.20.106 – logotyp och synlig zoom

Användarbilden visar en höjdbeskuren logotyp och en extra slogan ovanpå den som redan finns i bilden. Plus/minus för kartzoom fanns bara inne i en meny.

## Ändringar

- Logobilden ryms i sin behållare med object-fit:contain, utan förskjutning eller beskärning. Den extra sloganen är dold. Versionstexten är separat och reservutrymmet justeras på smalare datorfönster.
- Samma befintliga zoomkontroller flyttas till kartfönstrets övre högra hörn. Inga dubbla kontrolluppsättningar.
- Kontrollerna ligger utanför den skalade kartan och dess scrollcontainer, så de behåller placering och storlek när kartan panoreras eller zoomas.
- Arbetsytans placering följs med ResizeObserver och lägesväxling för mobilens snabbmeny och helskärm.
- Plus/minus ändrar zoom i steg om 10 procentenheter, från 25 till 150 %. Procentknappen återställer 100 %. Tryckytor minst 44 px.
- Samma canvastransform skalar rutor, text, pilar och inlagda bilder. Sparad kartgeometri ändras inte.

## Kontroller

516 Python-tester, 39 JavaScript-sviter och funktionella DOM-tester godkända. DOM-testet kontrollerar placering utanför zoom/scroll, verkliga knappar, zoomprocent, scrollmått, övre/nedre gräns, återställning och bevarade stegpositioner. Befintligt start-, läs-, redigerings-, sök-, import- och ångraflöde fungerar.

32 inbäddade skript syntaxkontrollerade, Python-kompilering och diffkontroll godkända.

DOM-testet utför ingen fysisk CSS-layout. Den publicerade datorvyn granskas separat i webbläsaren, inklusive faktisk skalning och kontrollplacering. Ingen fysisk mobilkontroll är utförd.
