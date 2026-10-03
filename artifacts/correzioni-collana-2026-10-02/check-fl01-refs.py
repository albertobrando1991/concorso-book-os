from pathlib import Path
import re,json
base=Path('wiki/books/moduli/m-fl01-comuni-unioni');out=[];total=0
for p in list((base/'chapters').glob('*.md'))+[base/'index.md',base/'planning/02-matrice-copertura-didattica.md']:
 text=p.read_text(encoding='utf8')
 for match in re.finditer(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]',text):
  target,_,anchor=match[1].partition('#');dest=Path('wiki')/target
  if dest.suffix!='.md':dest=dest.with_suffix('.md')
  total+=1
  if not dest.exists():out.append({'file':str(p),'target':match[1],'error':'missing-file'});continue
  if anchor:
   headings=re.findall(r'^#{1,6}\s+(.+?)\s*$',dest.read_text(encoding='utf8'),re.M)
   if anchor not in headings:out.append({'file':str(p),'target':match[1],'error':'missing-heading'})
print(json.dumps({'total':total,'invalid':out},ensure_ascii=False,indent=2))
