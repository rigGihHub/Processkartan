const fs=require('fs'),vm=require('vm');
const code=fs.readFileSync('maplini_document_interpretation_core.js','utf8');
const ctx={globalThis:{}};vm.createContext(ctx);vm.runInContext(code,ctx);const C=ctx.globalThis.MapliniDocumentInterpretationCore;
const docs=[
 {name:'rutin.txt',text:'Kundservice kontrollerar ordern. Skapa order. Skicka orderbekräftelse.'},
 {name:'instruktion.txt',text:'Ekonomi kontrollerar ordern. Skicka orderbekräftelse. Skapa order.'}
];
const p=C.interpretDocuments(docs,100);
if(!p.conflicts.length)throw new Error('expected conflicts');
const role=p.conflicts.find(x=>x.type==='responsibility');
if(!role||!role.id||role.options.length<2)throw new Error('responsibility choices missing');
const order=p.conflicts.find(x=>x.type==='order');
if(!order||!order.id||!Array.isArray(order.directions)||order.directions.length!==2)throw new Error('order directions missing');
if(!order.pairKey)throw new Error('pair key missing');
console.log('document conflict resolution core PASS',p.summary);
