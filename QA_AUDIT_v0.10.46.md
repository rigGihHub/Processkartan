# QA Audit – Maplini v0.10.46

Fokus: val av nodtyp vid **＋ Infoga steg** på markerad koppling.

Kontroller:
- Fyra tillåtna typer: Aktivitet, Beslut, Dokument, Slut.
- Samma split-link-flöde används som i v0.10.45.
- En Undo-operation per infogning.
- Menyn stängs vid val/klick utanför/read-only.
- Python- och JavaScript-syntax verifieras.
- Desktop DOM-kontrakt och regressionstester körs.
- Ingen schema-, OAuth-, secret- eller dependency-ändring.

Resultat:
- pytest: **154/154 passed**
- Node.js: **20/20 testsviter passed**
- `py_compile`: passed
- inbäddad huvud-JavaScript `node --check`: passed
- BeautifulSoup desktop DOM-kontrakt: passed
