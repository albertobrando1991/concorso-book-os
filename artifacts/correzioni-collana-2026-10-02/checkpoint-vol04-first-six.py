from pathlib import Path
import json,hashlib,re
A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc04-giustizia/chapters')
rows=[]
for n in range(1,7):
 p=next(B.glob(f'{n:02}-*.md'));t=p.read_text('utf-8');quiz=t.split('### Quiz commentato')[1].split('### Checklist')[0]
 keys=re.findall(r'Risposta corretta: ([ABC])',quiz);assert len(keys)==6
 rows.append(dict(chapter=n,path=p.as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),quizKeys=keys,applied=True,finalAuditPassed=False))
(A/'VOL-04-progress.json').write_text(json.dumps({'date':'2026-10-03','chapters':rows,'partialChapters':[12,17],'remainingRoot':[7,8,9,10,11,12,15,16,17],'agent06':[13,14],'publicationReady':False},ensure_ascii=False,indent=2),'utf-8')
report='''# VOL-04 — Applicazione in corso, 3 ottobre 2026

Il rapporto originario e i suoi29rilievi restano immutabili. Applicati i primi sei capitoli, con36quiz specifici, ma non ancora eseguito il riesame complessivo né l'audit specialistico finale. Pipeline13 in corso; nessuna autorizzazione a pubblicare.

| Rilievi | Intervento | Stato reale |
|---|---|---|
| V04-01 | Distinte funzioni giudicante/requirente; corretto esempio civile/penale. | Applicato cap1, da riesaminare. |
| V04-02 | Organigramma DIT e fonti aggiornati; prima propagazione cap12. | Applicato in parte; cap12 ancora da integrare. |
| V04-03 | DAG/DOG e direzioni, mappa uffici/composizione/territorio, GIP/GUP e doppia dirigenza. | Applicato cap2–3, da riesaminare. |
| V04-04 | Conversione DL100/L145 corretta, quiz4 riscritto, fonti e indice rettificati. | Applicato; controllare apparati finali e DL144 al freeze. |
| V04-05 | UPP artt1–4, struttura/personale, compiti residuali cancelleria nel coordinato. | Applicato cap4, da riesaminare. |
| V04-06 | Dossier8documenti, cronologia, scheda causa, nota ricerca, promemoria udienza e soluzione. | Applicato cap5; appendice15 ancora da fare. |
| V04-07 | CPC166/171bis/171ter, riti, provvedimenti, impugnazioni e calendario risolto. | Applicato cap6, calcoli verificati; audit finale pendente. |
| V04-27/28 | 36quiz riscritti cap1–6, primi refusi corretti. | Parziale sul volume. |

Le altre voci restano aperte. Capitoli13–14 assegnati al revisore dei volumi06/07/12, ora libero dopo chiusura testuale diVOL12; due dossier separati destinati al successivo cap15, senza modifica concorrente del capitolo. Root prosegue07–12e15–17.

Fonti nuove: organizzazione/UPP e processo civile del3ottobre. Acquisizione193articoli non equivale a lettura: primi estratti ordinamento e minori erano articoli di approvazione; esclusi dall'uso. Ordinamento-allegato corretto, minori in riacquisizione. La vigenza differita prevale sulle date superate delle pagine divulgative istituzionali.

Evidenze: `VOL-04-progress.json`, delta first/uffici/civile/fascicolo/org-propagation e backup nella cartella artefatti. Nessun nuovo PDFVOL04prodotto prima della chiusura testuale.
'''
(R/'VOL-04.md').write_text(report,'utf-8')
f=A/'figure-vol01-corrette-manifest.json';m=json.loads(f.read_text('utf-8'));pages=json.loads((A/'VOL-01-figure-page-map.json').read_text('utf-8'))
for row in m:
 page=next(x['page'] for x in pages if Path(row['newAsset']).name==Path(x['asset']).name)
 row['printProofReview']={'pdf':'vol-01-print-20261003-proof.pdf','page':page,'result':'Pagina completa esaminata: etichette leggibili, diagramma e didascalia non sovrapposti; non equivale a prova fisica.'}
f.write_text(json.dumps(m,ensure_ascii=False,indent=2),'utf-8')
freeze=json.loads((A/'M-PA01-freeze.json').read_text('utf-8'))
p=Path('wiki/reviews/pipeline/VOL-01/16-il-metodo-bando.md');t=p.read_text('utf-8')
for row in freeze['files']:
 assert hashlib.sha256(Path(row['path']).read_bytes()).hexdigest()==row['sha256'],row['path']
 t=re.sub(r'(\| '+re.escape(row['path'])+r' \| )[0-9a-f]{64}',lambda x:x.group(1)+row['sha256'],t)
if 'Delta controllato delle figure di stampa' not in t:t+='\n\n## Delta controllato delle figure di stampa\n\nDiciannove asset sostituiti con versioni a etichette grandi; alt/caption allineati e precisata distinzione quiz/prova pratica nel capitolo10. Hash aggiornati nel manifest M-PA01-freeze.json, storico nei delta VOL-01-print-figure*.json. Viste tutte19pagine interessate nella prova675pagine; verifica complessiva PDF ancora aperta.\n'
p.write_text(t,'utf-8')
p=Path('wiki/index.md');t=p.read_text('utf-8');s='vol-04-processo-civile-verifica-2026-10-03'
if s not in t:p.write_text(t+f'\n- [[sources/{s}]] — termini, riti e calendario verificati per il volume Giustizia.\n','utf-8')
with Path('wiki/log.md').open('a',encoding='utf-8') as f:f.write('\n\n## 2026-10-03 — Giustizia primi sei capitoli e nuove prove PDF\n\nApplicati cap01–06VOL04,36quiz, mappa uffici/doppia dirigenza, UPP coordinato, dossier8documenti e CPCcon calendario; fonti/topic/entitycollegati, auditfinaleaperto. VOL01nuova prova675pagine:19figure corrette viste integralmente su pagina,43contatti ancora da esaminare. VOL11prova253p eVOL12prova487p,zerooverflowautomatici; visiva pendente. Nessuna pubblicabilità finale.\n')
print('Checkpoint registrato; 6capitoli36quiz; manifest19figure e freezehash allineati')
