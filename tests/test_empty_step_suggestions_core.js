const assert=require('assert');require('../maplini_empty_step_suggestions_core.js');const C=global.MapliniEmptyStepSuggestionsCore;
assert.equal(C.isPlaceholder('Ny aktivitet','process'),true);assert.equal(C.isPlaceholder('Registrera order','process'),false);
let r=C.suggest({type:'process',title:'Ny aktivitet',inputs:['Order'],incoming:[],outgoing:[]});assert.equal(r.eligible,true);assert.equal(r.suggestions[0].text,'Hantera Order');
r=C.suggest({type:'process',title:'Ny aktivitet',incoming:[{title:'Order',type:'object'}],outgoing:[{title:'Bekräftelse',type:'object'}]});assert(r.suggestions.some(x=>x.text==='Hantera Order'));assert(r.suggestions.some(x=>x.text==='Ta fram Bekräftelse'));
r=C.suggest({type:'process',title:'Registrera order',inputs:['Order']});assert.equal(r.eligible,false);assert.equal(r.suggestions.length,0);
console.log('empty step suggestions core ok');
