from pathlib import Path
import json,hashlib,re,sys
import pymupdf as fitz
A=Path(__file__).parent;out=A/'publication-refinement-qa';out.mkdir(exist_ok=True)
pkgs=json.loads((A/'registro-package-verification.json').read_text('utf8'))['volumes']
results=[]
for number in sys.argv[1:] or ['01','06','09','10']:
 v=next(v for v in pkgs if v['volume']=='VOL-'+number);e=v['candidatePdfs'][0]
 oldpath=Path(v['manifest']).parent/e['path'];newpath=A/f'vol-{number}-publication-refined-20261003-proof.pdf'
 archived=A/'publication-refinement-before'/f'vol-{number}-interior.pdf'
 if archived.exists():oldpath=archived
 before=fitz.open(oldpath);after=fitz.open(newpath);assert len(before)==len(after),(number,len(before),len(after))
 if number=='01':
  def constitutional_body(d):
   text='\n'.join(p.get_text() for p in d[78:83])
   lines=[l for l in text.splitlines() if l not in ['Il Metodo BANDO','CONTINUA','4. COSTITUZIONE E ORDINAMENTO DELLO STATO'] and not re.fullmatch(r'\d+',l)]
   text='\n'.join(lines).replace('Caso\nTema costituzionale\nRisposta sintetica\n','')
   return re.sub(r'\s+',' ',text).strip()
  assert constitutional_body(before)==constitutional_body(after),'Constitutional content changed beyond pagination and repeated table header'
 changed=[];textChanges=[];low=[];fonts=set();outside=[]
 for i,(p,q) in enumerate(zip(before,after)):
  oldtext=p.get_text();newtext=q.get_text()
  expected=oldtext.replace('Universita,','Università,').replace('UNIVERSITA,','UNIVERSITÀ,').replace('universita,','università,') if number=='06' else oldtext
  if number=='01' and i+1 in [79,80,81,82,83]:pass # Compared as a continuous body above.
  elif number=='01' and i+1==8:assert expected.replace('libertà\n80\n','libertà\n81\n')==newtext
  else:assert expected==newtext,(number,i+1,'Unexpected text difference')
  if oldtext!=newtext:textChanges.append(i+1)
  assert p.rect==q.rect
  if hashlib.sha256(p.get_pixmap().samples).digest()!=hashlib.sha256(q.get_pixmap().samples).digest():
   changed.append(i+1);q.get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(out/f'vol-{number}-page-{i+1:03}.png')
  for im in q.get_image_info():
   rect=fitz.Rect(im['bbox']);dpi=min(im['width']/rect.width,im['height']/rect.height)*72
   if dpi<299.9:low.append(dict(page=i+1,dpi=dpi))
  for word in q.get_text('words'):
   if not (q.rect+(-.1,-.1,.1,.1)).contains(fitz.Rect(word[:4])):outside.append(dict(page=i+1,text=word[4]))
  for font in q.get_fonts():fonts.add((font[0],font[2]))
 unembedded=[]
 for xref,kind in fonts:
  if kind=='Type3':
   k,value=after.xref_get_key(xref,'CharProcs')
   if k=='xref':value=after.xref_object(int(value.split()[0]))
   refs=[int(x) for x in re.findall(r'(\d+)\s+0\s+R',value)]
   if not refs or not all(after.xref_is_stream(x) and after.xref_stream(x) for x in refs):unembedded.append(xref)
  elif not after.extract_font(xref)[3]:unembedded.append(xref)
 assert not low,(number,low)
 assert not outside,(number,outside)
 assert not unembedded,(number,unembedded)
 expectedPages={'01':[8,36,68,79,80,81,82,83,193,221,224,252,279,327,375,389,403,418,436,469,489,529,534,546,550], '06':[2,3,5,8,122,273,429],'09':[240],'10':[123]}[number]
 assert changed==expectedPages,(number,changed)
 result=dict(volume='VOL-'+number,source=oldpath.as_posix(),sourceSha256=hashlib.sha256(oldpath.read_bytes()).hexdigest(),pdf=newpath.as_posix(),pdfSha256=hashlib.sha256(newpath.read_bytes()).hexdigest(),pages=len(after),changedPages=changed,textChangedPages=textChanges,unchangedPagesPixelIdentical=len(after)-len(changed),unembeddedFonts=unembedded,imagesUnder300Ppi=low,textOutsidePage=outside,visualReviewed=False)
 (out/f'VOL-{number}-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf8')
 results.append(result);print(json.dumps(result,ensure_ascii=False),flush=True)
