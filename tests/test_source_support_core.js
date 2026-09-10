const assert=require('assert');require('../maplini_source_support_core.js');
const c=global.MapliniSourceSupportCore;
let s=c.summarize({sources:[{name:'A'},{name:'B'},{name:'C'}],disagreements:[]});
assert.equal(s.headline,'3 källor stödjer samma steg');assert.equal(s.hasDisagreement,false);
s=c.summarize({sources:[{name:'A'},{name:'B'}],disagreements:[{type:'responsibility',message:'Olika ansvar: Kundservice / Ekonomi',sources:['A','B'],resolution:'Ekonomi'}]});
assert.equal(s.hasDisagreement,true);assert.equal(s.disagreements[0].label,'Olika ansvar');assert.equal(s.disagreements[0].resolution,'Ekonomi');
console.log('source support core ok');
