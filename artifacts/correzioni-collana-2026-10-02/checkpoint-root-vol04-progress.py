from pathlib import Path
import json,re,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc04-giustizia/chapters')
rows=[]
for n in [*range(1,12),13,14]:
 p=next(B.glob(f'{n:02}-*.md'));t=p.read_text('utf-8');keys=re.findall(r'Risposta corretta: ([A-D])',t)
 rows.append(dict(chapter=n,path=p.as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),quizKeys=keys,applied=True,finalAuditPassed=False))
(A/'VOL-04-progress.json').write_text(json.dumps({'date':'2026-10-03','chapters':rows,'remainingRoot':[12,15,16,17],'publicationReady':False,'notes':'13capitoli applicati,78quiz;12digitale eapparati ancora da completare. NessunPDFfinale04.'},ensure_ascii=False,indent=2),'utf-8')
p=Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-04.md');p.write_text(p.read_text('utf-8')+'''\n\n## Aggiornamento successivo — capitoli01–11 e13–14 applicati

Il precedente avanzamento dei primi sei capitoli è superato da questo checkpoint:13capitoli applicati,78quiz riscritti; restano12e15–17, riesame trasversale, matrice e gate, PDF. Non è attestata pubblicabilità.

| ID | Intervento aggiuntivo | Stato |
|---|---|---|
| V04-08/09 | Cap7: CPP335/45bis,415bis,indagini,archiviazione,riti,impugnazioni; cronologia fittizia e6quiz; correttoUPPProcura. | Applicato, audit finale pendente. |
| V04-10/11 | Cap8: registri,modelli,accesso76dispCPC/116CPP,475duplicato,GDPR9/10/51; duecasi e6quiz. | Applicato, audit finale pendente. |
| V04-12/13 | Cap9: soglia13659.64 e famiglia,CUscaglioni43minimo,Corte137,liquidazioni/rimedi,248c3bis,SPEdiGIUS nazionale;6quiz. | Applicato, audit finale pendente. |
| V04-14/15 | Cap10: qualitàimputato,menzionabilità/eliminazione,25bisobbligo,validità6mesi,PDND/QuiCasellario,40;dossier4richieste6quiz. | Applicato, audit finale pendente. |
| V04-16/17 | Cap11:139/140/143,Corte3/2010,relata,titolo/precetto10/90/45,pignoramenti492bis,offerta;mappa4col,calendariocalcolato,verbale negativo6quiz. | Applicato, audit finale pendente. |
| V04-20–24 | Cap13/14: minorile,MAP,riparativa,misure/comunità/penitenziario;12quiz. | Handoffagente ricevuto; vediVOL-04-cap13-14.md. |
| V04-27/28 | 78quizsu84riscritti,primi refusi e strumenti concreti. | Parziale:12eapparati da completare. |

Fonti nuove per penale,cancelleria,spese,casellario,UNEP,minorile-penitenziario consolidate prima delle modifiche. Source UNEP registra esplicitamente rawapprovazione/CAPTCHA esclusi e acquisizioni alternative. Simulazioni minorile/penitenziario pronte inART/VOL-04-simulazioni-minorile-penitenziario.md, ancora da integrare nel15.
''','utf-8')
with Path('wiki/log.md').open('a',encoding='utf-8') as f:f.write('\n\n## 2026-10-03 — Correzioni Giustizia avanzate\n\nApplicati07–11con fonti consolidate,casi,30quiz; ricevuti13–14con12quiz e2dossier. Totale13capitoli78quiz, restano12eapparati, audit ePDF. Nuoveprove06(612p),07(448p),08(243p)con0overflowautomatici;visivaancoraaperta. Nessuna pubblicabilità finale.\n')
print('Checkpoint13capitoli',sum(len(r['quizKeys']) for r in rows),'quiz')
