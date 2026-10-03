from pathlib import Path
import re,json,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc04-giustizia');V=Path('wiki/books/vol-04-giustizia-upp');R=Path('wiki/reviews/pipeline/VOL-04')
p=Path('wiki/sources/vol-04-organizzazione-upp-verifica-2026-10-03.md');t=p.read_text('utf-8');t=t.replace('Camera approva il 28 settembre; fonte consultata segnala esame Senato. Non dedurre decadenza né legge di conversione già pubblicata dall\'assenza di un aggiornamento dell\'iter. Ultimo controllo della GU necessario prima del freeze.','Camera approva il 28 settembre; il comunicato della seduta del Senato n. 460 documenta approvazione definitiva il 30 settembre. La scheda parlamentare consultata il 3 ottobre indica non ancora pubblicato. Distinguere approvazione parlamentare, promulgazione/pubblicazione ed efficacia delle modifiche. Non attribuire un numero di legge non verificato. Raw aggiuntiva: `wiki/raw/correzioni-vol04-2026-10-03/senato-460-conversione-dl144.html`; [comunicato ufficiale](https://www.senato.it/lavori/assemblea/comunicato-di-seduta?num=460).');p.write_text(t,'utf-8')
p=Path('wiki/topics/giustizia-e-upp.md');t=p.read_text('utf-8').replace('La conversione del DL 144/2026 richiede controllo conclusivo al freeze, senza dedurre decadenza da iter incompleti.','La conversione del DL 144/2026 è stata approvata definitivamente il 30 settembre; al controllo del 3 ottobre la scheda parlamentare non segnala ancora la pubblicazione. L’approvazione non autorizza a inventare numero o decorrenza della legge.').replace('Depositi telematici ? verifica','Depositi telematici — verifica').replace('l?effetto','l’effetto').replace('2026?2030','2026–2030');p.write_text(t,'utf-8')
p=next((B/'chapters').glob('04-*.md'));t=p.read_text('utf-8').replace("Il quadro qui descritto è verificato al 3 ottobre 2026; per disposizioni ancora in corso di conversione va controllato l'esito legislativo prima della prova.","Il quadro qui descritto è verificato al 3 ottobre 2026. La conversione del D.L. 144 è stata approvata definitivamente dal Parlamento il 30 settembre; occorre distinguere tale approvazione dalla pubblicazione della legge e verificare il testo vigente alla data della prova.");p.write_text(t,'utf-8')
p=V/'front-matter/06-indice.md';p.write_text(p.read_text('utf-8').replace("Perché'",'Perché'),'utf-8')
p=next((B/'chapters').glob('17-*.md'));p.write_text(p.read_text('utf-8').replace('Alla data di aggiornamento il procedimento di conversione richiede ancora monitoraggio: controllare la pubblicazione finale, non soltanto una votazione parlamentare.','Approvazione parlamentare definitiva il 30 settembre 2026: controllare la successiva pubblicazione della legge e le decorrenze, distinguendole dalla votazione parlamentare.'),'utf-8')
evidence=[
'Distinte funzioni giudiziaria, requirente e giudicante; esempio ricondotto al settore pertinente; cap. 1.',
'Organigramma DIT aggiornato alle quattro direzioni e DGSIA qualificata storicamente; cap. 2 e 12, fonte organizzazione.',
'Sviluppate competenze, composizioni, territori e doppia dirigenza con artt. 1–4 D.Lgs. 240; cap. 2–3.',
'Rettificati fonte, capitolo, indice, bibliografia e quiz sulla L. 145/2026; successivo DL 144 distinto e iter aggiornato.',
'Cap. 4: artt. 1–4 D.Lgs. 151, progetto e composizione; personale lettera f e residuo cancelleria distinti dalla decisione.',
'Cap. 5: dossier di otto documenti, quattro prodotti svolti; cap. 15: simulazione UPP con cronologia e soluzione.',
'Cap. 6: termini, riti e provvedimenti spiegati; calendario udienza 29 giugno 2026, costituzione e memorie calcolate.',
'Cap. 7: segreteria PM distinta dall’UPP giudicante; specificità della Procura generale della Cassazione.',
'Cap. 7: status, 335/45-bis, indagini, 415-bis, archiviazione, fascicoli, riti e impugnazioni; cronologia e simulazione 15.2.',
'Cap. 8 e 11: copia conforme o duplicato ex art. 475, superata formula esecutiva senza cancellare distinzione storica.',
'Cap. 8: registri, rettifica dati, accesso civile/penale e regime dati 9/10 GDPR e D.Lgs. 51; richieste risolte.',
'Cap. 9: soglia 13.659,64 euro, redditi familiari ed eccezioni, incremento penale e competenze/termini distinti.',
'Cap. 9: scaglioni CU, minimo, patrocinio pendente, Corte 137/2026, liquidazioni, opposizione e recupero; calcoli e caso 15.3.',
'Cap. 10: separati casellario persone e anagrafe sanzioni enti.',
'Cap. 10: qualità imputato, menzionabilità/eliminazione, obbligo 25-bis, validità, PDND e rimedio 40; quattro richieste.',
'Cap. 11: competenza, 139/140/143, relata, titolo, precetto 10/90, pignoramento 45 e forme, 492-bis; caso 15.4.',
'Cap. 11: offerta reale e mora del creditore distinte da espropriazione e liberazione automatica.',
'Cap. 12: prima PEC del regime attuale condizionata all’accettazione, regime previgente distinto; orari ed esiti WARN/ERROR/FATAL.',
'Cap. 12: profondità legata al bando; ReGIndE, INI-PEC, IPA, INAD; specifiche rettificate e calendario PPT 2026–2030.',
'Cap. 13: imputabilità per età, MAP minorile/adulta, termini, effetti e misure di comunità; caso 15.5.',
'Cap. 13: mediatori formati, almeno due, consenso/riservatezza/garanzie e conseguenze della mancata partecipazione.',
'Cap. 14: misure, presupposti e autorità; 35-bis/ter, calcolo riduzione/ristoro e caso 15.6.',
'Cap. 14: internato con misura detentiva, istituti, programma entro sei mesi, lavoro e disciplina.',
'Cap. 14: problema/dispositivo/effetto di Corte 99/2019, 253/2019, 10/2024 coordinati alle norme successive.',
'Cap. 15: sei dossier, consegne, risposte modello e sei rubriche di 30 punti; soglia didattica distinta dal bando.',
'Cap. 17: bibliografia per capitoli e norme; sentenza Torreggiani distinta dal comunicato e rassegna da pronuncia.',
'84 quiz rielaborati con quattro alternative; chiavi A/B/C/D 21 ciascuna; 36 nuovi distrattori verificati nei primi sei capitoli.',
'Refusi e imperativi corretti nel testo; eliminato apostrofo residuo dopo Perché nell’indice; controllo delle occorrenze contestuale.',
'Cap. 15–16: rinvii al base con titoli/capitoli, VOL-12 con sezioni nominate, limiti dei profili pedagogici espliciti.'
]
p=R/'13-moduli-m-fc04-giustizia.md';old=p.read_text('utf-8');archive=A/'VOL-04-report13-prima-chiusura.md'
if not archive.exists():archive.write_text(old,'utf-8')
rows=[]
for line in old.splitlines():
 if line.startswith('| V04-'):
  cells=[v.strip() for v in line.strip('|').split('|')];n=int(cells[0].split('-')[1]);cells[5]=evidence[n-1];cells[6]='Corretto e verificato';rows.append('| '+' | '.join(cells)+' |')
