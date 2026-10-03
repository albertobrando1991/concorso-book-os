from pathlib import Path
import json,re,hashlib,collections
out=Path(__file__).parent
data=json.loads((out/'registro-applicazione.json').read_text(encoding='utf8'))
summary={}
for prefix in ['V01-','P01-','V09-']:
 rows=[r for r in data if r['id'].startswith(prefix)]
 summary[prefix]={'statuses':dict(collections.Counter(r['status'] for r in rows)),'open':[r['id'] for r in rows if r['status']!='applicato-da-verificare']}
files=[Path(r['file']) for r in json.loads((out/'baseline.json').read_text(encoding='utf8')) if 'il-metodo-bando' in r['file'] or 'm-tr02-appalti' in r['file']]
missing=[];internal=[]
for p in files:
 t=p.read_text(encoding='utf8');body=t.split('---',2)[-1]
 for ref in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',body):
  if not ref.startswith(('http','data:')):
   x=Path('wiki')/ref if ref.startswith('books/') else p.parent/ref
   if not x.exists():missing.append({'chapter':p.as_posix(),'asset':ref})
 for ref in re.findall(r'\[\[((?:sources|topics|entities|raw|planning|reviews)/[^\]]+)\]\]',body):internal.append({'chapter':p.as_posix(),'ref':ref})
summary['missingImages']=missing;summary['internalBodyRefs']=internal
(out/'root-progress-check.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(summary,ensure_ascii=False,indent=2))
