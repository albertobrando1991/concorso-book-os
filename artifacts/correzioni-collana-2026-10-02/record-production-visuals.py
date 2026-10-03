from pathlib import Path
import json,hashlib
A=Path(__file__).parent
specs={'08':[6,44,66,163,164,222,237,244],'09':[6,13,106,107,157,212,213,227,240,241,265,266,267],'10':[6,28,30,31,39,79,80,122,123,124,125,126],'11':[6,91,149,167,179,184,191,206,207,225,227,243,244,247,248,249,250]}
for v,pages in specs.items():
 label=f'vol-{v}-release-20261003';pdf=A/(label+'-proof.pdf');audit=A/(label+'-proof-audit');metrics=json.loads((audit/'metrics.json').read_text(encoding='utf8'))
 row={'volume':f'VOL-{v}','date':'2026-10-03','pdf':pdf.as_posix(),'pdfSha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':metrics['pages'],'allContactSheetsViewed':True,'contactSheets':metrics['contacts'],'zoomPagesViewed':pages,'limitations':['Copertura panoramica di ogni pagina per geometria e ritmo; non lettura di ogni parola del raster.','Ingrandimenti limitati alle pagine elencate.','Nessuna prova cartacea, caricamento KDP, certificazione PDF/X o verifica della piattaforma digitale.']}
 if v=='09':
  final=A/'vol-09-final-20261003-proof.pdf';row['finalPdf']=final.as_posix();row['finalPdfSha256']=hashlib.sha256(final.read_bytes()).hexdigest();row['finalChangedPagesViewed']=[266];row['comparisonEvidence']='VOL-09-final-render-comparison.json';row['finalCoverage']='Tutte le267pagine confrontate a scala1.8;266 identiche alla release esaminata, sola266 cambiata e vista ingrandita.'
 if v=='11':row['state']='Release esaminata; delta4master applicato; nuovo PDF ancora da verificare.'
 else:row['state']='Verifica visiva locale conclusa; dipendenza comune digitale/editoriale aperta.'
 (A/f'VOL-{v}-production-visual.json').write_text(json.dumps(row,ensure_ascii=False,indent=2),encoding='utf8')
print('Recorded actual visual coverage for08,09,10,11.')
