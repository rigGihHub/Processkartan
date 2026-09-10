const assert=require('assert');
require('../maplini_step_understanding_core.js');
const C=globalThis.MapliniStepUnderstandingCore;
let s=C.summarize({type:'process',title:'Kontrollera order',description:'Kontrollera att ordern är komplett.',responsibleRole:'Kundservice',inputs:['Order'],outputs:['Godkänd order'],next:[{title:'Registrera order'}]});
assert.equal(s.values.what,'Kontrollera att ordern är komplett.');
assert.equal(s.values.who,'Kundservice');
assert.equal(s.values.input,'Order');
assert.equal(s.values.output,'Godkänd order');
assert.equal(s.values.next,'Registrera order');
assert.equal(s.complete,5);
s=C.summarize({type:'decision',title:'Är ordern komplett?',next:[{title:'Registrera',label:'Ja'},{title:'Begär komplettering',label:'Nej'}]});
assert.equal(s.values.next,'2 möjliga vägar · Ja: Registrera · Nej: Begär komplettering');
assert.equal(s.values.who,'Inte angivet ännu');
assert.equal(s.complete,2); // title + next
s=C.summarize({type:'end',title:'Klar',next:[]});
assert.equal(s.values.next,'Processen slutar här');
console.log('step understanding core ok');
