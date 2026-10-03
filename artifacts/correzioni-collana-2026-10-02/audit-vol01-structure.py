from pathlib import Path
import re,json,hashlib
A=Path(__file__).parent; B=Path('wiki/books/il-metodo-bando')
spec=(B/'planning/00-scheda-pipeline.md').read_text(encoding='utf8')
paths=list(dict.fromkeys(re.findall(r'chapters/[a-z0-9-]+\.md',spec)))
assert len(paths)==32,len(paths)
rows=[]; missing=[]; internal=[]; refs=[]
for path in paths:
 p=B/path;t=p.read_text(encoding='utf8'); fm,body=t.split('---',2)[1:]
 headings=re.findall(r'^#{1,6} (.+)$',body,re.M)
 for ref in re.findall(r'!\[[^\]]*\]\(([^)]+)\)',body):
  target=Path('wiki')/ref if ref.startswith('books/') else p.parent/ref
  if not ref.startswith(('http','data:')) and not target.exists():missing.append([str(p),ref])
 for ref in re.findall(r'\[\[((?:sources|topics|entities|raw|planning|reviews)/[^\]]+)\]\]',body):internal.append([str(p),ref])
 for ref in re.findall(r'"(sources/[^"\]]+)"',fm):
  target=Path('wiki')/ref
  if not target.suffix:target=target.with_suffix('.md')
  if not target.exists():refs.append([str(p),ref])
 rows.append({'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'words':len(body.split()),'headings':headings,'images':len(re.findall(r'!\[',body)),'formatVersion':re.search(r'^format_version:\s*(.*)',fm,re.M).group(1) if re.search(r'^format_version:\s*(.*)',fm,re.M) else 'legacy'})
result={'date':'2026-10-03','units':rows,'unitCount':len(rows),'missingImages':missing,'internalBodyRefs':internal,'missingSourceRefs':refs,'limits':'Inventario e controlli di presenza: non provano la correttezza normativa o la qualità visiva.'}
(A/'VOL-01-structure.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='units'},ensure_ascii=False))
