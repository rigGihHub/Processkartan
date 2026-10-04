const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
require('../maplini_walkthrough_core.js');
const W=global.MapliniWalkthroughCore;
for(const edges of [[],[{label:'Ja'}],[{label:'Ja'},{label:''}],[{label:'Ja'},{label:'YES!'}],[{label:'Köp'},{label:' köp. '}]]){
 assert.equal(W.decisionStatus(edges).complete,false,'missing or ambiguous branches cannot be followed');
 assert.ok(W.decisionStatus(edges).message.length>20);
}
assert.equal(W.decisionStatus([{label:'Ja'},{label:'Nej'}]).complete,true);
assert.equal(W.decisionStatus([{label:'E-post'},{label:'Telefon'},{label:'Post'}]).complete,true,'named non-binary decisions stay usable');
const source=fs.readFileSync(require.resolve('../app.py'),'utf8');
const starter=vm.runInNewContext('('+source.match(/const starter=({[\s\S]*?});/)[1]+')');
const decision=starter.nodes.find(n=>n.type==='decision');
const edges=W.nextEdges(decision.id,starter.nodes,starter.links);
assert.equal(W.decisionStatus(edges).complete,true);
for(const answer of ['yes','no']){
 const route=W.automaticRoute([{id:'r',text:decision.text,kind:'route'}],{r:answer},edges);
 assert.equal(route.mode,'auto');
 let id=route.edge.to;const visited=new Set();
 while(true){assert.ok(!visited.has(id));visited.add(id);const node=starter.nodes.find(n=>n.id===id);assert.ok(node);
  const next=W.nextEdges(id,starter.nodes,starter.links);
  if(node.type==='end'){assert.equal(next.length,0);break}
  assert.equal(next.length,1);assert.ok(node.processInfo.description&&node.processInfo.responsibleRole);
  id=next[0].to;
 }
}
assert.ok(starter.nodes.every(n=>n.fontSize>=16),'sample text is readable by default');
const brokenNodes=[{id:'d',type:'decision'},{id:'e',type:'end'}];
assert.equal(W.decisionStatus(W.nextEdges('d',brokenNodes,[['d','e','right',{label:'Ja'}],['d','missing','right',{label:'Nej'}]])).complete,false,'dangling destinations do not count as branches');
console.log('Feedback flow tests passed.');
