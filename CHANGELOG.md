# Maplini Changelog

## 0.10.40 - Menu auto-close & node visual styles
- Öppna dropdown-menyer stängs när användaren klickar utanför dem, och en ny dropdown stänger den tidigare.
- Delningspanelen stängs också vid klick utanför.
- Ny inställning **Rutstil** för markerade rutor: Standard, 3D, Upphöjd skugga, Glas och Minimal/platt.
- Ny knapp för att applicera vald rutstil på alla rutor i processen.
- Rutstil sparas per nod, stöds av Undo och återskapas efter reload.
- PDF/DOCX-snapshot återger de nya visuella stilarna med motsvarande skuggbehandling.

## 0.10.39 - Global text typography
- Global formatting action now applies both selected font family and text size to all process nodes at once.
- Inputs/Outputs and document-link text inherit the node typography consistently.
- Global typography change is one Undo operation and persists with the process.

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

# v0.10.38 — DOCUMENT LINK ADD FIX

- Fixar **+ Lägg till dokumentlänk** direkt i en Dokument-ruta.
- Klick markerar dokumentrutan, visar Dokument-panelen och fokuserar fältet **Dokumentlänk**.
- Dokumentfältet scrollas fram vid behov så att länken kan klistras in direkt.
- Befintliga giltiga dokumentlänkar fortsätter öppnas i ny flik.
- Ingen databas-, dependency- eller konfigurationsändring.
