# QA audit – Maplini v0.20.84

## Scope

Focused rendering hotfix for the primary labels in the selected-step editor.

## Verification

- Full Python regression suite.
- All JavaScript regression files.
- JavaScript syntax checks.
- Browser verification on deployed Streamlit app: label position, field position and computed flex direction.

## Risk

Low. The change is limited to explicit label markup and scoped sidebar CSS. No process data, editor behavior, persistence or integrations are changed.
