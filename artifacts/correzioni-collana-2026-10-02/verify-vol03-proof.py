from pathlib import Path
import json,re,hashlib,unicodedata,pymupdf
R=Path(__file__).parent/'vol03-proof'
def norm(s):return ' '.join(unicodedata.normalize('NFKC',s).split()).casefold()
payload=json.loads((R/'payload.json').read_text(encoding='utf8'));m=json.loads((R/'vol-03-current-proof-metrics.json').read_text(encoding='utf8'));manifest=json.loads((R/'manifest.json').read_text(encoding='utf8'))
idx=next(c for c in payload['chapters'] if c.get('frontMatterLayout')=='analytical-index')
lines=[l.strip() for p in m['pages'] if p['path']==idx['path'] for l in p['text'].splitlines() if l.strip()]
checks=[]
for b in idx['blocks']:
 if b['type'] not in ('index-chapter','index-row'):continue
 pos=[i for i,l in enumerate(lines) if norm(l)==norm(b['text']) and i and norm(lines[i-1])==norm(b['number'])]
 printed=int(lines[pos[0]+1]) if len(pos)==1 and lines[pos[0]+1].isdigit() else None
 pages=[p for p in m['pages'] if p['path']==b['path']]
 if b['type']=='index-chapter':actual=pages[0]['page']
 else:
  targets=[p['page'] for p in pages if norm(b['text']) in norm(p['text']) and re.search(r'(?<!\d)'+re.escape(b['number'])+r'(?!\d)',p['text'])]
  actual=targets[0] if targets else None
 checks.append({'number':b['number'],'title':b['text'],'printed':printed,'actual':actual,'match':printed is not None and printed==actual})
text='\n'.join(p['text'] for p in m['pages']);pdf=R/'vol-03-current-proof.pdf';doc=pymupdf.open(pdf)
pdftexts=[p.get_text() for p in doc]
indexPageNumbers=[p['page'] for p in m['pages'] if p['path']==idx['path']]
pdfIndex=norm(' '.join(pdftexts[n-1] for n in indexPageNumbers if n<=len(doc)))
for check in checks:
 target=check['printed']
 check['pdfIndexMatch']=target is not None and norm(check['number']+' '+check['title']+' '+str(target)) in pdfIndex
 check['pdfTargetTitlePresent']=bool(target and target<=len(doc) and norm(check['title']) in norm(pdftexts[target-1]))
fontchecks=[]
for xref in sorted({f[0] for p in doc for f in p.get_fonts()}):
 name,ext,kind,data=doc.extract_font(xref)
 charprocs=doc.xref_get_key(xref,'CharProcs')
 fontchecks.append({'xref':xref,'name':name,'format':ext,'kind':kind,'bytes':len(data),'charProcs':charprocs,'embedded':bool(data) or (kind=='Type3' and charprocs[0] not in ('null','none'))})
sources=[{**r,'currentMatch':hashlib.sha256(Path(r['path']).read_bytes()).hexdigest()==r['sha256']} for r in manifest['sourceHashes']]
schemes=[]
for c in payload['chapters']:
 for b in c['blocks']:
  if b['type']=='heading' and re.match(r'^Schema \d+\.\d+ —',b.get('text','')):
   pages=[p['page'] for p in m['pages'] if p['path']==c['path'] and norm(b['text']) in norm(p['text'])]
   schemes.append({'path':c['path'],'title':b['text'],'pages':pages})
result={'pdfSha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':len(doc),'trimPt':[doc[0].rect.width,doc[0].rect.height],'mainChapters':50,'indexEntries':checks,'indexMismatches':[c for c in checks if not c['match']],'overflowPages':[p['page'] for p in m['pages'] if p['overflows']],'internalLeaks':re.findall(r'wiki/(?:sources|topics|books)|\[\[|source_refs|review_required|@@LINK',text),'fonts':fontchecks,'sourceHashes':sources,'nativeSchemes':schemes,'KDPBlackWhitePaperPageLimit':828,'withinWhitePaperLimit':len(doc)<=828,'withinCreamPaperLimit':len(doc)<=776,'missingImages':m['missingImages'],'limitations':['Technical checks plus separate visual contact-sheet review; no KDP upload or physical print proof.','Unresolved common digital-service and publisher-data dependency.']}
result['domPageCount']=m['pageCount'];result['domPdfPageCountMatch']=m['pageCount']==len(doc)
result['pdfIndexMismatches']=[c for c in checks if not c['pdfIndexMatch'] or not c['pdfTargetTitlePresent']]
(R/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'pages':len(doc),'domPages':m['pageCount'],'indexEntries':len(checks),'indexMismatches':result['indexMismatches'],'pdfIndexMismatches':result['pdfIndexMismatches'],'sourceMismatches':[s for s in sources if not s['currentMatch']],'schemas':len(schemes),'missingSchemaCount':sum(not s['pages'] for s in schemes),'fontsEmbedded':all(f['embedded'] for f in fontchecks),'leaks':result['internalLeaks'],'overflowPages':result['overflowPages']},ensure_ascii=False))
