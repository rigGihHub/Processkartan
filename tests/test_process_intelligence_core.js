const assert=require('assert');
require('../maplini_process_intelligence_core.js');
const P=global.MapliniProcessIntelligenceCore;
let r=P.analyze([
 {id:'s',type:'start',text:'Start'},
 {id:'d',type:'decision',text:'Godkänd?'},
 {id:'a',type:'process',text:'A'}
],[['s','d'],['d','a']]);
assert(r.findings.some(f=>f.code==='missing_end'));
assert(r.findings.some(f=>f.code==='decision_branches'));
assert(r.findings.some(f=>f.code==='dead_end'&&f.nodeIds.includes('a')));
assert(r.score<10);

r=P.analyze([
 {id:'s',type:'start',text:'Start'},
 {id:'d',type:'decision',text:'Val?'},
 {id:'a',type:'process',text:'Ja'},
 {id:'b',type:'process',text:'Nej'},
 {id:'e',type:'end',text:'Slut'}
],[['s','d'],['d','a'],['d','b'],['a','e'],['b','e']]);
assert(!r.findings.some(f=>['missing_start','missing_end','decision_branches','dead_end','isolated'].includes(f.code)));
assert(r.score>=9);

r=P.analyze([
 {id:'s',type:'start',text:'Start'}, {id:'a',type:'process',text:'A'},
 {id:'b',type:'process',text:'B'}, {id:'e',type:'end',text:'Slut'}
],[['s','a'],['a','b'],['b','a'],['b','e']]);
assert(r.findings.some(f=>f.code==='loop'&&f.nodeIds.includes('a')&&f.nodeIds.includes('b')));

r=P.analyze([{id:'n',type:'note',text:'Notering'}],[]);
assert(!r.findings.some(f=>f.code==='isolated'),'notes are annotations, not structural errors');
console.log('process intelligence core ok');

// v0.18.2 actionable guidance contract
r=P.analyze([
 {id:'s',type:'start',text:'Start'},
 {id:'a',type:'process',text:'A'}
],[['s','a']]);
const dead=r.findings.find(f=>f.code==='dead_end');
assert(dead && typeof dead.action==='string' && dead.action.length>10);
assert(dead.priority==='Åtgärda först');
const missEnd=r.findings.find(f=>f.code==='missing_end');
assert(missEnd && missEnd.action.includes('Slut'));
console.log('actionable guidance contract ok');

{
  const nodes=[
    {id:'a',type:'start',text:'Start'},
    {id:'b',type:'process',text:'Granska'},
    {id:'c',type:'process',text:'Skicka'},
    {id:'d',type:'end',text:'Slut'}
  ];
  const links=[['a','b','right',{}],['b','c','right',{}],['c','d','right',{}]];
  const r=MapliniProcessIntelligenceCore.analyze(nodes,links,{longChainThreshold:5});
  const f=r.findings.find(x=>x.code==='direct_activity');
  if(!f)throw new Error('direct activity dependency finding missing');
  if(f.severity!=='warning')throw new Error('direct activity should be warning');
  if(f.meta.linkIndex!==1)throw new Error('direct activity should expose link index');
}
