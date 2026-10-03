from pathlib import Path
import io,json,hashlib
import numpy as np
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pymupdf

out=Path('wiki/books/moduli/m-sa04-tecnici-sanitari-prevenzione/assets/correzioni-2026-10');out.mkdir(parents=True,exist_ok=True)
pdfmetrics.registerFont(TTFont('Arial','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold','C:/Windows/Fonts/arialbd.ttf'))
W,H=400,245
manifest=[]
def finish(c,name):
 c.save();p=out/(name+'.pdf')
 d=pymupdf.open(p);d[0].get_pixmap(matrix=pymupdf.Matrix(4,4),alpha=False).save(out/(name+'.png'))
 manifest.append({'name':name,'pdf':p.as_posix(),'png':(out/(name+'.png')).as_posix(),'sha256':hashlib.sha256((out/(name+'.png')).read_bytes()).hexdigest(),'width':1600,'height':980})
def new(name):
 c=canvas.Canvas(str(out/(name+'.pdf')),pagesize=(W,H));c.setFillColorRGB(1,1,1);c.rect(0,0,W,H,fill=1,stroke=0);c.setFillColorRGB(0,0,0);return c
def raster(c,arr,x,y,size):
 im=Image.fromarray(np.uint8(np.clip(arr,0,1)*255));c.drawImage(ImageReader(im),x,y,width=size,height=size)

# Original analytic test object: no existing clinical or editorial image is read.
n=384;y,x=np.mgrid[0:n,0:n];xx=x/n;yy=y/n
def phantom(dx=0):
 q=xx-dx;a=np.full((n,n),.9)
 grid=((np.abs((q-.15)%(.10))<.012)&(q>.1)&(q<.9)&(yy>.12)&(yy<.48))
 grid|=((np.abs((yy-.12)%(.09))<.01)&(q>.1)&(q<.9)&(yy>.12)&(yy<.48))
 a[grid]=.25
 for cx,r in [(.27,.085),(.50,.06),(.70,.035)]:a[(q-cx)**2+(yy-.71)**2<r*r]=.40
 return a
a=phantom();b=np.mean([phantom(dx) for dx in np.linspace(-.035,.035,25)],axis=0)
c=new('movimento-dettaglio');raster(c,a,20,35,170);raster(c,b,210,35,170)
c.setFont('ArialBold',14);c.drawString(20,220,'A');c.drawString(210,220,'B')
c.setFont('Arial',11);c.drawString(40,220,'Contorni netti');c.drawString(230,220,'Movimento')
c.setFont('Arial',10);c.drawCentredString(200,14,'Stesso oggetto di prova — simulazione originale')
finish(c,'movimento-dettaglio')

# Fixed target contrast; noise mean zero separately in target/background, no clipping.
mask=(xx-.5)**2+(yy-.5)**2<.135**2;mean=np.where(mask,.54,.62)
rng=np.random.default_rng(7032026);noise=rng.uniform(-1,1,(n,n))
for m in [mask,~mask]:noise[m]-=noise[m].mean()
low=mean+.012*noise;high=mean+.16*noise
assert np.all((high>0)&(high<1))
contrasts=[float(im[~mask].mean()-im[mask].mean()) for im in [low,high]]
assert abs(contrasts[0]-contrasts[1])<1e-12
c=new('rumore-contrasto');raster(c,low,20,35,170);raster(c,high,210,35,170)
c.setFont('ArialBold',14);c.drawString(20,220,'A');c.drawString(210,220,'B')
c.setFont('Arial',11);c.drawString(40,220,'Rumore basso');c.drawString(230,220,'Rumore maggiore')
c.setFont('Arial',10);c.drawCentredString(200,14,'Stesso contrasto medio — simulazione originale')
finish(c,'rumore-contrasto')

# Levey–Jennings plot: exact supplied standardized series, no acceptance verdict.
values=[0,.5,1,1.5,2,2.5,3,3.5];c=new('serie-controllo-qc')
left,right,bottom,top=48,380,35,215
X=lambda i:left+(i-1)*(right-left)/7
Y=lambda z:bottom+(z+3)*(top-bottom)/7
c.setFont('Arial',10)
for z in range(-3,5):
 c.setStrokeGray(.68 if z else .1);c.setLineWidth(.45 if z else .9);c.setDash(2,2) if z else c.setDash()
 c.line(left,Y(z),right,Y(z));c.setFillGray(0);c.drawRightString(left-9,Y(z)-3,str(z))
c.setDash();c.setStrokeGray(0);c.setLineWidth(.8);c.line(left,bottom,left,top)
for i,v in enumerate(values,1):
 c.drawCentredString(X(i),20,str(i))
 if i>1:c.line(X(i-1),Y(values[i-2]),X(i),Y(v))
 c.circle(X(i),Y(v),2.8,fill=1,stroke=0)
c.setFont('Arial',11);c.drawString(15,225,'z');c.drawCentredString(220,3,'Seduta di controllo')
c.setFont('ArialBold',11);c.drawString(48,230,'Serie didattica: andamento crescente')
finish(c,'serie-controllo-qc')
Path('artifacts/correzioni-collana-2026-10-02/figure-scientifiche-verifica.json').write_text(json.dumps({'figures':manifest,'seed':7032026,'contrastMeans':contrasts,'qcSeries':values,'existingImagesRead':False,'pdfVisualReviewPending':True},indent=2),encoding='utf8')
print(json.dumps(manifest))