assert len(rows)==29
text='''# Revisione trasversale dopo le correzioni — VOL-04 / M-FC04

Data: 3 ottobre 2026. Nuova revisione dei 17 capitoli; audit originario del 2 ottobre conservato immutato nella sua cartella e copia del report precedente negli artifact.

## 1. Sintesi generale

Il manuale specialistico ora sviluppa ordinamento, processo operativo, cancelleria, spese, casellario, UNEP, digitale, minorile e penitenziario. Le regole sono seguite da casi risolti e 84 quiz; sei simulazioni finali hanno documenti fittizi, soluzioni e rubriche. La revisione elimina le lacune dell’audit senza estendere la promessa a preparazione integrale di magistratura o discipline professionali pedagogiche. I prerequisiti comuni e i rinvii sono dichiarati. Questo rapporto riguarda il testo: nuova produzione PDF e conferma conclusiva restano separate.

## 2. Checklist di revisione

Applicati i punti 1–26, 29–30 ai 17 capitoli, front matter, indice e matrice. Il punto 28 è verificato nel sorgente per gerarchie, tabelle e strumenti; punti 27 e resa finale del 28 saranno chiusi sul nuovo PDF. Verificati progressione, definizioni, fonti, esempi, calcoli, quiz, registri linguistici, terminologia e autonomia. Il conteggio delle parole non è usato come attestazione di completezza. Nessuna promozione dei capitoli legacy al formato 2.

## 3. Tabella errori e correzioni

La descrizione conserva il problema rilevato nel testo precedente; la colonna correzione registra il risultato attuale.

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
'''+ '\n'.join(rows)+'''

## 4. Osservazioni per capitolo

Capitoli 1–4: competenze, strutture e organizzazione aggiornate, evitando equivalenze PM/giudice e AUPP/intera struttura. Capitoli 5–7: fascicolo, termini e fasi collegati a dati concreti; processo amministrativo d’ufficio distinto dalla titolarità giurisdizionale. Capitoli 8–12: servizi, spese, certificati, notificazioni e depositi risolti attraverso presupposti e conseguenze. Capitoli 13–14: garanzie, soglie, competenze e rimedi spiegati con casi. Capitoli 15–17: apparati riscritti per applicare il contenuto effettivamente insegnato.

## 5. Coerenza globale e copertura dei profili

Matrice ricostruita in planning/02-matrice-copertura-didattica.md del volume: 14 righe con nuclei, fonte, applicazione e verifica. AUPP e cancelleria hanno dossier distinti; UNEP ha calendario e verbale; DAP/DGMC hanno casi specifici. Le materie comuni restano nel base con destinazioni esplicite. Per profili giuridico-pedagogici e sociali, l’introduzione dichiara il confine giuridico-organizzativo e le discipline ulteriori del bando. Nessun generico rinvio al base sostituisce il processo civile o penale.

## 6. Dubbi e verifiche residue

Nessuna delle 29 criticità testuali resta aperta. D.L. 144/2026: approvazione parlamentare definitiva del 30 settembre distinta dalla pubblicazione e dall’efficacia; la verifica è datata e non attribuisce numero di legge ignoto. I cambiamenti successivi al 3 ottobre richiedono aggiornamento prima della distribuzione. Restano nuova prova PDF, indici reali, preflight, confezionamento e dati commerciali finali: non sono deleghe per sanare errori normativi.

## 7. Migliorie opzionali

Eventuali ulteriori simulazioni per bandi molto specifici possono estendere l’allenamento, senza cambiare il perimetro dichiarato. La bibliografia distingue testi normativi, atti tecnici, rassegne e decisioni.

## 8. Priorità operative

Chiudere audit specialistico e freeze, produrre e controllare il nuovo PDF, quindi completare pacchetto e conferma finale. Il vecchio PDF di agosto non prova le modifiche attuali.

## 9. Giudizio di pubblicabilità

**Pubblicabile con correzioni minori**, limitatamente al testo revisionato nel perimetro dichiarato: zero criticità testuali note residue; la formula del template non equivale ad autorizzazione alla distribuzione. Il volume impaginato resta da verificare negli step 21–23 prima della conferma 24.

## 10. Limiti e tracciabilità

Verifica integrale dei 17 sorgenti e degli 84 quiz nel ciclo di correzzione, fonti ufficiali mirate alle regole introdotte, sei simulazioni ricontrollate. Non è una lettura integrale di ogni codice o di tutti i bandi futuri. Le nove source notes del 3 ottobre precedono la scrittura; raw immutabili e manifest documentano acquisizioni e limiti. Evidenze: VOL-04-text-verifica.json, VOL-04-quiz-uniformazione.json e delta tematici negli artifact; capitoli 13–14 anche nel rapporto dedicato. Controllati 237−43=194, 60/10=6, 60×8=480, scadenza 415-bis 26 ottobre e novanta giorni 1 giugno. La revisione visiva sarà attestata separatamente.
'''
p.write_text(text.replace('correzzione','correzione'),'utf-8')
ledger=[dict(id=f'V04-{i:02}',status='corretto-verificato',evidence=e) for i,e in enumerate(evidence,1)]
(A/'VOL-04-ledger.json').write_text(json.dumps(dict(volume='VOL-04',date='2026-10-03',findings=ledger,publicationReady=False),ensure_ascii=False,indent=2),'utf-8')
d=json.loads((A/'VOL-04-text-verifica.json').read_text('utf-8'))
for ch in d['chapters']:
 p=Path(ch['path']);ch['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
(A/'VOL-04-text-verifica.json').write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf-8')
print('Report 13 aggiornato, 29 interventi verificati.')
