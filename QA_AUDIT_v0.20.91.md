# QA audit – Maplini v0.20.91

## Fokus

Visible Formatting gör de viktigaste rutinställningarna omedelbart åtkomliga när ett steg markeras utan att öppna den avancerade Utseende-gruppen.

## Verifierat

- Bakgrund, textfärg, fet, kursiv, understruken och textstorlek visas före stegets redigeringsformulär.
- Snabbkontrollerna använder samma stilmodell, Undo och sparflöde som de befintliga kontrollerna.
- Kontrollerna synkroniseras vid byte av markering och fungerar för en eller flera markerade rutor.
- B/I/U visar aktivt läge och exponerar `aria-pressed` för hjälpmedel.
- Mer avancerad formatering finns kvar under Utseende.

## Automatiska kontroller

- `pytest`: 510 godkända
- JavaScript: 38 testfiler godkända
- Core JavaScript: 30 filer syntaxkontrollerade
- Python-kompilering och `git diff --check`: godkända
