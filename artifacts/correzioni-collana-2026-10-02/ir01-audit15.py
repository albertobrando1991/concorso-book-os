from pathlib import Path
import json,re
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-ir01-scuola');R=Path('wiki/reviews/pipeline/VOL-06');C=Path('wiki/reviews/correzioni-collana-2026-10-02')
changes=json.loads((A/'VOL-06-changes.json').read_text())['changes'];rows=[]
for n in range(1,9):
 fid=f'V06-{n:02}';x=changes[fid];rows.append(f"| {fid} | Capitoli indicati nel registro | Audit specialistico | {'Media' if n==2 else 'Grave'} | {x['change']} | {x['evidence']} | Corretto |")
p=R/'15-moduli-m-ir01-scuola.md';arc=C/'archive'/'pre-correzioni-15-m-ir01.md'
if not arc.exists():arc.write_bytes(p.read_bytes())
p.write_text('''# M-IR01 — Audit specialistico delle correzioni del 3 ottobre 2026

## 1. Sintesi editoriale

Riesaminati i delta V06-01–08 e i raccordi scolastici dei rilievi trasversali 23, 33 e 35. La baseline resta la lettura integrale diagnostica dei 13 capitoli; il presente passaggio verifica correzioni, fonti puntuali e coerenza applicativa. Nessun errore grave o medio aperto nel perimetro testuale corretto del modulo. Pubblicabilità del volume non attestata.

## 2. Punti applicati della checklist

Controlli testuali 1–26 e 28–30: perimetro, autonomia, completezza delle promesse, definizioni, fonti, esempi, ruoli, procedure, calcoli, quesiti, refusi e metadati. Humanizer sui passaggi aggiunti. Il punto 27 richiede il nuovo PDF, distinto dall’esito testuale.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''+ '\n'.join(rows)+'''

## 4. Osservazioni per capitolo

01: perimetro dei quattro profili e destinazioni VOL-08/VOL-09 riconfermate sulla tassonomia. Nessuna promessa di appendice disciplinare inesistente. 02–04: ordinamenti, organi, composizioni, quorum e ciclo PTOF/SNV; quorum di 19 componenti pari a 10, variazione 35%→28% pari a −7 punti e −20% relativo. 05–06: trasferimento documentato con confini privacy/competenza; proposta DSGA, adozione DS e attuazione DSGA del piano ATA; relazioni aggiornate al CCNL 2025. 07–08: D.I.129 con programma, gestione e consuntivo, ruoli e scadenze ordinarie; 30.000 di cassa +10.000 residui attivi −15.000 passivi =25.000 risultato. Inventario con consegnatario, ricognizione, rinnovo e scarico; DNSH come vincolo generale delle misure RRF.

09–10: art.25 D.Lgs.165, competenze collegiali, relazioni sindacali, datore/RSPP/RLS/ente edilizio; nello scenario si protegge prima di completare i documenti. Art.18, commi3.1–3.3, non interpretato come esonero automatico mediante una lettera. 11: modelli selezionati, differenza fra prestazione autonoma e assistita, PEI/PDP e GLO/GLI; sei quiz risolti con chiavi B/C/A/D/B/C e commenti coerenti. D.L.170/2026 vigente dal 1° ottobre recepito senza anticipare conversione o imporre retroattivamente il termine di giugno2026. 12: O.M.3/2025 e sei aree canoniche DigCompEdu; O.M.172 conservata soltanto per spiegare il precedente regime. 13: lezione originale quarta primaria, 60 minuti, materiali analogici, 3/6=1/2, confronto 1/2>1/3 a parità d’intero, soluzione e rubrica; durata della lezione distinta dalla prova concorsuale e rubrica distinta dai giudizi periodici.

## 5. Coerenza globale

Matrice collegata alle evidenze effettive; topic, indice del modulo e quota scolastica dell’indice di volume aggiornati. Note di review archiviate e riferimenti interni rimossi dal corpo; riferimenti normativi e professionali leggibili presenti. I capitoli restano legacy: nessuna attestazione di formato2 o di soglie di 600 parole per nucleo. Conteggi persistiti, senza riempitivo. Le altre famiglie del volume restano in correzione.

## 6. Contenuti verificati

Fonti e copie acquisite nelle note scolastiche: D.Lgs.297 artt.5/7/8/10/37; DPR275 art.3; D.Lgs.165 art.25; D.I.129 artt.5/12–17/23/30/31/33; CCNL23dicembre2025 artt.1/5/6/11 e disposizioni compatibili precedenti; D.Lgs.81 art.18 nei passaggi scolastici; O.M.3/2025 e AllegatoA; JRC DigCompEdu; D.Lgs.66 art.7, L.104 art.15 e D.L.170 art.1; Linee guida DSA §§3–3.1. Riletti i consolidati e le pagine pertinenti indicati nelle source, con limiti espliciti per il materiale bibliografico. Nessun box Dato operativo rilevato dal CLI, quindi nessuna riga automatica omessa. Il controllo non certifica tutto il corpus normativo, bandi locali o diagnosi.

## 7. Suggerimenti facoltativi

Nessun ampliamento estraneo ai rilievi necessario per il presente passaggio.

## 8. Priorità degli interventi

Registrare il text freeze tramite CLI; verificare poi il nuovo PDF, in particolare tabelle, quiz, soluzioni e spazi di risposta. Seguono gli altri tre moduli del volume e i controlli complessivi. Per una successiva data editoriale, aggiornare l’esito della conversione del D.L.170/2026.

## 9. Giudizio di pubblicabilità

Testo del modulo idoneo al congelamento nel perimetro dichiarato; l’intero volume non è ancora dichiarato pubblicabile. Il gate del report non sostituisce l’ispezione visiva, il preflight o la chiusura degli altri moduli.

## 10. Limiti della revisione

Audit automatico editoriale e riscontri esterni selettivi. Nuova rilettura dei delta e dei raccordi, non nuova lettura integrale dichiarata delle parti invariate. Esempi originali didattici, non modelli obbligatori delle scuole. Bandi specifici e documenti individuali non vengono inventati. Report storico conservato in archivio.
''',encoding='utf8')
for p in (B/'chapters').glob('*.md'):
 t=p.read_text();t=re.sub(r'^review_required:.*$','review_required: false',t,flags=re.M);t=re.sub(r'^draft_stage:.*$','draft_stage: specialist-audit-complete',t,flags=re.M)
 if p.name.startswith('13-'):t=t.replace('"sources/prove-concorsuali-quiz-scritto-orale-dpr-487-1994", ','')
 p.write_text(t,encoding='utf8')
print('Report 15 scritto, gate da eseguire')
