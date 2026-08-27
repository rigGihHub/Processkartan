# Maplini v0.7.0 — Cloud & Sharing

## Nytt
- Skapa konto och logga in med e-post/lösenord.
- Molnlagring via Supabase.
- Samma konto kan öppna sina processer på andra datorer.
- `Spara` sparar lokalt och, när du är inloggad, även i molnet.
- `Spara i molnet` finns som separat knapp.
- `Dela` skapar en unik read-only-länk.
- Lokal lagring fungerar fortsatt utan Supabase.

## Engångsinställning
1. Skapa ett projekt på Supabase.
2. Öppna SQL Editor och kör `supabase_schema.sql`.
3. Aktivera Email under Authentication → Providers.
4. Lägg följande i Streamlit → Settings → Secrets:

```toml
[supabase]
url = "https://DIN-PROJEKT-ID.supabase.co"
anon_key = "DIN_ANON_KEY"

[app]
public_url = "https://processkartan.streamlit.app"
```

Supabase URL och anon key finns under projektets API-inställningar.

## Test
- Skapa konto i Maplini.
- Spara en process i molnet.
- Logga in med samma konto i en annan webbläsare/dator.
- Klicka `Dela` och öppna länken i privat fönster.

Nästa steg efter detta är team/workspaces, editor/viewer-roller och versionshistorik.
