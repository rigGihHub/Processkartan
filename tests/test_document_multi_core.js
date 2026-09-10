const fs=require('fs'),vm=require('vm');
vm.runInThisContext(fs.readFileSync('maplini_document_interpretation_core.js','utf8'));
const c=globalThis.MapliniDocumentInterpretationCore;
function ok(v,m){if(!v)throw new Error(m)}
const docs=[
 {name:'Rutin.txt',text:'Kundservice kontrollerar ordern. Kundservice registrerar ordern. Ekonomi skickar fakturan.'},
 {name:'Instruktion.txt',text:'Ekonomi kontrollerar ordern. Ekonomi skickar fakturan. Kundservice registrerar ordern.'}
];
const r=c.interpretDocuments(docs,100);
ok(r.summary.documents===2,'documents');
ok(r.items.length>=3,'merged steps');
ok(r.items.some(x=>(x.sourceNames||[]).length===2),'sources merged');
ok(r.summary.conflicts>=1,'conflict detected');
ok(r.items.some(x=>(x.conflictMessages||[]).some(m=>m.includes('Olika ansvar'))),'responsibility conflict');
ok(r.items.some(x=>(x.conflictMessages||[]).some(m=>m.includes('Olika ordning'))),'order conflict');
ok(r.edges.some(e=>e.conflict),'conflicting edge marked');
console.log('multi document core PASS',r.summary);
