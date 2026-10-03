import {chromium} from '@playwright/test'
const browser=await chromium.launch({channel:'msedge'});const p=await browser.newPage({viewport:{width:1500,height:1050}})
await p.goto('http://127.0.0.1:3020/?bookId=volumi%2Fvol-10#studio');await p.getByRole('button',{name:'Libro',exact:true}).click();await p.waitForTimeout(30000)
console.log(JSON.stringify(await p.evaluate(()=>{
 const pages=[...document.querySelectorAll('.bookPages .bookPage')];return pages.filter(x=>x.dataset.chapterPath?.includes('02-ufficio')).slice(-2).map(p=>({path:p.dataset.chapterPath,footer:p.querySelector('.pageFooter').getBoundingClientRect().top,blocks:[...p.querySelector('.previewBlocks').children].map(c=>({type:c.tagName,text:c.innerText.slice(0,70),top:c.getBoundingClientRect().top,bottom:c.getBoundingClientRect().bottom,marginTop:getComputedStyle(c).marginTop,marginBottom:getComputedStyle(c).marginBottom}))}))
}),null,2));await browser.close()
