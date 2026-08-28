# Maplini v0.9.1 — Critical interaction fix

Grundfelet var att flera visuella regler låg utanför editor-iframe:n.

## Pilar/kopplingar
- Kritisk CSS ligger nu inne i editor-iframe:n.
- Dokumentnivå-capture används för klick.
- Närmaste koppling inom 22 px markeras.
- HTML-klickkorridor är 28 px.
- Markerad koppling får blå halo.

## Kopplingspunkter
- Storlek appliceras explicit på alla punkter samtidigt.
- Färg appliceras explicit på alla punkter samtidigt.
- Dölj kopplingspunkter döljer alla direkt.
- Nya rutor ärver aktuell punktinställning.
