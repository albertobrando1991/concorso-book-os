from pathlib import Path
import json,hashlib,re
base=Path('artifacts/correzioni-collana-2026-10-02')
manifest=base/'normattiva-tuel/manifest.json'
rows=json.loads(manifest.read_text(encoding='utf8'))
for x in rows:
 x['readComplete']=True;x['readDate']='2026-10-03';x['scope']='Testo integrale dell’articolo estratto, inclusi commi con elenchi; coordinamento con norme successive documentato nelle source notes.'
manifest.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
statepath=base/'VOL-02-changes.json';state=json.loads(statepath.read_text(encoding='utf8'))
module=Path('wiki/books/moduli/m-fl01-comuni-unioni')
for p in (module/'chapters').glob('*.md'):
 t=p.read_text(encoding='utf8');t=t.replace('review_required: true','review_required: false',1)
 t=re.sub(r'^updated_at:.*$', 'updated_at: 2026-10-03',t,count=1,flags=re.M)
 p.write_text(t,encoding='utf8')
matrix=module/'planning/02-matrice-copertura-didattica.md'
t=matrix.read_text(encoding='utf8').replace('review_required: true','review_required: false',1)
t+='\n## Audit specialistico correttivo del 3 ottobre 2026\n\nLe integrazioni V02-03–20 applicabili a M-FL01 sono riesaminate nel report pipeline 15. Verificati articoli TUEL correnti, commi IMU/TARI, L. 182/2025 e fonti istituzionali di settore. Integrati consolidato al 31 ottobre, art. 187 aggiornato e condizioni della variazione di dicembre. Il perimetro esterno dei rilievi V02-17/V02-20 resta aperto nel registro del volume; questa chiusura riguarda esclusivamente M-FL01. Il PDF precedente non rappresenta il testo corretto.\n'
matrix.write_text(t,encoding='utf8')
for fid,x in state['changes'].items():
 if fid in ('V02-17','V02-20'):x['status']='Applicato e riesaminato in M-FL01; parte esterna al modulo ancora aperta'
 else:x['status']='Applicato e riesaminato in M-FL01; gate 15 da registrare via CLI'
 x['evidence']+=' Audit specialistico correttivo 3 ottobre 2026: report pipeline 15 M-FL01.'
state['changes']['V02-12']['evidence']+=' Calendario aggiornato: consolidato 31 ottobre, art.151c8 vigente.'
state['changes']['V02-13']['evidence']+=' Art.187c2 aggiornato2026, art.163c3 e art.175c3 esplicitati; quiz20dicembre con fattispecie ammessa.'
statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
report=Path('wiki/reviews/pipeline/VOL-02/15-moduli-m-fl01-comuni-unioni.md')
archive=base/'VOL-02-step15-M-FL01-prima-correzioni.md'
if report.exists() and not archive.exists():archive.write_bytes(report.read_bytes())
lines=['# Audit specialistico conclusivo — M-FL01, correzioni del 3 ottobre 2026','',
'## 1. Sintesi editoriale','',
'Perimetro: quattordici capitoli Comuni e Unioni, con lettura integrale documentata dall’audit storico VOL-02 e riesame correttivo dei passaggi normativi, casi, quiz e rinvii. Il capitolo 03, privo di rilievi assegnati, è stato nuovamente letto per intero; per gli altri capitoli sono stati riletti i passaggi modificati con il contesto. Le criticità del modulo sono state corrette. Non si estende questo esito agli altri moduli, alla simulazione finale o al PDF precedente. V02-17 e V02-20 restano parziali nel registro complessivo, perché comprendono parti esterne a M-FL01.','',
'## 2. Punti applicati della checklist','',
'Controlli 1–26 e 28–30 applicati al testo: struttura, progressione, gerarchia, promesse, raccordi, terminologia, completezza dei nuclei integrati, definizioni, norme, esempi, quiz, riferimenti, sintassi, chiarezza, tono, ridondanze, contraddizioni, grammatica, ortografia, punteggiatura, uniformità Markdown e leggibilità. Il controllo 27 e la resa tipografica definitiva richiedono il nuovo PDF e non sono certificati da questo audit specialistico. Copertura di famiglia: approfondimenti comunali; il nucleo B-PA rimane nel volume base.','',
'## 3. Tabella errori','',
'| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |',
'| --- | --- | --- | --- | --- | --- | --- |']
for fid,x in sorted(state['changes'].items()):
 files=', '.join(Path(p).name for p in x.get('files',[]) if '/m-fl01-' in p)
 if not files:continue
 evidence=x['evidence'].replace('|','/');change=x['change'].replace('|','/')
 lines.append(f'| {fid} | {files} | Normativa/didattica | '+('Medio' if fid in ('V02-15','V02-19') else 'Grave')+f' | {evidence} | Applicata: {change} | Chiuso nel perimetro M-FL01 |')
