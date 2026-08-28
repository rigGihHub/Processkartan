# Maplini v0.8.8

## Fixar
1. Kopplingar/pilar är nu betydligt enklare att markera.
   - Osynlig klickyta är 20 px bred.
   - Klickytan ligger över den synliga linjen.
   - Pointer events stoppas så canvasen inte tar klicket.

2. Gröna kopplingspunkter
   - Dolda som standard.
   - Visas endast på markerad ruta.

3. Kant- och linjeformatering
   - Ett enda ställe används för färg och tjocklek:
     `Kantfärg` + `Kanttjocklek`.
   - Markerad ruta: ändrar rutans kant.
   - Markerad koppling: ändrar linjens färg och tjocklek.
   - Kopplingspanelen innehåller bara kopplingsspecifika val:
     slutmarkör och linjetyp.

4. Globalt typsnitt
   - Ny knapp `Använd typsnitt på all text`.
   - Välj typsnitt och klicka knappen för att uppdatera alla rutor i processen.
