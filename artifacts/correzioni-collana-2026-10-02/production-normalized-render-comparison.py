from pathlib import Path
import sys,json,hashlib,pymupdf
A=Path(__file__).parent;oldlabel,newlabel=sys.argv[1:3];old=pymupdf.open(A/(oldlabel+'-proof.pdf'));new=pymupdf.open(A/(newlabel+'-proof.pdf'))
def digest(p):
    # Mirrored binding margins differ by 28.34765625 pt. Normalize only this
    # rigid horizontal translation during PDF rasterization, never edit assets.
    left=65.19140625 if (p.number+1)%2 else 36.84375
    rect=pymupdf.Rect(left-2,0,left+382,p.rect.height-50)
    matrix=pymupdf.Matrix(1,1).pretranslate(-left+2,0)
    pix=p.get_pixmap(matrix=matrix,clip=rect,alpha=False)
    return hashlib.sha256(pix.samples).hexdigest()
previous={digest(p):i+1 for i,p in enumerate(old) if i>=12}
rows=[{'page':i+1,'matchesReviewedPage':previous.get(digest(p)) if i>=12 else None} for i,p in enumerate(new)]
result={'previousPDF':str(old.name),'currentPDF':str(new.name),'method':'Rendering PDF PyMuPDF a 72 dpi con sola traslazione orizzontale dei margini speculari, area contenuti larga 384 pt, esclusi 50 pt del piè di pagina. SHA-256 pixel esatto; nessuna modifica degli asset. Prime 12 pagine escluse dal riuso. Margini e geometria della pagina verificati separatamente.','pages':rows}
(A/(newlabel+'-normalized-render-comparison.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'matching':sum(bool(r['matchesReviewedPage']) for r in rows),'unmatched':[r['page'] for r in rows if not r['matchesReviewedPage']]}))
