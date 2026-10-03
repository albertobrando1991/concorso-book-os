from pathlib import Path
from reportlab.pdfgen import canvas
import pymupdf, math, json, hashlib, shutil

OUT=Path('wiki/books/moduli/m-tr03-tecnico-ingegneristico/assets/correzioni-2026-10')
OUT.mkdir(parents=True,exist_ok=True)
files=[]
def start(name,h):
 c=canvas.Canvas(str(OUT/(name+'.pdf')),pagesize=(650,h))
 c.setFillColorRGB(1,1,1);c.rect(0,0,650,h,fill=1,stroke=0)
 c.setFillColorRGB(0,0,0);c.setStrokeColorRGB(0,0,0);c.setLineWidth(1.5)
 return c
def label(c,x,y,s,size=18,bold=False):
 c.setFont('Helvetica-Bold' if bold else 'Helvetica',size);c.drawString(x,y,s)
def arrow(c,x,y,X,Y):
 c.line(x,y,X,Y);a=math.atan2(Y-y,X-x);d=9
 c.line(X,Y,X-d*math.cos(a-.4),Y-d*math.sin(a-.4));c.line(X,Y,X-d*math.cos(a+.4),Y-d*math.sin(a+.4))
def triangle(c,x,y,roller=False):
 p=c.beginPath();p.moveTo(x,y);p.lineTo(x-15,y-22);p.lineTo(x+15,y-22);p.close();c.drawPath(p)
 if roller:
  c.circle(x-8,y-27,4);c.circle(x+8,y-27,4);gy=y-33
 else:gy=y-23
 c.line(x-24,gy,x+24,gy)
 for xx in range(-24,25,8):c.line(x+xx,gy,x+xx-7,gy-8)
def finish(c,name):
 c.save();d=pymupdf.open(OUT/(name+'.pdf'));d[0].get_pixmap(matrix=pymupdf.Matrix(2,2)).save(OUT/(name+'.png'))
 files.append({'name':name,'pdf':(OUT/(name+'.pdf')).as_posix(),'png':(OUT/(name+'.png')).as_posix(),'sha256':hashlib.sha256((OUT/(name+'.png')).read_bytes()).hexdigest()})

c=start('vincoli-piani',660)
label(c,24,626,'Vincoli ideali nel piano',24,True)
label(c,24,596,'Corpo rigido: traslazione x, traslazione y, rotazione',18)
for i,(title,block,free) in enumerate([
 ('Carrello su piano orizzontale','Blocca: spostamento y','Consente: spostamento x e rotazione'),
 ('Cerniera','Blocca: spostamenti x e y','Consente: rotazione'),
 ('Incastro','Blocca: x, y e rotazione','Nessun grado di libertà del nodo')]):
 y=505-i*175;label(c,24,y+52,title,21,True)
 c.setLineWidth(3);c.line(85,y,260,y);c.setLineWidth(1.5)
 if i<2:triangle(c,110,y,i==0)
 else:
  c.setLineWidth(3);c.line(85,y-36,85,y+38);c.setLineWidth(1.5)
  for yy in range(-32,39,10):c.line(85,y+yy,72,y+yy-10)
 rx=110 if i<2 else 85
 arrow(c,rx,y,rx,y+40);label(c,rx+9,y+27,'Ry',18,True)
 if i>0:arrow(c,rx,y,245,y);label(c,225,y+17,'Rx',18,True)
 if i==2:
  c.arc(118,y-24,162,y+20,startAng=20,extent=290)
  a=math.radians(310);x=140+22*math.cos(a);Y=y-2+22*math.sin(a)
  arrow(c,x-5,Y-5,x,Y);label(c,149,y+28,'M',18,True)
 label(c,295,y+8,block,18);label(c,24,y-68,free,18)
 if i<2:
  c.setStrokeColorRGB(.75,.75,.75);c.line(24,y-94,626,y-94);c.setStrokeColorRGB(0,0,0)
