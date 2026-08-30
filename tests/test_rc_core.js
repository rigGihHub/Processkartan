const fs=require('fs'),vm=require('vm');
vm.runInThisContext(fs.readFileSync('maplini_rc_core.js','utf8'));
const R=globalThis.MapliniRcCore;
function ok(v,m){if(!v)throw new Error(m)}
const p={a:{id:'a'},b:{id:'b'}}, ids=new Set(['a']), scopes=new Map([['a','personal']]);
const snap=R.captureScopeState(p,'a',ids,scopes);
p.a.name='mutated';ids.add('b');scopes.set('b','x');
const restored=R.restoreScopeState(snap);
ok(restored.processes.a.name===undefined,'deep restore');
ok(restored.cloudLoadedIds.join(',')==='a','ids restored');
ok(restored.cloudLoadedScopes.length===1&&restored.cloudLoadedScopes[0][1]==='personal','scope restored');
ok(R.ensureCurrentId({b:{id:'b'}},'a',['b'])==='b','preferred fallback');
ok(R.ensureCurrentId({c:{id:'c'}},'a',[])==='c','first fallback');
ok(R.validateStoreInvariant({a:{id:'a'}},'a'),'valid invariant');
ok(!R.validateStoreInvariant({a:{id:'a'}},'missing'),'invalid invariant');
console.log('rc core OK');
