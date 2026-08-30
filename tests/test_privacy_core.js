const fs=require('fs'),vm=require('vm');
vm.runInThisContext(fs.readFileSync('maplini_privacy_core.js','utf8'));
const P=globalThis.MapliniPrivacyCore;
function ok(v,m){if(!v)throw new Error(m)}
ok(P.shouldPersistLocally({sharedView:false}),'normal local');
ok(!P.shouldPersistLocally({sharedView:true}),'shared ephemeral');
ok(P.persistenceMode({sharedView:true})==='ephemeral','mode');
console.log('privacy core OK');
