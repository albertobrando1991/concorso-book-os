import {chromium} from '@playwright/test'
const browser=await chromium.launch({channel:'msedge'})
try{
 const page=await browser.newPage();
 page.on('pageerror',e=>console.log('PAGEERROR',e.message.slice(0,600)))
 page.on('response',r=>{if(r.status()>=400)console.log('HTTP',r.status(),r.url())})
 await page.goto('http://127.0.0.1:3020/?bookId=volumi%2Fvol-10#studio',{waitUntil:'domcontentloaded'})
 await page.waitForTimeout(12000)
 console.log('BUTTONS',await page.locator('button').allTextContents())
 console.log('BODY',(await page.locator('body').innerText()).slice(-2500))
}finally{await browser.close()}
