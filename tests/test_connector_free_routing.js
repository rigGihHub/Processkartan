
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const code=fs.readFileSync('maplini_connector_core.js','utf8');
const ctx={globalThis:{}};vm.createContext(ctx);vm.runInContext(code,ctx);
const C=ctx.globalThis.MapliniConnectorCore;
const links=[['a','b','right',{routing:'straight'}]];
C.setFreeOffset(links,0,30,40);
const st=C.style(links[0]);
assert.equal(st.routing,'free');
assert.equal(st.freeDx,30);
assert.equal(st.freeDy,40);
const p=C.routePoints(0,0,100,0,'right','left',st);
assert.deepEqual(JSON.parse(JSON.stringify(p)),[[0,0],[55,40],[105,40],[100,0]]);
const moved=C.routePoints(20,10,120,10,'right','left',st);
assert.deepEqual(JSON.parse(JSON.stringify(moved)),[[20,10],[75,50],[125,50],[120,10]]);
console.log('connector free routing ok');
