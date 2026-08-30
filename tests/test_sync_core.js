const fs=require('fs'),vm=require('vm');vm.runInThisContext(fs.readFileSync('maplini_sync_core.js','utf8'));const S=globalThis.MapliniSyncCore;
function ok(v,m){if(!v)throw new Error(m)}
ok(!S.contentChanged({id:'p',name:'A',localModifiedAt:1},{id:'p',name:'A',localModifiedAt:99,cloudUpdatedAt:'x'}),'meta ignored');
ok(S.contentChanged({id:'p',name:'A'},{id:'p',name:'B'}),'content changes');
const row={id:'p',name:'Cloud',updated_at:'2026-08-29T06:00:00Z',data:{id:'p',name:'Cloud'}};
ok(S.chooseSource({id:'p',localModifiedAt:Date.parse('2026-08-29T06:01:00Z')},row)==='local','local newer');
ok(S.chooseSource({id:'p',localModifiedAt:Date.parse('2026-08-29T05:00:00Z')},row)==='cloud','cloud newer');
let m=S.mergeCloudRows({p:{id:'p',name:'Local',localModifiedAt:Date.parse('2026-08-29T06:01:00Z')}},[row]);ok(m.processes.p.name==='Local'&&m.preservedLocalIds[0]==='p','preserve local');
m=S.mergeCloudRows({p:{id:'p',name:'Old',localModifiedAt:Date.parse('2026-08-29T05:00:00Z')}},[row]);ok(m.processes.p.name==='Cloud'&&m.cloudLoadedIds[0]==='p','load cloud');
let plan=S.signOutPlan({a:{id:'a',cloudUpdatedAt:'2026-08-29T06:00:00Z',localModifiedAt:Date.parse('2026-08-29T05:00:00Z')},b:{id:'b',cloudUpdatedAt:'2026-08-29T06:00:00Z',localModifiedAt:Date.parse('2026-08-29T07:00:00Z')},c:{id:'c'}},['a','b'],'a');
ok(!plan.processes.a&&plan.processes.b&&plan.processes.c,'purge cloud copy');ok(plan.currentId==='b'&&plan.preservedModifiedIds[0]==='b','preserve changed');
console.log('sync core OK');
