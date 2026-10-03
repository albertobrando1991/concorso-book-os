from pathlib import Path
import json,re,hashlib,unicodedata,pymupdf
from PIL import Image,ImageDraw
A=Path(__file__).parent;R=A/'vol05-proof';label='vol-05-candidate-20261003'
def norm(s):return ' '.join(unicodedata.normalize('NFKC',s).split()).casefold()
payload=json.loads((R/'payload.json').read_text(encoding='utf8'));m=json.loads((A/f'{label}-proof-metrics.json').read_text(encoding='utf8'))
idx=next(c for c in payload['chapters'] if c.get('frontMatterLayout')=='analytical-index')
lines=[l.strip() for p in m['pages'] if p['path']==idx['path'] for l in p['text'].splitlines() if l.strip()]
checks=[];pdf=A/f'{label}-proof.pdf';doc=pymupdf.open(pdf);pdftexts=[p.get_text() for p in doc]
indexPdf=norm(' '.join(pdftexts[p['page']-1] for p in m['pages'] if p['path']==idx['path']))
for b in idx['blocks']:
 if b['type'] not in ('index-chapter','index-row'):continue
 pos=[i for i,l in enumerate(lines) if norm(l)==norm(b['text']) and i and norm(lines[i-1])==norm(b['number'])]
 printed=int(lines[pos[0]+1]) if len(pos)==1 and lines[pos[0]+1].isdigit() else None
 pages=[p for p in m['pages'] if p['path']==b['path']]
 if b['type']=='index-chapter':actual=pages[0]['page']
 else:
  targets=[p['page'] for p in pages if norm(b['text']) in norm(p['text']) and re.search(r'(?<!\d)'+re.escape(b['number'])+r'(?!\d)',p['text'])];actual=targets[0] if targets else None
 checks.append({'number':b['number'],'title':b['text'],'printed':printed,'actual':actual,'match':printed is not None and printed==actual,'pdfIndexMatch':printed is not None and norm(b['number']+' '+b['text']+' '+str(printed)) in indexPdf,'pdfTargetTitlePresent':bool(printed and norm(b['text']) in norm(pdftexts[printed-1]))})
fontchecks=[]
for xref in sorted({f[0] for p in doc for f in p.get_fonts()}):
 name,ext,kind,data=doc.extract_font(xref);cp=doc.xref_get_key(xref,'CharProcs');fontchecks.append({'xref':xref,'name':name,'kind':kind,'embedded':bool(data) or (kind=='Type3' and cp[0] not in ('null','none'))})
sources=[{'path':'wiki/'+c['path'],'sha256':hashlib.sha256(Path('wiki/'+c['path']).read_bytes()).hexdigest()} for c in payload['chapters'] if c['sectionType']=='chapter']
records=json.loads((A/'VOL-05-native-schemes.json').read_text(encoding='utf8'))['records'];schemes=[]
for r in records:
 title=r['nativeText'].splitlines()[0].removeprefix('#### ');found=[i+1 for i,t in enumerate(pdftexts) if norm(title) in norm(t)]
 schemes.append({'schema':r['schema'],'title':title,'pages':found})
text='\n'.join(pdftexts);outside=[];small=[];sizes={};short=[]
for i,p in enumerate(doc):
 body=[]
 for b in p.get_text('dict')['blocks']:
  for l in b.get('lines',[]):
   for s in l['spans']:
    sz=round(s['size'],2);sizes[(s['font'],sz)]=sizes.get((s['font'],sz),0)+len(s['text'])
    x0,y0,x1,y1=s['bbox']
    if x0<0 or y0<0 or x1>p.rect.width+0.5 or y1>p.rect.height+0.5:outside.append({'page':i+1,'text':s['text'],'bbox':s['bbox']})
    if 60<y0<620:body.append(s['text'])
    if sz<9.45 and s['text'].strip():small.append({'page':i+1,'size':sz,'font':s['font'],'text':s['text'][:80]})
 if len(' '.join(body).split())<40:short.append({'page':i+1,'words':len(' '.join(body).split()),'text':' '.join(body)[:220]})
v={'pdfSha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':len(doc),'domPages':m['pageCount'],'domPdfPageCountMatch':len(doc)==m['pageCount'],'trimPt':[doc[0].rect.width,doc[0].rect.height],'mainChapters':len(sources),'indexEntries':checks,'indexMismatches':[c for c in checks if not c['match'] or not c['pdfIndexMatch'] or not c['pdfTargetTitlePresent']],'fonts':fontchecks,'fontSizes':[{'font':f,'pt':sz,'characters':n} for (f,sz),n in sorted(sizes.items())],'smallText':small,'outsidePage':outside,'shortPages':short,'overflowPages':[p['page'] for p in m['pages'] if p['overflows']],'internalLeaks':re.findall(r'wiki/(?:sources|topics|books)|\[\[|source_refs|review_required|@@LINK',text),'literalBr':m['literalBr'],'sourceHashes':sources,'nativeSchemes':schemes,'missingImages':m['missingImages'],'rasterImageCount':sum(len(p.get_images()) for p in doc),'indexMinimumPt':m['indexMinimumPt'],'limitations':['Full contact-sheet review and targeted detail are recorded separately.','No physical print proof, KDP upload, ISBN or digital-service verification.']}
(R/'verification.json').write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf8')
out=R/'contacts';out.mkdir(exist_ok=True);sheets=[]
for start in range(0,len(doc),16):
 sheet=Image.new('RGB',(1280,1904),'#cccccc');draw=ImageDraw.Draw(sheet)
 for j in range(min(16,len(doc)-start)):
  p=doc[start+j];pix=p.get_pixmap(matrix=pymupdf.Matrix(0.6,0.6));im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((310,447));x=(j%4)*320;y=(j//4)*476;sheet.paste(im,(x+5,y+24));draw.text((x+8,y+6),f'PDF p. {start+j+1}',fill='black')
 fn=f'contact-{start//16+1:02}.jpg';sheet.save(out/fn,quality=90);sheets.append({'file':fn,'pages':list(range(start+1,min(start+16,len(doc))+1)),'viewed':False})
(R/'contact-ledger.json').write_text(json.dumps(sheets,indent=2),encoding='utf8')
print(json.dumps({k:v[k] for k in ['pages','domPages','indexMismatches','outsidePage','shortPages','overflowPages','internalLeaks']},ensure_ascii=False))
print('Schemes:',len(schemes),'missing:',[s['schema'] for s in schemes if len(s['pages'])!=1],'font embedded:',all(f['embedded'] for f in fontchecks))
