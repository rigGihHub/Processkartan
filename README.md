# Maplini v0.10.0 — Definitive canvas top alignment

Grundorsaken hittades: tidigare layoutfixar riktade `.p48-main` / `.p48-app`,
men den faktiska editorn använder `.p48-body`.

## Ny layout
- `.p48-body` är den fasta editorcontainern.
- vänsterpanelen ligger absolut på `top: 0`, `left: 0`
- canvasområdet ligger absolut på `top: 0`, `left: 220px`
- båda börjar därför exakt på samma höjd direkt under toolbaren
- vänsterpanelen har egen vertikal scroll
- canvasområdet har egen vertikal/horisontell scroll
- canvasen kan inte längre skjutas ned av sidebarens innehåll

När en process öppnas återställs även arbetsytans scrollposition till top-left.
