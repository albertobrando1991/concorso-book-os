from pathlib import Path
from datetime import date,timedelta
import json
from reportlab.pdfgen import canvas
import pymupdf
tasks={'A':(2,[]),'B':(4,['A']),'C':(3,['A']),'D':(2,['B','C']),'E':(1,['B']),'F':(1,['D','E'])}
es={};ef={}
for k,(dur,pred) in tasks.items():es[k]=max([ef[p] for p in pred],default=0);ef[k]=es[k]+dur
total=max(ef.values());lf={};ls={}
for k,(dur,pred) in reversed(list(tasks.items())):
 succ=[s for s,(_,pr) in tasks.items() if k in pr];lf[k]=min([ls[s] for s in succ],default=total);ls[k]=lf[k]-dur
assert total==9 and {k:ls[k]-es[k] for k in tasks}==dict(A=0,B=0,C=1,D=0,E=1,F=0)
days=[];d=date(2026,10,6)
while len(days)<total:
 if d.weekday()<5:days.append(d)
 d+=timedelta(days=1)
assert days[-1]==date(2026,10,16)
out=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/assets/correzioni-2026-10');out.mkdir(parents=True,exist_ok=True)
pdf=out/'gantt-sportello-digitale.pdf';c=canvas.Canvas(str(pdf),pagesize=(650,470))
c.setFillColorRGB(1,1,1);c.rect(0,0,650,470,fill=1,stroke=0)
c.setFillColorRGB(0,0,0);c.setFont('Helvetica-Bold',22);c.drawString(24,436,'Sportello digitale: nove giorni lavorativi')
c.setFont('Helvetica',18);c.drawString(24,409,'6-16 ottobre 2026 | Attività A-F definite nella tabella')
x0=63;w=62;y0=345;h=45
for j,d in enumerate(days):
 c.setFont('Helvetica-Bold',18);c.drawCentredString(x0+j*w+w/2,374,d.strftime('%d/%m'))
 c.setStrokeColorRGB(.8,.8,.8);c.line(x0+j*w,88,x0+j*w,360)
c.line(x0+9*w,88,x0+9*w,360)
labels=['A Requisiti','B Configurazione','C Bonifica dati','D Caricamento e test','E Manuale e formazione','F Accettazione e avvio']
for i,(k,label) in enumerate(zip(tasks,labels)):
 y=y0-i*h;c.setFillColorRGB(0,0,0);c.setFont('Helvetica-Bold',21);c.drawString(26,y-12,k)
 critical=ls[k]==es[k];c.setFillColorRGB(*((.1,.1,.1) if critical else (.72,.72,.72)))
 c.rect(x0+es[k]*w+3,y-26,(ef[k]-es[k])*w-6,32,fill=1,stroke=0)
 c.setFillColorRGB(*((1,1,1) if critical else (0,0,0)));c.setFont('Helvetica-Bold',19);c.drawCentredString(x0+(es[k]+ef[k])/2*w,y-16,str(tasks[k][0])+' g')
c.setFillColorRGB(0,0,0);c.setFont('Helvetica-Bold',18);c.drawString(24,53,'Nero: percorso critico A-B-D-F = 2 + 4 + 2 + 1 = 9 giorni')
c.setFont('Helvetica',18);c.drawString(24,25,'Grigio: C ed E hanno un giorno di margine totale.')
c.save();doc=pymupdf.open(pdf);doc[0].get_pixmap(matrix=pymupdf.Matrix(1.6,1.6)).save(out/'gantt-sportello-digitale.png')
data={'tasks':{k:{'duration':tasks[k][0],'predecessors':tasks[k][1],'ES':es[k],'EF':ef[k],'LS':ls[k],'LF':lf[k],'float':ls[k]-es[k],'start':str(days[es[k]]),'end':str(days[ef[k]-1])} for k in tasks},'duration':total,'criticalPath':['A','B','D','F'],'verified':True}
Path('artifacts/correzioni-collana-2026-10-02/vol09-project-calculation.json').write_text(json.dumps(data,indent=2),encoding='utf8');print(json.dumps(data))
