# QA audit – Maplini v0.20.86

## Scope

Restore user-controlled activity sizing after the v0.20.85 readability change.

## Expected result

- Selected activities can be resized down to 120 px with the corner handles.
- Normal word wrapping remains active.
- Small-map scrollbar cleanup remains active.
- No process data migration is required.

## Verification

- Full Python regression suite.
- All JavaScript test files and core syntax checks.
- Live CSS verification after deployment.