label(c,24,24,'Le frecce indicano versi assunti per le reazioni.',18)
finish(c,'vincoli-piani')

c=start('trave-carico-taglio-momento',720)
label(c,24,686,'Trave semplicemente appoggiata',24,True)
label(c,24,655,'L = 4 m  |  q = 10 kN/m uniforme verso il basso',18)
x0=105;x1=585;scale=120;y=550
c.setLineWidth(3);c.line(x0,y,x1,y);c.setLineWidth(1.5)
triangle(c,x0,y);triangle(c,x1,y,True)
c.line(x0,y+60,x1,y+60)
for xx in range(x0,x1+1,40):arrow(c,xx,y+60,xx,y+7)
arrow(c,x0-28,y-60,x0-28,y+20);arrow(c,x1+28,y-60,x1+28,y+20)
label(c,24,475,'A: Ry = 20 kN',18);label(c,440,475,'B: Ry = 20 kN',18)
label(c,270,504,'4 m',18,True)
c.line(x0,497,x1,497);c.line(x0,491,x0,503);c.line(x1,491,x1,503)
label(c,24,435,'Taglio V(x) = 20 - 10x [kN]',21,True)
v0=355
arrow(c,x0-5,v0,x1+28,v0);arrow(c,x0,v0-68,x0,v0+70)
c.setStrokeColorRGB(.35,.35,.35);c.setDash(3,4);c.line(x0+240,275,x0+240,410);c.setDash();c.setStrokeColorRGB(0,0,0)
c.setLineWidth(3);c.line(x0,v0+55,x1,v0-55);c.setLineWidth(1.5)
label(c,44,v0+48,'+20',18);label(c,42,v0-7,'0',18);label(c,535,v0-81,'-20',18)
label(c,327,v0-25,'2',18);label(c,573,v0+8,'4',18);label(c,602,v0-24,'x [m]',18)
label(c,24,237,'Momento M(x) = 20x - 5x² [kN m]',21,True)
m0=88
arrow(c,x0-5,m0,x1+28,m0);arrow(c,x0,m0-8,x0,m0+110)
p=c.beginPath()
for j in range(101):
 x=4*j/100;X=x0+x*scale;Y=m0+(20*x-5*x*x)*4.5
 if j==0:p.moveTo(X,Y)
 else:p.lineTo(X,Y)
c.setLineWidth(3);c.drawPath(p);c.setLineWidth(1.5)
c.setDash(3,4);c.line(x0+240,m0,x0+240,m0+90);c.setDash()
label(c,315,190,'+20',18,True);label(c,79,64,'0',18);label(c,335,64,'2',18);label(c,576,64,'4',18)
label(c,592,99,'x [m]',18)
label(c,24,23,'M positivo: fibre inferiori tese; diagrammi positivi in alto.',18)
finish(c,'trave-carico-taglio-momento')

c=start('planimetria-sopralluogo',700)
label(c,24,666,'D1 - Planimetria didattica del sopralluogo',23,True)
label(c,24,638,'Quote nette in metri; muri senza spessore nel modello.',18)
ox=83;oy=233;k=40
def xy(x,y):return ox+x*k,oy+y*k
def line(x,y,X,Y):c.line(*xy(x,y),*xy(X,Y))
# Closed area hatched before perimeter and labels; no hazard implied.
c.saveState();p=c.beginPath();p.rect(*xy(6,2),6*k,6*k);c.clipPath(p,stroke=0)
c.setStrokeColorRGB(.82,.82,.82)
for j in range(-260,530,18):c.line(ox+6*k+j,oy+2*k,ox+6*k+j+240,oy+8*k)
c.restoreState()
c.setLineWidth(3)
for a in [(0,0,5.4,0),(6.6,0,12,0),(12,0,12,8),(12,8,0,8),(0,8,0,0),(0,2,2.5,2),(3.5,2,8.5,2),(9.5,2,12,2),(6,2,6,8)]:line(*a)
c.setLineWidth(1.2)
# Threshold markers make door openings explicit, without fictitious wall thickness.
for a in [(2.5,2,3.5,2),(8.5,2,9.5,2),(5.4,0,6.6,0)]:
 c.setDash(3,3);line(*a);c.setDash()
