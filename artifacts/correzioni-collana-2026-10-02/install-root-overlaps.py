from pathlib import Path
import json,shutil,hashlib
root=Path('wiki/books/il-metodo-bando');out=Path(__file__).parent
rows=json.loads((out/'figure-overlap-results.json').read_text(encoding='utf8'))
for r in rows:
 p=root/'assets'/r['path'];q=p.with_stem(p.stem+'-corretto');shutil.copyfile(r['generatedPath'],q)
 r['newAsset']=q.as_posix();r['sha256']=hashlib.sha256(q.read_bytes()).hexdigest();r['chapters']=[]
 r['visualReview']='Immagine intera vista: numeri, titoli e testo separati senza sovrapposizioni; PDF ancora necessario'
 for ch in (root/'chapters').glob('*.md'):
  t=ch.read_text(encoding='utf8');new=r['path'].replace('.png','-corretto.png')
  if r['path'] in t:
   t=t.replace(r['path'],new)
   if 'chapter-16/' in r['path']:t=t.replace('Struttura universale della risposta orale','Struttura flessibile della risposta orale')
   ch.write_text(t,encoding='utf8');r['chapters'].append(ch.as_posix())
  elif new in t:r['chapters'].append(ch.as_posix())
 assert r['chapters'],r
manifest=out/'figure-vol01-corrette-manifest.json';old=json.loads(manifest.read_text(encoding='utf8'));old=[r for r in old if r['path'] not in {x['path'] for x in rows}]
manifest.write_text(json.dumps(old+rows,ensure_ascii=False,indent=2),encoding='utf8')
reg=out/'registro-applicazione.json';data=json.loads(reg.read_text(encoding='utf8'))
for r in data:
 if r['id']=='P01-10':
  r['status']='applicato-da-verificare';r['changedFiles']=[x['newAsset'] for x in rows]+[p for x in rows for p in x['chapters']]
  r['verification']=['Sette immagini corrette e ispezionate; nessuna sovrapposizione residua negli asset. PDF ancora da verificare.']
reg.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8');print('Installate7; totale figure corrette',len(old+rows))
