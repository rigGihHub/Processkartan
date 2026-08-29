# v0.10.37 — BACKGROUND LIBRARY

Integrerad bakgrundsväljare i **Processyta ▾**.

## Mönstrade
- Prickar / Dot grid
- Rutor / Graf
- Linjer / Linjerat
- Befintliga korslinjer, diagonal och tekniskt rutnät finns kvar

## Enfärgade och tonade
- Solid färg
- Gradient med startfärg, slutfärg och riktning

## Grafiska
- Uppladdad bakgrundsbild med reglerbar opacitet
- Vattenstämpel som text, t.ex. UTKAST/KONFIDENTIELLT
- Alternativ att använda uppladdad processlogga som vattenstämpel
- Reglerbar vattenstämpelopacitet
- Texturer: gammalt papper, pergament, canvas och betong

## Persistens och export
- Alla nya bakgrundsinställningar sparas per process i befintlig JSON-state
- PDF/DOCX-kartbilden återger gradienter, bilder, vattenstämplar och texturer
- Bakgrundsbilder begränsas till 1,5 MB för att skydda lokal lagring och backup

Ingen Supabase-migrering, OAuth-, secret- eller dependency-ändring.
