from pathlib import Path
import json,hashlib
A=Path(__file__).parent
rows=json.loads((A/'VOL-06-wide-worksheets.json').read_text(encoding='utf8')); changes=[]
def digest(b):return hashlib.sha256(b).hexdigest()
for r in rows:
 p=Path(r['path']); before=p.read_bytes(); text=p.read_text(encoding='utf8'); table=r['table']; assert table in text
 cells=[[c.strip() for c in l.strip().strip('|').split('|')] for l in table.strip().splitlines()]; blocks=[]
 for row in cells[2:]:
  blocks.append('### '+row[0]+'\n\n| Campo | La tua risposta |\n| --- | --- |\n'+'\n'.join('| '+label+' | '+value+' |' for label,value in zip(cells[0][1:],row[1:])))
 text=text.replace(table,'\n\n'.join(blocks)+'\n',1)
 if p.name=='07-contabilita-scolastica.md':text=text.replace('title: "Contabilita\' scolastica"','title: "Contabilità scolastica"')
 p.write_text(text,encoding='utf8');changes.append({'path':str(p).replace('\\','/'),'before':digest(before),'after':digest(p.read_bytes()),'change':'Scheda a due colonne per scenario, con tutti i campi originari conservati; accento del titolo corretto ove necessario.'})
p=Path('wiki/books/moduli/m-ir01-scuola/chapters/10-relazioni-sindacali-sicurezza-responsabilita.md');b=p.read_bytes();s=b.decode('utf8');s=s.replace('title: "Relazioni sindacali, sicurezza e responsabilita\'"','title: "Relazioni sindacali, sicurezza e responsabilità"');p.write_text(s,encoding='utf8');changes.append({'path':p.as_posix(),'before':digest(b),'after':digest(p.read_bytes()),'change':'Accento del titolo corretto: evita la duplicazione dell’intestazione.'})
(A/'VOL-06-production-native-changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8')
p=A/'M-IR01-freeze.json';f=json.loads(p.read_text(encoding='utf8'));f['controlledPrintCorrections']={'date':'2026-10-03','description':'Cinque schede suddivise per scenario in due colonne e due accenti dei titoli; contenuto dei campi e risposte invariato. Verifica PDF successiva necessaria.','files':changes};p.write_text(json.dumps(f,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'modified':len(changes),'worksheets':len(rows)}))
