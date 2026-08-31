# QA Audit v0.16.0
## Scope
Introduce Object → Activity → Object as Maplini's core process-mapping method.

## Verified
- `object` is a first-class normalized node type.
- Main palette presents Objekt in → Aktivitet → Objekt ut.
- Both Objekt in/out create the same underlying object type.
- Object nodes have a distinct compact visual treatment.
- Empty-process onboarding starts from an object/trigger.
- Contextual + Nästa offers Activity after Object and Object/result after Activity.
- Existing node types remain supported.
- A4 portrait default from v0.15.11 remains.

## Gates
- py_compile: passed.
- pytest: 198/198 passed.
- JavaScript suites: 25/25 passed.
- v0.16.0 focused Chromium smoke: passed (Object creation + contextual next Activity).
- Full legacy Chromium smoke reaches its known v0.14.9 nested-menu assertion and currently fails there; this is unrelated to the v0.16.0 method changes and is not represented as a full browser pass.
- Core JS syntax: passed.
- Embedded JS syntax: passed.
- Critical DOM: passed.
- Duplicate IDs: none.
- ZIP integrity: passed.

## Deployment
Not pushed or deployed.
