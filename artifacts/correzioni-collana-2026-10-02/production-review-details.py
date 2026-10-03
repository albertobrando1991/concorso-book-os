from pathlib import Path
import json, hashlib, sys
import pymupdf
A=Path(__file__).parent
label=sys.argv[1]
doc=pymupdf.open(A/(label+'-proof.pdf'))
out=A/(label+'-details');out.mkdir(exist_ok=True)
pages=[int(n) for n in sys.argv[2].split(',')]
for n in pages:
    doc[n-1].get_pixmap(matrix=pymupdf.Matrix(1.65,1.65),alpha=False).save(out/f'page-{n:03}.png')
print(json.dumps({'directory':str(out),'pages':pages}))
