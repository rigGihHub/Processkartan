const fs=require('fs'),vm=require('vm');
vm.runInThisContext(fs.readFileSync('maplini_any_source_core.js','utf8'));
const C=globalThis.MapliniAnySourceCore;
function ok(v,m){if(!v)throw new Error(m)}
let c=C.classifySource('Kundservice ska ta emot ordern. Ekonomi godkänner ordern. Lagret levererar varan.');ok(c.type==='work_process','work process');
c=C.classifySource('Kommunen beslutade att inleda upphandling. Anbud lämnas. Tilldelning beslutas och kan överprövas.');ok(c.type==='case_flow','case flow');
c=C.classifySource('Bolaget lanserade tjänsten på måndagen. Aktien steg senare. Företaget meddelade därefter en investering.');ok(c.type==='event_timeline','event timeline');
const p=C.eventItems('Bolaget lanserade tjänsten. Aktien steg senare. Företaget meddelade en investering.');ok(p.items.length===3&&p.edges.length===2,'event plan');
ok(C.normalizeUrl('example.com').startsWith('https://example.com'),'url normalize');
ok(C.readerUrl('https://example.com/x')==='https://r.jina.ai/https://example.com/x','reader url');
console.log('test_any_source_core: PASS');
let r=C.explicitRelation('Kostnaderna ökade kraftigt.','Därför beslutade bolaget att stänga fabriken.');ok(r&&r.kind==='cause_effect','cause relation');
r=C.explicitRelation('Efterfrågan föll.','Bolaget lanserade en ny tjänst.');ok(r&&r.kind==='actor_action','actor action relation');
r=C.explicitRelation('A hände.','B hände senare.');ok(!r,'no invented relation');
const rp=C.eventItems('Bolaget meddelade en prishöjning. Därför föll efterfrågan. Företaget lanserade därefter en billigare tjänst.');ok(rp.summary.relations>=1,'relation count');ok(rp.edges.some(e=>e.relationLabel),'relation edge label');
