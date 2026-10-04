# Maplini v0.20.101 – användarfeedback och verifiering

Utgångspunkt: granskningen av den publicerade v0.20.93 och den lokala mobilförbättringen v0.20.100. Ändringarna är lokala och inte publicerade.

| Punkt | Genomförd ändring |
| --- | --- |
| Komplett exempel och beslut | Sju steg med ansvar, beskrivningar, namngivna Ja/Nej-vägar och två avslut. Ofullständiga beslut får varningar i redigering, Förstå och Följ. Följ kan inte passera beslutet förrän dess vägar är kompletta och unikt namngivna. |
| Tydlig start | Skapa själv, Utgå från dokument och Prova exempel på första besöket. Start återöppnar vyn. Dokumentimport från denna ingång och exempel får egna process-ID:n. Återvändande användare fortsätter i sparat arbete. |
| Innehåll före formatering | Stegnamn, beskrivning och ansvar visas före snabbformatering. Namn och ansvar använder befintlig lagring och ångra. |
| Export direkt | Befintlig exportmeny är synlig i verktygsraden. På mobil flyttas samma meny till läsvyn och tillbaka vid redigering. Exportfunktionerna behåller sina händelsehanterare. |
| Enklare språk | Underlag, Resultat, Vad behövs före? och Vad blir resultatet? i palett, stegpanel, läspanel och tabellrubriker. Modellens inputs/outputs och objectRole är oförändrade. |
| Läsbarhet och orientering | Standardstorlek 16 px för nya texter, fungerande sans-serif-reserv för Inter, större innehållsfält, synliga Ny/Hitta/Mer och ett kompakt förgrenat exempel. Startvyn ger första besökaren tydliga nästa steg. |

## Utförda kontroller

- 516 Python-tester godkända.
- 39 JavaScript-sviter godkända, inklusive beslut med saknade, omärkta, dubbla och ogiltiga vägar samt giltiga alternativ med fler än två grenar.
- 32 inbäddade JavaScript-block syntaxkontrollerade; Python kompilerar och git diff --check passerar.
- Funktionella DOM-tester kör den faktiska inbäddade editorn med jsdom 26.1.0. De verifierar de tre startvalen, skapande från textunderlag, bevarad originalprocess, separat exempel, Ja- och Nej-väg till sina avslut, Nej utan avvikelse, ändring av steg och ansvar, ångra, återställd äldre process, stopp vid ofullständigt beslut och exportens placering på mobil.
- Ingen processdata från den publicerade appen har ändrats i denna verifiering.

## Begränsning

Visuell webbläsar-QA och verklig träfftestning på dator/mobil återstår. Cloud Browser avvisade lokal förhandsvisning på grund av URL-policyn. DOM-testernas geometri är simulerad och verifierar därför inte verklig layout, touch eller exportfiler. Inga exportmotorer har ändrats; exportmenyn har flyttats och sans-serif-reserven förbättrats.

Befintliga sparade processer skrivs inte över med det nya exemplet. Ett äldre ofullständigt beslut behöver däremot kompletteras innan det går att passera i Följ, vilket är det avsedda nya beteendet.

## Reproducera funktionstest

```bash
npm install --prefix /tmp/maplini-test-dom jsdom@26.1.0 --no-audit --no-fund
python3 -c "import sys;sys.path.insert(0,'tests');from browser_interaction_smoke import extract_editor_html;print(extract_editor_html())" > /tmp/maplini-editor.html
NODE_PATH=/tmp/maplini-test-dom/node_modules node tests/feedback_dom_smoke.cjs /tmp/maplini-editor.html
```

jsdom är endast en testberoende i den tillfälliga miljön och ingår inte i appens beroenden.
