from pathlib import Path
import pymupdf,json,hashlib
R=Path(__file__).parent/'vol03-proof'
old=pymupdf.open(R/'before-map-813.pdf');new=pymupdf.open(R/'vol-03-current-proof.pdf')
def pagehash(p):
 return hashlib.sha256(p.get_pixmap(matrix=pymupdf.Matrix(1,1),clip=pymupdf.Rect(0,0,p.rect.width,p.rect.height-50),alpha=False).samples).hexdigest()
oldhash={pagehash(p):p.number+1 for p in old}
rows=[]
for p in new:
 h=pagehash(p);rows.append({'page':p.number+1,'bodyRasterSha256':h,'identicalToViewedPriorPage':oldhash.get(h)})
changed=[r['page'] for r in rows if not r['identicalToViewedPriorPage']]
targets={6,7,8,9,10,11,174,194,258,301,322,340,376,388,410,468,477,478,489,505,506,533,534,535,536,791,792}|set(changed)
for n in targets:
 if n<=len(new):new[n-1].get_pixmap(matrix=pymupdf.Matrix(2,2),alpha=False).save(R/f'final-page-{n:03}.png')
(R/'visual-delta.json').write_text(json.dumps({'priorPdfSha256':hashlib.sha256((R/'before-map-813.pdf').read_bytes()).hexdigest(),'priorPagesViewedIn51ContactSheets':813,'currentPdfSha256':hashlib.sha256((R/'vol-03-current-proof.pdf').read_bytes()).hexdigest(),'method':'Exact raster equality at 72dpi excluding last50pt footer; prior all813pages viewed as contact sheets. Changed pages rendered separately at144dpi. Not full-text proofread at full resolution.','pages':rows,'changedPages':changed,'fullResolutionRendered':sorted(targets)},indent=2),encoding='utf8')
print(json.dumps({'pages':len(new),'unchangedBodies':len(rows)-len(changed),'changedPages':changed,'rendered':sorted(targets)}))
