from pathlib import Path
import json,xml.etree.ElementTree as ET,re,hashlib
A=Path(__file__).parent;B=Path('wiki/books/il-metodo-bando');ns='{http://www.w3.org/2000/svg}'
allrows=json.loads((A/'VOL-01-figure-page-map.json').read_text(encoding='utf8'))
excluded=json.loads((A/'figure-vol01-corrette-manifest.json').read_text(encoding='utf8'))
ex={Path(x['newAsset']).resolve() for x in excluded};rows=[]
for i,r in enumerate(allrows):
 p=B/'chapters'/r['chapter'];asset=(p.parent/r['asset']).resolve()
 if asset in ex:continue
 assert not r['corrected'] and '-stampa.' not in asset.name
 svg=asset.with_suffix('.svg');text=p.read_text(encoding='utf8');target=f"![{r['alt']}]({r['asset']})";pos=text.index(target)
 row={**r,'id':f'F{len(rows)+1:03}','path':asset.relative_to(Path.cwd()).as_posix(),'sha256':hashlib.sha256(asset.read_bytes()).hexdigest(),'svg':svg.relative_to(Path.cwd()).as_posix() if svg.exists() else None,'context':text[max(0,pos-600):pos+len(target)+600]}
 if svg.exists():
  doc=ET.fromstring(svg.read_text(encoding='utf8'));row['title']=' '.join(doc.find(ns+'title').itertext()) if doc.find(ns+'title') is not None else ''
  row['texts']=[{'text':' '.join(''.join(t.itertext()).split()),'x':t.get('x'),'y':t.get('y')} for t in doc.iter(ns+'text')]
  row['elements']={tag:sum(1 for t in doc.iter(ns+tag)) for tag in ['text','rect','path','line','circle','image']}
 rows.append(row)
assert len(rows)==133
(A/'VOL-01-native-inventory.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
D=A/'vol01-native';D.mkdir(exist_ok=True)
for ch in dict.fromkeys(r['chapter'] for r in rows):
 group=[r for r in rows if r['chapter']==ch]
 txt='\n\n'.join('## '+r['id']+' '+r['asset']+'\n'+r.get('title','')+'\n\n'+'\n'.join(f"({x['x']},{x['y']}) {x['text']}" for x in r.get('texts',[]))+'\n\nCONTESTO\n'+r['context'] for r in group)
 (D/(ch+'.txt')).write_text(txt,encoding='utf8')
print(json.dumps({'remaining':len(rows),'withSVG':sum(bool(r['svg']) for r in rows),'chapters':list(dict.fromkeys(r['chapter'] for r in rows))},ensure_ascii=False,indent=2))
