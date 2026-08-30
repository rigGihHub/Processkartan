const fs=require('fs'),vm=require('vm');
vm.runInThisContext(fs.readFileSync('maplini_export_core.js','utf8'));
const e=globalThis.MapliniExportCore;
function ok(v,m){if(!v)throw new Error(m);}
ok(e.validateBytes(Uint8Array.from([0x25,0x50,0x44,0x46,1]),'pdf').ok,'pdf');
ok(!e.validateBytes(Uint8Array.from([1,2,3,4,5]),'pdf').ok,'bad pdf');
ok(e.validateBytes(Uint8Array.from([0x50,0x4b,0x03,0x04,1]),'zip').ok,'zip');
ok(!e.validateBytes(Uint8Array.from([0,0,0,0,1]),'zip').ok,'bad zip');
ok(e.safeFileName('a/b:c?.pdf')==='a_b_c_.pdf','safe filename');
ok(e.safeFileName('').length>0,'fallback filename');
const p=e.deletionPlan({currentId:'a',processes:{a:{},b:{},c:{}}},'a');
ok(p.deletingCurrent&&p.remainingIds.length===2&&p.nextId==='b','delete plan');
console.log('export core OK');
