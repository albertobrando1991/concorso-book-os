from pathlib import Path
from collections import Counter
import pymupdf,json,sys
from PIL import Image,ImageDraw
p=Path(sys.argv[1]);d=pymupdf.open(p);out=p.parent/(p.stem+'-audit');out.mkdir(exist_ok=True)
rows=[];sizes=Counter();sheets=[]
for start in range(0,len(d),16):
 sheet=Image.new('RGB',(1000,1480),'#e3e3e3');draw=ImageDraw.Draw(sheet)
 for i in range(start,min(start+16,len(d))):
  pg=d[i];pix=pg.get_pixmap(matrix=pymupdf.Matrix(.49,.49),alpha=False);im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);x=(i-start)%4*250;y=(i-start)//4*370;sheet.paste(im,(x+7,y+25));draw.text((x+8,y+6),f'Pagina {i+1}',fill='black')
  text=pg.get_text();spans=[s for b in pg.get_text('dict')['blocks'] if b['type']==0 for l in b['lines'] for s in l['spans']]
  for s in spans:sizes[(s['font'],round(s['size'],2))]+=len(s['text'])
  images=pg.get_image_info();rows.append({'page':i+1,'words':len(text.split()),'images':[{'bbox':j['bbox'],'width':j['width'],'height':j['height']} for j in images],'replacementGlyphs':text.count('\ufffd'),'textOutsidePage':[s['text'] for s in spans if s['bbox'][0]<-1 or s['bbox'][2]>pg.rect.width+1 or s['bbox'][1]<-1 or s['bbox'][3]>pg.rect.height+1]})
 name=f'contact-{start+1:03}-{min(start+16,len(d)):03}.png';sheet.save(out/name);sheets.append(name)
result={'pdf':str(p),'pages':len(d),'pageSizePt':[d[0].rect.width,d[0].rect.height],'fonts':[{'name':n,'pt':s,'characters':c} for (n,s),c in sizes.most_common()],'pagesData':rows,'contacts':sheets,'limits':'Controlli geometrici e tavole da esaminare; non equivale a lettura visiva.'}
(out/'metrics.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'pages':len(d),'sheets':len(sheets),'output':str(out),'fontTop':result['fonts'][:8],'outOfPage':sum(bool(x['textOutsidePage']) for x in rows),'imagePages':[x['page'] for x in rows if x['images']]},ensure_ascii=False))
