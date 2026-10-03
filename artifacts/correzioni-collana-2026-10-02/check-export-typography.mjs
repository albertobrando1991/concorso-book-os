import fs from 'node:fs/promises'
import assert from 'node:assert/strict'
import {chromium} from '@playwright/test'
let browser
try {browser=await chromium.launch({channel:'msedge'})} catch {browser=await chromium.launch()}
try {
  const page=await browser.newPage()
  await page.setContent(`<html lang="it"><style>${await fs.readFile('app/globals.css','utf8')}</style><article class="bookPage"><div class="frontMatter-analytical-index"><div class="indexPart"><span>M-FC02</span><strong>Modulo</strong></div><div class="indexLine indexChapterLine"><span class="indexChapterLabel">Cap. 10</span><span class="indexLineTitle">Un titolo lungo di prova per verificare la leggibilità dell’indice completo</span><span class="indexLeader"></span><span class="indexPageNumber">150</span></div><div class="indexLine indexSubLine"><span class="indexSubNumber">10.1</span><span class="indexLineTitle">Una sezione didattica nel sommario</span><span class="indexLeader"></span><span class="indexPageNumber">151</span></div></div><div class="previewBlocks"><table class="previewTable"><tbody><tr class="worksheetRow"><td>Motivazione</td><td></td></tr></tbody></table><figure><figcaption>Figura 1 — Una didascalia leggibile</figcaption></figure></div></article></html>`)
  const sizes=await page.evaluate(()=>Object.fromEntries(['.indexPart span','.indexPart strong','.indexChapterLine','.indexChapterLabel','.indexSubLine','.previewBlocks figcaption'].map(s=>[s,parseFloat(getComputedStyle(document.querySelector(s)).fontSize)*72/96])))
  await fs.writeFile(`artifacts/correzioni-collana-2026-10-02/typography-${process.argv[2]||'check'}.json`,JSON.stringify(sizes,null,2))
  console.log(sizes)
  for(const [selector,size] of Object.entries(sizes)) assert.ok(size>=9.49,`${selector}: ${size} pt < 9.5 pt`)
  await page.evaluate(()=>{
    document.querySelector('.previewBlocks').innerHTML='<div class="previewTableWrap"><table class="previewTable"><tbody><tr><td>Prima riga</td></tr></tbody></table></div><div class="previewTableWrap continuedTable"><table class="previewTable"><tbody><tr><td>Seconda riga</td></tr></tbody></table></div>'
  })
  const gap=await page.evaluate(()=>{const tables=document.querySelectorAll('.previewTable');return tables[1].getBoundingClientRect().top-tables[0].getBoundingClientRect().bottom})
  console.log({continuationGapPx:gap})
  assert.ok(gap<=1,`Continuation of same table has ${gap}px gap`)
} finally {await browser.close()}
