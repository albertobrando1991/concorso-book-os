from pathlib import Path
import json,re,unicodedata,pymupdf
A=Path(__file__).parent;D=A/'vol01-native';pdf=A/'vol-01-native-final-20261003-proof.pdf';doc=pymupdf.open(pdf)
metrics={'pages':[{'page':i+1,'text':p.get_text()} for i,p in enumerate(doc)]}
inv=json.loads((A/'VOL-01-native-inventory.json').read_text(encoding='utf8'))
def norm(s):return re.sub(r'[^\w]','',unicodedata.normalize('NFKC',s)).lower()
out=D/'final-pdf-pages';out.mkdir(exist_ok=True)
rows=[];selected=set()
for r in inv:
 rep=(D/(r['id']+'.md')).read_text(encoding='utf8').strip();lines=rep.splitlines();anchor=norm(lines[0]);last=norm(lines[-1]);candidates=metrics['pages']
 starts=[p['page'] for p in candidates if anchor in norm(p['text'])]
 if len(starts)>1:
  second=norm(next(x for x in lines[1:] if x.strip()))[:55]
  starts=[p['page'] for p in candidates if p['page'] in starts and second in norm(p['text'])]
 assert len(starts)==1,(r['id'],starts)
 ends=[p['page'] for p in candidates if p['page']>=starts[0] and last[-55:] in norm(p['text'])]
 end=ends[0] if ends else starts[0]+1
 pages=list(range(starts[0],end+1))
 ch=Path('wiki/books/il-metodo-bando/chapters')/r['chapter'];current=ch.read_text(encoding='utf8');tail=current.split(rep,1)[1];cm=re.match(r'\s*\*Schema (\d+\.\d+)',tail)
 captionPages=[p['page'] for p in candidates if re.search(r'Schema '+re.escape(cm.group(1))+r'\b',p['text'])] if cm else []
 pages=sorted(set(pages+captionPages));selected.update(pages)
 rows.append({'id':r['id'],'chapter':r['chapter'],'start':starts[0],'end':end,'endMatched':bool(ends),'captionPages':captionPages,'pages':pages,'visualReview':False})
protected=json.loads((A/'figure-vol01-corrette-manifest.json').read_text(encoding='utf8'));pr=[]
for r in protected:
 before=Path(r['chapters'][0]).read_text(encoding='utf8');m=re.search(r'!\[[^\]]*\]\([^\n]*'+re.escape(Path(r['newAsset']).name)+r'\)\s*\*Figura (\d+\.\d+)',before);assert m,r
 caption=m.group(1);pages=[p['page'] for p in metrics['pages'] if re.search(r'Figura '+re.escape(caption)+r'\b',p['text'])]
 # Caption can be on next page; image page in same chapter immediately preceding.
 for p in list(pages):
  if not doc[p-1].get_images() and p>1 and doc[p-2].get_images():pages.insert(0,p-1)
 selected.update(pages);pr.append({'asset':r['newAsset'],'caption':caption,'pages':pages,'visualReview':False})
extra=[p['page'] for p in metrics['pages'] if norm('Prendi un bando reale e compila questa griglia.') in norm(p['text'])]
for p in extra:selected.update([p,p+1])
for p in sorted(selected):doc[p-1].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5),alpha=False).save(out/f'page-{p:03}.png')
result={'pdf':str(pdf),'pages':len(doc),'native':rows,'protected':pr,'extra':extra,'selectedPages':sorted(selected),'allEndMatched':all(r['endMatched'] for r in rows)}
(A/'VOL-01-native-final-pdf-map.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'pages':len(doc),'native':len(rows),'protected':len(pr),'selectedPages':len(selected),'allEndMatched':result['allEndMatched'],'extra':extra}))
