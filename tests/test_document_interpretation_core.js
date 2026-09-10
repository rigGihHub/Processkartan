const fs=require('fs'),vm=require('vm');
const src=fs.readFileSync('maplini_document_interpretation_core.js','utf8');vm.runInThisContext(src);
const c=globalThis.MapliniDocumentInterpretationCore;
function ok(v,m){if(!v)throw new Error(m)}
let items=c.interpret('Kundservice tar emot en beställning. Kundservice kontrollerar kunduppgifterna i systemet CRM. Är uppgifterna kompletta? Ekonomi godkänner ordern. Kundservice skickar en orderbekräftelse.');
ok(items.length>=4,'steps');ok(items.some(x=>x.type==='decision'),'decision');ok(items.some(x=>x.responsibleRole),'role');ok(items.some(x=>x.system),'system');ok(items.some(x=>x.inputs.length),'input');ok(items.some(x=>x.outputs.length),'output');
const s=c.summary(items);ok(s.steps===items.length,'summary steps');ok(s.decisions>=1,'summary decisions');
console.log('document interpretation core PASS',s);
