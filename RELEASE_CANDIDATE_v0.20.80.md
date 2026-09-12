# Maplini v0.20.80 – Release Candidate

## Scope
Stabilisering och full regressionskontroll av den samlade Maplini-editorn. Ingen ny datamodell eller backendfunktion.

## RC-fynd
1. **Mobil läsvy:** desktop-fit kunde köras efter mobil Förstå-fit och tvinga zoom till 25 %. Fixat genom att avbryta den schemalagda fitten om `readMode` hunnit aktiveras.
2. **Historiska browsertester:** flera äldre tester följde UI-kontrakt som senare avsiktligt ändrats (grupperad export, uppercase snabböverblick, canvas-plus, cleanup preview, fokusmarkering). Testerna är uppdaterade till nuvarande användarflöden.
3. **Performance harness:** äldre benchmark-harness saknade nyare core-moduler, inklusive navigation. Uppdaterat.

## QA
- `pytest`: 479/479 PASS
- Core JS syntax (`node --check`): 30/30 PASS
- JS testfiler: 38/38 PASS
- Chromium browser scripts: 35/35 passerade under RC-körningen
- Mobil fit/readability: PASS vid 360, 390 och 430 px
- Mobile Read/Follow: PASS
- Large-process performance harness: PASS upp till 1000 noder
- Export Fidelity PDF/DOCX: PASS
- Export Preview: PASS
- ZIP-integritet: verifieras vid paketering

## Release status
Push-kandidat. Deploy/live-verifiering återstår.
