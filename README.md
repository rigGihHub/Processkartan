# Maplini v0.8.9

## Fler typsnitt
Maplini har nu ett större fontbibliotek, bland annat:
Inter, Poppins, Montserrat, DM Sans, Manrope, Space Grotesk, Roboto,
Open Sans, Lato, Nunito, Raleway, Rubik, Quicksand, Fira Sans, Ubuntu,
Oswald, Bebas Neue, Playfair Display, Merriweather, Pacifico och Caveat.

`Använd typsnitt på all text` finns kvar.

## Kopplingar – ny markeringsmotor
Kopplingar markeras inte längre enbart genom SVG-klick.

Maplini gör nu även en geometrisk träfftestning:
- klicka inom ca 14 px från en linje
- närmaste koppling markeras
- markerad koppling får en tydlig blå halo
- detta fungerar även om SVG-lagret i webbläsaren missar klicket

## Linjetyp och slutmarkör
Ändringar renderas om direkt:
- Heldragen
- Streckad
- Prickad

Slutmarkör:
- Pil
- Ingen
- Cirkel
- Diamant

Maplini visar också en bekräftelse när linjetyp/slutmarkör ändrats.
