from pathlib import Path
import json,re,shutil,hashlib
root=Path.cwd();art=root/'artifacts/correzioni-collana-2026-10-02';p=root/'wiki/reviews/pipeline/VOL-03/14-moduli-m-fc02-agenzie-fiscali.md'
bk=art/'before-text/VOL-03/14-report-fc02-precedente.md'
if not bk.exists():shutil.copy2(p,bk)
ledger=json.loads((art/'VOL-03-ledger.json').read_text(encoding='utf-8'));rows=[r for r in ledger['findings'] if r['status'].startswith('applicato')]
text='''# Correzioni integrali M-FC02 — step 14, 3 ottobre 2026

## 1. Sintesi editoriale

Applicate le 23 correzioni dell’audit integrale pertinenti al modulo fiscale, su 16 capitoli. Il precedente rapporto è conservato negli artefatti. Questo rapporto riguarda il nuovo mandato approvato del 2 ottobre 2026. Il testo è una bozza revisionata: audit specialistico finale, freeze ed export candidato restano a valle.

## 2. Controlli applicati

Corrette prima le norme e le lacune didattiche, quindi metodo, rimandi, apparati staff e grafie. Le nuove parti espongono condizioni, esempi risolti e limiti applicativi; non eliminano spiegazioni legittime per superare controlli automatici. Le note di produzione sono archiviate e sostituite da riferimenti pubblici. Riletti i blocchi modificati; gli esercizi numerici nuovi sono stati ricalcolati. Il controllo automatico dei wikilink nel corpo restituisce zero destinazioni o titoli mancanti.

## 3. Tabella delle correzioni

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''
for r in rows:text+='| '+r['id']+' | '+r['position'].replace('|','/')+' | Correzione integrale | Media | '+r['diagnosis'].replace('|','/')+' | '+r['correction']+' | Applicato al testo; verifica specialistica e PDF successivi |\n'
text+='''
## 4. Evidenze e fonti

- Fonti nuove: `processo-tributario-regime-2026-rettifica-2026-10-03.md`, `dogane-accise-rettifiche-2026-10-03.md`; delte datate nelle note di sanzioni, reati, accertamento, TCF, redditi, dichiarazioni, riscossione, estimo, contabilità, civile e assetti.
- Primarie: Gazzetta Ufficiale, Normattiva/AKN acquisito, banca MEF, EUR-Lex, ADM, AdER, Agenzia delle entrate, OIC e Camera. URL puntuali nelle note.
- Snapshot prima delle modifiche e script applicati in `artifacts/correzioni-collana-2026-10-02/`; controllo link `VOL-03-FC02-links.json`.
- Calcoli: imposta/art. 4 (110.000 e 25%); IVA/art. 10-ter (260.000 e data 31 dicembre 2026); reddito professionale 22.000; valori estimativi 170.000/200.000/180.000; margini −90/0; rimanenze 10.500.

## 5. Coerenza del percorso

Il regime processuale 2026 è il D.Lgs. 546/1992, con rinvio del TU al 2027; i riferimenti alla vecchia source note sono sostituiti. D significa Diario nella mappa BANDO. Le appendici richiamano i titoli effettivi. La matrice conserva il censimento storico e aggiunge un delta esplicito con verifiche finali pendenti.

## 6. Verifiche successive

Step 15: riesame specialistico del testo corretto, inclusi tempi e regimi speciali. Step 16: integrità, copertura e freeze solo dopo esito positivo. Export: tabelle nuove, continuità delle figure, impaginazione e confronto testo/PDF. Nessuna attestazione di pubblicabilità è dedotta dai soli controlli Markdown.

## 7. Osservazioni non bloccanti per l’applicazione delle correzioni

Le figure sono gestite dal coordinatore e non sono state alterate in questa fase. I dati dei singoli bandi restano esempi di lettura; non sono presentati come calendario aperto di candidature.

## 8. Priorità

Eseguire il riesame specialistico sul candidato corrente, poi congelare e controllare il PDF. Proseguire in parallelo logico le correzioni degli altri due moduli senza confondere i loro stati.

## 9. Stato del risultato

Correzioni M-FC02 applicate; pubblicabilità non ancora attestata. Il registro di volume conserva per ciascun ID la distinzione tra applicazione e verifica finale.

## 10. Limiti e controllo delle trasformazioni

La lettura integrale iniziale di tutti i capitoli e quiz è documentata nell’audit del 2 ottobre. Questo passaggio ha riesaminato le parti modificate, fonti mirate, contesto e rinvii: non dichiara un secondo audit integrale già concluso. Nel Decoder due blocchi omonimi hanno richiesto una regola specifica: il controllo link ha rilevato la rimozione transitoria del corpo, ripristinato integralmente dallo snapshot; il controllo finale conta 16 capitoli e zero rimandi mancanti. Nessuna modifica ai PDF o alle figure in questa fase.
'''
p.write_text(text,encoding='utf-8');print('Rapporto step 14 scritto:',len(rows),'ID')
