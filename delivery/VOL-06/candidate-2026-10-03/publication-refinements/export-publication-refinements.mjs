import fs from 'node:fs/promises'
import path from 'node:path'
import {fileURLToPath} from 'node:url'
import {chromium} from '@playwright/test'
import {createPdfExportContract} from '../../scripts/book-studio-pdf-export-core.mjs'
import {waitForStableBookPageCount} from '../../scripts/book-studio-layout-options.mjs'
const number=process.argv[2]
if(!['01','06','09','10'].includes(number))throw new Error('Expected 01,06,09,10')
const bookId=number==='01'?'il-metodo-bando':'volumi/vol-'+number
const label='vol-'+number+'-publication-refined-20261003'
const out=path.resolve('artifacts/correzioni-collana-2026-10-02')
const frozenPath=path.join(out,label+'-payload.json')
let payload
try {payload=JSON.parse(await fs.readFile(frozenPath,'utf8'))}
catch(e){
 if(e.code!=='ENOENT')throw e
 if(number==='10'||number==='09')payload=JSON.parse(await fs.readFile('delivery/VOL-'+number+'/candidate-2026-10-03/payload.json','utf8'))
 else if(number==='01')payload=JSON.parse(await fs.readFile('artifacts/correzioni-collana-2026-10-02/vol01-final-payload.json','utf8'))
 else{
  const response=await fetch('http://127.0.0.1:3021/api/book-studio?bookId=volumi%2Fvol-06')
  if(!response.ok)throw new Error('Payload fetch '+response.status)
  payload=await response.json()
  payload=JSON.parse(JSON.stringify(payload).replaceAll('Scuola, Universita, Ricerca, Cultura','Scuola, Università, Ricerca, Cultura'))
 }
 await fs.writeFile(frozenPath,JSON.stringify(payload))
}
let browser
try {browser=await chromium.launch({channel:'msedge'})} catch {browser=await chromium.launch()}
const page=await browser.newPage({viewport:{width:1500,height:1050}})
page.setDefaultTimeout(180000)
try {
  await page.route('**/api/book-studio?**',route=>route.fulfill({status:200,contentType:'application/json',body:JSON.stringify(payload)}))
  console.log(number,'navigate');
  await page.goto(`http://127.0.0.1:3021/?bookId=${encodeURIComponent(bookId)}#studio`,{waitUntil:'domcontentloaded',timeout:180000})
  console.log(number,'loaded');
  await page.locator('#studio').waitFor({state:'visible',timeout:120000})
  await page.getByRole('button',{name:'Libro',exact:true}).click()
  await page.locator('.bookPages .bookPage').first().waitFor({state:'visible',timeout:120000})
  await page.evaluate(()=>document.fonts.ready)
  await page.$$eval('.bookPages img',async images=>{for(const img of images) img.loading='eager';await Promise.all(images.map(img=>img.decode?.().catch(()=>{})))})
  await page.waitForTimeout(20000)
  // Development HMR or a deferred initial payload can reset the view to chapter.
  await page.getByRole('button',{name:'Libro',exact:true}).click()
  console.log(number,'pagination');
  const count=await waitForStableBookPageCount(page,{maxReadings:180,stableReadings:12,intervalMs:500,confirmationDelayMs:5000})
  if(!(await page.getByRole('button',{name:'Libro',exact:true}).getAttribute('class'))?.includes('active')) throw new Error('Book view reset during export')
  const contract=createPdfExportContract(path.join(out,`${label}-proof.pdf`))
  await page.addStyleTag({content:contract.pageCss})
  await page.emulateMedia({media:'print'})
  await page.evaluate(()=>document.fonts.ready)
  await waitForStableBookPageCount(page,{maxReadings:180,stableReadings:16,intervalMs:500,confirmationDelayMs:5000})
  await page.evaluate(()=>document.body.replaceChildren(document.querySelector('.bookPages').cloneNode(true)))
  await page.$$eval('.bookPages img',async images=>{for(const img of images)img.loading='eager';await Promise.all(images.map(img=>img.decode?.().catch(()=>{})))})
  if(number==='01'){
   await page.$$eval('.bookPages .indexChapterLabel',els=>{for(const el of els)el.textContent=el.textContent.replace(/^Capitolo /,'Cap. ').replace(/^Introduzione$/,'Introd.').replace(/^Conclusione$/,'Concl.').replace(/^Appendice /,'App. ')})
   const figures=await page.evaluate(()=>{
    const images=[...document.querySelectorAll('.bookPages img')].filter(i=>decodeURIComponent(i.src).includes('-stampa.png'))
    if(images.length!==19)throw new Error('Expected19printfigures')
    return images.map(img=>{
     const before=img.getBoundingClientRect(),styles=getComputedStyle(img),width=img.naturalWidth/301*96,height=img.naturalHeight/301*96
     const page=img.closest('.bookPage')
     img.style.width=width+'px';img.style.maxWidth=width+'px';img.style.height=height+'px';img.style.display='block';img.style.marginLeft='auto';img.style.marginRight='auto'
     img.style.marginBottom=styles.marginBottom
     const after=img.getBoundingClientRect()
     return {src:img.getAttribute('src'),page:[...document.querySelectorAll('.bookPage')].indexOf(page)+1,before:{width:before.width,height:before.height},after:{width:after.width,height:after.height},ppiX:img.naturalWidth/(after.width/96),ppiY:img.naturalHeight/(after.height/96)}
    })
   })
   if(figures.some(x=>x.ppiX<300||x.ppiY<300))throw new Error('Figure remains below300ppi')
   await fs.writeFile(path.join(out,label+'-figure-placement.json'),JSON.stringify(figures,null,2))
  }
  if(number==='10'){
   const photo=await page.evaluate(()=>{
    const images=[...document.querySelectorAll('.bookPages img')].filter(i=>decodeURIComponent(i.src).includes('f01-alone-illustrativo.png'))
    if(images.length!==1)throw new Error('Expected exactly one F01 photograph')
    const img=images[0], before=img.getBoundingClientRect(),styles=getComputedStyle(img)
    const width=img.naturalWidth/301*96,height=img.naturalHeight/301*96
    img.style.width=width+'px';img.style.maxWidth=width+'px';img.style.height=height+'px';
    img.style.marginBottom=(parseFloat(styles.marginBottom)+before.height-height)+'px'
    const after=img.getBoundingClientRect()
    return {widthPixels:img.naturalWidth,heightPixels:img.naturalHeight,before:{width:before.width,height:before.height},after:{width:after.width,height:after.height},ppiX:img.naturalWidth/(after.width/96),ppiY:img.naturalHeight/(after.height/96),scope:'Placement only; source bitmap unchanged'}
   })
   if(photo.ppiX<300||photo.ppiY<300)throw new Error('Photograph remains below300ppi')
   await fs.writeFile(path.join(out,label+'-photo-placement.json'),JSON.stringify(photo,null,2))
  }
  const metrics=await page.evaluate(()=>{
    const pages=Array.from(document.querySelectorAll('.bookPages .bookPage'))
    return {
      pageCount:pages.length,
      indexMinimumPt:Math.min(...Array.from(document.querySelectorAll('.bookPages .indexSubLine,.bookPages .indexChapterLabel')).map(el=>parseFloat(getComputedStyle(el).fontSize)*72/96)),
      literalBr:pages.reduce((n,p)=>n+(p.innerText.match(/<br\s*\/?\s*>/gi)||[]).length,0),
      maxTableColumns:Math.max(...Array.from(document.querySelectorAll('.bookPages .previewTable tr')).map(r=>r.children.length)),
      missingImages:Array.from(document.querySelectorAll('.bookPages img')).filter(i=>!i.complete||i.naturalWidth<1).length,
      pages:pages.map((p,i)=>{
        const content=p.querySelector('.previewBlocks,.frontMatterBlocks'),rect=content?.getBoundingClientRect(),footer=p.querySelector('.pageFooter')?.getBoundingClientRect()
        const children=content?Array.from(content.children):[]
        const overflows=children.filter(c=>footer && c.getBoundingClientRect().bottom>footer.top+1).map(c=>({type:c.tagName,text:c.textContent.slice(0,110),bottom:c.getBoundingClientRect().bottom-footer.top}))
        return {page:i+1,path:p.dataset.chapterPath,overflows,text:p.innerText}
      })
    }
  })
  await fs.writeFile(path.join(out,`${label}-proof-metrics.json`),JSON.stringify(metrics,null,2))
  if(!Number.isFinite(metrics.indexMinimumPt)) throw new Error('Full volume index absent: refusing a partial export')
  console.log(JSON.stringify({bookId,count,indexMinimumPt:metrics.indexMinimumPt,literalBr:metrics.literalBr,maxTableColumns:metrics.maxTableColumns,overflowPages:metrics.pages.filter(p=>p.overflows.length).map(p=>p.page)}))
  await page.pdf(contract.pdfOptions)
  if(number==='01'){const {execFileSync}=await import('node:child_process');console.log(execFileSync('python',['-X','utf8','artifacts/correzioni-collana-2026-10-02/normalize-base-orphan.py',path.join(out,label+'-proof.pdf')],{encoding:'utf8'}))}
  console.log('PDF saved: '+label)
} finally {await browser.close()}
