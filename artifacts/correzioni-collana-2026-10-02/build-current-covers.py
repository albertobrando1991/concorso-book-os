from pathlib import Path
import json,hashlib,math,re
import pymupdf as fitz
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import CMYKColor

ROOT=Path.cwd(); OUT=ROOT/'delivery/copertine-2026-10-03'; QA=ROOT/'artifacts/correzioni-collana-2026-10-02/cover-qa'
OUT.mkdir(exist_ok=True);QA.mkdir(exist_ok=True)
for name,file in [('Arial','arial.ttf'),('ArialBold','arialbd.ttf'),('Garamond','GARA.TTF'),('GaramondBold','GARABD.TTF')]:
 p=Path('C:/Windows/Fonts')/file
 assert p.exists(),p
 pdfmetrics.registerFont(TTFont(name,str(p)))
NAVY=CMYKColor(.73,.56,0,.76);IVORY=CMYKColor(0,.025,.085,.06);GOLD=CMYKColor(0,.19,.68,.18);RED=CMYKColor(0,.66,.68,.43);INK=CMYKColor(.1,.1,0,.75);WHITE=CMYKColor(0,0,0,0)
PW=6.69*72;PH=9.61*72;BLEED=9;H=PH+18
# Titles transcribed from the current title pages. No business promise from catalog metadata is used as cover copy.
DATA=[
('01','Il Metodo BANDO',['Il Metodo','BANDO'],'Leggere il bando, costruire il piano, studiare le materie comuni e allenarsi sulle prove. Un manuale-workbook per organizzare la preparazione e riutilizzare quanto appreso nei concorsi successivi.',['Metodo di studio e materie comuni della PA','Quiz, scritti, casi e colloquio orale','Bando Decoder, piano di studio e diario degli errori'],'Metodo e materie comuni'),
('02-I','Comuni, Regioni, area vasta e Camere di commercio',['Comuni, Regioni,','area vasta e','Camere di','commercio'],'Il primo tomo sviluppa il percorso per gli enti territoriali e le Camere di commercio. Collega ordinamenti, procedimenti e servizi a casi, esercizi e simulazioni per la preparazione concorsuale.',['Comuni, Unioni e servizi locali','Regioni, Province e Città metropolitane','Camere di commercio e Registro delle imprese'],'Manuale-workbook per i concorsi territoriali'),
('02-II','Polizia locale',['Polizia','locale'],'Il secondo tomo è dedicato alla Polizia locale. Affronta funzioni, procedimenti, controlli e prove attraverso spiegazioni, casi applicativi, quiz commentati e strumenti di ripasso.',['Codice della strada e procedimenti sanzionatori','Polizia amministrativa e sicurezza urbana','Casi operativi e simulazione finale'],'Manuale-workbook per i concorsi territoriali'),
('03','Funzioni centrali, Fisco, Previdenza e Ispettivo',['Funzioni centrali,','Fisco, Previdenza','e Ispettivo'],'Un percorso specialistico per comprendere amministrazioni centrali, funzioni fiscali e previdenziali. Il volume collega istituti e organizzazione alle attività degli uffici e alle prove concorsuali.',['Ministeri e amministrazioni centrali','Agenzie fiscali, riscossione, dogane e accise','Previdenza, assicurazione e attività ispettiva'],'Preparazione ai concorsi pubblici'),
('04','Giustizia e UPP',['Giustizia','e UPP'],'Leggere il sistema Giustizia dalla prospettiva del candidato: comprendere uffici, processi e servizi, applicare le distinzioni fondamentali e costruire risposte motivate.',['Ufficio per il processo, cancelleria e UNEP','Processo civile, penale e giustizia digitale','Spese, casellario, minorile e penitenziario'],'Preparazione ai concorsi pubblici'),
('05','Authority e regolazione',['Authority','e regolazione'],'Comprendere il ruolo delle autorità indipendenti, distinguere i poteri e collegare le regole ai mercati. Spiegazioni, casi e verifiche accompagnano la preparazione alle prove specialistiche.',['Autorità indipendenti e settori regolati','Vigilanza, istruttorie e sanzioni','Economia della regolazione e casi applicativi'],'Preparazione ai concorsi pubblici'),
('06','Scuola, Università, Ricerca, Cultura',['Scuola, Università,','Ricerca, Cultura'],'Percorsi distinti per i concorsi di scuola, università, ricerca e cultura. Lavoro degli uffici, fonti e competenze specialistiche sono collegati a casi, esercizi e strumenti di preparazione.',['Scuola, personale e servizi amministrativi','Università, AFAM ed enti di ricerca','Cultura, patrimonio e istituti culturali'],'Preparazione ai concorsi pubblici'),
('07','Sanità amministrativa e professioni sanitarie',['Sanità','amministrativa','e professioni','sanitarie'],'Il volume organizza percorsi diversi per amministrativi, professioni sanitarie, dirigenza e tecnici. Norme, organizzazione e casi aiutano a preparare le prove nel perimetro del proprio profilo.',['Amministrazione e organizzazione sanitaria','Professioni sanitarie e dirigenza','Tecnici sanitari e prevenzione'],'Preparazione ai concorsi pubblici'),
('08','ICT, digitale, cybersecurity e dati',['ICT, digitale,','cybersecurity','e dati'],'Un percorso per i profili informatici della pubblica amministrazione. Concetti tecnici, trasformazione digitale e casi applicativi sono collegati a esercizi e verifiche della preparazione.',['Sistemi, reti e servizi digitali','Cybersecurity e protezione dei dati','Dati, interoperabilità e trasformazione della PA'],'Preparazione ai concorsi pubblici'),
('09','Appalti, PNRR e procurement',['Appalti, PNRR','e procurement'],'Dalla programmazione all’esecuzione: un percorso per comprendere contratti pubblici, gestione dei fondi e lavoro degli uffici. Casi e simulazioni allenano decisioni motivate e controllo degli adempimenti.',['Programmazione, affidamento ed esecuzione','Procurement e ciclo digitale dei contratti','PNRR, fondi europei e gestione dei progetti'],'Preparazione ai concorsi pubblici'),
('10','Tecnico-ingegneristico, territorio, lavori pubblici',['Tecnico-ingegneristico,','territorio,','lavori pubblici'],'Materie specialistiche, casi e strumenti per le prove dei profili tecnici della pubblica amministrazione. Il percorso collega il quadro normativo alle valutazioni e agli elaborati richiesti al candidato.',['Territorio, edilizia e urbanistica','Lavori pubblici e attività tecniche','Casi, verifiche e strumenti operativi'],'Preparazione ai concorsi pubblici'),
('11','Ambiente, protezione civile e sostenibilità',['Ambiente,','protezione civile','e sostenibilità'],'Un percorso per collegare fonti ambientali, gestione del territorio e sostenibilità. Esempi, casi e strumenti accompagnano lo studio delle competenze specialistiche richieste dai diversi profili.',['Tutela ambientale e controlli','Protezione civile e rischi territoriali','Energia, risorse e sostenibilità'],'Preparazione ai concorsi pubblici'),
('12','Carriere speciali premium',['Carriere speciali','premium'],'Percorsi di orientamento e preparazione per selezioni con requisiti e prove differenti. Il volume aiuta a distinguere le carriere e a organizzare lo studio con casi, schede e verifiche mirate.',['Forze di polizia e Vigili del fuoco','Carriere giuridiche e prove specialistiche','Carriera prefettizia e diplomatica'],'Preparazione ai concorsi pubblici')]

