from pathlib import Path
import sys,json,hashlib,pymupdf
A=Path(__file__).parent;oldlabel,newlabel=sys.argv[1:3];old=pymupdf.open(A/(oldlabel+'-proof.pdf'));new=pymupdf.open(A/(newlabel+'-proof.pdf'))
limit=int(sys.argv[3]) if len(sys.argv)>3 else len(old)
def digest(p):return hashlib.sha256(p.get_pixmap(matrix=pymupdf.Matrix(1,1),clip=pymupdf.Rect(0,0,p.rect.width,p.rect.height-40),alpha=False).samples).hexdigest()
previous={digest(p):i+1 for i,p in enumerate(old) if i<limit}
rows=[{'page':i+1,'matchesReviewedPage':previous.get(digest(p))} for i,p in enumerate(new)]
result={'previousPDF':str(old.name),'currentPDF':str(new.name),'previousPanoramaPages':[1,limit],'method':'Confronto pixel SHA-256, PyMuPDF 72 dpi, esclusi 40 pt inferiori del piè di pagina. Il confronto trasferisce soltanto il grado di revisione documentato per le pagine precedenti.','pages':rows}
(A/(newlabel+'-render-comparison.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'matching':sum(bool(r['matchesReviewedPage']) for r in rows),'unmatched':[r['page'] for r in rows if not r['matchesReviewedPage']]}))
