import pathlib,json,hashlib,sys
from PIL import Image,ImageDraw
root=pathlib.Path(__file__).resolve().parents[2]
volume=sys.argv[1] if len(sys.argv)>1 else 'VOL-01'
out=root/'artifacts/review-integrale-2026-10-02'/('figures' if volume=='VOL-01' else 'figures-'+volume);out.mkdir(exist_ok=True)
data=json.loads((root/f'artifacts/review-integrale-2026-10-02/{volume}-current-export.json').read_text(encoding='utf8'))
rows=[]; imgs=[]
for c in data:
 for b in c['blocks']:
  if b['type']!='image':continue
  p=root/'wiki'/b['path'];im=Image.open(p).convert('RGB');im.thumbnail((800,500))
  rows.append({'n':len(rows)+1,'file':str(p.relative_to(root)).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'chapter':c['title'],'alt':b.get('alt'),'pixels':Image.open(p).size})
  imgs.append(im)
for start in range(0,len(imgs),4):
 canvas=Image.new('RGB',(1640,1080),'#dddddd');draw=ImageDraw.Draw(canvas)
 for offset,im in enumerate(imgs[start:start+4]):
  x=(offset%2)*820;y=(offset//2)*540
  draw.text((x+8,y+5),f'{start+offset+1}: '+rows[start+offset]['file'].split('/assets/')[-1],fill='black')
  canvas.paste(im,(x+8,y+28))
 canvas.save(out/f'figures-{start+1:03}-{min(start+4,len(imgs)):03}.png')
(out/'manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(len(rows),'assets',len(list(out.glob('figures*.png'))),'sheets')
