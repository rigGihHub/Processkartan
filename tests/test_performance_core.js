const fs=require('fs'),vm=require('vm');
let queue=[];
global.requestAnimationFrame=(cb)=>{queue.push(cb);return queue.length};
vm.runInThisContext(fs.readFileSync('maplini_performance_core.js','utf8'));
const P=globalThis.MapliniPerformanceCore;
function ok(v,m){if(!v)throw new Error(m);}
ok(P.signature(['a',1,true])===P.signature(['a',1,true]),'stable signature');
ok(P.signature(['a',1])!==P.signature(['a',2]),'signature changes');
let count=0;P.rafOnce('x',()=>count++);P.rafOnce('x',()=>count++);
ok(queue.length===1,'raf coalesced');queue.shift()();ok(count===1,'raf ran once');
ok(P.shouldRun('a','b')&&!P.shouldRun('a','a'),'shouldRun');
console.log('performance core OK');
