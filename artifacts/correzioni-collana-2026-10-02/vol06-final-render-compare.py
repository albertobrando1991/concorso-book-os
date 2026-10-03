from pathlib import Path
import json,hashlib,pymupdf
A=Path(__file__).parent
old=pymupdf.open(A/'vol-06-print-20261003-proof.pdf');new=pymupdf.open(A/'vol-06-final-20261003-proof.pdf')
def digest(p):
    return hashlib.sha256(p.get_pixmap(matrix=pymupdf.Matrix(1,1),clip=pymupdf.Rect(0,0,p.rect.width,p.rect.height-40),alpha=False).samples).hexdigest()
previous={digest(p):i+1 for i,p in enumerate(old)}
rows=[{'page':i+1,'matchesReviewedPage':previous.get(digest(p))} for i,p in enumerate(new)]
out={'previousPDF':str(old.name),'currentPDF':str(new.name),'method':'Confronto SHA-256 dei pixel PyMuPDF a 72 dpi, esclusi i 40 pt inferiori del piè di pagina. Le pagine precedenti sono state tutte viste in panoramica, non tutte ingrandite.','pages':rows}
(A/'VOL-06-final-render-comparison.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'matching':sum(bool(r['matchesReviewedPage']) for r in rows),'changed':[r['page'] for r in rows if not r['matchesReviewedPage']]}))
