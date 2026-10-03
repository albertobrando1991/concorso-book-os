from pathlib import Path
import pymupdf,json,hashlib
A=Path(__file__).parent;old=pymupdf.open(A/'vol-01-native-final-20261003-proof.pdf');new=pymupdf.open(A/'vol-01-native-release-20261003-proof.pdf')
selected=json.loads((A/'VOL-01-native-final-pdf-map.json').read_text(encoding='utf8'))['selectedPages']
def digest(page):
 rect=pymupdf.Rect(0,0,page.rect.width,page.rect.height-40)
 return hashlib.sha256(page.get_pixmap(matrix=pymupdf.Matrix(1,1),clip=rect,alpha=False).samples).hexdigest()
oldHashes={digest(old[p-1]):p for p in selected}
rows=[]
for i,p in enumerate(new):
 h=digest(p);rows.append({'page':i+1,'renderSHA256':h,'matchesReviewedPage':oldHashes.get(h)})
out={'previous':str(old.name),'current':str(new.name),'previousPages':len(old),'currentPages':len(new),'method':'Rendering PyMuPDF 72 dpi, pagina esclusi i 40 pt inferiori del piè di pagina; confronto SHA-256 dei pixel. Nessuna manipolazione degli asset.','pages':rows}
(A/'VOL-01-native-release-render-comparison.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'pages':len(new),'matchingReviewedPages':sum(bool(r['matchesReviewedPage']) for r in rows)}))
