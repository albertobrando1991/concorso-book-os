from pathlib import Path
import json,re,hashlib,shutil
A=Path(__file__).parent
f=A/'M-PA01-freeze.json'; freeze=json.loads(f.read_text('utf8')); rows=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for row in freeze['files']:
 p=Path(row['path'])
 if '/chapters/' not in p.as_posix():continue
 before=p.read_text('utf8'); lines=[]
 for line in before.splitlines():
  if line.startswith('|') and not re.search(r'https?://',line):
   line=re.sub(r'(?<=[A-Za-zÀ-ÿ])/(?=[A-Za-zÀ-ÿ])',' / ',line)
  lines.append(line)
 after='\n'.join(lines)+'\n'
 if before==after:continue
 backup=A/'vol01-labels-before'/p.name;backup.parent.mkdir(exist_ok=True);shutil.copy2(p,backup)
 old=sha(p);p.write_text(after,'utf8');rows.append(dict(path=p.as_posix(),before=old,after=sha(p),reason='Spazi ai separatori nelle celle per ritorno fra parole; significato e valori invariati.'))
 row['sha256']=sha(p)
freeze['controlledTableLabels']=rows
f.write_text(json.dumps(freeze,ensure_ascii=False,indent=2),'utf8')
(A/'VOL-01-final-labels.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8')
src=(A/'export-proof.mjs').read_text('utf8')
src=src.replace("const bookId=process.argv[2]||'volumi/vol-12'","const bookId='il-metodo-bando'")
src=src.replace("const label=process.argv[3]||bookId.split('/').at(-1)","const label='vol-01-reader-final-20261003'")
src=src.replace("  await page.goto(","  const response=await fetch('http://127.0.0.1:3020/api/book-studio?bookId=il-metodo-bando');if(!response.ok)throw Error('API '+response.status);const payload=await response.json();await fs.writeFile(path.join(out,'vol01-final-payload.json'),JSON.stringify(payload));\n  await page.route('**/api/book-studio?**',route=>route.fulfill({status:200,contentType:'application/json',body:JSON.stringify(payload)}));\n  await page.goto(")
src=src.replace("  const metrics=await page.evaluate", """  const labels=await page.$$eval('.bookPages .indexChapterLabel', els=>els.map(el=>{const before=el.textContent;el.textContent=before.replace(/^Capitolo /,'Cap. ').replace(/^Introduzione$/,'Introd.').replace(/^Conclusione$/,'Concl.').replace(/^Appendice /,'App. ');const title=el.parentElement.querySelector('.indexLineTitle');const range=document.createRange();range.selectNodeContents(el);return {before,after:el.textContent,overlapsTitle:!!title && range.getBoundingClientRect().right>title.getBoundingClientRect().left-2}}));
  if(labels.some(r=>r.overlapsTitle))throw Error('Index label overlaps');
  await fs.writeFile(path.join(out,'VOL-01-index-labels.json'),JSON.stringify(labels,null,2));
  const metrics=await page.evaluate""")
(A/'export-vol01-final.mjs').write_text(src,'utf8')
print('Table label files',len(rows))
