/* Functional DOM check of the actual editor, without browser layout/hit testing.
 * python3 -c "import sys;sys.path.insert(0,'tests');from browser_interaction_smoke import extract_editor_html;print(extract_editor_html())" > /tmp/maplini-editor.html
 * NODE_PATH=/tmp/maplini-test-dom/node_modules node tests/feedback_dom_smoke.cjs /tmp/maplini-editor.html
 * Requires jsdom 26.1.0 in the test environment only.
 */
const assert=require('node:assert/strict');
const fs=require('node:fs');
const {JSDOM,VirtualConsole}=require('jsdom');
const html=fs.readFileSync(process.argv[2],'utf8');
const delay=ms=>new Promise(resolve=>setTimeout(resolve,ms));
async function editor(store=null,mobile=false){
 const errors=[],console=new VirtualConsole();console.on('jsdomError',e=>errors.push(e.message));
 const dom=new JSDOM(html,{url:'https://maplini.test/',runScripts:'dangerously',pretendToBeVisual:true,virtualConsole:console,beforeParse(w){
  w.matchMedia=q=>({matches:mobile&&q.includes('max-width'),media:q,addListener(){},removeListener(){},addEventListener(){},removeEventListener(){}});
  w.ResizeObserver=class{observe(){}disconnect(){}};
  w.HTMLElement.prototype.scrollIntoView=function(){};w.HTMLElement.prototype.scrollTo=function(){};
  Object.defineProperty(w.HTMLElement.prototype,'clientWidth',{get(){return this.id==='p48-scroll'?1100:180}});
  Object.defineProperty(w.HTMLElement.prototype,'clientHeight',{get(){return this.id==='p48-scroll'?650:80}});
  w.HTMLCanvasElement.prototype.getContext=function(){return new Proxy({measureText:t=>({width:String(t).length*8})},{get:(o,k)=>o[k]||(()=>{})})};
  if(store)w.localStorage.setItem('maplini_v050',JSON.stringify(store));
 }});
 await delay(70);const doc=dom.window.document;
 return {dom,doc,errors,setMobile:async next=>{mobile=next;dom.window.dispatchEvent(new dom.window.Event('resize'));await delay(120)},click:id=>{const el=doc.querySelector(id);assert.ok(el,id);el.click()},change:(id,value)=>{const el=doc.querySelector(id);el.value=value;el.dispatchEvent(new dom.window.Event('change',{bubbles:true}))}};
}
async function finishBranch(e,answer){
 e.click('#p48-walkthrough-launch');e.click('#p48-walkthrough-start-btn');
 assert.equal(e.doc.querySelector('#p48-walkthrough-step-title').textContent,'Upphandling identifieras');
 e.click('#p48-walkthrough-next');
 e.click('.p48-walkthrough-answer[data-answer="yes"]');await delay(420);
 assert.equal(e.doc.querySelector('#p48-walkthrough-step-title').textContent,'Är upphandlingen relevant?');
 assert.equal(e.doc.querySelector('.p48-walkthrough-question-kind').textContent,'VÄGVAL');
 assert.equal(e.doc.querySelector('#p48-walkthrough-next').hidden,true,'an unanswered decision cannot continue');
 e.click(`.p48-walkthrough-answer[data-answer="${answer}"]`);await delay(420);
 assert.equal(e.doc.querySelector('#p48-walkthrough-step-title').textContent,answer==='yes'?'Kvalificera upphandlingen':'Dokumentera varför vi avstår');
 e.click('.p48-walkthrough-answer[data-answer="yes"]');await delay(420);
 assert.equal(e.doc.querySelector('#p48-walkthrough-step-title').textContent,answer==='yes'?'Redo att förbereda anbud':'Upphandlingen avslutad');
 e.click('#p48-walkthrough-finish');
 assert.equal(e.doc.querySelector('#p48-walkthrough-summary').hidden,false);
 assert.equal(e.doc.querySelector('#p48-walkthrough-summary-stats .p48-walkthrough-summary-stat:last-child strong').textContent,'0','No at a decision is a normal branch');
 e.click('#p48-walkthrough-close');
}
(async()=>{
 const e=await editor();try{
  assert.equal(e.doc.querySelector('#p48-welcome').hidden,false);
  assert.equal(e.doc.querySelectorAll('.p48-welcome-choices button').length,3);
  e.click('#p48-welcome-document');assert.equal(e.doc.querySelector('#p48-doc-dialog').hidden,false);
  e.change('#p48-source-text','Handläggaren tar emot beställningen.\nHandläggaren kontrollerar beställningen.\nHandläggaren skickar bekräftelse.');e.click('#p48-source-text-run');
  assert.equal(e.doc.querySelector('#p48-doc-create').disabled,false);e.click('#p48-doc-create');
  assert.equal(e.doc.querySelector('#p48-name').value,'Process från dokument');
  await delay(220);const imported=JSON.parse(e.dom.window.localStorage.getItem('maplini_v050'));
  assert.equal(Object.keys(imported.processes).length,2);assert.equal(imported.processes['proc-1'].nodes.length,7,'document entry preserves the previous process');
  e.click('#p48-home');e.click('#p48-welcome-create');assert.equal(e.doc.querySelector('#p48-new-process-dialog').hidden,false);e.click('#p48-new-process-cancel');
  e.click('#p48-home');e.click('#p48-welcome-example');
  assert.equal(e.doc.querySelector('#p48-welcome').hidden,true);
  assert.equal(e.doc.querySelector('#p48-export-menu').parentElement.className,'p48-top-utilities','export stays in the main toolbar');
  await delay(220);
  const saved=JSON.parse(e.dom.window.localStorage.getItem('maplini_v050'));
  assert.equal(Object.keys(saved.processes).length,3,'sample does not replace the existing process');
  await finishBranch(e,'yes');await finishBranch(e,'no');
  e.click('#p48-mode-draw');e.click('.p48-node[data-id="n2"] .p48-label');
  assert.equal(e.doc.querySelector('#p48-info-name').value,'Bedöm upphandlingen');
  e.change('#p48-info-name','Granska kraven');e.change('#p48-info-role','Inköpare');
  assert.equal(e.doc.querySelector('.p48-node[data-id="n2"] .p48-label').textContent,'Granska kraven');
  e.click('#p48-undo');e.click('.p48-node[data-id="n2"] .p48-label');assert.equal(e.doc.querySelector('#p48-info-role').value,'Anbudsansvarig');
  e.click('#p48-undo');e.click('.p48-node[data-id="n2"] .p48-label');assert.equal(e.doc.querySelector('#p48-info-name').value,'Bedöm upphandlingen');
  assert.match(e.doc.querySelector('.p48-node[data-id="n2"] .p48-label').style.fontFamily,/system-ui/);
  assert.deepEqual(e.errors,[]);
 }finally{e.dom.window.close()}
 const legacy={schemaVersion:1,currentId:'my-process',processes:{'my-process':{id:'my-process',name:'Mitt sparade arbete',nodes:[{id:'s',type:'start',text:'Start'},{id:'d',type:'decision',text:'Relevant?'},{id:'a',type:'process',text:'Nästa steg'}],links:[['s','d','right'],['d','a','right']]}}};
 const old=await editor(legacy);try{
  assert.equal(old.doc.querySelector('#p48-welcome').hidden,true,'returning users resume their own work');
  assert.equal(old.doc.querySelector('#p48-name').value,'Mitt sparade arbete');
  old.click('.p48-node[data-id="d"] .p48-label');
  assert.equal(old.doc.querySelector('#p48-info-decision-warning').hidden,false);
  old.click('#p48-walkthrough-launch');old.click('#p48-walkthrough-start-btn');old.click('#p48-walkthrough-next');
  assert.equal(old.doc.querySelector('#p48-walkthrough-step-title').textContent,'Relevant?');
  assert.match(old.doc.querySelector('#p48-walkthrough-next-choices').textContent,/saknar alternativa vägar/);
  assert.equal(old.doc.querySelector('#p48-walkthrough-next').hidden,true);assert.equal(old.doc.querySelector('#p48-walkthrough-finish').hidden,true);
  assert.deepEqual(old.errors,[]);
 }finally{old.dom.window.close()}
 const phone=await editor(null,true);try{
  phone.click('#p48-welcome-example');await delay(80);
  assert.equal(phone.doc.querySelector('#p48-export-menu').parentElement.id,'p48-mobile-reader-extras');
  assert.equal(phone.doc.querySelector('#p48-home').parentElement.id,'p48-mobile-main-actions');
  assert.equal(phone.doc.querySelector('#p48-find-menu').parentElement.id,'p48-mobile-main-actions');
  assert.equal(phone.doc.querySelector('#p48-save-state').parentElement.className,'p48-brand-inner');
  const swipe=(target,type,y)=>{
   const event=new phone.dom.window.Event(type,{bubbles:true,cancelable:true});
   Object.assign(event,{pointerType:'touch',pointerId:7,clientX:150,clientY:y,button:0});
   target.dispatchEvent(event);return event;
  };
  const map=phone.doc.querySelector('#p48-canvas'),viewport=phone.doc.querySelector('#p48-scroll');
  const connector=phone.doc.querySelector('.p48-link-hit-segment,.p48-link-hit');assert.ok(connector,'a real connector receives a native swipe');
  for(const target of [map,phone.doc.querySelector('.p48-node .p48-label'),connector]){
   const top=viewport.scrollTop;
   assert.equal(swipe(target,'pointerdown',200).defaultPrevented,false,'reading lets the browser start a native swipe');
   assert.equal(swipe(target,'pointermove',80).defaultPrevented,false,'reading lets the browser scroll vertically');
   assert.equal(viewport.scrollTop,top,'reading does not pan the map vertically');
   swipe(target,'pointerup',80);
  }
  phone.click('#p48-mobile-reader-home');assert.equal(phone.doc.querySelector('#p48-welcome').hidden,false);
  phone.click('#p48-welcome-close');phone.click('#p48-mobile-reader-edit');
  assert.equal(phone.doc.querySelector('#p48-export-menu').parentElement.className,'p48-top-utilities');
  // jsdom does not apply viewport media queries. Activate their actual CSS for
  // a 360 px phone to check matching selectors and explicit placement, not layout.
  const mobileCSS=phone.doc.createElement('style');
  const rules=[...phone.doc.styleSheets].flatMap(sheet=>[...sheet.cssRules]);
  mobileCSS.textContent=rules.filter(rule=>rule.media&&/max-width:(?:360|480|700|900)px/.test(rule.conditionText.replace(/\s/g,'')))
   .flatMap(rule=>[...rule.cssRules].map(child=>child.cssText)).join('\n');
  phone.doc.head.appendChild(mobileCSS);
  const style=id=>phone.dom.window.getComputedStyle(phone.doc.querySelector(id));
  const actionIDs=['#p48-save','#p48-new','#p48-export-menu','#p48-more-menu'];
  const actionRows=actionIDs.map(id=>style(id).gridRow);
  assert.ok(actionRows.every(row=>/^\d+$/.test(row)&&row===actionRows[0]),'every process action has the same explicit row');
  assert.equal(new Set(actionIDs.map(id=>style(id).gridColumn)).size,4,'actions occupy four distinct columns');
  assert.equal(style('#p48-mobile-tools').display,'none','the toolbar does not duplicate the quick menu Tools button');
  phone.click('#p48-more-menu>summary');phone.click('#p48-find-menu>summary');await delay(50);
  assert.equal(phone.doc.querySelector('#p48-more-menu').open,true,'nested search keeps Mer open');
  const search=phone.doc.querySelector('#p48-find-input');search.value='upphandling';search.dispatchEvent(new phone.dom.window.Event('input',{bubbles:true}));
  assert.ok(phone.doc.querySelector('.p48-find-result'),'moved search retains its input handler');
  phone.click('.p48-find-result');assert.ok(phone.doc.querySelector('.p48-node.selected'),'moved search navigates to a real step');
  phone.click('#p48-find-menu>summary');phone.click('#p48-more-menu>summary');
  assert.equal(swipe(map,'pointerdown',200).defaultPrevented,true,'editing retains custom canvas panning');
  swipe(map,'pointerup',200);
  const count=phone.doc.querySelectorAll('.p48-node').length;
  phone.click('#p48-mobile-add');assert.equal(phone.doc.querySelector('#p48-mobile-sheet').getAttribute('aria-hidden'),'false');
  phone.click('[data-mobile-add="process"]');
  assert.equal(phone.doc.querySelectorAll('.p48-node').length,count+1,'the mobile add menu creates a real editable step');
  assert.equal(phone.doc.querySelector('#p48-mobile-sheet').getAttribute('aria-hidden'),'true');
  phone.click('#p48-mobile-format');phone.click('#p48-mobile-sheet-format');
  assert.equal(phone.doc.querySelector('#p48-mobile-tools').getAttribute('aria-expanded'),'true');
  phone.click('#p48-mobile-tools-close');
  assert.equal(phone.doc.querySelector('#p48-mobile-tools').getAttribute('aria-expanded'),'false','the drawer has an accessible close action');
  phone.click('#p48-mobile-more');
  phone.change('#p48-info-name','Kontrollera mobilredigering');
  assert.ok([...phone.doc.querySelectorAll('.p48-node .p48-label')].some(el=>el.textContent==='Kontrollera mobilredigering'));
  phone.click('#p48-readmode-toggle');
  assert.equal(phone.doc.querySelector('#p48-mobile-tools').getAttribute('aria-expanded'),'false','reading closes the editing drawer');
  assert.equal(phone.doc.querySelector('#p48-mobile-sheet').getAttribute('aria-hidden'),'true');
  assert.equal(phone.doc.querySelector('#p48-export-menu').parentElement.id,'p48-mobile-reader-extras');
  await phone.setMobile(false);
  for(const id of ['#p48-home','#p48-find-menu','#p48-export-menu'])assert.equal(phone.doc.querySelector(id).parentElement.className,'p48-top-utilities','desktop restores original controls');
  assert.ok(phone.doc.querySelector('#p48-save-state').parentElement.classList.contains('p48-top'));
  await phone.setMobile(true);
  assert.equal(phone.doc.querySelector('#p48-home').parentElement.id,'p48-mobile-main-actions');
  assert.equal(phone.doc.querySelectorAll('#p48-home').length,1,'resizing preserves a single live control');
  assert.deepEqual(phone.errors,[]);
 }finally{phone.dom.window.close()}
 console.log('Feedback DOM smoke passed: onboarding, export placement, both branches, content edits, undo, legacy data, incomplete decisions, native mobile swipes and mobile editing.');
})().catch(e=>{console.error(e);process.exitCode=1});
