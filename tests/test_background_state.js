
const fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={globalThis:{}};vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(__dirname,'..','maplini_state_core.js'),'utf8'),ctx);
const M=ctx.globalThis.MapliniStateCore;
const p=M.normalizeProcess({id:'p',nodes:[],links:[],processBackgroundType:'gradient',
 processGradientStart:'#ffeeee',processGradientEnd:'#eeeeff',processGradientAngle:90,
 processBackgroundImageOpacity:.35,processWatermarkText:'KONFIDENTIELLT',processWatermarkOpacity:.2,processWatermarkUseLogo:true},'p');
if(p.processGradientAngle!==90)throw new Error('gradient angle');
if(p.processWatermarkText!=='KONFIDENTIELLT')throw new Error('watermark text');
if(p.processWatermarkUseLogo!==true)throw new Error('watermark logo');
console.log('background state OK');
