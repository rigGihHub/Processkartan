# Maplini v0.8.3 — A4/A3 + flersidig PDF + enklare inloggning

## PDF
- Välj `A4` eller `A3`.
- Välj:
  - Auto sidor
  - 1 sida
  - 2 sidor
  - 3 sidor
  - 4 sidor
- `Visa PDF-yta` visar sidramarna direkt på canvasen.
- Vid flera sidor visas ramarna bredvid varandra.
- PDF-exporten skapar motsvarande antal PDF-sidor.
- Auto-läget räknar ut hur många sidor som behövs utifrån processens bredd.
- Varje sida skalas för god passning.

## Inloggning
- Maplini/Supabase är huvudkontot.
- Google är **inte** ett andra obligatoriskt konto.
- Google behöver bara anslutas om användaren vill skapa Google Docs/Sheets direkt i sitt Drive.
- Lokal PDF/DOCX/XLSX-export fungerar utan Google.

## Rekommenderad nästa nivå
På sikt kan Maplini använda Google som SSO via Supabase, så att samma Google-inloggning används både för Maplini och Google-export.
