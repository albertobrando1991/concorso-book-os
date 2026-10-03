from pathlib import Path
import json, hashlib, shutil

A = Path('artifacts/correzioni-collana-2026-10-02')
G = Path('C:/Users/info/.codex/generated_images/01a0fe3a-1334-77b1-8b26-48afd5f441ff')
jobs = {
 'chapter-09/02-ciclo-fabbisogno-esecuzione.png': 'exec-11012f89-1efa-4e97-83df-39d67587951c.png',
 'chapter-04/04-organi-costituzionali-flussi.png': 'exec-bc5a3a51-d308-49d6-8d7b-df05825f5b8b.png',
 'chapter-08/02-ciclo-entrate-spese.png': 'exec-1ab050f7-212b-4d14-b60c-9d62584f05a3.png',
 'chapter-09/03-procedure-affidamento-concorrenza.png': 'exec-a32bac35-a60f-42b6-b72d-eb5f10eba012.png',
 'chapter-10/03-file-office-dati.png': 'exec-a06ffa8f-3919-4c0a-b44e-8ddc1c5ba501.png',
 'chapter-10/07-istanza-online-conservazione.png': 'exec-11bf6ab4-9d09-4335-a598-ee7bd5501215.png',
 'chapter-12/03-parole-logiche-decisive.png': 'exec-b0b6b2db-a311-4528-a6f0-672daca837e9.png',
}
manifest = json.loads((A/'figure-vol01-corrette-manifest.json').read_text('utf-8'))
delta = []
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def change(p, old, new):
 t=p.read_text('utf-8'); assert old in t, (p,old)
 backup=A/'before-text/VOL-01/print-figures'/p.name
 if not backup.exists():
  backup.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,backup)
 before=sha(p); p.write_text(t.replace(old,new),'utf-8')
 delta.append({'path':p.as_posix(),'before':before,'after':sha(p),'reason':'Figura più leggibile o didascalia coerente con contenuto già verificato'})
for row in manifest:
 if row['path'] not in jobs: continue
 src=G/jobs[row['path']]; assert src.exists()
 old=Path(row['newAsset']); new=old.with_name(old.name.replace('-corretto.png','-stampa.png'))
 if not new.exists(): shutil.copyfile(src,new)
 assert sha(src)==sha(new)
 for chapter in row['chapters']:
  p=Path(chapter)
  if old.name in p.read_text('utf-8'): change(p,old.name,new.name)
 row['previousAsset']=old.as_posix(); row['newAsset']=new.as_posix()
 row['generatedPath']=str(src); row['sha256']=sha(new)
 row['visualReview']='Versione in bianco e nero con etichette grandi esaminata integralmente; nuova verifica su pagina PDF ancora necessaria'
p=Path('wiki/books/il-metodo-bando/chapters/anatomia-del-bando.md')
old='Schema per classificare le materie del bando in obbligatorie, probabili, accessorie, killer e solo orali.'
if old in p.read_text('utf-8'): change(p,old,'Scheda delle materie: presenza nel programma, peso nella prova, livello personale e priorità di studio.')
p=Path('wiki/books/il-metodo-bando/chapters/contratti-pubblici-essenziali.md')
old='Procedure di affidamento: al crescere di importo, complessità e impatto sul mercato aumentano concorrenza, pubblicità, formalità e controlli.'
if old in p.read_text('utf-8'): change(p,old,'Procedure di affidamento: modalità distinte, da scegliere secondo oggetto, valore e presupposti previsti dalla legge.')
p=Path('wiki/books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali.md')
old='Nei concorsi, la produttività personale è una delle aree più richieste. Non viene chiesto di usare davvero il programma durante il quiz, ma di conoscere funzioni, comandi, differenze e lessico.'
if old in p.read_text('utf-8'): change(p,old,'La produttività personale può essere verificata con quiz su funzioni, comandi, differenze e lessico, oppure con una prova pratica di utilizzo del programma. Il bando e le istruzioni della prova indicano la modalità richiesta.')
(A/'figure-vol01-corrette-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf-8')
(A/'VOL-01-print-figure-delta.json').write_text(json.dumps(delta,ensure_ascii=False,indent=2),'utf-8')
f=A/'M-PA01-freeze.json'; m=json.loads(f.read_text('utf-8'))
changes=[]
for row in m['files']:
 p=Path(row['path']); current=sha(p)
 if current!=row['sha256']:
  assert any(x['path']==row['path'] for x in delta), row['path']
  changes.append({'path':row['path'],'before':row['sha256'],'after':current})
  row['sha256']=current
m['controlledPrintCorrections']={'date':'2026-10-03','changes':changes,'description':'Sette figure ridisegnate con testo grande; alt/caption allineati e modalità quiz/prova pratica esplicitate. Nessuna dichiarazione di PDF finale.'}
f.write_text(json.dumps(m,ensure_ascii=False,indent=2),'utf-8')
print(json.dumps({'installed':len(jobs),'changes':len(delta),'freezeChanges':len(changes)}))
