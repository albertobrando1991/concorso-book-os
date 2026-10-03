from pathlib import Path
import hashlib,json,shutil
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-tr04-ambiente-protezione-civile');D=A/'before-text/VOL-11';D.mkdir(parents=True,exist_ok=True)
old=json.loads(Path('artifacts/review-integrale-2026-10-02/VOL-11-ledger.json').read_text(encoding='utf8'));oldhash={r['path']:r['sha256'] for r in old['chapters']+old['supportFiles']}
paths=sorted((B/'chapters').glob('*.md'))+[B/'index.md',B/'planning/01-indice-analitico-vol-11.md',B/'planning/02-matrice-copertura-didattica.md',B/'planning/17-bibbia-del-modulo.md'];rows=[]
for p in paths:
 h=hashlib.sha256(p.read_bytes()).hexdigest();rows.append({'path':p.as_posix(),'sha256':h,'auditReadComplete':p.as_posix() in oldhash,'unchangedSinceIntegralAudit':oldhash.get(p.as_posix())==h});target=D/p.name
 if not target.exists():shutil.copy2(p,target)
(A/'VOL-11-baseline.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
s=(A/'recall-vol10.ts').read_text(encoding='utf8').replace('VOL-10 NTC edilizia urbanistica esecuzione collaudo strutture BIM catasto','VOL-11 ambiente protezione civile sostenibilità energia rifiuti VIA AIA AUA acque CAM DNSH');(A/'recall-vol11.ts').write_text(s,encoding='utf8')
print('Baseline:',len(rows),'files; changes since audit:',[r['path'] for r in rows if not r['unchangedSinceIntegralAudit']])
