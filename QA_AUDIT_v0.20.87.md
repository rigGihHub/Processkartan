# QA audit – Maplini v0.20.87

## Scope

Direct, discoverable node sizing for one or several selected nodes.

## Verification targets

- Compact, normal and large presets update width and height.
- Free corner resizing remains available.
- Multiple selected nodes can receive one size category in one undoable operation.
- Decisions remain square.
- Persisted width and height restore through the existing state model.
- Connectors are rerendered after the geometry change.
