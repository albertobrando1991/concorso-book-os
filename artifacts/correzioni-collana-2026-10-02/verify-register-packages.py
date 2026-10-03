"""Read-only integrity check for the 12 current candidate packages."""
from pathlib import Path
import json,hashlib,datetime
A=Path(__file__).parent
results=[]
for number in range(1,13):
    vol=f'VOL-{number:02}'
    root=Path('delivery')/vol/('candidate-tomi-2026-10-03' if number==2 else 'candidate-2026-10-03')
    manifest=next((p for p in [root/'package-manifest.json',root/'manifest.json'] if p.exists()),None)
    if not manifest:
        results.append({'volume':vol,'status':'awaiting-package','root':root.as_posix()})
        continue
    data=json.loads(manifest.read_text(encoding='utf-8-sig'))
    errors=[]
    files=data['files']
    for entry in files:
        path=root/entry['path']
        if not path.resolve().is_relative_to(root.resolve()):
            errors.append({'path':entry['path'],'error':'outside-package'});continue
        if not path.is_file():
            errors.append({'path':entry['path'],'error':'missing'});continue
        raw=path.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=entry['sha256']:
            errors.append({'path':entry['path'],'error':'hash-mismatch'})
        if 'bytes' in entry and len(raw)!=entry['bytes']:
            errors.append({'path':entry['path'],'error':'size-mismatch'})
    expected=[t['sha256'] for t in data['tomes']] if 'tomes' in data else [data['pdfSha256']]
    pdfs=[e for e in files if e['path'].lower().endswith('.pdf') and e['sha256'] in expected]
    if set(e['sha256'] for e in pdfs)!=set(expected):
        errors.append({'error':'candidate-pdf-not-in-manifest'})
    results.append({'volume':vol,'status':'verified' if not errors else 'integrity-errors',
        'manifest':manifest.as_posix(),'manifestSha256':hashlib.sha256(manifest.read_bytes()).hexdigest(),
        'fileCount':len(files),'errors':errors,'candidatePdfs':pdfs,'releaseApproved':False})
summary={'verifiedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'all12PackagesVerified':len(results)==12 and all(r['status']=='verified' for r in results),
    'volumes':results,'scope':'Package file hashes and declared candidate identity only; no publication approval or new textual/visual review.'}
(A/'registro-package-verification.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'all12PackagesVerified':summary['all12PackagesVerified'],'volumes':[{k:v for k,v in r.items() if k in ['volume','status','fileCount','errors']} for r in results]},ensure_ascii=False))
