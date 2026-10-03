from pathlib import Path
from PIL import Image,ImageDraw
import json
A=Path(__file__).parent;D=A/'vol01-native';m=json.loads((A/'VOL-01-native-pdf-map.json').read_text(encoding='utf8'));out=D/'pdf-sheets';out.mkdir(exist_ok=True);sheets=[]
for start in range(0,len(m['selectedPages']),4):
 pages=m['selectedPages'][start:start+4];sheet=Image.new('RGB',(1470,2130),'#cccccc');draw=ImageDraw.Draw(sheet)
 for j,p in enumerate(pages):
  im=Image.open(D/'pdf-pages'/f'page-{p:03}.png');x=(j%2)*735;y=(j//2)*1065;sheet.paste(im,(x+6,y+24));draw.text((x+10,y+6),f'PDF p. {p}',fill='black')
 name=f'sheet-{start//4+1:02}.png';sheet.save(out/name);sheets.append({'file':str(out/name),'pages':pages,'visualReviewed':False})
(A/'VOL-01-native-pdf-visual-ledger.json').write_text(json.dumps(sheets,indent=2),encoding='utf8');print(len(sheets))
