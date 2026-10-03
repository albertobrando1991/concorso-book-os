from pathlib import Path
import json,shutil,hashlib,re
root=Path('wiki/books/il-metodo-bando');out=Path(__file__).parent
rows=json.loads((out/'figure-batch-2-results.json').read_text(encoding='utf8'))
for r in rows:
 p=root/'assets'/r['path'];q=p.with_stem(p.stem+'-corretto')
 shutil.copyfile(r['generatedPath'],q)
 r['newAsset']=q.as_posix();r['sha256']=hashlib.sha256(q.read_bytes()).hexdigest()
 r['visualReview']='Esaminata immagine completa: testi leggibili, nessi e correzioni richieste presenti; controllo dimensione stampa ancora necessario'
for old in ['chapter-04/04-organi-costituzionali-flussi.png','chapter-08/02-ciclo-entrate-spese.png','chapter-12/03-parole-logiche-decisive.png','chapter-23/07-caso-marta-pattern-errori.png']:
 p=root/'assets'/old;q=p.with_stem(p.stem+'-corretto');assert q.exists()
 rows.append({'path':old,'newAsset':q.as_posix(),'sha256':hashlib.sha256(q.read_bytes()).hexdigest(),'visualReview':'Esaminata in sessione; controllo PDF ancora necessario'})
for r in rows:
 old=r['path'];new=old.replace('.png','-corretto.png');r['chapters']=[]
 for p in (root/'chapters').glob('*.md'):
  t=p.read_text(encoding='utf8')
  if old in t:
   t=t.replace(old,new);p.write_text(t,encoding='utf8');r['chapters'].append(p.as_posix())
  elif new in t:r['chapters'].append(p.as_posix())
 assert r['chapters'],r
(out/'figure-vol01-corrette-manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
reg=out/'registro-applicazione.json';data=json.loads(reg.read_text(encoding='utf8'))
mapping={'P01-04':['organi-costituzionali'],'P01-05':['ciclo-entrate'],'P01-06':['ciclo-fabbisogno','istanza-online','caso-luca'],'P01-07':['procedure-affidamento'],'P01-08':['parole-logiche'],'P01-09':['pesatura-tempo'],'P01-11':['file-office'],'P01-12':['gerarchia-materie','caso-marta']}
for r in data:
 if r['id'] in mapping:
  matched=[x for x in rows if any(k in x['path'] for k in mapping[r['id']])]
  r['status']='applicato-da-verificare'
  r['changedFiles']=list(dict.fromkeys(r.get('changedFiles',[])+[x['newAsset'] for x in matched]+[p for x in matched for p in x['chapters']]))
  r['verification']=['Immagini corrette e ispezionate integralmente in sessione; serve ancora collazione sul PDF rigenerato. Evidenze in figure-vol01-corrette-manifest.json']
reg.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print('Installate e collegate',len(rows),'figure; PDF ancora da verificare')
