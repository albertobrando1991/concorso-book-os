"""Merge evidence into a NEW register; never edits the historical audit or baseline.

Default: inventory only. --merge requires explicit per-volume evidence handoffs,
including final evidence for VOL-01 and VOL-04. Extra findings stay separate from
the original582, so identity/completeness checks cannot be satisfied by padding.
"""
from pathlib import Path
from collections import Counter,defaultdict
import json,csv,hashlib,re,sys,datetime,copy
A=Path(__file__).parent;W=Path('wiki/reviews/correzioni-collana-2026-10-02');BASE=A/'registro-applicazione.json';AUDIT=Path('wiki/reviews/audit-integrale-2026-10-02/registro-interventi.csv');HANDOFF=A/'registro-evidence-handoffs.json'
sha=lambda b:hashlib.sha256(b).hexdigest()
def load(p):return json.loads(p.read_text(encoding='utf8'))
def save(p,data):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
ID=re.compile(r'\b(?:[VPC]\d{2}-(?:FM\d+|\d{2,3})|FM\d{2}-\d{2}|EXP-\d{2})\b')
def ids_in_cell(cell):
 result=ID.findall(cell)
 for m in re.finditer(r'\b([VP]\d{2}-)(\d{2,3})([/–—-])(\d{2,3})(?!\d)',cell):
  prefix,start,op,end=m.groups();numbers=[int(end)] if op=='/' else range(int(start)+1,int(end)+1)
  result.extend(prefix+str(n).zfill(len(start)) for n in numbers)
 return list(dict.fromkeys(result))
def parse_tables(path):
 raw=path.read_bytes();lines=raw.decode('utf-8-sig').splitlines();rows=[];headers=[];warnings=[]
 for number,line in enumerate(lines,1):
  if not line.lstrip().startswith('|'):headers=[];continue
  cells=[c.strip() for c in re.split(r'(?<!\\)\|',line.strip().strip('|'))]
  if all(re.fullmatch(r'[:\- ]+',c or '-') for c in cells):continue
  ids=ids_in_cell(cells[0])
  if not ids:headers=cells;continue
  if headers and len(cells)!=len(headers):warnings.append({'source':path.as_posix(),'line':number,'headerCells':len(headers),'rowCells':len(cells)})
  mapped={h:cells[i] for i,h in enumerate(headers) if i<len(cells)}
  def field(*names):return next((v for k,v in mapped.items() if k.casefold() in names),'')
  for id in ids:
   rows.append({'id':id,'source':path.as_posix(),'sourceSha256':sha(raw),'line':number,'raw':line,'columns':mapped,'status':field('stato','stato reale','stato finale','esito') or cells[-1],'intervention':field('correzione applicata','correzione proposta','correzione','modifica','intervento','intervento aggiuntivo'),'evidence':field('evidenza','fonte/evidenza','evidenza consolidata'),'file':field('file','file modificato','file modificati')})
 return rows,warnings
baseline_bytes=BASE.read_bytes();audit_bytes=AUDIT.read_bytes();baseline=json.loads(baseline_bytes);audit=list(csv.DictReader(audit_bytes.decode('utf-8-sig').splitlines(),delimiter=';'))
base_ids=[r['id'] for r in baseline];audit_ids=[r['id'] for r in audit]
assert len(baseline)==582 and len(base_ids)==len(set(base_ids))
assert Counter(base_ids)==Counter(audit_ids),'Immutable audit and application baseline identities differ'
sources=[*sorted(W.glob('VOL-??.md')),*sorted(W.glob('PDF-VOL-??.md'))]
evidence=defaultdict(list);warnings=[]
for p in sources:
 rows,issues=parse_tables(p);warnings+=issues
 for row in rows:evidence[row['id']].append(row)
