const fs=require('fs'),vm=require('vm'),assert=require('assert');
vm.runInThisContext(fs.readFileSync('maplini_performance_core.js','utf8'));
assert.equal(MapliniPerformanceCore.policy(20,20).mode,'normal');
assert.equal(MapliniPerformanceCore.policy(80,10).mode,'large');
assert.equal(MapliniPerformanceCore.policy(50,150).mode,'large');
assert.equal(MapliniPerformanceCore.policy(60,100).mode,'normal');
console.log('performance core PASS');
