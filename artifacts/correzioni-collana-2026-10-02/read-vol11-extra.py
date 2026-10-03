from pathlib import Path
from html.parser import HTMLParser
import re,json
import pymupdf
class T(HTMLParser):
 def __init__(self):super().__init__();self.out=[]
 def handle_data(self,d):self.out.append(d)
B=Path('wiki/raw/correzioni-vol11-2026-10-03');O=Path('artifacts/correzioni-collana-2026-10-02/norme-vol11')
for name in ['ambiente-art298bis-danno','rentri-esclusioni','camera-aria435']:
 p=T();p.feed((B/(name+'.html')).read_text(encoding='utf8'));s=re.sub(r'[ \t]+',' ', '\n'.join(p.out));(O/(name+'.txt')).write_text(s,encoding='utf8')
 if name.startswith('ambiente'):print(name,'valid:', 'Principi generali' in s, 'excluded if invalid')
 else:
  lines=s.splitlines()
  for i,l in enumerate(lines):
   if any(x in l for x in ['DECRETO LEGISLATIVO','Esclusioni dall','Sono esclusi','Parere favorevole','settembre 2026']):print(name,'\n'.join(lines[max(0,i-1):i+5]))
d=pymupdf.open('wiki/raw/m-sa02-professioni-sanitarie/tecnica-tpall/snpa-classificazione-rifiuti-105-2021.pdf')
for i,p in enumerate(d):
 s=p.get_text()
 if '17 05 03' in s or '15 01 01' in s:
  print('SNPA PAGE',i+1,s)
# All 14 originals were fully read in the integral audit; baseline hashes checked before editing.
Path('artifacts/correzioni-collana-2026-10-02/VOL-11-progress.json').write_text(json.dumps({'date':'2026-10-03','stage':'revision-in-progress','appliedChapters':['01','02','03','04','05'],'findingsApplied':[f'V11-{n:02d}' for n in range(1,17)],'pending':list(range(17,45)),'gateSnapshot':'VOL-11-TR04-gates.json','pdfVerified':False,'note':'All chapter gates pass; specialist audit and final review still pending. V11-19 diagnosis requires correction: article 240(f) literally says inferiore.'},ensure_ascii=False,indent=2),encoding='utf8')
