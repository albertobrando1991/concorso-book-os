from pathlib import Path
import re,json,hashlib,sys,shutil
A=Path(__file__).parent;B=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue');R=Path('wiki/reviews/pipeline/VOL-09')
mode=sys.argv[1]
if mode=='audit':
 for p in sorted((B/'chapters').glob('*.md')):
  t=p.read_text(encoding='utf8');t=re.sub(r'^review_required:.*$','review_required: false',t,flags=re.M);t=re.sub(r'^status:.*$','status: reviewed_text',t,flags=re.M);p.write_text(t,encoding='utf8')
 t=(R/'14-moduli-m-tr02-appalti-pnrr-fondi-ue.md').read_text(encoding='utf8')
 t=t.replace('# Report editoriale — VOL-09 Appalti, PNRR e fondi UE','# Audit specialistico conclusivo — VOL-09 Appalti, PNRR e fondi UE')
 t=t.replace('## 6. Contenuto verificato e fonti','''## 6. Contenuto verificato e fonti

Audit dello step 15: nessun box «Dato operativo» rilevato dal CLI. Riesaminati soglie, termini, presupposti, deroghe, effetti e casi descritti nelle tredici note consolidate. Nessun errore grave o medio noto resta aperto nel testo; `review_required` dei capitoli passa a false soltanto per questo perimetro. La produzione resta da verificare.

| ID | File e posizione | Categoria | Gravità | Evidenza consolidata | Correzione applicata | Stato finale |
| --- | --- | --- | --- | --- | --- | --- |
| A09-01 | Cap.2, governance/qualificazione | Norma | Grave originaria | artt.15,62,63; I.2 e II.4, fonte governance | Soglie, livelli, requisiti e RACI con modello dichiarato | Chiuso |
| A09-02 | Cap.3 e 14, programmazione | Coerenza normativa | Media | art.37, fonte programmazione e laboratorio | Uniformato 140.000 beni/servizi contro 150.000 lavori; 234.000 nel caso | Chiuso |
| A09-03 | Cap.4–5, gara/sotto soglia | Norma e calcoli | Grave originaria | artt.14,17,48–52,94–108, fonti gara e sotto soglia | Confini UE/nazionali, RTI, rimedi alle carenze, griglia OEPV risolta | Chiuso |
| A09-04 | Cap.6–7, digitale/Consip | Procedure | Grave originaria | artt.19–36,32,59; commi449/450/510/512/516 e DPCM2026 | Obblighi e strumenti distinti; prova dei commi dalle pagine corrette | Chiuso |
| A09-05 | Cap.8, esecuzione | Norma e termini | Grave originaria | artt.60,116,119–126,215; allegati; DD743/2026 | Regimi, tempi e calcoli; assenza tetto generale 30% subappalto | Chiuso |
| A09-06 | Cap.9, tutela | Norma processuale | Grave originaria | artt.18,35–36,55,210–213,220; CPA120 | 10/30/32 distinti; eccezioni e blocco cautelare, rimedi in esecuzione | Chiuso |
| A09-07 | Cap.10, PNRR | Architettura e calendario | Grave originaria | RRF; COM2025/310; guidaPCM16aprile2026; esempioDPO | Sette missioni, CID, prevalidazione/validazione; agosto/settembre trascorsi | Chiuso |
| A09-08 | Cap.11, spesa/antifrode | Norma e caso | Grave originaria | L136, L3, DL66, D231; art61Reg2024/2509 | Fatture, filiera, quote >25%, conflitto; riconciliazione 122.000 euro | Chiuso |
| A09-09 | Cap.12, ambiente | Norma e prove | Grave originaria | art17tassonomia; DNSH2024scheda3; art57; DM254/2022 | Notebook con prove pertinenti; minimo CAM distinto da premio | Chiuso |
| A09-10 | Cap.13–14, progetto/laboratorio | Metodo e coerenza | Media | PM²3.1; fonte casi; verifica-esempi.json | C sempre bonifica dati, rete 9/10/11 giorni; dieci soluzioni | Chiuso |
| A09-11 | Cap.4,8,12,14, numeri | Refuso | Lieve | Ricalcolo indipendente dei casi | Rimossi spazi dentro decimali senza alterare elenchi di articoli | Chiuso |

''')
 t=t.replace('Concludere audit specialistico e freeze tramite CLI;','Audit specialistico concluso; eseguire freeze tramite CLI;')
 p=R/'15-moduli-m-tr02-appalti-pnrr-fondi-ue.md';backup=A/'before-text/VOL-09/15-report-luglio.md'
 if p.exists() and not backup.exists():shutil.copy2(p,backup)
 p.write_text(t,encoding='utf8');print('Audit report and chapter metadata updated')
