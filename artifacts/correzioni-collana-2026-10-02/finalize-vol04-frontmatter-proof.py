from pathlib import Path
import json,re,hashlib,unicodedata,pymupdf
A=Path(__file__).parent;R=A/'vol04-proof'
def load(p):return json.loads(p.read_text(encoding='utf8'))
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf8')
v=load(R/'frontmatter-proof-verification.json');m=load(A/'vol-04-reader-final-20261003-proof-metrics.json');payload=load(R/'payload-frontmatter.json');doc=pymupdf.open(A/'vol-04-reader-final-20261003-proof.pdf')
def norm(s):return ' '.join(unicodedata.normalize('NFKC',s).split()).casefold()
idx=next(c for c in payload['chapters'] if c.get('frontMatterLayout')=='analytical-index');rows=[l.strip() for p in m['pages'] if p['path']==idx['path'] for l in p['text'].splitlines() if l.strip()];checks=[]
for block in idx['blocks']:
    if block['type']!='index-chapter':continue
    positions=[i for i,l in enumerate(rows) if norm(l)==norm(block['text']) and i and norm(rows[i-1])==norm(block['number'])]
    printed=int(rows[positions[0]+1]) if len(positions)==1 and rows[positions[0]+1].isdigit() else None
    actual=next(p['page'] for p in m['pages'] if p['path']==block['path'])
    checks.append({'number':block['number'],'title':block['text'],'printed':printed,'actual':actual,'match':printed==actual,'pdfTargetPresent':bool(printed and norm(block['text']) in norm(doc[printed-1].get_text()))})
assert len(checks)==17 and all(r['match'] and r['pdfTargetPresent'] for r in checks)
contacts=load(R/'contact-ledger.json')
for r in contacts:r['viewed']=True;r['scope']='Panorama geometrico: margini, tabelle, titoli, interruzioni, densità; non rilettura del testo minuto.'
save(R/'contact-ledger.json',contacts)
details=[1,3,6,38,109,110,112,114,115,116,130,131,132,136,354,356,367]
ledger={'volume':'VOL-04','pdf':'artifacts/correzioni-collana-2026-10-02/vol-04-reader-final-20261003-proof.pdf','pdfSha256':v['pdfSha256'],'pages':367,'allContactSheetsViewed':True,'contactSheets':23,'allPagesVisuallyCovered':True,'contactPageCoverage':list(range(1,368)),'fullResolutionPagesViewed':details,'sourceHashMismatches':v['sourceHashMismatches'],'indexChecks':checks,'overflowPages':v['overflowPages'],'missingImages':v['missingImages'],'literalBr':v['literalBr'],'projectionScope':'FM1 and FM3 only: title, path and blocks. All other 22 payload chapters identical to current API. No source or renderer modifications.','comparison':'Baseline 369 pages; two repetitive closing tails condensed by parent, plus chapter 15 spacing corrections. Pixel comparison is indicative only because parity swaps margins and changes text rounding. Final 367-page panorama reviewed independently.','findings':['FM1/FM3 present, titled correctly and each on one page; no unverified included-service promise remains in FM1.','Former isolated closing tails fit pages 38 and 136.','Reflow of quiz at 109–112 and continued tables at 114–116 and 130–132 checked in detail, no overlap or clipping.','Corrected numeric spacing in chapter 15 visible on 354 and 356.'],'limitations':['No new integral legal or textual review.','Small text on contact sheets not read in full; details limited to declared 17 pages.','Chapter closures retain white space, for example 112 and 342; no removal of legitimate content or font reduction.','Commercial metadata, ISBN, cover, physical print and KDP upload outside this task.'],'parentHandoff':'Root handles reports, package and pipeline; no further edits by this agent.'}
save(R/'visual-review.json',ledger)
v['visualReviewPending']=[];v['visualReviewScope']='All 367 pages in 23 contact sheets plus 17 declared detail pages. See visual-review.json.';save(R/'frontmatter-proof-verification.json',v)
print(json.dumps({'pages':len(doc),'pdfSha256':v['pdfSha256'],'contactsViewed':23,'detailsViewed':len(details),'indexChecks':len(checks)}))
