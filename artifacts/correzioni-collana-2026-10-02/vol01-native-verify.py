from pathlib import Path
import json,hashlib,re
A=Path(__file__).parent;D=A/'vol01-native';B=Path('wiki/books/il-metodo-bando/chapters')
inv=json.loads((A/'VOL-01-native-inventory.json').read_text(encoding='utf8'))
protected=json.loads((A/'figure-vol01-corrette-manifest.json').read_text(encoding='utf8'))
rows=[]
for r in inv:
 s=(B/r['chapter']).read_text(encoding='utf8');rep=(D/(r['id']+'.md')).read_text(encoding='utf8').strip()
 original=Path(r['path']);caption=re.search(r'\*Figura (\d+\.\d+)',r['context'])
 rows.append({'id':r['id'],'chapter':r['chapter'],'originalReferenceAbsent':r['asset'] not in s,'replacementCount':s.count(rep),'originalAssetUnchanged':hashlib.sha256(original.read_bytes()).hexdigest()==r['sha256'],'caption':caption.group(1) if caption else None,'chapterSHA256':hashlib.sha256((B/r['chapter']).read_bytes()).hexdigest()})
pr=[]
for r in protected:
 p=Path(r['newAsset']);refs=[]
 for c in r['chapters']:
  s=Path(c).read_text(encoding='utf8');before=(D/'before'/Path(c).name).read_text(encoding='utf8')
  refs.append({'chapter':c,'count':s.count(p.name),'beforeCount':before.count(p.name),'unchanged':s.count(p.name)==before.count(p.name)})
 pr.append({'id':r.get('id',p.stem),'asset':str(p),'hashUnchanged':hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'],'refs':refs})
result={'nativeCount':len(rows),'protectedCount':len(pr),'native':rows,'protected':pr,'allPassed':all(x['originalReferenceAbsent'] and x['replacementCount']==1 and x['originalAssetUnchanged'] for x in rows) and all(x['hashUnchanged'] and all(z['unchanged'] for z in x['refs']) for x in pr)}
(A/'VOL-01-native-verifica.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'native':len(rows),'protected':len(pr),'allPassed':result['allPassed']}))
