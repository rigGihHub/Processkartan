const fs=require('fs'),vm=require('vm');
vm.runInThisContext(fs.readFileSync('maplini_flow_core.js','utf8'));
const F=globalThis.MapliniFlowCore;
function ok(v,m){if(!v)throw new Error(m)}
let p=F.sharedProcess({id:'p',name:'N',data:{id:'old',name:'Old',nodes:[],links:[]}});
ok(p.id==='p'&&p.name==='N','shared row canonical');
ok(F.sharedProcess({id:'p',data:null})===null,'invalid shared');
let d=F.afterProcessDelete({a:{id:'a'},b:{id:'b'}},'a','a');
ok(!d.processes.a&&d.currentId==='b','delete current fallback');
d=F.afterProcessDelete({a:{id:'a'},b:{id:'b'}},'a','b');
ok(d.processes.a&&d.currentId==='a','delete other keeps current');
console.log('flow core OK');
