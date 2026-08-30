const fs=require('fs'),vm=require('vm');
vm.runInThisContext(fs.readFileSync('maplini_access_core.js','utf8'));
const A=globalThis.MapliniAccessCore;
function ok(v,m){if(!v)throw new Error(m)}
ok(A.canEdit({sharedView:false,currentRole:'owner'}),'owner edits');
ok(A.canEdit({sharedView:false,currentRole:'editor'}),'editor edits');
ok(!A.canEdit({sharedView:false,currentRole:'viewer'}),'viewer readonly');
ok(!A.canEdit({sharedView:true,currentRole:'owner'}),'shared readonly');
ok(A.mode({currentRole:'viewer'})==='view','mode');
console.log('access core OK');
