const fs=require('fs'),vm=require('vm');vm.runInThisContext(fs.readFileSync('maplini_mobile_core.js','utf8'));const M=globalThis.MapliniMobileCore;
function ok(v,m){if(!v)throw new Error(m)}
let p=M.clientToLocal(125,80,{left:-375,top:20});ok(p.x===500&&p.y===60,'scrolled coordinate');ok(M.dragThreshold('touch')>M.dragThreshold('mouse'),'threshold');
ok(!M.movedEnough(3,3,'touch'),'jitter');ok(M.movedEnough(8,5,'touch'),'touch drag');ok(M.movedEnough(2,0,'mouse'),'mouse precision');ok(M.isCoarse('touch')&&M.isCoarse('pen')&&!M.isCoarse('mouse'),'coarse');console.log('mobile core OK');
