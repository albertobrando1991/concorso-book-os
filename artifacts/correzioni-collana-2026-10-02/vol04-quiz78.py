from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-fc04-giustizia/chapters');A=Path('artifacts/correzioni-collana-2026-10-02')
extra={7:["Soltanto quando il giudice pronuncia la sentenza definitiva.","Attendere la richiesta di rinvio a giudizio e svolgere l’interrogatorio soltanto se lo dispone il GUP.","Proscioglimento pronunciato dal pubblico ministero.","Il trasferimento di tutti gli atti d’indagine non contestati dalla cancelleria.","Un quarto, subordinato al consenso del pubblico ministero.","Le garanzie operano soltanto dopo una richiesta scritta del difensore al giudice."],8:["Esclusivamente procedimenti civili di cognizione ordinaria, con esclusione delle esecuzioni.","No: il 45-bis è il registro delle sole sentenze penali irrevocabili.","Una copia conforme munita anche dell’autorizzazione del presidente del tribunale in ogni caso.","Il pubblico ministero, anche se il procedimento è già nella fase dibattimentale.","No: è un dato sottratto a qualsiasi regola di protezione quando la sentenza è pubblica.","Per ogni gestione amministrativa del personale del Ministero della giustizia, indipendentemente dalla finalità."]}
rows=[]
for n,choices in extra.items():
 p=next(B.glob(f'{n:02}-*.md'));t=p.read_text('utf-8');i=0
 def change(m):
  global i
  x='   - D. '+choices[i]+'\n'+m.group(0);i+=1;return x
 t=re.sub(r'(?m)^   \*\*Risposta corretta:',change,t);assert i==6;p.write_text(t,'utf-8')
 rows.extend(dict(chapter=n,question=i+1,addedDistractor=s,keyUnchanged=True) for i,s in enumerate(choices))
(A/'VOL-04-quiz78-uniformazione.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8')
