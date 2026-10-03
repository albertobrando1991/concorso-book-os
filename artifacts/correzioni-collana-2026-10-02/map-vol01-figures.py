from pathlib import Path
import json,re,pymupdf,sys
label=sys.argv[1] if len(sys.argv)>1 else 'vol-01-current-20261003'
A=Path(__file__).parent;B=Path('wiki/books/il-metodo-bando');d=pymupdf.open(A/f'{label}-proof.pdf')
metrics=json.loads((A/f'{label}-proof-metrics.json').read_text(encoding='utf8'))
inv=json.loads((A/'VOL-01-structure.json').read_text(encoding='utf8'))
changed=json.loads((A/'figure-vol01-corrette-manifest.json').read_text(encoding='utf8'));changedpaths={Path(x['newAsset']).resolve() for x in changed}
rows=[]
for u in inv['units']:
 p=Path(u['path']);refs=re.findall(r'!\[([^\]]*)\]\(([^)]+)\)',p.read_text(encoding='utf8'))
 pages=[]
 for m in metrics['pages']:
  if (m.get('path') or '').endswith('/'+p.name):
   pages += [m['page']]*len(d[m['page']-1].get_image_info())
 assert len(refs)==len(pages),(p.name,len(refs),pages)
 for (alt,ref),page in zip(refs,pages):
  target=(Path('wiki')/ref if ref.startswith('books/') else p.parent/ref).resolve();isnew=target in changedpaths
  row={'chapter':p.name,'asset':ref,'alt':alt,'page':page,'corrected':isnew};rows.append(row)
  if isnew:d[page-1].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).save(A/f'{label}-corrected-page-{page:03}.png')
assert len([r for r in rows if r['corrected']])==19
(A/'VOL-01-figure-page-map.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps([r for r in rows if r['corrected']],ensure_ascii=False,indent=1))
