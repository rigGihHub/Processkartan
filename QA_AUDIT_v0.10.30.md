# Maplini v0.10.30 — Read-only & Role Enforcement Hardening

## Verifierad brist
Viewer/shared-view var visuellt begränsade men flera canvasmutationer saknade faktisk klientguard.
Det gick därför att lokalt ändra en read-only process via drag, resize, connectors, inline edit,
keyboard delete/undo/redo och vissa format/processyta-flöden.

## Fix
- Ny `maplini_access_core.js`.
- Shared-view är alltid read-only.
- Endast owner/editor får mutera.
- Hårda guards på add/delete/style/inline-edit/cloud-save.
- Drag, resize, connector creation och connector-handle drag blockeras i read-only.
- Undo/redo/delete via keyboard blockeras.
- Processnamn, save/new/undo/redo/delete och processyta-kontroller disabled.
- Resize/connector handles döljs i read-only.
- Share respekterar edit-behörighet.

Export/visning påverkas inte. Ingen Supabase/RLS-migrering görs.
