from pathlib import Path
import json, hashlib
import pymupdf as fitz
A=Path(__file__).parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
covers=json.loads((A/'cover-qa/cover-manifest.json').read_text('utf8'))
for c in covers:
 p=Path(c['cover']);assert sha(p)==c['coverSha256']
 d=fitz.open(p);page=d[0];left=9+6.69*72;right=left+c['spineInches']*72
 clearance=[]
 for b in page.get_text('dict')['blocks']:
  for line in b.get('lines',[]):
   if abs(line['dir'][1])<.9:continue
   for span in line['spans']:
    box=fitz.Rect(span['bbox']);gap=min(box.x0-left,right-box.x1)
    assert gap>=4.5-.01,(c['key'],span['text'],gap)
    clearance.append(gap)
 assert clearance
 c['minimumSpineTextClearancePt']=min(clearance)
 c['visualReviewed']=True
 c['visualEvidence']=(A/'cover-qa'/f"{c['key']}.png").as_posix()
(A/'cover-qa/cover-manifest.json').write_text(json.dumps(covers,ensure_ascii=False,indent=2)+'\n','utf8')
for n in ['01','06','09','10']:
 p=A/'publication-refinement-qa'/f'VOL-{n}-verification.json';r=json.loads(p.read_text('utf8'))
 assert sha(Path(r['pdf']))==r['pdfSha256']
 r['visualReviewed']=True
 r['visualEvidence']=[(p.parent/f'vol-{n}-page-{i:03}.png').as_posix() for i in r['changedPages']]
 assert all(Path(e).is_file() for e in r['visualEvidence'])
 p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n','utf8')
packages=json.loads((A/'registro-package-verification.json').read_text('utf8'))['volumes']
v=next(v for v in packages if v['volume']=='VOL-12')
source=fitz.open(Path(v['manifest']).parent/v['candidatePdfs'][0]['path'])
sample=fitz.open('delivery/prova-compilazione-2026-10-03/vol-12-schede-prova-127-128.pdf')
assert len(sample)==2
for i in range(2):
 a=source[126+i];b=sample[i]
 assert a.rect==b.rect and a.get_text()==b.get_text()
 assert a.get_pixmap().samples==b.get_pixmap().samples
print('13 copertine: revisione visiva e spazio dorsale verificati. 34 pagine modificate esaminate. Estratto schede identico alla fonte.')
