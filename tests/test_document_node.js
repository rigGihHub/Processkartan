
const fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={globalThis:{}};vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(__dirname,'..','maplini_state_core.js'),'utf8'),ctx);
const M=ctx.globalThis.MapliniStateCore;
const p=M.normalizeProcess({id:'p',nodes:[{id:'d1',type:'document',text:'Avtal',documentUrl:'https://example.com/a.pdf'}],links:[]},'p');
if(p.nodes[0].type!=='document')throw new Error('document type lost');
if(p.nodes[0].documentUrl!=='https://example.com/a.pdf')throw new Error('document URL lost');
console.log('document node OK');
