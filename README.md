# Maplini v0.10.5

## Spara
Det finns nu bara en `Spara`-knapp.

- Utloggad: sparar lokalt.
- Inloggad: sparar lokalt och synkar till Supabase/molnet.
- Om molnsynken misslyckas ligger den lokala sparningen kvar.

## Pilmarkering
Pilmarkering använder inte längre den optimerade dirty-link-cachen för UI-state.
Varje gång en ny pil klickas renderas connector-lagret om direkt, så markering,
halo och formateringspanel ska följa den pil som faktiskt klickades.
