import fs from 'node:fs/promises'
import {chromium} from '@playwright/test'
import {createPdfExportContract} from '../../scripts/book-studio-pdf-export-core.mjs'
const browser=await chromium.launch({channel:'msedge'})
try {
 const page=await browser.newPage({viewport:{width:1500,height:1050}})
 const css=await fs.readFile('app/globals.css','utf8')
 const article='<article class="bookPage"><header class="chapterPreviewHeader"><span class="chapterNumber">M-FC02 22</span><div><h2>Tutela e processo tributario</h2><div class="bandoPhaseBar">'+['B','A','N','D','O'].map(x=>`<span><strong>${x}</strong><small>ETICHETTA</small></span>`).join('')+'</div></div></header><div class="previewBlocks"><h3>Apertura editoriale</h3><p>Testo di verifica della separazione fra fascia e primo titolo.</p></div></article>'
 await page.setContent('<style>'+css+'</style><div class="bookPages">'+article.repeat(320)+'</div>')
 const contract=createPdfExportContract('artifacts/correzioni-collana-2026-10-02/header-probe.pdf')
 await page.addStyleTag({content:contract.pageCss})
 await page.emulateMedia({media:'print'})
 console.log(await page.evaluate(()=>({header:document.querySelector('header').getBoundingClientRect().toJSON(),h3:document.querySelector('h3').getBoundingClientRect().toJSON()})))
 await page.pdf(contract.pdfOptions)
} finally {await browser.close()}
