# Maplini v0.10.20 — Export & Destructive Actions Audit

## Fokus
- PDF/DOCX/XLSX export integrity
- Save-before-export
- Safe filenames
- Destructive process deletion
- Pre-delete recovery snapshot
- Local/cloud delete consistency and error reporting

## Förbättringar
PDF validates `%PDF` signature before download. DOCX/XLSX validate ZIP signatures before download.
All three local exports flush current process state before building files.
Process deletion creates a pre-delete session snapshot and immediately persists local state.
Cloud deletion reports failure distinctly instead of silently swallowing the error.

## Oförändrat
No Supabase migration, OAuth setup, secrets, dependencies, or deployment changes.

## Känd begränsning
Real Google Drive creation, browser file-open validation, physical mobile interaction, and deployed behavior are not claimed verified here.
