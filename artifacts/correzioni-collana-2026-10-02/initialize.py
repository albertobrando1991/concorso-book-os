from pathlib import Path
import json,hashlib,zipfile

base=Path('artifacts/correzioni-collana-2026-10-02')
reports=Path('wiki/reviews/correzioni-collana-2026-10-02')
reports.mkdir(parents=True,exist_ok=True)
audit=Path('artifacts/review-integrale-2026-10-02')
actions=json.loads((audit/'action-register.json').read_text(encoding='utf8'))
register=base/'registro-applicazione.json'
if not register.exists():
    for a in actions:
        a['auditStatus']=a.pop('status')
        a['status']='da-applicare'
        a['changedFiles']=[]
        a['verification']=[]
    register.write_text(json.dumps(actions,ensure_ascii=False,indent=2),encoding='utf8')
snapshot=base/'manoscritti-prima.zip'
if not snapshot.exists():
    rows=json.loads((audit/'complete-chapter-register.json').read_text(encoding='utf8'))
    records=[]
    with zipfile.ZipFile(snapshot,'x',zipfile.ZIP_DEFLATED) as z:
        for row in rows:
            p=Path(row['file']); data=p.read_bytes(); sha=hashlib.sha256(data).hexdigest()
            z.writestr(str(p),data)
            records.append({'file':str(p),'sha256':sha,'matchesAudit':sha==row['sha256']})
    (base/'baseline.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf8')
    print('Snapshot:',len(records),'files; audit mismatches:',sum(not r['matchesAudit'] for r in records))
print('Tracking:',len(actions),'findings; no source corrections performed by initialization')
