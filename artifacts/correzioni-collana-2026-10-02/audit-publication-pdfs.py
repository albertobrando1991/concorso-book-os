from pathlib import Path
import json,hashlib,datetime
import pymupdf as fitz
A=Path(__file__).parent
packages=json.loads((A/'registro-package-verification.json').read_text('utf8'))['volumes']
rows=[]
for v in packages:
 for entry in v['candidatePdfs']:
  p=Path(v['manifest']).parent/entry['path'];d=fitz.open(p)
  images=[];unembedded=set();sizes=set();outside=[];checked_fonts=set();type3=[]
  for number,page in enumerate(d,1):
   sizes.add((round(page.rect.width,2),round(page.rect.height,2)))
   for f in page.get_fonts():
    if f[0] in checked_fonts:continue
    checked_fonts.add(f[0])
    if f[2]=='Type3':
     # Type3 glyph programs are embedded in CharProcs, not a FontFile stream.
     import re
     kind,procs=d.xref_get_key(f[0],'CharProcs')
     if kind=='xref':procs=d.xref_object(int(procs.split()[0]))
     refs=[int(x) for x in re.findall(r'(\d+)\s+0\s+R',procs)]
     valid=bool(refs) and all(d.xref_is_stream(x) and bool(d.xref_stream(x)) for x in refs)
     type3.append(dict(xref=f[0],glyphStreams=len(refs),embedded=valid))
     if not valid:unembedded.add(f[0])
    elif not d.extract_font(f[0])[3]:unembedded.add(f[0])
   for im in page.get_image_info():
    box=fitz.Rect(im['bbox'])
    if box.width==0 or box.height==0:continue
    dpi=min(im['width']/box.width*72,im['height']/box.height*72)
    images.append(dict(page=number,width=im['width'],height=im['height'],dpi=round(dpi,2)))
   for word in page.get_text('words'):
    if not (page.rect+(-.1,-.1,.1,.1)).contains(fitz.Rect(word[:4])):outside.append(dict(page=number,text=word[4]))
  rows.append(dict(volume=v['volume'],pdf=p.as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),pages=len(d),pageSizesPt=sorted(sizes),unembeddedFontXrefs=sorted(unembedded),embeddedType3=type3,encrypted=d.is_encrypted,textOutsidePage=outside,imageCount=len(images),imagesUnder300Ppi=[x for x in images if x['dpi']<299.9],images=images))
out=dict(checkedAt=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Physical PDF properties and effective raster resolution; not a new content review or Print Previewer',pdfs=rows)
(A/'publication-pdf-preflight.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps([{k:v for k,v in r.items() if k in ['volume','pages','unembeddedFontXrefs','encrypted','textOutsidePage','imageCount','imagesUnder300Ppi']} for r in rows],ensure_ascii=False))
