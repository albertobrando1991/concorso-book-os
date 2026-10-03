from pathlib import Path
import re,json,hashlib
A=Path(__file__).parent;root=A.parent.parent;changes=[]
for filename in ['07-bando-decoder.md','08-piano-30-60-90-doppio-binario.md']:
 p=root/'wiki/books/moduli/m-sp01-forze-ordine/chapters'/filename;s=p.read_text(encoding='utf8');before=hashlib.sha256(p.read_bytes()).hexdigest()
 if filename.startswith('07'):
  start=s.index('### Scheda personale: un concorso per foglio');end=s.index('## Riferimenti normativi',start);old=s[start:end]
  groups=re.split(r'\*\*(Identità e accesso|Candidatura|Preparazione e controlli successivi)\*\*',old)[1:]
  parts=['### Scheda personale: identità e accesso','', 'Compila una scheda per concorso. Registra identità e accesso, candidatura e preparazione; usa un secondo foglio per un altro concorso.','']
  total=0
  for i in range(0,len(groups),2):
   title,body=groups[i:i+2]
   if i:parts+=['### '+title,'']
   parts+=['| Campo | La tua risposta |','| --- | --- |']
   for line in body.splitlines():
    if ': _' in line:
     field=re.sub(r': _+\s*$','',line);parts.append('| '+field+' | |');total+=1
   parts.append('')
  assert total==16,total
  s=s[:start]+'\n'.join(parts)+'\n'+s[end:]
 else:
  s=re.sub(r'(?<=[A-Za-zàèéìòù]),(?=\d)',', ',s).replace('PSviceispettori','PS viceispettori')
 p.write_text(s,encoding='utf8',newline='\n');changes.append({'path':p.relative_to(root).as_posix(),'beforeSHA256':before,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'change':'Scheda a tre tabelle native: conservati tutti i 16 campi e rimossa separazione tra consegna e campi.' if filename.startswith('07') else 'Ripristinati gli spazi mancanti dopo virgole nel piano orario e in PS viceispettori.'})
p=A/'M-SP01-freeze.json';data=json.loads(p.read_text(encoding='utf8'));data['controlledPrintCorrections']={'date':'2026-10-03','files':changes,'verification':'Correzioni native di stampa autorizzate; verifica PDF pendente.'};p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8');(A/'VOL-12-production-native-changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(changes,ensure_ascii=False))
