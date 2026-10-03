from pathlib import Path
from collections import Counter
import csv,json,hashlib,datetime
A=Path(__file__).parent
W=Path('wiki/reviews/correzioni-collana-2026-10-02')
load=lambda p:json.loads(p.read_text('utf-8-sig'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=load(A/'registro-applicazione-consolidato-2026-10-03.json')
summary=load(A/'registro-applicazione-consolidato-summary.json')
inventory=load(A/'registro-evidence-inventory.json')
packages=load(A/'registro-package-verification.json')
csvrows=list(csv.DictReader((W/'registro-applicazione-consolidato-2026-10-03.csv').read_text('utf-8-sig').splitlines(),delimiter=';'))
assert len(rows)==582 and len({r['id'] for r in rows})==582
assert Counter(r['status'] for r in rows)==Counter(summary['statusCounts'])
assert [(r['id'],r['status']) for r in rows]==[(r['id'],r['status']) for r in csvrows]
mismatches=[]
for entry in inventory['sources']:
 if sha(Path(entry['path']))!=entry['sha256']:mismatches.append(entry['path'])
for r in rows:
 for e in r['applicationEvidence']+r['sourceLedgerEvidence']:
  if sha(Path(e['source']))!=e['sourceSha256']:mismatches.append(e['source'])
assert not mismatches,mismatches
assert sha(Path(inventory['baselinePath']))==summary['baselineSha256']
assert sha(Path(inventory['auditPath']))==summary['auditSha256']
assert packages['all12PackagesVerified']
for volume in packages['volumes']:
 assert sha(Path(volume['manifest']))==volume['manifestSha256']
result=dict(verifiedAt=datetime.datetime.now(datetime.timezone.utc).isoformat(),records=len(rows),verified=sum(r['status'].startswith('applicato-verificato-') for r in rows),openOrPartial=[{'id':r['id'],'status':r['status']} for r in rows if not r['status'].startswith('applicato-verificato-')],csvAligned=True,evidenceHashMismatches=mismatches,packageFiles=sum(v['fileCount'] for v in packages['volumes']),all12PackagesVerified=True,originalAuditUnchanged=True,originalApplicationRegisterUnchanged=True,releaseApproved=False)
(A/'registro-consolidato-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps(result,ensure_ascii=False))
