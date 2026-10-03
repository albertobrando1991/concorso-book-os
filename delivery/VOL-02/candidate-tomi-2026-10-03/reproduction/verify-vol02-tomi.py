from pathlib import Path
import json, re, hashlib, unicodedata
ROOT=Path(__file__).parent/'vol02-tomi'
def norm(s):return ' '.join(unicodedata.normalize('NFKC',s).split()).casefold()
for tomo in ('tomo-1','tomo-2'):
 payload=json.loads((ROOT/f'{tomo}-payload.json').read_text(encoding='utf8'))
 metrics=json.loads((ROOT/f'vol-02-{tomo}-proof-metrics.json').read_text(encoding='utf8'))
 idx=next(c for c in payload['chapters'] if c.get('frontMatterLayout')=='analytical-index')
 lines=[l.strip() for p in metrics['pages'] if p['path']==idx['path'] for l in p['text'].splitlines() if l.strip()]
 checks=[]
 for b in idx['blocks']:
  if b['type'] not in ('index-chapter','index-row'):continue
  positions=[i for i,l in enumerate(lines) if norm(l)==norm(b['text']) and i and norm(lines[i-1])==norm(b['number'])]
  printed=int(lines[positions[0]+1]) if len(positions)==1 and lines[positions[0]+1].isdigit() else None
  pages=[p for p in metrics['pages'] if p['path']==b['path']]
  if b['type']=='index-chapter':actual=pages[0]['page']
  else:
   targets=[p['page'] for p in pages if norm(b['text']) in norm(p['text']) and re.search(r'(?<!\d)'+re.escape(b['number'])+r'(?!\d)',p['text'])]
   actual=targets[0] if targets else None
  checks.append({'number':b['number'],'title':b['text'],'printedPage':printed,'actualPage':actual,'match':printed is not None and printed==actual})
 text='\n'.join(p['text'] for p in metrics['pages'])
 result={'tomo':tomo,'pdfSha256':hashlib.sha256((ROOT/f'vol-02-{tomo}-proof.pdf').read_bytes()).hexdigest(),'pages':metrics['pageCount'],'indexEntries':checks,'indexMismatches':[c for c in checks if not c['match']],'overflowPages':[p['page'] for p in metrics['pages'] if p['overflows']],'internalLeaks':re.findall(r'wiki/(?:sources|topics|books)|\[\[|source_refs|review_required',text),'budgetAmountPreserved':tomo!='tomo-1' or 'disponibilità residua del capitolo 2.680' in text,'oldReferenceTableAbsent':tomo!='tomo-1' or 'Capitolo 4 sugli atti' not in text,'newReferenceTablePresent':tomo!='tomo-1' or 'Capitolo 7 sugli atti' in text}
 (ROOT/f'{tomo}-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
 print(json.dumps({k:v for k,v in result.items() if k!='indexEntries'},ensure_ascii=True))
