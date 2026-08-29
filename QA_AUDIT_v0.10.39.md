# QA AUDIT v0.10.39

Scope: global font + text-size control.

- Applies chosen font family and text size to all canvas nodes in one action.
- Inputs/Outputs use the same font family and a proportional readable size.
- Document-link text inherits node typography.
- Existing single-node font/size editing remains unchanged.
- Global action is undoable as one operation and persists through process state.
- No database, OAuth, secret, or dependency changes.
