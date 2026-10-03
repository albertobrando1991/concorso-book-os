from pathlib import Path
import pymupdf,hashlib,json
A=Path(__file__).parent;old=pymupdf.open(A/'vol-10-release-20261003-proof.pdf');new=pymupdf.open(A/'vol-10-final-20261003-proof.pdf');out=A/'vol-10-final-20261003-proof-audit';out.mkdir(exist_ok=True);rows=[]
assert len(old)==len(new)
for i in range(len(new)):
 a=hashlib.sha256(old[i].get_pixmap(matrix=pymupdf.Matrix(1.8,1.8),alpha=False).samples).hexdigest();pix=new[i].get_pixmap(matrix=pymupdf.Matrix(1.8,1.8),alpha=False);b=hashlib.sha256(pix.samples).hexdigest();rows.append({'page':i+1,'oldRasterSha256':a,'newRasterSha256':b,'identical':a==b})
 if a!=b:pix.save(out/f'zoom-{i+1:03}.png')
r={'oldPages':len(old),'newPages':len(new),'renderScale':1.8,'changedPages':[r['page'] for r in rows if not r['identical']],'pages':rows};(A/'VOL-10-final-render-comparison.json').write_text(json.dumps(r,indent=2),encoding='utf8');print(json.dumps({k:v for k,v in r.items() if k!='pages'}))
