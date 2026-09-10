const fs=require('fs'),vm=require('vm');vm.runInThisContext(fs.readFileSync('maplini_source_change_core.js','utf8'));
const c=globalThis.MapliniSourceChangeCore;
let r=c.compareEvidence('Kundservice kontrollerar ordern.','Kundservice kontrollerar ordern. Därefter registreras den.');if(r.status!=='unchanged')throw new Error('unchanged failed');
r=c.compareEvidence('Kundservice kontrollerar ordern.','Ekonomi kontrollerar och godkänner ordern.');if(!['changed','missing'].includes(r.status))throw new Error('change failed');
const comp=c.compareSteps([{id:'n1',text:'Kontrollera ordern',sourceTrace:{sources:[{name:'rutin.docx',evidence:'Kundservice kontrollerar ordern.'}]}}],'Kundservice kontrollerar ordern.','rutin.docx');if(comp.summary.unchanged!==1)throw new Error('summary failed');
console.log('source change core ok');
