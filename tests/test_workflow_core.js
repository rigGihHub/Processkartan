const fs=require('fs'),vm=require('vm');for(const f of ['maplini_connector_core.js','maplini_state_core.js','maplini_workflow_core.js'])vm.runInThisContext(fs.readFileSync(f,'utf8'));const W=globalThis.MapliniWorkflowCore;
function ok(v,m){if(!v)throw new Error(m)}
let p=W.emptyProcess('p','P');p=W.addNode(p,{id:'a',type:'start'});p=W.addNode(p,{id:'b',type:'end'});p=W.connect(p,'a','b','right');ok(W.validateCriticalFlow(p).ok&&p.links.length===1,'valid');
let h=W.pushHistory([],p);h=W.pushHistory(h,p);ok(h.length===1,'dedupe');p=W.deleteNodes(p,['a']);ok(p.nodes.length===1&&p.links.length===0,'cascade');console.log('workflow core OK');
