from pathlib import Path
import sys,re,json,unicodedata,pymupdf
A=Path(__file__).parent;label=sys.argv[1];d=pymupdf.open(A/(label+'-proof.pdf'))
def norm(s):return re.sub(r'[^\w]','',unicodedata.normalize('NFKC',s)).lower()
rows=[]
for i,p in enumerate(d):
 s=p.get_text()
 if 'Indice completo' not in s and 'INDICE COMPLETO' not in s:continue
 for m in re.finditer(r'^(\d+\.\d+)[ \t]*\n(.*?)\n(\d+)[ \t]*(?=\n|$)',s,re.S|re.M):
  number,title,target=m[1],' '.join(m[2].split()),int(m[3]);actual=d[target-1].get_text()
  rows.append({'number':number,'title':title,'indexPage':i+1,'targetPage':target,'match':norm(number+' '+title) in norm(actual)})
out={'pdf':str(d.name),'entries':rows,'mismatches':[r for r in rows if not r['match']]};(A/(label+'-index-subentries.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'entries':len(rows),'mismatches':out['mismatches']},ensure_ascii=False))
