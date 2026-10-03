from pathlib import Path
import json,hashlib,re,collections
A=Path(__file__).parent;D=A/'digital-publication'
load=lambda p:json.loads(p.read_text('utf8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
baseline=load(Path('artifacts/review-integrale-2026-10-02/complete-chapter-register.json'))
reviewed={r['file'] for r in baseline}
errors=[];extra=[];flags=[];summary=[]
for directory in sorted(D.glob('VOL-*')):
 bundle=load(directory/'bundle.json');volume=bundle['volume'];units=volume['chapters']
 assets={a['id']:a for a in bundle['assets']};images=0;words=0
 for asset in assets.values():
  p=directory/asset['bundlePath']
  if not p.is_file() or sha(p)!=asset['sha256']:errors.append([volume['code'],'asset',str(p)])
 for unit in units:
  source=Path(unit['sourcePath'])
  if not source.is_file() or sha(source)!=unit['sourceHash']:errors.append([volume['code'],'source',str(source)])
  text=json.dumps(unit['blocks'],ensure_ascii=False)
  words+=len(text.split())
  if not unit['blocks']:errors.append([volume['code'],'empty',unit['id']])
  if unit['sourcePath'] not in reviewed:extra.append({k:unit[k] for k in ['id','title','sourcePath','scope','reviewRequired','contentState']})
  for block in unit['blocks']:
   if block['type']=='image':
    images+=1
    if block.get('assetId') not in assets:errors.append([volume['code'],'image-reference',unit['id'],block])
  for pattern in [r'\[\[(?:sources|topics|entities|raw|planning|reviews)/',r'capitolo in preparazione',r'\b(?:TODO|TBD|FIXME)\b',r'source note|source_refs|Bozza agente|Testo editoriale',r'mese gratuito|mese gratis|servizi digitali inclusi']:
   for match in re.finditer(pattern,text,re.I):
    flags.append({'volume':volume['code'],'sourcePath':unit['sourcePath'],'pattern':pattern,'context':text[max(0,match.start()-90):match.end()+150]})
 summary.append({'volume':volume['code'],'chapters':len(units),'ricettario':sum(u['scope']=='ricettario' for u in units),'assets':len(assets),'imageBlocks':images,'states':dict(collections.Counter(u['contentState'] for u in units)),'reviewRequired':sum(u['reviewRequired'] for u in units)})
result={'errors':errors,'summary':summary,'outsideOriginalReviewPerimeter':extra,'textFlagsForReview':flags,'scope':'Integrity, source identity and perimeter reconciliation only; does not certify textual accuracy or rendered web layout.'}
(D/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps({'errors':errors,'summary':summary,'extraCount':len(extra),'extra':[{'title':r['title'],'scope':r['scope']} for r in extra],'flags':flags[:12],'totalFlags':len(flags)},ensure_ascii=False))
