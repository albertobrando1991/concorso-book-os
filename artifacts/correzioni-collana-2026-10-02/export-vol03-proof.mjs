import fs from 'node:fs/promises'
import path from 'node:path'
import {chromium} from '@playwright/test'
import {createPdfExportContract} from '../../scripts/book-studio-pdf-export-core.mjs'
import {waitForStableBookPageCount} from '../../scripts/book-studio-layout-options.mjs'
const bookId='volumi/vol-03'
const tomo='current'
const payload=JSON.parse(await fs.readFile(`artifacts/correzioni-collana-2026-10-02/vol03-proof/payload.json`,'utf8'))
const label=`vol-03-${tomo}`
const out=path.resolve('artifacts/correzioni-collana-2026-10-02/vol03-proof')
let browser
try {browser=await chromium.launch({channel:'msedge'})} catch {browser=await chromium.launch()}
const page=await browser.newPage({viewport:{width:1500,height:1050}})
page.setDefaultTimeout(180000)
try {
  await page.route('**/api/book-studio?**',route=>route.fulfill({status:200,contentType:'application/json',body:JSON.stringify(payload)}))
  await page.goto(`http://127.0.0.1:3020/?bookId=${encodeURIComponent(bookId)}#studio`,{waitUntil:'domcontentloaded',timeout:180000})
  await page.locator('#studio').waitFor({state:'visible',timeout:120000})
  await page.addStyleTag({content:'.bookPages .previewBlocks pre { font-size: 9.5pt !important; line-height: 1.2 !important; }'})
  await page.getByRole('button',{name:'Libro',exact:true}).click()
  await page.locator('.bookPages .bookPage').first().waitFor({state:'visible',timeout:120000})
  await page.evaluate(()=>document.fonts.ready)
  await page.$$eval('.bookPages img',async images=>{for(const img of images) img.loading='eager';await Promise.all(images.map(img=>img.decode?.().catch(()=>{})))})
  await page.waitForTimeout(20000)
  // Development HMR or a deferred initial payload can reset the view to chapter.
  await page.getByRole('button',{name:'Libro',exact:true}).click()
  await waitForStableBookPageCount(page,{maxReadings:180,stableReadings:12,intervalMs:500,confirmationDelayMs:5000})
  if(!(await page.getByRole('button',{name:'Libro',exact:true}).getAttribute('class'))?.includes('active')) throw new Error('Book view reset during export')
  const contract=createPdfExportContract(path.join(out,`${label}-proof.pdf`))
  await page.addStyleTag({content:contract.pageCss})
  await page.emulateMedia({media:'print'})
  await page.evaluate(()=>document.fonts.ready)
  await waitForStableBookPageCount(page,{maxReadings:180,stableReadings:16,intervalMs:500,confirmationDelayMs:5000})
  await page.evaluate(()=>document.body.replaceChildren(document.querySelector('.bookPages').cloneNode(true)))
  const count=await page.locator('.bookPages .bookPage').count()
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
  const absent=payload.chapters.filter(c=>!metrics.pages.some(p=>p.path===c.path)).map(c=>c.path)
  if(absent.length) throw new Error('Missing chapters: '+absent.join(','))
  if(count>828) throw new Error('KDP page limit exceeded: '+count)
  if(metrics.missingImages) throw new Error('Images missing')
  console.log(JSON.stringify({bookId,count,indexMinimumPt:metrics.indexMinimumPt,literalBr:metrics.literalBr,maxTableColumns:metrics.maxTableColumns,overflowPages:metrics.pages.filter(p=>p.overflows.length).map(p=>p.page)}))
  await page.pdf(contract.pdfOptions)
  console.log('PDF saved: '+label)
} finally {await browser.close()}
