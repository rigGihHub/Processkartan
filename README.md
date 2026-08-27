# Maplini v0.7.1 — Supabase Auth Fix

## Vad som är ändrat
- Stöd för Supabases nya `sb_publishable_...`-nyckel.
- Maplini accepterar både `publishable_key` och det äldre konfigurationsnamnet `anon_key`.
- Inloggning verifierar access token mot `/auth/v1/user`.
- Ny knapp `Testa Supabase-anslutning`.
- Riktiga felmeddelanden från Supabase visas under konto-rutan.
- Vanliga fel översätts till begriplig svenska, t.ex.:
  - Kontot finns redan
  - Fel lösenord
  - E-post inte bekräftad
  - Registrering avstängd
  - Fel publishable key
  - Supabase går inte att nå

## Rekommenderade Streamlit Secrets
```toml
[supabase]
url = "https://DIN-PROJEKT-ID.supabase.co"
publishable_key = "sb_publishable_DIN_NYCKEL"

[app]
public_url = "https://processkartan.streamlit.app"
```

Det gamla namnet `anon_key` fungerar fortfarande, men `publishable_key` är tydligare.

## Testordning
1. Push v0.7.1.
2. Klicka `Testa Supabase-anslutning`.
3. Logga in med användaren du redan skapade manuellt i Supabase.
4. Om något misslyckas visas nu det faktiska Supabase-felet direkt i Maplini.
5. När inloggningen fungerar: `Spara i molnet`.
