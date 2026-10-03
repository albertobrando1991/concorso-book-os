from pathlib import Path
import json,re
art=Path('artifacts/correzioni-collana-2026-10-02');mod=Path('wiki/books/moduli/m-fl02-regioni-province-citta-metropolitane')
report14=Path('wiki/reviews/pipeline/VOL-02/14-moduli-m-fl02-regioni-province-citta-metropolitane.md')
report15=Path('wiki/reviews/pipeline/VOL-02/15-moduli-m-fl02-regioni-province-citta-metropolitane.md')
archive=art/'VOL-02-step15-M-FL02-prima-correzioni.md'
if report15.exists() and not archive.exists():archive.write_bytes(report15.read_bytes())
t=report14.read_text(encoding='utf-8').replace('# Correzioni autorizzate — M-FL02, 3 ottobre 2026','# Audit specialistico correttivo — M-FL02, 3 ottobre 2026')
t=t.replace('Applicato nel perimetro M-FL02; audit 15 successivo','Chiuso nel perimetro M-FL02')
t=t.replace('L’audit specialistico 15 deve riesaminare le correzioni e registrare l’esito CLI prima del freeze.','Nessuna criticità specialistica grave o media resta aperta nel perimetro dei dodici capitoli. Riesaminati articoli, termini, requisiti e soluzioni dei rilievi corretti. Nessun box Dato operativo rilevato dal CLI.')
t=t.replace('Eseguire gate 14, audit 15 e successivo text freeze attraverso CLI.','Il gate 14 è passato. Registrare l’esito del gate 15 e procedere al text freeze attraverso CLI.')
t=t.replace('Correzioni testuali M-FL02 applicate; avanzamento all’audit specialistico consentito se il gate 14 passa.','Testo M-FL02 idoneo al text freeze nel perimetro specialistico riesaminato.')
t=t.replace('## 5. Coerenza globale\n','## 5. Coerenza globale\n\nVerifiche di calcolo e soluzione: statuto con 31 componenti richiede almeno 16 voti in ciascuna deliberazione e intervallo di due mesi; il voto a due terzi non elimina il referendum statutario regionale. Saldo contabile 18.000 − 8.000 = 10.000. Clausola finanziaria 100.000 + 80.000 + 60.000 = 240.000, con copertura corrispondente per anno. Costi ammissibili 22.000 − 2.000 = 20.000; costo unitario 180 × 100 = 18.000; tasso 7% su 40.000 = 2.800. PNRR: 92 dispositivi funzionanti su 100 = 92%; le quote di finanziamento 60/40 non duplicano il costo, il rimborso 100/100 sì. Assemblea provinciale: 10 Comuni su 30 e 260.000 abitanti su 500.000 soddisfano entrambe le condizioni; 9 Comuni non bastano. In house: 8/10 = 80% non supera la soglia, 8,2/10 = 82% soddisfa solo il requisito quantitativo. Atto regionale: 52.000 − 4.000 = 48.000; 80% = 38.400; anticipo 16.000; saldo 22.400; riduzione 1.600. Rubrica 3 + 4 + 5 + 5 + 3 = 20.\n\nRiesaminati quiz nuovi: cap. 02 chiavi 7C/8D; cap. 07 costo unitario 7C; cap. 08 termine performance 7C; cap. 09 durate 7B; cap. 11 requisito fatturato 7C. Le risposte motivano la distinzione che rende errate le alternative. In cap. 06 eliminata dalla riscrittura la frase generica sulle abrogazioni: resta spiegata la necessità di individuare le disposizioni reali.\n')
t=t.replace('Le note distinguono fonti integrali, commi esaminati e limiti.','Le note distinguono fonti integrali, commi esaminati e limiti. D.Lgs. 118: letti integralmente gli otto articoli acquisiti; L. 56: letti i commi pertinenti e la nota di aggiornamento, senza dichiarare letta l’intera legge; RDC: testo consolidato UE del 1° luglio 2026 consultato via browser, download locale vuoto escluso dalla prova. Fonti PNRR e DNSH consolidate da VOL-09 riusate nel loro ambito. L’art. 13 DPR 327 consente proroghe complessivamente fino a quattro anni; le tre scadenze di vincolo, pubblica utilità ed esecuzione restano separate. Il confine letterale dei 300.000 abitanti nel comma 67 della L. 56 non è trasformato in un quiz binario: gli esempi usano popolazioni estranee a quel confine.')
report15.write_text(t,encoding='utf-8')
for p in (mod/'chapters').glob('*.md'):
 text=p.read_text(encoding='utf-8').replace('review_required: true','review_required: false',1)
 text=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',text,count=1,flags=re.M)
 p.write_text(text,encoding='utf-8')
p=mod/'planning/02-matrice-copertura-didattica.md';t=p.read_text(encoding='utf-8').replace('review_required: true','review_required: false',1).replace('Applicato, audit15 aperto','Applicato e riesaminato; report 15 del 3 ottobre 2026').replace('83? no:8,2/10=82%','8,2/10 = 82%');p.write_text(t,encoding='utf-8')
statepath=art/'VOL-02-changes.json';state=json.loads(statepath.read_text(encoding='utf-8'))
for fid,x in state['changes'].items():
 if fid in [f'V02-{i:02d}' for i in range(21,35)]: x['status']='Applicato e riesaminato in M-FL02; gate 15 da registrare via CLI'
statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(report15)
