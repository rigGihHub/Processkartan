# Maplini v0.10.21 — Full Critical Flow E2E & Connector Persistence Fix

The cross-module E2E suite exposed a real bug: state normalization could drop canonical connector arrays during save/restore. v0.10.21 preserves `[sourceId,targetId,side,style]` links and migrates legacy object links into that canonical format.

E2E covered: create → edit → connect → save/restore → export validation → destructive delete → undo → orphan recovery → process fallback.

No physical mobile QA, live Google Drive write, Supabase mutation or deployed smoke test is claimed.