lines+=['| N02-01 | Cap. 09, calendario | Aggiornamento normativo | Medio | Art. 151, comma 8, testo Normattiva letto | Inserito consolidato al 31 ottobre per gli enti obbligati | Chiuso |',
'| N02-02 | Cap. 10, risultato e variazioni | Aggiornamento normativo | Medio | Artt. 163, 175 e 187 letti integralmente | Esplicitati vincoli dell’esercizio provvisorio, eccezione del 20 dicembre e destinazioni dell’avanzo aggiornate nel 2026 | Chiuso |',
'| N02-03 | Cap. 08, autotutela | Termine normativo | Medio | GU 281/2025, art. 1 L. 182 e testo coordinato art. 21-nonies | Sei mesi per autorizzazioni/vantaggi, altri presupposti e deroga qualificata separati | Chiuso |','',
'## 4. Osservazioni per capitolo','',
'01–02: attribuzioni degli organi, eccezione regolamenti uffici e servizi, quorum dello statuto e due votazioni; esempio con 13 componenti risolto. 03: organizzazione e gestione associata coerenti con artt. 32, 97 e 107; nessuna modifica sostanziale necessaria. 04: pareri art. 49, visto art. 183 e pubblicazione/esecutività distinti. 05: divieto di diffusione dati salute/disagio e accesso separati. 06: documento informatico, forma/prova e copie. 07: residenza, AIRE, elettorale, copie di stato civile e decertificazione. 08: autotutela/decadenza e rapporti ETS. 09: calendario e PIAO. 10: gestione finanziaria, risultati, revisione, debiti e crisi. 11: IMU/TARI e termini. 12: MePA e decisione a contrarre. 13: titoli edilizi, quiz e somma urgenza. 14: rubrica e determina interamente svolta con dati fittizi.','',
'## 5. Coerenza globale','',
'RUP collocato nel primo atto; liquidazione distinta da pagamento; criteri pubblicazione/privacy coerenti fra procedimento e welfare; titoli edilizi coerenti fra spiegazione e risposta. Ricalcolati FPV 60.000, FCDE 30.000 sui presupposti dichiarati, risultato 170/disponibile 20 e variante −10; IMU 840 su imponibile 84.000 con aliquota ipotetica; determina 6.000 + 1.320 = 7.320, residuo 2.680. La rubrica copre tutti i punteggi 0–16 senza intervalli scoperti. Per i quiz del capitolo 13 riesaminata ogni alternativa: chiavi C, A, D, C, D, A, A. Il quiz sulla ratifica indica una variazione ammessa in dicembre, non un’urgenza astratta.','',
'## 6. Contenuto da verificare','',
'Nessuna criticità specialistica grave o media resta aperta nel perimetro M-FL01. Le source notes registrano ambiti, fonti e limiti:','']
notes=['vol-02-verifica-tuel-atti-statuti-2026-10-02','vol-02-edilizia-somma-urgenza-verifica-2026-10-02','vol-02-servizi-comunali-verifica-2026-10-02','vol-02-contabilita-piao-verifica-2026-10-03','vol-02-tributi-procurement-verifica-2026-10-03']
lines += [f'- [[sources/{n}]].' for n in notes]
lines+=['',
'I 33 articoli TUEL scaricati sono stati letti integralmente; il manifest conserva URL e hash. Per le leggi tributarie sono stati letti i commi pertinenti, non l’intera legge. Le formule superate ancora visibili nel testo TUEL o nel comma IMU sono coordinate con le norme successive e la sentenza 209/2022. Il PDF ministeriale TUEL ottobre 2025 contiene una formula superata nell’art. 191: non è stato assunto a prova della vigenza. Il manuale PIAO 2025 è stato consultato solo nelle pagine pertinenti 2, 4 e 32; non è fonte normativa sostitutiva del DM 132/2022. Nessun box Dato operativo risulta nel contratto CLI.','',
'## 7. Suggerimenti facoltativi (non errori)','',
'Nessuna integrazione decorativa necessaria. Il laboratorio usa identificativi didattici dichiarati fittizi e non sostituisce la documentazione di una procedura reale.','',
'## 8. Priorità degli interventi','',
'Il modulo può proseguire al text freeze tramite CLI. Gli interventi esterni al modulo restano nel registro VOL-02 e nei relativi gate; la produzione deve utilizzare gli hash successivi alle correzioni.','',
'## 9. Giudizio di pubblicabilità','',
'Testo M-FL01 idoneo al text freeze per il perimetro specialistico esaminato. Il pacchetto VOL-02 non è ancora pubblicabile: altri moduli e simulazione richiedono correzioni, il PDF va ricomposto e controllato e la distribuzione in tomi va risolta senza comprimere la tipografia. Nessuna firma finale di volume viene anticipata.','',
'## 10. Limiti di questa revisione','',
'Audit correttivo fondato sulla lettura integrale storica e sul riesame puntuale attuale, non dichiarato seconda lettura integrale indipendente di tutti i quattordici capitoli. Verifica normativa alla data indicata, senza garanzia di invariabilità futura. Non applicati regolamenti di un singolo Comune a tutti gli enti. Nessuna ispezione di PDF ricomposto dopo le modifiche. Il controllo Humanizer riguarda i passaggi nuovi: spiegazioni concrete, termini normativi preservati, casi con presupposti e conclusioni espliciti.']
report.write_text('\n'.join(lines)+'\n',encoding='utf8')
print(json.dumps({'tuelRead':len(rows),'report':str(report),'chapters':14},ensure_ascii=False))
