from pathlib import Path
import json,re
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-ir01-scuola');R=Path('wiki/reviews/pipeline/VOL-06');C=Path('wiki/reviews/correzioni-collana-2026-10-02')
changes=json.loads((A/'VOL-06-changes.json').read_text())['changes']
p=B/'planning/02-matrice-copertura-didattica.md';t=p.read_text();t=re.sub(r'^status:.*$','status: coverage_reconciled',t,flags=re.M);t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M)
t=t.replace("Lo stato `completo` attesta la progettazione didattica: per ogni nucleo sono definiti teoria, applicazione, output e verifica in un capitolo preciso dell'indice. Non attesta la redazione o pubblicazione del capitolo, che appartiene alla fase C. Fonti mobili e norme settoriali restano soggette a review normativa prima della redazione finale.","La tabella descrive il perimetro didattico del modulo. Il riesame del 3 ottobre 2026 collega i concetti al testo effettivo e alle evidenze sotto elencate. `Completo` è limitato a questo perimetro: non comprende tutti i programmi disciplinari docenti o tutti i bandi e non attesta la pubblicabilità del PDF.")
t=t.replace('[[sources/prove-concorsuali-quiz-scritto-orale-dpr-487-1994]], ','')
i=t.index('\n## Blocker ordinati');t=t[:i]+'''
## Evidenze della riconciliazione del 3 ottobre 2026

| Capitoli | Teoria e applicazione effettiva | Verifica |
| --- | --- | --- |
| 01–02 | Quattro profili, sistema statale/paritario, cicli, obbligo e autonomia | Decoder e caso sui limiti dell’autonomia |
| 03 | Organi, composizioni, competenze e quorum | Consiglio di 19 componenti, quorum 10; caso PTOF |
| 04 | DS/collegio/consiglio nel PTOF, RAV/PdM/rendicontazione e SNV | 35%→28%, −7 punti e −20% relativo, obiettivo 25% non raggiunto |
| 05–06 | Pratica di trasferimento, confini privacy/competenza, piano ATA, area EQ | Nota istruttoria risolta, rubrica, carico 90+20−50=60 |
| 07–08 | D.I.129, fasi entrata/spesa, termini, residui, inventario e DNSH | 30.000+10.000−15.000=25.000; trasferimento inventariale di un computer |
| 09–10 | Art.25, relazioni CCNL2025, sicurezza scuola/ente edilizio | Decisione motivata e caduta di frammenti: protezione prima della protocollazione |
| 11 | Modelli psicopedagogici selezionati, PEI/PDP/GLO/GLI, D.L.170/2026 | Caso assistenza/autonomia, sei quiz con soluzioni e commenti |
| 12 | Metodologie, O.M.3/2025, sei aree DigCompEdu | Casi valutativi, progettazione e domande commentate |
| 13 | Lezione originale completa su frazioni equivalenti | Traccia, materiali, 60 minuti, verifica 3/6=1/2 e rubrica |

Le fonti nazionali puntualmente verificate sono documentate nelle source note; il bando scelto resta necessario per requisiti, programma e formato della prova. I riferimenti a DVR, atti locali e misure progettuali indicano il documento competente senza inventarne il contenuto. Il D.L.170/2026 va seguito nella conversione successiva alla data editoriale.

## Limite di formato e controlli successivi

I 13 capitoli conservano il formato legacy: non sono dichiarati formato 2 né artificiosamente suddivisi in nuclei da 600 parole. Conteggi reali per capitolo in `artifacts/correzioni-collana-2026-10-02/M-IR01-surface-counts.json`; i target di progetto non sono una soglia usata per aggiungere riempitivi. Le appendici scolastiche promesse nel vecchio piano sono ricondotte agli esercizi nei capitoli 05–13, senza dichiarare esistente un verticale per ogni disciplina. Audit specialistico e nuovo PDF restano passaggi separati.
''';p.write_text(t,encoding='utf8')
p=Path('wiki/topics/m-ir01-scuola-fonti-e-profili.md');t=p.read_text();t+='''
## Correzioni del 3 ottobre 2026

Capitoli 02–10 ampliati con ordinamenti, organi e quorum, PTOF/SNV, trasferimento, piano ATA, fasi contabili, inventario, relazioni sindacali e sicurezza. Fonti puntuali in [[sources/fonti-ufficiali-m-ir01-scuola-2026-07-24]]. Capitoli 11–13 raccordati a [[sources/programmi-concorsi-docenti-dm-205-206-2023]], [[sources/inclusione-scolastica-disabilita-dsa-dlgs-66-2017-legge-170-2010]] (incluso D.L.170/2026) e [[sources/valutazione-e-competenze-digitali-docenti-dlgs-62-2017-om-172-digcompedu]] (O.M.3/2025). La matrice corrente documenta teoria, esempi e verifiche; il PDF deve essere rigenerato e ispezionato.
''';p.write_text(t,encoding='utf8')
p=Path('wiki/books/volumi/vol-06-scuola-universita-ricerca-cultura/planning/01-indice-analitico.md');t=p.read_text();t=t.replace('Appendici: ATA; DSGA; dirigenza scolastica; disciplina e didattica; piano e simulazioni. Target: 35.000 parole.','Apparati effettivi integrati nei capitoli: pratica ATA e rubrica nel 05; piano e casi DSGA nei 06–08; scenari DS nei 09–10; quiz e progettazione nei 11–13. Non sono previste appendici separate per ogni disciplina docente. Il precedente target di 35.000 parole resta un riferimento progettuale, non una dichiarazione di lunghezza effettiva.');p.write_text(t,encoding='utf8')
p=B/'index.md';t=p.read_text();t=t.replace('outline_ready','editorial_revision').replace('outline-ready','editorial-revision').replace('scaffold pronto per scrittura','testo corretto; audit specialistico e PDF da completare').replace('Scuola, personale ATA, DSGA, profili amministrativi scolastici e concorsi correlati.','Scuola: assistente amministrativo ATA, DSGA/EQ, dirigente scolastico e nucleo pedagogico-progettuale dei docenti.');t=t.split('\n## Prossimo passo')[0];t+='\n## Capitoli per il lettore\n\n'
for c in sorted((B/'chapters').glob('*.md')):
 title=re.search(r'^title: "(.*)"',c.read_text(),re.M).group(1);t+=f'- [[books/moduli/m-ir01-scuola/chapters/{c.stem}|{c.name[:2]} — {title}]]\n'