inventory={'createdAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'baselinePath':BASE.as_posix(),'baselineSha256':sha(baseline_bytes),'auditPath':AUDIT.as_posix(),'auditSha256':sha(audit_bytes),'baselineCount':582,'baselineDuplicateIds':[],'auditMissingIds':[],'sources':[{'path':p.as_posix(),'sha256':sha(p.read_bytes())} for p in sources],'tableWarnings':warnings,'missingEvidenceIds':[i for i in base_ids if i not in evidence],'multipleEvidenceIds':{i:len(e) for i,e in evidence.items() if len(e)>1},'supplementaryIds':sorted(set(evidence)-set(base_ids)),'evidence':dict(evidence)}
save(A/'registro-evidence-inventory.json',inventory)
if '--merge' not in sys.argv:
 print(json.dumps({k:inventory[k] for k in ['baselineCount','tableWarnings','missingEvidenceIds','multipleEvidenceIds','supplementaryIds']},ensure_ascii=False));sys.exit(0)
handoff=load(HANDOFF)
assert handoff.get('readyToMerge'),'Handoff is still a draft'
assert all(handoff.get('volumes',{}).get(v,{}).get('finalEvidenceApproved') for v in ['VOL-01','VOL-04']), 'Await parent final evidence for01/04'
assert not warnings,'Resolve table parsing before merging'
records=[];unmapped=[];manual=handoff.get('overrides',{});ledger_evidence=defaultdict(list)
for p in [*sorted(A.glob('VOL-??-changes.json')),*sorted(A.glob('VOL-??-ledger.json'))]:
 data=load(p);entries=dict(data.get('changes',{}))
 for item in data.get('findings',[]):
  if isinstance(item,dict) and item.get('id'):entries.setdefault(item['id'],item)
 for id,item in entries.items():ledger_evidence[id].append({'source':p.as_posix(),'sourceSha256':sha(p.read_bytes()),'entry':item})
for old in baseline:
 row=copy.deepcopy(old);id=row['id'];vol=row['volume'];h=handoff.get('volumes',{}).get(vol,{});candidates=evidence.get(id,[])
 expected=h.get('pdfReport') if id.startswith('P') else h.get('textReport')
 selected=[e for e in candidates if e['source']==expected]
 if len(selected)>1:
  substantive=[e for e in selected if e['intervention']]
  assert len(substantive)==1,f'Ambiguous substantive evidence for{id}: {expected}'
  # A correction table plus a file/source table is complementary evidence.
  e=copy.deepcopy(substantive[0]);e['file']='; '.join(x['file'] for x in selected if x['file']);e['evidence']='; '.join(x['evidence'] for x in selected if x['evidence'])
 else:e=selected[0] if selected else None
 row['baselineStatus']=old['status'];row['applicationEvidence']=candidates;row['releaseApproved']=False;row['productionStatus']=h.get('productionStatus','non-verificato');row['changedFiles']=list(old.get('changedFiles',[]));row['verification']=list(old.get('verification',[]))
 if id in manual:
  override=manual[id];assert override.get('reason') and override.get('evidence') and override.get('status');row.update({k:v for k,v in override.items() if k in ['status','changedFiles','verification']});row['manualResolution']=override;row['appliedIntervention']=override['reason']
  for path in override['evidence']:
   p=Path(path);assert p.is_file(),f'Missing manual evidence: {path}'
   row['verification'].append({'source':p.as_posix(),'sha256':sha(p.read_bytes()),'evidence':override['reason']})
 elif e:
  status=e['status'].casefold();row['appliedIntervention']=e['intervention'];row['verification'].append({'source':e['source'],'line':e['line'],'sha256':e['sourceSha256'],'evidence':e['evidence'] or e['intervention'],'reportedStatus':e['status']})
  if any(k in status for k in ['pendente','ancora aperto','non verificato']):
   row['status']='applicato-da-verificare' if 'applicato' in status else 'da-applicare'
  elif any(k in status for k in ['parzial','in parte','aperto per','non applicato','da applicare','da riesaminare']):
   row['status']='parzialmente-applicato' if any(k in status for k in ['parzial','in parte','applicato']) and 'non applicato' not in status else 'da-applicare'
  elif id.startswith('P'):
   row['status']='applicato-verificato-pdf' if h.get('pdfVerified') and any(k in status for k in ['corretto','verificato','risolto','chiuso']) else 'applicato-da-verificare'
  elif h.get('textVerified') and any(k in status for k in ['applicato','verificato','risolto','corretto','congelato']):row['status']='applicato-verificato-testo'
  else:row['status']='applicato-da-verificare'
  targets=re.findall(r'\]\(([^)]+)\)',e['file'])
  if h.get('chapterRoot'):targets.extend(str(Path(h['chapterRoot'])/name.strip()) for name in e['file'].split(';') if name.strip().endswith('.md') and '[' not in name)
  for target in targets:
   normalized=target[target.find('wiki/'):] if 'wiki/' in target else target
   if Path(normalized).is_file() and normalized not in row['changedFiles']:row['changedFiles'].append(normalized)
 else:unmapped.append(id)
 row['sourceLedgerEvidence']=ledger_evidence.get(id,[])
 for item in row['sourceLedgerEvidence']:
  for path in item['entry'].get('files',[]):
   if isinstance(path,str) and Path(path).is_file() and path not in row['changedFiles']:row['changedFiles'].append(path)
 row['verification']=list({json.dumps(v,sort_keys=True,ensure_ascii=False):v for v in row['verification']}.values());records.append(row)
ids=[r['id'] for r in records];assert len(records)==582 and len(ids)==len(set(ids)) and set(ids)==set(base_ids)
assert not unmapped,f'No approved evidence for{unmapped}'
counts=Counter(r['status'] for r in records);pervol={v:dict(Counter(r['status'] for r in records if r['volume']==v)) for v in sorted({r['volume'] for r in records})}
summary={'baselineCount':582,'outputCount':len(records),'duplicateIds':[],'missingIds':[],'unexpectedIds':[],'unmappedIds':unmapped,'statusCounts':dict(counts),'byVolume':pervol,'baselineSha256':sha(baseline_bytes),'auditSha256':sha(audit_bytes),'handoffSha256':sha(HANDOFF.read_bytes()),'releaseApproved':False,'supplementaryIds':inventory['supplementaryIds']}
save(A/'registro-applicazione-consolidato-2026-10-03.json',records);save(A/'registro-applicazione-consolidato-summary.json',summary)
save(A/'registro-rilievi-aggiuntivi-2026-10-03.json',{i:evidence[i] for i in inventory['supplementaryIds']})
with (W/'registro-applicazione-consolidato-2026-10-03.csv').open('w',encoding='utf-8-sig',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=['id','volume','status','productionStatus','releaseApproved','changedFiles','appliedIntervention','evidenceReports'],delimiter=';');writer.writeheader()
 for r in records:
  reports={e['source'] for e in r['applicationEvidence']}|{e['source'] for e in r['sourceLedgerEvidence']}|set(r.get('manualResolution',{}).get('evidence',[]))
  writer.writerow({k:r.get(k,'') for k in writer.fieldnames if k not in ['evidenceReports','changedFiles']}|{'changedFiles':'; '.join(r['changedFiles']),'evidenceReports':'; '.join(sorted(reports))})
md='# Registro di applicazione consolidato — 3 ottobre 2026\n\nRegistro derivato dei 582 ID storici; audit originale e registro iniziale immutati. Gli ID aggiuntivi di produzione sono elencati separatamente. Nessun esito equivale al signoff della collana: servizi digitali e dati editoriali comuni conservano il proprio stato.\n\n'
md+='| Volume | Totale | Stati |\n|---|---|---|\n'+'\n'.join(f'| {v} | {sum(c.values())} | '+', '.join(f'{s}: {n}' for s,n in c.items())+' |' for v,c in pervol.items())
md+='\n\nIdentità: 582 record, zero ID duplicati, mancanti o estranei. Evidenze per ogni ID nel JSON e nel CSV; hash delle fonti nel riepilogo. Gli esiti testo/PDF hanno perimetri distinti e non attestano una nuova rilettura integrale da parte del consolidatore.\n'
md+='\n## Esiti ancora aperti o parziali\n\n| ID | Stato | Evidenza e limite |\n|---|---|---|\n'
for r in records:
 if r['status'] not in ['applicato-verificato-testo','applicato-verificato-pdf']:
  limit=r.get('manualResolution',{}).get('reason') or r.get('appliedIntervention','')
  md+=f"| {r['id']} | {r['status']} | {limit.replace('|','/')} |\n"
md+='\nI 13 ID aggiuntivi sono conservati nel JSON dedicato: sei correzioni di produzione verificate e sette dipendenze comuni aperte (C05-01 e FM06/07/12-01/02). Non vengono sommati ai 582 per colmare presunti mancanti.\n'
md+='\nVerifica dei pacchetti: `artifacts/correzioni-collana-2026-10-02/registro-package-verification.json`. I dodici pacchetti contengono i candidati correnti identificati con hash; VOL-02 comprende due tomi. La verifica di integrità non costituisce una prova fisica né una conferma finale di pubblicazione.\n'
(W/'registro-applicazione-consolidato-2026-10-03.md').write_text(md,encoding='utf8')
assert BASE.read_bytes()==baseline_bytes and AUDIT.read_bytes()==audit_bytes
print(json.dumps(summary,ensure_ascii=False))
