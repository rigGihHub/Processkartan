# QA AUDIT – Maplini v0.11.3

Scope: Fit-to-screen + Align/Distribute.

Kontroller:
- Python syntax
- pytest
- samtliga JS-testsviter
- JS syntax för core-filer och embedded editor-script
- desktop DOM-kontrakt med `.p48-body`, `.p48-side`, `#p48-scroll`, `#p48-controls`, `#p48-canvas`
- ZIP-integritet

Fit-to-screen ändrar endast zoom/scroll, inte processdata. Align/Distribute är edit-only och använder en Undo-checkpoint per operation.
