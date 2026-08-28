# Maplini v0.9.0 — Connector Selection & Contact Points

## Pilar/kopplingar
Kopplingarna har nu ett separat HTML-baserat klicklager ovanpå SVG-linjerna.

Det innebär:
- varje linjesegment får en 24 px hög transparent klickyta
- klicket fångas av vanlig HTML, inte bara SVG
- böjda kopplingar får en klickyta per segment
- markerad koppling får fortsatt blå markering och formateringspanel

Den geometriska fallbacken finns också kvar.

## Kopplingspunkter
De gröna kopplingspunkterna är nu mycket mindre som standard: 8 px.

Under Formatering finns `Kopplingspunkter` med:
- Storlek: 6 / 8 / 10 / 12 / 14 px
- Färg
- `Dölj kopplingspunkter`

Inställningarna sparas per process.

Kopplingspunkterna visas bara på den markerade rutan.
