from pathlib import Path
import json, hashlib, shutil
A=Path('artifacts/correzioni-collana-2026-10-02')
G=Path('C:/Users/info/.codex/generated_images/01a0fe3a-1334-77b1-8b26-48afd5f441ff')
jobs={
'chapter-02/04-gerarchia-materie-bando.png':'df9a7a04-d9af-46a7-9ee9-8a2ef447d77b',
'chapter-14/04-banca-dati-quattro-passaggi.png':'c48feb4f-6238-439d-bab1-1d76cb0c2ac0',
'chapter-15/04-schema-risposta-concorsuale.png':'fbcfb7a2-d896-4af3-a2da-9377a45c1a4d',
'chapter-16/03-struttura-universale-risposta-orale.png':'71302cb6-7eed-4462-b90a-f2c8fd196311',
'chapter-17/04-schema-risposta-caso-pratico.png':'c8648bca-dd6c-421e-9be2-beca3253d4ca',
'chapter-18/03-anatomia-quesito-situazionale.png':'b5d59b63-074c-4edd-9bcd-d44f12ca5a21',
'chapter-19/07-sequenza-famiglia-piano.png':'668adec7-7da1-4447-973c-ac083929f9d8',
'chapter-20/06-semaforo-e-pesatura-tempo.png':'8945aff6-0be9-4291-b204-d0149ee21591',
'chapter-22/07-caso-luca-ciclo-controllo.png':'c0968dbc-8d8f-4f58-a624-dfb1bbb6b49d',
'chapter-23/02-sei-categorie-errore.png':'5b2fe59e-ee40-42bd-ab98-06460d2d70b7',
'chapter-23/07-caso-marta-pattern-errori.png':'aed010bf-8d8c-4ee6-8b56-52faaaf5bda4',
'chapter-24/02-tre-regole-checklist.png':'2e37c0c6-dbd4-4d26-8972-a731882b4089',
}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((A/'figure-vol01-corrette-manifest.json').read_text('utf-8'))
delta=[]
def change(p,old,new):
 t=p.read_text('utf-8')
 if old not in t:return
 b=A/'before-text/VOL-01/print-figures-second'/p.name
 b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():shutil.copyfile(p,b)
 before=sha(p);p.write_text(t.replace(old,new),'utf-8')
 delta.append(dict(path=p.as_posix(),before=before,after=sha(p)))
for row in manifest:
 if row['path'] not in jobs:continue
 src=G/('exec-'+jobs[row['path']]+'.png');assert src.exists()
 old=Path(row['newAsset']);new=old.with_name(old.name.replace('-corretto.png','-stampa.png'))
 if not new.exists():shutil.copyfile(src,new)
 assert sha(src)==sha(new)
 if old!=new:
  for chapter in row['chapters']:change(Path(chapter),old.name,new.name)
  row['previousAsset']=old.as_posix()
 row.update(newAsset=new.as_posix(),generatedPath=str(src),sha256=sha(new),visualReview='Immagine completa esaminata: testo grande, nessi e calcoli corretti. Verifica sulla nuova pagina PDF ancora necessaria.')
B=Path('wiki/books/il-metodo-bando/chapters')
change(B/'anatomia-del-bando.md','Scheda delle materie: presenza nel programma, peso nella prova, livello personale e priorità di studio.','Scheda delle materie: presenza nel programma, fase della selezione, peso nella prova e priorità di studio.')
change(B/'mappe-profilo-cosa-resta-comune-cosa-cambia.md','Figura 20.6 - Semaforo e pesatura del tempo','Figura 20.6 - Semaforo delle materie e azioni di studio')
(A/'figure-vol01-corrette-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf-8')
if delta:
 (A/'VOL-01-print-figure-second-delta.json').write_text(json.dumps(delta,ensure_ascii=False,indent=2),'utf-8')
 f=A/'M-PA01-freeze.json';m=json.loads(f.read_text('utf-8'));changes=[]
 for row in m['files']:
  p=Path(row['path']);current=sha(p)
  if current!=row['sha256']:
   assert any(x['path']==row['path'] for x in delta),row['path']
   changes.append(dict(path=row['path'],before=row['sha256'],after=current));row['sha256']=current
 m['controlledPrintCorrectionsSecond']={'date':'2026-10-03','changes':changes,'description':'Dodici figure con caratteri grandi; didascalie coerenti. PDF da rigenerare e verificare.'}
 f.write_text(json.dumps(m,ensure_ascii=False,indent=2),'utf-8')
print(json.dumps({'installed':len(jobs),'mutations':len(delta),'totalFigures':len(manifest)}))
