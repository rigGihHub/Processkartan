const fs=require('fs'),vm=require('vm');vm.runInThisContext(fs.readFileSync('maplini_autosave_core.js','utf8'));const A=globalThis.MapliniAutosaveCore;
function ok(v,m){if(!v)throw new Error(m)}
const store={schemaVersion:1,currentId:'p1',processes:{p1:{id:'p1',nodes:[],links:[]}}};
const snap=A.makeRecoverySnapshot(store,1234);ok(snap.kind==='maplini-recovery'&&snap.capturedAt===1234,'snapshot');
const parsed=A.parseRecovery(JSON.stringify(snap));ok(parsed&&parsed.store.currentId==='p1','parse');
ok(!A.shouldOfferRecovery(parsed,store),'same store not offered');
const changed={schemaVersion:1,currentId:'p1',processes:{p1:{id:'p1',nodes:[{id:'n1'}],links:[]}}};
ok(A.shouldOfferRecovery(A.makeRecoverySnapshot(changed,2000),store),'changed store offered');
ok(A.saveLabel('saving')==='Sparar…','saving label');ok(A.saveLabel('saved','22:26')==='Autosparad · 22:26','saved label');
console.log('autosave core OK');
