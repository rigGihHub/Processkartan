const fs=require('fs'),vm=require('vm');
vm.runInThisContext(fs.readFileSync('maplini_session_core.js','utf8'));
const S=globalThis.MapliniSessionCore;
function ok(v,m){if(!v)throw new Error(m)}
ok(S.workspacePrefKey('u1')==='maplini_workspace_u1','pref key');
ok(S.scopeKey(null)==='personal'&&S.scopeKey('w1')==='workspace:w1','scope');
let c=S.chooseWorkspace('w2',[{workspace_id:'w1',role:'editor'},{workspace_id:'w2',role:'viewer'}]);
ok(c.id==='w2'&&c.role==='viewer','preferred valid');
c=S.chooseWorkspace('missing',[{workspace_id:'w1',role:'editor'}]);
ok(c.id===null&&c.role==='owner','invalid preference falls to personal');
ok(S.sessionState({access_token:'x',user:{id:'u'}}).valid,'valid session');
ok(!S.sessionState({access_token:'x'}).valid,'invalid session');
const m=new Map([['a','personal'],['b','workspace:w1'],['c','personal']]);
ok(S.scopedIds(m,'personal').sort().join(',')==='a,c','scoped ids');
console.log('session core OK');