c.setFillColorRGB(.6,.6,.6);c.rect(*xy(1,6),2*k,k,fill=1,stroke=0);c.setFillColorRGB(0,0,0)
label(c,*xy(.65,7.25),'Proiezione alone',18)
label(c,*xy(3.5,6.25),'2 m²',18)
label(c,*xy(.4,3.1),'Aula A',22,True);label(c,*xy(.4,2.5),'6 × 6 m',18)
# White patch behind area name for contrast.
c.setFillColorRGB(1,1,1);c.rect(*xy(6.45,4.1),5.1*k,1.4*k,fill=1,stroke=0);c.setFillColorRGB(0,0,0)
label(c,*xy(6.8,5.0),'Aula B: 6 × 6 m',19,True);label(c,*xy(6.8,4.35),'Non accessibile',18)
label(c,*xy(6.9,.72),'Corridoio 12 × 2 m',18)
# Route and observation points.
for a in [(6,-.45,6,1),(6,1,3,1),(3,1,3,2.8),(3,2.8,3.5,4.5)]:arrow(c,*xy(a[0],a[1]),*xy(a[2],a[3]))
for x,y,name,dx,dy in [(6,.35,'P1',.2,-.15),(3,2.8,'P2',.22,0),(3.5,4.5,'P3 / F01',.3,0)]:
 c.circle(*xy(x,y),4,fill=1);label(c,*xy(x+dx,y+dy),name,18,True)
arrow(c,*xy(3.5,4.5),*xy(2.45,5.55))
label(c,*xy(4.4,-1.15),'Ingresso sud',18)
# Overall dimensions, north arrow, metric scale.
c.line(ox,590,ox+480,590);c.line(ox,582,ox,598);c.line(ox+480,582,ox+480,598)
label(c,292,598,'12 m',18,True)
c.line(49,oy,49,oy+320);c.line(41,oy,57,oy);c.line(41,oy+320,57,oy+320)
label(c,6,389,'8 m',18,True)
arrow(c,608,502,608,553);label(c,601,565,'N',21,True)
c.setLineWidth(4);c.line(83,151,163,151);c.setLineWidth(1);c.line(83,145,83,157);c.line(163,145,163,157)
label(c,79,122,'0',18);label(c,146,122,'2 m',18)
label(c,230,142,'Freccia da P3: direzione di F01',18)
label(c,24,83,'Il tratteggio indica solo il limite del sopralluogo.',18)
label(c,24,54,'Non dimostra una condizione di pericolo.',18)
label(c,24,25,'Usare le quote e la scala grafica, non misurare la stampa.',18)
finish(c,'planimetria-sopralluogo')

src=Path('C:/Users/info/.codex/generated_images/01a0fe3a-1334-77b1-8b26-48afd5f441ff/exec-b553dad7-6ec3-429e-b00a-0cf43aa16e47.png')
shutil.copy2(src,OUT/'f01-alone-illustrativo.png')
assert 10*4/2==20 and 20*2-5*2**2==20 and 6*6*24==864
data={'assets':files,'checks':{'beam':{'L_m':4,'q_kN_m':10,'RA_kN':20,'RB_kN':20,'V_zero_m':2,'M_max_kNm':20},'plan':{'total_area_m2':96,'room_A_m2':36,'room_B_m2':36,'corridor_m2':24,'stain_projection_m2':2,'whole_ceiling_cost_eur':864}},'visualReview':'pending'}
Path('artifacts/correzioni-collana-2026-10-02/figure-vol10-scientifiche.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(data,ensure_ascii=False))
