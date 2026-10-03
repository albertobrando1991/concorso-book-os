from pathlib import Path
import json,re
out=[]
for p in Path('wiki/books/moduli').glob('m-ir*/chapters/*.md'):
 text=p.read_text(encoding='utf8')
 for m in re.finditer(r'(?m)^\|[^\n]*\n\|[ :|\-]+\|\s*\n(?:\|[^\n]*\n)+',text):
  lines=m.group().strip().splitlines(); cells=[[c.strip() for c in l.strip().strip('|').split('|')] for l in lines]; blank=any(any(not c for c in row) for row in cells[2:])
  if blank and len(cells[0])>3:out.append({'path':str(p),'line':text[:m.start()].count('\n')+1,'heading':re.findall(r'^## .*$',text[:m.start()],re.M)[-1],'table':m.group(),'cols':len(cells[0])})
A=Path(__file__).parent;(A/'VOL-06-wide-worksheets.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps([{'path':r['path'],'line':r['line'],'cols':r['cols'],'heading':r['heading']} for r in out],ensure_ascii=False))
