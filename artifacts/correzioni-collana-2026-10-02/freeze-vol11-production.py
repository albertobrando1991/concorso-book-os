from pathlib import Path
import json,hashlib
A=Path(__file__).parent;f=A/'M-TR04-freeze.json';d=json.loads(f.read_text(encoding='utf8'));delta=json.loads((A/'VOL-11-production-delta.json').read_text(encoding='utf8'));by={x['path']:x for x in delta};changes=[]
for r in d['files']:
 current=hashlib.sha256(Path(r['path']).read_bytes()).hexdigest()
 if current!=r['sha256']:
  x=by[Path(r['path']).as_posix()];assert r['sha256']==x['beforeSha256'] and current==x['afterSha256'];r['sha256']=current;changes.append(x)
assert len(changes)==4
d.setdefault('controlledLayoutCorrections',[]).append({'date':'2026-10-03','note':'P11-01, P11-02, P11-06: intestazione, metadati audit e conversione kg/t. Gate14 e15 passati; formula ricalcolata; norme e fonti immutate.','files':changes})
f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
p=Path('wiki/reviews/pipeline/VOL-11/16-moduli-m-tr04-ambiente-protezione-civile.md');t=p.read_text(encoding='utf8')
for x in changes:
 assert x['beforeSha256'] in t;t=t.replace(x['beforeSha256'],x['afterSha256'])
t+='\n\nDelta produzione del 3 ottobre 2026: quattro file modificati come nel manifest VOL-11-production-delta.json; tutti gli altri hash del freeze immutati. Correzioni rilette, formula kg/t ricalcolata, metadati audit estratti correttamente dal prompt15 con fonte/versione/data/posizione. Gate14 e15 passati senza warning. Nuovo PDF ancora da verificare.\n';p.write_text(t,encoding='utf8')
p=Path('wiki/reviews/pipeline/VOL-11/15-moduli-m-tr04-ambiente-protezione-civile.md')
with p.open('a',encoding='utf8') as out:out.write('\n\n| Dato operativo migrato | Evidenza conservata | Esito del delta |\n|---|---|---|\n| DO-TR04-11-IT-ALERT-2026-08-17 | sources/vol-11-protezione-civile-verifica-2026-10-03; fonte e stato nazionale del3ottobre già consolidati | Nessuna modifica al dato; ID sottratto alla pagina pubblica e rilevato nel prompt15 da frontmatter strutturato |\n| DO-TR04-12-CLIMA-2026-08-18 | sources/vol-11-energia-sostenibilita-verifica-2026-10-03; regolamenti2021/1119 e2026/667 già verificati | Nessuna modifica al dato; preservati fonte, ambito, versione e data, oltre alla posizione nel corpo |\n')
print(json.dumps({'filesVerified':len(d['files']),'controlledDeltas':len(changes)}))