packages=json.loads((ROOT/'artifacts/correzioni-collana-2026-10-02/registro-package-verification.json').read_text('utf8'))['volumes']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def wrap(text,font,size,width):
 lines=[];line=''
 for word in text.split():
  candidate=(line+' '+word).strip()
  if pdfmetrics.stringWidth(candidate,font,size)>width and line:lines.append(line);line=word
  else:line=candidate
 if line:lines.append(line)
 return lines
def para(c,text,x,y,width,font='Garamond',size=13,leading=17,color=INK):
 c.setFillColor(color);c.setFont(font,size)
 for line in wrap(text,font,size,width):c.drawString(x,y,line);y-=leading
 return y

manifest=[]
for key,title,lines,copy,bullets,tagline in DATA:
 vol='VOL-'+key[:2];pv=next(v for v in packages if v['volume']==vol)
 entry=pv['candidatePdfs'][1 if key=='02-II' else 0]
 interior=Path(pv['manifest']).parent/entry['path'];assert sha(interior)==entry['sha256']
 doc=fitz.open(interior);pages=len(doc);kp=pages+(pages%2);spine=kp*.002252*72;W=2*PW+spine+18;fx=BLEED+PW+spine
 file=OUT/f'vol-{key.lower()}-cover.pdf'
 c=canvas.Canvas(str(file),pagesize=(W,H),pageCompression=1,initialFontName='Arial',initialFontSize=10)
 c.setTitle(title);c.setAuthor('');c.setSubject('Metodo BANDO');c.setCreator('');c.setProducer('')
 c.setFillColor(NAVY);c.rect(0,0,W,H,fill=1,stroke=0)
 for left in [BLEED,fx]:
  c.setFillColor(IVORY);c.roundRect(left+23,32,PW-46,H-64,11,fill=1,stroke=0)
 x=fx+57;y=H-82;width=PW-114
 label=f'METODO BANDO  /  VOLUME {int(key[:2])}'+('  /  TOMO '+key.split('-')[1] if '-' in key else '')
 c.setFillColor(RED);c.setFont('ArialBold',9);c.drawString(x,y,label)
 c.setStrokeColor(GOLD);c.setLineWidth(1.5);c.line(x,y-14,x+110,y-14)
 size=36 if len(lines)<3 else 31
 while max(pdfmetrics.stringWidth(l,'GaramondBold',size) for l in lines)>width:size-=.5
 y-=66;c.setFillColor(NAVY);c.setFont('GaramondBold',size)
 for line in lines:c.drawString(x,y,line);y-=size*1.15
 y-=18;y=para(c,tagline,x,y,width,'ArialBold',11,15)
 # The diagram stays below title and tagline and inside the safe panel.
 top=min(y-35,330);bottom=128;gx=fx+PW-75
 c.setStrokeColor(GOLD);c.setLineWidth(1.25);c.line(gx,bottom,gx,top)
 for i in range(5):
  yy=bottom+(top-bottom)*i/4;start=gx-56-12*i
  c.line(start,yy,gx,yy);c.setFillColor(RED if i==2 else NAVY);c.circle(gx,yy,6 if i==2 else 3.5,fill=1,stroke=0)
 c.setFillColor(NAVY);c.setFont('ArialBold',10);c.drawString(x,72,'CAPITALE PERSONALE')
 # Back cover
 bx=BLEED+57;by=H-82
 c.setFillColor(RED);c.setFont('ArialBold',9);c.drawString(bx,by,'DAL BANDO ALLA PROVA')
 c.setStrokeColor(GOLD);c.line(bx,by-14,bx+110,by-14)
 by=para(c,copy,bx,by-52,width,'GaramondBold',14,18,NAVY)-24
 for bullet in bullets:
  c.setFillColor(GOLD);c.circle(bx+2,by+3,2,stroke=0,fill=1)
  by=para(c,bullet,bx+14,by,width-14,'Arial',10.5,15)-14
 common=('Metodo, teoria, esercizi e strumenti cartacei per costruire un percorso di studio riutilizzabile.' if key=='01' else 'Percorso specialistico della collana Metodo BANDO. Per metodo e materie comuni si integra con il manuale base.')
 by=para(c,common,bx,by-10,width,'Garamond',11.5,15)
 assert by>180,(key,by)
 # Reserve the platform barcode zone at lower right of the back, no fake ISBN.
 barcode=(BLEED+PW-18-144,BLEED+18,144,86.4)
 c.setFillColor(WHITE);c.rect(*barcode,fill=1,stroke=0)
 c.setFillColor(NAVY);c.setFont('ArialBold',8.5);c.drawString(bx,72,'CAPITALE PERSONALE')
 # Rotated spine; size reduced only for physical spine width, never below 7 pt.
 center=BLEED+PW+spine/2;fs=min(12,(spine-9)/1.4)
 assert fs>=7,(key,spine,fs)
 short=f'{int(key[:2]):02}'+(' / '+key.split('-')[1] if '-' in key else '')
 spine_text=title
 while pdfmetrics.stringWidth(spine_text,'ArialBold',fs)>PH-150:fs-=.2
 assert fs>=7
 c.saveState();c.translate(center,H/2);c.rotate(90);c.setFillColor(IVORY);c.setFont('ArialBold',fs);c.drawCentredString(0,-fs*.32,spine_text);c.restoreState()
 c.saveState();c.translate(center,H-60);c.rotate(90);c.setFillColor(GOLD);c.setFont('ArialBold',min(fs,9));c.drawCentredString(0,-min(fs,9)*.32,short);c.restoreState()
 c.showPage();c.save()
 pdf=fitz.open(file);page=pdf[0]
 page.get_pixmap(matrix=fitz.Matrix(1.35,1.35),alpha=False).save(QA/f'{key}.png')
 front=page.get_pixmap(matrix=fitz.Matrix(1.2,1.2),clip=fitz.Rect(fx,BLEED,fx+PW,H-BLEED),alpha=False);front.save(QA/f'{key}-front.png')
 spans=[s for b in page.get_text('dict')['blocks'] if 'lines'in b for l in b['lines'] for s in l['spans']]
 outside=[s['text'] for s in spans if not page.rect.contains(fitz.Rect(s['bbox']))]
 assert not outside,(key,outside)
 embedded=all(bool(pdf.extract_font(f[0])[3]) for f in page.get_fonts())
 assert embedded,(key,page.get_fonts())
 manifest.append(dict(key=key,volume=vol,title=title,cover=file.relative_to(ROOT).as_posix(),coverSha256=sha(file),interior=interior.as_posix(),interiorSha256=sha(interior),pdfPages=pages,kdpPages=kp,spineInches=spine/72,widthInches=W/72,heightInches=H/72,bleedInches=.125,fontMinPt=min(s['size'] for s in spans),fontsEmbedded=embedded,encrypted=pdf.is_encrypted,textOutsidePage=outside,visualReviewed=False,authorConfirmed=False,isbnAssigned=False,releaseApproved=False))
 pdf.close();doc.close()

# Review booklet, one full wrap per page at a readable screen size.
overview=fitz.open()
for row in manifest:
 src=fitz.open(row['cover']);page=overview.new_page(width=src[0].rect.width,height=src[0].rect.height);page.show_pdf_page(page.rect,src,0)
overview.save(OUT/'copertine-collana-panorama.pdf',deflate=True);overview.close()
(QA/'cover-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps([{k:r[k] for k in ['key','pdfPages','kdpPages','spineInches','fontsEmbedded','fontMinPt']} for r in manifest],ensure_ascii=False))
