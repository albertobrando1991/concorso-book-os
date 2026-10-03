from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-fc03-enti-non-economici/chapters');A=Path('artifacts/correzioni-collana-2026-10-02')
plans=[]
for c,p in enumerate(sorted(B.glob('*.md')),1):
 s=p.read_text(encoding='utf8');fm,body=s.split('---',2)[1:];body=re.sub(r'^## N-FC03-.*\n+','',body,flags=re.M)
 body=body.replace('### Testo editoriale\n\n','')
 starts=[];headings=[]
 for m in re.finditer(r'^### (.+)$',body,re.M):
  title=m.group(1)
  if title in ['Scenario','Lettura del caso','Risposta modello','Errore da evitare','Mini-atto possibile','Soluzioni commentate','Caso ragionato di chiusura','Soluzioni della simulazione situazionale']:continue
  if title.startswith('Quesito '):continue
  # Keep the eight-question simulation and all its answers together.
  sim=body.find('### Simulazione situazionale:');end=body.find('### Come leggere le opzioni in prova')
  if sim>=0 and sim<m.start()<end:continue
  starts.append(m.start());headings.append(title)
 starts.append(len(body));headings.append('END')
 if starts[0]>0:starts[0]=0
 def words(a,b):return len(re.findall(r"\b[\wÀ-ÿ]+(?:[’'-][\wÀ-ÿ]+)*\b",body[a:b]))
 total=words(0,len(body));target=total/5
 # Dynamic programming only at complete semantic section boundaries.
 dp={(0,0):(0,[])}
 for k in range(1,6):
  for j in range(1,len(starts)):
   best=None
   for i in range(j):
    prev=dp.get((k-1,i))
    if prev is None:continue
    w=words(starts[i],starts[j]);pen=(w-target)**2+max(0,600-w)**2*100
    cand=(prev[0]+pen,prev[1]+[(i,j,w)])
    if best is None or cand[0]<best[0]:best=cand
   if best:dp[(k,j)]=best
 choice=dp[(5,len(starts)-1)][1];groups=[]
 for n,(i,j,w) in enumerate(choice,1):groups.append({'id':f'N-FC03-{c:02d}-{n:02d}','start':starts[i],'end':starts[j],'heading':headings[i],'words':w})
 plans.append({'path':p.as_posix(),'groups':groups,'total':total})
 print(p.stem,[(g['heading'],g['words']) for g in groups])
(A/'FC03-nuclei-plan.json').write_text(json.dumps(plans,ensure_ascii=False,indent=2),encoding='utf8')