elif mode=='freeze':
 files=sorted((B/'chapters').glob('*.md'));assert len(files)==14
 for p in files:
  t=p.read_text(encoding='utf8');assert 'review_required: false' in t;t=re.sub(r'^draft_stage:.*$','draft_stage: text_frozen',t,flags=re.M);p.write_text(t,encoding='utf8')
 p=B/'index.md';t=p.read_text(encoding='utf8').replace('status: editorial_review','status: text_frozen').replace('draft_stage: editorial-review','draft_stage: text_frozen').replace('correzioni testuali applicate; audit e PDF corrente da completare.','38 correzioni testuali verificate; audit specialistico concluso e testo congelato. PDF corrente e produzione da verificare.');p.write_text(t,encoding='utf8')
 files += [B/'index.md',B/'planning/01-indice-analitico-vol-09.md',B/'planning/02-matrice-copertura-didattica.md',B/'planning/10-manifest-nuclei-format-2.json']
 files += sorted(Path('wiki/sources').glob('vol-09-*-2026-10-03.md'))
 files += sorted((B/'assets/correzioni-2026-10').glob('*'))
 checks=['14 capitoli, 73 nuclei e matrice coerenti; 38 rilievi applicati e verificati.','Audit 14 e 15 superati via CLI; nessuna revisione normativa lasciata pending.','Tutti i gate di capitolo passati senza blocker/warning; fonti consolidate aggiornate al 3 ottobre.','23 calcoli e calendario lavorativo verificati; zero asset mancanti e wikilink staff nel corpo.','Gantt visto come asset; PDF corrente escluso dal giudizio di freeze.','Text-freeze non automatizzato: verifica manuale dei file e hash effettivi.']
 manifest={'volume':'VOL-09','module':'M-TR02','date':'2026-10-03','textVerified':True,'finalPublicationVerified':False,'checks':checks,'files':[{'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
 (A/'M-TR02-freeze.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
 p=R/'16-moduli-m-tr02-appalti-pnrr-fondi-ue.md';backup=A/'before-text/VOL-09/16-report-luglio.md'
 if p.exists() and not backup.exists():shutil.copy2(p,backup)
 p.write_text('# M-TR02 — Congelamento del testo, 3 ottobre 2026\n\nGate automatico non implementato: verifica manuale documentata.\n\n'+'\n'.join('- '+x for x in checks)+'\n\n| File | SHA-256 |\n| --- | --- |\n'+''.join('| '+x['path']+' | '+x['sha256']+' |\n' for x in manifest['files'])+'\nIl PDF non è certificato; nessuna approvazione finale simulata.\n',encoding='utf8')
 rows=json.loads((A/'registro-applicazione.json').read_text(encoding='utf8'))
 for r in rows:
  if re.fullmatch(r'V09-\d+',r['id']):r['fileHashes']={p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in r['changedFiles'] if Path(p).exists()};r['freezeManifest']=(A/'M-TR02-freeze.json').as_posix()
 (A/'registro-applicazione.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print('Manual freeze manifest:',len(files),'files')
