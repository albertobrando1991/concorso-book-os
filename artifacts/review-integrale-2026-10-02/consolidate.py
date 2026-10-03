from pathlib import Path
import json,hashlib,re,csv,sys,collections
base=Path('artifacts/review-integrale-2026-10-02')
reports=Path('wiki/reviews/audit-integrale-2026-10-02')
draft='--draft' in sys.argv
inventory=json.loads(Path('artifacts/review-collana-2026-10-02/inventory.json').read_text(encoding='utf-8-sig'))
expected=[32,51,50,17,15,50,25,13,14,13,14,32]
register=[]; summary=[]; problems=[]; actions=[]
for i,v in enumerate(inventory['volumes']):
 code=v['code']; p=base/f'{code}-ledger.json'; report=reports/f'{code}.md'
 if not p.exists() or not report.exists():
  problems.append(code+': report/ledger absent');continue
 d=json.loads(p.read_text(encoding='utf-8-sig')); rows=d.get('files',d.get('chapters',[]))
 if len(rows)!=expected[i]:problems.append(code+': count mismatch')
 for r in rows:
  file=r.get('path',r.get('file','')); f=Path(file)
  sha=hashlib.sha256(f.read_bytes()).hexdigest() if f.exists() else None
  if sha!=r.get('sha256'):problems.append(code+': hash mismatch '+file)
  if r.get('readComplete') is not True or r.get('quizReview')!='complete':problems.append(code+': review not complete '+file)
  register.append({'volume':code,'file':file,'sha256':sha,'readComplete':r.get('readComplete'),'quizReview':r.get('quizReview'),'report':str(report).replace('\\','/'),'pdfReport':str(reports/f'PDF-{code}.md').replace('\\','/'),'chapterObservation':r.get('chapterObservation',''),'findings':r.get('findings',[]),'limitations':r.get('limitations',[])})
 sections=re.findall(r'^##\s+(\d+)\.',report.read_text(encoding='utf-8-sig'),re.M)
 if set(sections)!=set(map(str,range(1,11))):problems.append(code+': report sections '+','.join(sections))
 if not (reports/f'PDF-{code}.md').exists():problems.append(code+': PDF report absent')
 summary.append({'volume':code,'title':v['title'],'chapters':len(rows),'read':sum(r.get('readComplete') is True for r in rows),'report':str(report).replace('\\','/')})
for report in sorted(reports.glob('*.md')):
 for line in report.read_text(encoding='utf-8-sig').splitlines():
  if not re.match(r'^\|\s*(?:V\d\d-(?:FM)?\d+|P\d\d-\d+|EXP-\d+)\s*\|',line):continue
  cells=[s.strip() for s in re.split(r'(?<!\\)\|',line)[1:-1]]
  if len(cells)==6:
   ident,pos,severity,desc,proposal,status=cells
   cells=[ident,pos,'Contenuto e apparati',severity,desc,proposal,status]
  if len(cells)==5:
   ident,pos,severity,desc,proposal=cells
   cells=[ident,pos,'Contenuto e apparati',severity,desc,proposal,'Proposta, non applicata']
  if len(cells)!=7:problems.append('invalid table '+report.name+' '+cells[0]);continue
  ident,pos,category,severity,desc,proposal,status=cells
  severity={'medio':'media'}.get(severity.lower(),severity.lower())
  actions.append({'id':ident,'volume':'VOL-'+ident[1:3] if ident[0] in 'VP' else 'COLLANA','position':pos,'category':category,'severity':severity,'description':desc,'proposal':proposal,'status':status,'report':str(report).replace('\\','/')})
ids=[a['id'] for a in actions]
actions.sort(key=lambda a:(a['volume'],{'bloccante':0,'grave':1,'media':2,'lieve':3}.get(a['severity'],4),a['id']))
if len(ids)!=len(set(ids)):problems.append('duplicate finding IDs')
if len(register)!=326:problems.append('total chapter count '+str(len(register)))
for s in summary:s['findings']=sum(a['volume']==s['volume'] and a['id'].startswith('V') for a in actions)
result={'textReviewComplete':not problems,'chapters':len(register),'volumes':summary,'actions':len(actions),'contentActions':sum(a['id'].startswith('V') for a in actions),'pdfAndExportActions':sum(not a['id'].startswith('V') for a in actions),'severityCounts':dict(collections.Counter(a['severity'].lower() for a in actions)),'problems':problems,'scope':'326 print chapters/appendices; separate digital cookbook excluded; selective external checks; PDF panorama plus detailed samples'}
print(json.dumps(result,ensure_ascii=False,indent=2))
if problems and not draft:raise SystemExit('Cannot finalize: unresolved verification items')
if draft:raise SystemExit(0)
(base/'complete-chapter-register.json').write_text(json.dumps(register,ensure_ascii=False,indent=2),encoding='utf-8')
(base/'action-register.json').write_text(json.dumps(actions,ensure_ascii=False,indent=2),encoding='utf-8')
(base/'final-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
with (reports/'registro-interventi.csv').open('w',encoding='utf-8-sig',newline='') as out:
 w=csv.DictWriter(out,fieldnames=list(actions[0]),delimiter=';');w.writeheader();w.writerows(actions)
lines=['# Registro completo degli interventi proposti','',f'{len(actions)} voci operative aggregate. Non rappresentano altrettanti errori indipendenti: alcune registrano propagazione fra testo, figure e PDF. Nessuna correzione applicata. Fonti, grado di verifica e limiti restano nel rapporto di origine.','']
for s in summary+[{'volume':'COLLANA','title':'Esportazione e apparati comuni'}]:
 lines += [f"## {s['volume']} — {s['title']}",'','| ID | Gravità | Posizione | Intervento | Rapporto |','| --- | --- | --- | --- | --- |']
 for a in actions:
  if a['volume']!=s['volume']:continue
  lines.append(f"| {a['id']} | {a['severity']} | {a['position']} | {a['proposal']} | [{Path(a['report']).stem}]({Path(a['report']).name}) |")
 lines.append('')
(reports/'registro-interventi.md').write_text('\n'.join(lines),encoding='utf-8')
