from pathlib import Path
import fitz,sys
volume=sys.argv[1]; pages=list(map(int,sys.argv[2:]))
doc=fitz.open(f'delivery/{volume}/candidate/{volume.lower()}-interior-kdp.pdf')
out=Path('artifacts/review-integrale-2026-10-02/pdf/root-details');out.mkdir(exist_ok=True)
for n in pages:
 p=doc[n-1];p.get_pixmap(matrix=fitz.Matrix(1.6,1.6)).save(out/f'{volume}-p{n:04}.png')
 print(n,'fonts',sorted({round(s['size'],2) for b in p.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans']}))
 print(p.get_text()[:450])
