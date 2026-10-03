from pathlib import Path
import re,json,hashlib
base=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters');changes={}
def move(t,code,target,title=None):
 m=re.search(r'^## '+re.escape(code)+r' · (.+)\n\n?',t,re.M);assert m,code
 heading='## '+code+' · '+(title or m[1])+'\n\n';t=t[:m.start()]+t[m.end():]
 assert t.count(target)==1,(code,target,t.count(target));return t.replace(target,heading+target)
def save(p,t,ids):
 t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8')
 for i in ids:changes.setdefault(i,[]).append(p.as_posix())
for p in sorted(base.glob('*.md')):
 t=p.read_text(encoding='utf8');n=p.name[:2];ids=[]
 if n=='01':
  t=move(t,'N-TR02-01-02','Il ciclo integrato dal fabbisogno alla chiusura\n','Il ciclo dal fabbisogno alla chiusura');ids+=['V09-01']
 if n=='02':t=move(t,'N-TR02-02-05','### ▣ Verifica 2: qualificazione, controlli e RACI');ids+=['V09-02']
 if n=='03':t=move(t,'N-TR02-03-05','### Fase 4 - impostare i KPI');ids+=['V09-03']
 if n=='04':t=move(t,'N-TR02-04-05','### Fase 5 - controllare il fascicolo');ids+=['V09-03']
 if n=='05':t=move(t,'N-TR02-05-03','| Formula debole |', 'Motivare la scelta e controllare i requisiti');ids+=['V09-01']
 if n=='06':t=move(t,'N-TR02-06-03','### Quiz 3\n\nPerché il CIG');ids+=['V09-02']
 if n=='08':t=move(t,'N-TR02-08-02','- contratto e capitolato;','Documenti e controlli dell’esecuzione');ids+=['V09-03']
 if n=='09':
  t=move(t,'N-TR02-09-03',"### Quiz 3\n\nLa presentazione di un'istanza");t=move(t,'N-TR02-09-04','### Da sapere in 5 righe\n\nIl ricorso');t=t.replace('almeno sei dati:','almeno sette dati:');ids+=['V09-01','V09-02','V09-25']
 if n=='12':t=move(t,'N-TR02-12-03','Clausole ambientali, criteri premiali e mezzi di prova\n','Verificare la sostenibilità dichiarata');ids+=['V09-02']
 if n=='13':
  t=move(t,'N-TR02-13-05','### Simulazione 2 - WBS confusa con organigramma');t=t.replace('N-TR02-XX-04','N-TR02-13-02').replace('N-TR02-XX-08','N-TR02-13-04');ids+=['V09-03','V09-04']
 if n=='14':
  t=move(t,'N-TR02-14-03','### Simulazione 5','Simulazioni e correzioni operative');t=move(t,'N-TR02-14-04','### Simulazione 10 - Project management e recupero del ritardo');ids+=['V09-03']
 if ids:save(p,t,ids)
reg=Path(__file__).with_name('registro-applicazione.json');rows=json.loads(reg.read_text(encoding='utf8'))
for r in rows:
 if r['id'] in changes:r.update(status='applicato-da-verificare',changedFiles=changes[r['id']],verification=['Titoli spostati a confini didattici; collazione PDF finale pendente'])
reg.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(changes,ensure_ascii=False))
