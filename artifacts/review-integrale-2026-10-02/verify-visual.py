from pathlib import Path
import json, hashlib

base = Path('artifacts/review-integrale-2026-10-02')
reports = Path('wiki/reviews/audit-integrale-2026-10-02')
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
inventory = read(base/'pdf/inventory.json')
selected = [p for p in inventory if not (p['volume']=='VOL-02' and 'rebuild' not in p['file'])]
roots = {r['volume']: r for r in read(base/'pdf/root-visual-review.json')}
problems = []
pdf_records = []
for p in selected:
    volume = p['volume']
    if digest(Path(p['file'])) != p['sha256']:
        problems.append(volume+': PDF changed')
    if volume in roots:
        r = roots[volume]
        complete = r['panoramicCoverage'].startswith('all ')
        details = r['detailPages']
    elif volume in ['VOL-02','VOL-04','VOL-05']:
        r = read(base/(volume+'-ledger.json'))['pdfReview']
        complete = r['allContactSheetsViewed']
        details = r['zoomPages']
    else:
        ledger = base/('PDF-'+volume+'-ledger.json')
        if not ledger.exists():
            problems.append(volume+': visual ledger absent')
            continue
        r = read(ledger)
        complete = r['contactCoverageComplete']
        details = r['detailPagesViewed']
    if r['pages'] != p['pages'] or not complete:
        problems.append(volume+': incomplete visual coverage')
    if not (reports/('PDF-'+volume+'.md')).exists():
        problems.append(volume+': visual report absent')
    pdf_records.append({'volume': volume, 'file':p['file'], 'sha256':p['sha256'], 'pages':p['pages'], 'allPagesPanorama':complete, 'detailPages':details})

figures = []
for folder in ['figures','figures-VOL-02','figures-VOL-03','figures-VOL-05']:
    for f in read(base/folder/'visual-review.json'):
        if not f.get('visuallyInspected') or digest(Path(f['file'])) != f['sha256']:
            problems.append('Figure incomplete or changed: '+f['file'])
        figures.append({'file':f['file'], 'sha256':f['sha256'], 'visuallyInspected':f['visuallyInspected']})
if len(figures)!=308 or len(set(f['file'] for f in figures))!=308:
    problems.append('Figure count or uniqueness mismatch')
if len(pdf_records)!=12 or sum(p['pages'] for p in pdf_records)!=4861:
    problems.append('PDF count or page count mismatch')
result = {'complete':not problems,'pdfCount':len(pdf_records),'panoramaPages':sum(p['pages'] for p in pdf_records),'figures':len(figures),'pdfs':pdf_records,'figureRecords':figures,'problems':problems,'limitations':'Panorama of all PDF pages plus selected details; no full-size second proofreading or physical print. All figures inspected; QR service not tested.'}
(base/'visual-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k not in ['pdfs','figureRecords']},ensure_ascii=False,indent=2))
if problems: raise SystemExit(1)
