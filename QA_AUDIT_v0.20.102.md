# Maplini v0.20.102 – mobilscrollning

Rapporterat fel: vertikala svep i mobilens läsvy når inte resten av steglistan.

## Rättning

- Streamlits HTML-komponent tillåter scrollning.
- Läsvyn låter webbläsaren hantera touch över kartans bakgrund, steg och kopplingar. Redigeringsläget behåller sin manuella panorering.
- Kartans vertikala scrollbehållare låser inte längre sidscrollningen i läsvyn. Horisontell kartscrollning finns kvar.
- Steglistan har naturlig höjd och följer sidans scrollning. Överblickens kort ryms i två kolumner och kan radbrytas.

## Verifiering

- 516 Python-tester godkända.
- 39 JavaScript-sviter godkända.
- Funktionella DOM-tester av den faktiska editorn: touchstart och touchmove över kartan, stegnamn och pil avbryts inte i mobil läsvy; egen vertikal kartpanorering körs inte. Redigeringslägets touchpanorering finns kvar.
- Befintliga DOM-flöden för startval, export, båda beslutsvägarna, ångra och sparad användardata godkända.
- Python-kompilering och diffkontroll godkända.

DOM-miljön simulerar inte fysisk touch eller CSS-layout. Riktig Android-/iOS-scrollning har inte verifierats där.
