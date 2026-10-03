import fs from 'node:fs/promises'
import path from 'node:path'
import {chromium} from '@playwright/test'
import {createPdfExportContract} from '../../scripts/book-studio-pdf-export-core.mjs'
import {waitForStableBookPageCount} from '../../scripts/book-studio-layout-options.mjs'
const bookId='il-metodo-bando'
const label='vol-01-reader-final-20261003'
const out=path.resolve('artifacts/correzioni-collana-2026-10-02')
let browser
try {browser=await chromium.launch({channel:'msedge'})} catch {browser=await chromium.launch()}
const page=await browser.newPage({viewport:{width:1500,height:1050}})
page.setDefaultTimeout(180000)
try {
  const response=await fetch('http://127.0.0.1:3020/api/book-studio?bookId=il-metodo-bando');if(!response.ok)throw Error('API '+response.status);const payload=await response.json();await fs.writeFile(path.join(out,'vol01-final-payload.json'),JSON.stringify(payload));
  await page.route('**/api/book-studio?**',route=>route.fulfill({status:200,contentType:'application/json',body:JSON.stringify(payload)}));
  await page.goto(`http://127.0.0.1:3020/?bookId=${encodeURIComponent(bookId)}#studio`,{waitUntil:'domcontentloaded',timeout:180000})
  await page.locator('#studio').waitFor({state:'visible',timeout:120000})
  await page.getByRole('button',{name:'Libro',exact:true}).click()
  await page.locator('.bookPages .bookPage').first().waitFor({state:'visible',timeout:120000})
  await page.evaluate(()=>document.fonts.ready)
  await page.$$eval('.bookPages img',async images=>{for(const img of images) img.loading='eager';await Promise.all(images.map(img=>img.decode?.().catch(()=>{})))})
  await page.waitForTimeout(20000)
  // Development HMR or a deferred initial payload can reset the view to chapter.
  await page.getByRole('button',{name:'Libro',exact:true}).click()
  const count=await waitForStableBookPageCount(page,{maxReadings:180,stableReadings:12,intervalMs:500,confirmationDelayMs:5000})
  if(!(await page.getByRole('button',{name:'Libro',exact:true}).getAttribute('class'))?.includes('active')) throw new Error('Book view reset during export')
  const contract=createPdfExportContract(path.join(out,`${label}-proof.pdf`))
  await page.addStyleTag({content:contract.pageCss})
  await page.emulateMedia({media:'print'})
  await page.evaluate(()=>document.fonts.ready)
  await waitForStableBookPageCount(page,{maxReadings:180,stableReadings:16,intervalMs:500,confirmationDelayMs:5000})
  await page.evaluate(()=>document.body.replaceChildren(document.querySelector('.bookPages').cloneNode(true)))
  await page.$$eval('.bookPages img',async images=>{for(const img of images)img.loading='eager';await Promise.all(images.map(img=>img.decode?.().catch(()=>{})))})
  const labels=await page.$$eval('.bookPages .indexChapterLabel', els=>els.map(el=>{const before=el.textContent;el.textContent=before.replace(/^Capitolo /,'Cap. ').replace(/^Introduzione$/,'Introd.').replace(/^Conclusione$/,'Concl.').replace(/^Appendice /,'App. ');const title=el.parentElement.querySelector('.indexLineTitle');const range=document.createRange();range.selectNodeContents(el);return {before,after:el.textContent,overlapsTitle:!!title && range.getBoundingClientRect().right>title.getBoundingClientRect().left-2}}));
  if(labels.some(r=>r.overlapsTitle))throw Error('Index label overlaps');
  await fs.writeFile(path.join(out,'VOL-01-index-labels.json'),JSON.stringify(labels,null,2));
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
  console.log('PDF saved: '+label)
} finally {await browser.close()}
