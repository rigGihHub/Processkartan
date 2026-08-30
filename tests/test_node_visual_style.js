const assert=require('assert');
const fs=require('fs');
const vm=require('vm');
const code=fs.readFileSync('maplini_state_core.js','utf8');
const sandbox={globalThis:{}};vm.createContext(sandbox);vm.runInContext(code,sandbox);
const core=sandbox.globalThis.MapliniStateCore;
const p=core.normalizeProcess({id:'p',nodes:[
  {id:'a',type:'process',nodeStyle:'3d'},
  {id:'b',type:'document',nodeStyle:'glass'},
  {id:'c',type:'process',nodeStyle:'invalid'}
],links:[]},'p');
assert.equal(p.nodes[0].nodeStyle,'3d');
assert.equal(p.nodes[1].nodeStyle,'glass');
assert.equal(p.nodes[2].nodeStyle,'standard');
console.log('node visual styles OK');
