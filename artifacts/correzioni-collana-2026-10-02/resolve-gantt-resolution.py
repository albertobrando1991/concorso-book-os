from pathlib import Path
import json,hashlib,shutil
import pymupdf as fitz
A=Path(__file__).parent
asset=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/assets/correzioni-2026-10/gantt-sportello-digitale.png')
pdf=asset.with_suffix('.pdf')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before=sha(asset);backup=A/'gantt-before-publication-300ppi.png'
if not backup.exists():shutil.copy2(asset,backup)
d=fitz.open(pdf);assert len(d[0].get_images())==0 and len(d[0].get_drawings())==17
d[0].get_pixmap(matrix=fitz.Matrix(3,3),alpha=False).save(asset)
after=sha(asset)
freeze=A/'M-TR02-freeze.json';f=json.loads(freeze.read_text('utf8'))
for e in f['files']:
 if e['path']==asset.as_posix():
  assert e['sha256'] in [before,after]
  e['sha256']=after
f['controlledAssetResolution']={'date':'2026-10-03','asset':asset.as_posix(),'before':before,'after':after,'vectorSource':pdf.as_posix(),'vectorSourceSha256':sha(pdf),'pixels':[1950,1410],'reason':'Rerender from vector PDF; no interpolation of old bitmap. Text, data and size in layout unchanged.'}
freeze.write_text(json.dumps(f,ensure_ascii=False,indent=2)+'\n','utf8')
(A/'VOL-09-publication-gantt-resolution.json').write_text(json.dumps(f['controlledAssetResolution'],ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps(f['controlledAssetResolution']))
