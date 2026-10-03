from pathlib import Path
import pymupdf,json,hashlib,shutil
A=Path(__file__).parent;B=Path('wiki/books/moduli/m-tr03-tecnico-ingegneristico/assets/correzioni-2026-10');backup=A/'vol10-assets-before-production';backup.mkdir(exist_ok=True);rows=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['vincoli-piani','trave-carico-taglio-momento','planimetria-sopralluogo']:
 source=B/(name+'.pdf');target=B/(name+'.png');doc=pymupdf.open(source);page=doc[0];assert not page.get_images() and len(page.get_drawings())>0
 old=sha(target);shutil.copy2(target,backup/target.name);pix=page.get_pixmap(matrix=pymupdf.Matrix(3,3),alpha=False);pix.save(target)
 rows.append({'source':source.as_posix(),'sourceSha256':sha(source),'target':target.as_posix(),'beforeSha256':old,'afterSha256':sha(target),'drawingPaths':len(page.get_drawings()),'rasterImagesInSource':0,'width':pix.width,'height':pix.height,'printedWidthPt':378,'effectivePpi':pix.width*72/378,'method':'Rendering della pagina PDF vettoriale a scala3; nessuna modifica della composizione né upscaling di bitmap.'})
(A/'VOL-10-vector-render-delta.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(rows,ensure_ascii=False))
