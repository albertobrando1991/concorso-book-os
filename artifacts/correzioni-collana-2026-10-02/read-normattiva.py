from pathlib import Path
import re,html,sys
for name in sys.argv[1:]:
 p=Path('artifacts/correzioni-collana-2026-10-02',name)
 t=p.read_text(encoding='utf8')
 start=t.find('<span class="comma-num-akn">')
 end=t.find('<!--',start)
 if start<0: parts=[]
 else: parts=[t[start:end if end>start else start+35000]]
 print(p.name, 'commi',len(parts))
 for x in parts:
  v=html.unescape(re.sub('<[^>]+>',' ',x)).split('articolo precedente')[0].split('Avvertenza:')[0]
  print(re.sub(r'\s+',' ',v).strip())