t+='\n## Stato della revisione\n\nCorrezioni autorizzate del 3 ottobre 2026 presenti; audit specialistico e verifica del nuovo impaginato sono tracciati separatamente nella pipeline.\n';p.write_text(t,encoding='utf8')
p=R/'14-moduli-m-ir01-scuola.md';arc=C/'archive'/'pre-correzioni-14-m-ir01.md'
if not arc.exists():arc.write_bytes(p.read_bytes())
rows=[]
for n in range(1,9):
 fid=f'V06-{n:02}';x=changes[fid];rows.append(f"| {fid} | Capitoli e fonti nel registro per ID | Testo e copertura | Grave | {x['change']} | {x['evidence']} | Corretto |")
p.write_text('''# M-IR01 — Correzioni editoriali del 3 ottobre 2026

Il nuovo mandato applica i rilievi V06-01–08 dell’audit integrale. La precedente dichiarazione di assenza di errori è conservata in archivio e non descrive più il lavoro corrente. Corretti anche la quota scolastica di DNSH (V06-23), i residui interni (V06-33) e le promesse di appendici (V06-35); questi ID restano aperti nel registro di volume finché tutti i moduli pertinenti sono corretti.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''+ '\n'.join(rows)+'''

## Evidenze

Registro dettagliato: [[reviews/correzioni-collana-2026-10-02/VOL-06]]. Le fonti sono consolidate prima del testo, con copie dei consolidati in raw e hash. Controllati i passaggi normativi insegnati: O.M.3/2025; DigCompEdu; D.Lgs.297 organi e quorum; art.25 D.Lgs.165; D.I.129; CCNL 2025 e disposizioni compatibili precedenti; D.Lgs.81 art.18; D.L.170/2026 PEI. I riscontri sono selettivi, non una certificazione di ogni atto del corpus.

Risolti i casi numerici e i sei quiz del capitolo 11; verificata la coerenza fra obiettivi, materiali, soluzione e rubrica della lezione. Riletti i delta e i raccordi. Rimossi dal corpo i wikilink interni, archiviata la sezione di review e corretti gli accenti ASCII. Riferimenti finali leggibili aggiunti ai 13 capitoli. Matrice e indice raccordati ai contenuti effettivi.

## Limiti

Formato legacy conservato secondo la regola per interventi fuori dagli step 08–12. Non si dichiara formato 2 né una lunghezza minima non raggiunta. Conversione del D.L.170/2026 da controllare per aggiornamenti successivi al 3 ottobre. Il nuovo PDF non è ancora verificato; nessuna dichiarazione di pubblicabilità.
''',encoding='utf8')
print('Raccordi e report 14 IR01 scritti')
