from pathlib import Path
A=Path(__file__).parent
s=Path('delivery/VOL-10/candidate-2026-10-03/reproduction/export-frozen.mjs').read_text('utf8')
s=s.replace("from '../../../../scripts/", "from '../../scripts/")
start=s.index("const bookId=")
end=s.index('let browser',start)
s=s[:start]+'''const number=process.argv[2]
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
  const response=await fetch('http://127.0.0.1:3020/api/book-studio?bookId=volumi%2Fvol-06')
  if(!response.ok)throw new Error('Payload fetch '+response.status)
  payload=await response.json()
  payload=JSON.parse(JSON.stringify(payload).replaceAll('Scuola, Universita, Ricerca, Cultura','Scuola, Università, Ricerca, Cultura'))
 }
 await fs.writeFile(frozenPath,JSON.stringify(payload))
}
''' + s[end:]
point="  const metrics=await page.evaluate(()=>{"
assert s.count(point)==1
addition='''  if(number==='01'){
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
'''
s=s.replace(point,addition+point)
s=s.replace('http://127.0.0.1:3020','http://127.0.0.1:3021')
s=s.replace("  await page.goto(","  console.log(number,'navigate');\n  await page.goto(")
s=s.replace("  await page.locator('#studio').waitFor", "  console.log(number,'loaded');\n  await page.locator('#studio').waitFor")
s=s.replace("  const count=await waitForStableBookPageCount", "  console.log(number,'pagination');\n  const count=await waitForStableBookPageCount")
s=s.replace("  console.log('PDF saved: '+label)", "  if(number==='01'){const {execFileSync}=await import('node:child_process');console.log(execFileSync('python',['-X','utf8','artifacts/correzioni-collana-2026-10-02/normalize-base-orphan.py',path.join(out,label+'-proof.pdf')],{encoding:'utf8'}))}\n  console.log('PDF saved: '+label)")
(A/'export-publication-refinements.mjs').write_text(s,'utf8')
print('Export congelato predisposto per06/10')
