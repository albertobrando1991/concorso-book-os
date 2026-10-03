from pathlib import Path
import json,sys,pymupdf
from PIL import Image,ImageDraw
A=Path(__file__).parent;label=sys.argv[1]
pages=[int(x) for x in sys.argv[2].split(',')]
d=pymupdf.open(A/(label+'-proof.pdf'));out=A/(label+'-selected');out.mkdir(exist_ok=True)
for start in range(0,len(pages),16):
    batch=pages[start:start+16];canvas=Image.new('RGB',(1000,1480),'#dddddd');draw=ImageDraw.Draw(canvas)
    for i,n in enumerate(batch):
        pix=d[n-1].get_pixmap(matrix=pymupdf.Matrix(.5,.5),alpha=False)
        im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((240,340))
        x=(i%4)*250+5;y=(i//4)*370;draw.text((x,y+4),f'Pagina {n}',fill='black');canvas.paste(im,(x,y+24))
    canvas.save(out/f'contact-{start//16+1:02}.png')
print(json.dumps({'directory':str(out),'pages':pages}))
