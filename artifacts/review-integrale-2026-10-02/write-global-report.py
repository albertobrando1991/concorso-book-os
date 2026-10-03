from pathlib import Path
import json
base=Path('artifacts/review-integrale-2026-10-02')
reports=Path('wiki/reviews/audit-integrale-2026-10-02')
v=json.loads((base/'final-verification.json').read_text(encoding='utf8'))
assert v['textReviewComplete'] and v['chapters']==326 and not v['problems']
visual=json.loads((base/'visual-verification.json').read_text(encoding='utf8'))
assert visual['complete'] and visual['pdfCount']==12 and visual['figures']==308
pdfs=json.loads((base/'pdf/inventory.json').read_text(encoding='utf8'))
selected=[p for p in pdfs if not(p['volume']=='VOL-02' and 'rebuild' not in p['file'])]
assert sum(p['pages'] for p in selected)==4861
rows=[]
focus={
'VOL-01':'Definizioni e copertura del nucleo comune, criteri BANDO, quiz e figure; rinvii degli specialistici da riallineare.',
'VOL-02':'Chiavi e commenti dei quiz discordanti, rubriche incoerenti, competenze amministrative e copertura PL; candidato oltre il limite di pagine KDP.',
'VOL-03':'Regimi temporali tributari e aggiornamento contrattuale; copertura EPNE; capitoli fiscali aggiunti dopo le appendici.',
'VOL-04':'Conversione del decreto del 2026 e organizzazione ministeriale; quiz con soluzioni prima delle opzioni.',
'VOL-05':'Teoria specialistica insufficiente, esercizi ripetitivi, rinvii vuoti e figure con testi generici non sviluppati.',
'VOL-06':'Valutazione scolastica, competenze e ordinamenti; spiegazione universitaria eliminata in export; ordine del blocco cultura.',
'VOL-07':'NEWS2, documentazione e accesso, codice deontologico e dati PASSI; tabella clinica illeggibile nel PDF.',
'VOL-08':'Copertura NIS/cloud e competenze tecniche; coerenza BANDO. Aggiornamenti AI 2026 controllati senza ripristinare calendari superati.',
'VOL-09':'Soglie, termini e istituti degli appalti non insegnati in modo sufficiente; appendici promesse assenti, titoli dentro tabelle/quiz.',
'VOL-10':'Teoria ed esempi tecnici insufficienti: costruzioni, NTC, casi e laboratorio; rinvii al comune da completare.',
'VOL-11':'Disciplina e casi ambientali, allertamento e qualità delle acque; fonti e novità 2026 da distinguere dalle lacune didattiche.',
'VOL-12':'Requisiti e procedure delle carriere, esercizi e punteggi; tag HTML stampati nelle tabelle e schede prive di spazio utile.'}
for s in v['volumes']:
 code=s['volume'];p=next(p for p in selected if p['volume']==code)
 rows.append(f"| [{code}]({code}.md) | {s['read']}/{s['chapters']} | {s['findings']} | [{p['pages']} pagine](PDF-{code}.md) | {focus[code]} |")
content=f'''---
id: review-audit-integrale-collana-2026-10-02
type: review
title: "Revisione integrale prepubblicazione della collana — 2 ottobre 2026"
status: review_completed_corrections_pending
domain: concorsi-pubblici
topics: []
entities: []
source_refs: []
book_refs: [VOL-01, VOL-02, VOL-03, VOL-04, VOL-05, VOL-06, VOL-07, VOL-08, VOL-09, VOL-10, VOL-11, VOL-12]
confidence: medium
updated_at: 2026-10-02
created_at: 2026-10-02
review_required: true
canonical: false
tags: [audit, revisione-integrale, prepubblicazione]
issue_type: editorial_audit
severity: high
affected_pages: []
---

# Revisione integrale della collana

## 1. Sintesi editoriale

**La revisione diagnostica dei dodici volumi cartacei è conclusa. La collana non è pubblicabile allo stato attuale.** Sono stati letti integralmente tutti i **326 capitoli e appendici**, inclusi quiz, commenti, esercizi e casi presenti. Il dossier raccoglie **{v['actions']} voci di intervento**: {v['contentActions']} sul testo e {v['pdfAndExportActions']} su PDF, figure ed esportazione. Le voci includono errori, lacune, incoerenze e proposte di integrazione; non sono altrettanti errori indipendenti, perché alcuni problemi ricompaiono fra testo, immagine e PDF.

Il pubblico è costituito da concorsisti che devono studiare il nucleo comune nel VOL-01 e applicarlo ai profili specialistici. La revisione ha valutato l'autonomia del libro cartaceo, la preparazione alle prove e la corrispondenza fra promesse, teoria ed esercitazioni. Il metodo è riconoscibile, ma in diversi moduli le indicazioni su come studiare sostituiscono conoscenze che il candidato deve effettivamente apprendere.

**Nessuna correzione proposta è stata applicata ai manoscritti, alle immagini, ai PDF o alla pipeline in questo audit.** Le integrazioni già presenti da lavorazioni distinte sono state preservate. Il lavoro consegnato è la diagnosi completa del perimetro descritto, non il nulla osta alla pubblicazione né una certificazione di ogni affermazione normativa.

## 2. Punti applicati della checklist

La checklist editoriale a 30 punti è stata applicata attraverso dodici rapporti individuali: forma linguistica, chiarezza, terminologia, coerenza, struttura, indice, progressione, contenuti, norme, esempi, quiz, rimandi, apparati e promessa didattica. I rapporti distinguono risultati, proposte, questioni ancora da verificare e suggerimenti facoltativi.

| Controllo | Copertura effettiva | Evidenza e limite |
| --- | --- | --- |
| Lettura del testo | 326/326 unità cartacee | Registri individuali e registro unico con SHA-256; nessun capitolo marcato completo sulla sola base dei gate |
| Quiz, esercizi e casi | Tutti quelli presenti nei 326 file | Valutati consegna, soluzione, commento, calcoli e utilità; presenza di quiz non significa qualità sufficiente |
| Indici, matrici e apparati | Esaminati con ciascun volume e nell'export corrente | Rinvii e promesse confrontati con contenuti disponibili; non assunta la completezza dalle matrici |
| Normativa e dati esterni | Verifiche mirate su fonti ufficiali | Fonti e limiti nei §6 dei rapporti; non verificata indipendentemente ogni singola proposizione |
| PDF candidati | 12 PDF, 4.861 pagine | Tutte le pagine viste in tavole panoramiche; approfondimenti a pagina intera indicati nei rapporti PDF |
| Figure originali | 308 immagini: 153 base, 10 VOL-02, 70 VOL-03, 75 VOL-05 | Tutte esaminate visualmente; il totale comprende il QR del base, il cui servizio non è stato collaudato |
| Export corrente | 423 unità: 326 capitoli/appendici e 97 apparati | Verificati inventario, ordine, materiali interni e incipit dei nuclei; non una collazione parola per parola di tutti i PDF |

La versione precedente del VOL-02 da 830 pagine è inventariata, ma la revisione panoramica è sul rebuild da 867. Non sommare entrambe per dichiarare una copertura visuale più ampia. I 23 capitoli del ricettario digitale separato non fanno parte dei 326: non sono oggetto di questa revisione dei volumi cartacei.

## 3. Tabella errori

Il [registro completo degli interventi](registro-interventi.md) raccoglie tutte le proposte, ordinate per volume e gravità. È disponibile anche in [CSV filtrabile](registro-interventi.csv), con ID, posizione, categoria, gravità, descrizione, proposta, stato e rapporto di origine. Per l'evidenza esterna e i limiti si deve leggere il rapporto collegato: una voce «da verificare» non va trasformata in un errore accertato.

Distribuzione operativa: {v['severityCounts'].get('bloccante',0)} bloccanti, {v['severityCounts'].get('grave',0)} gravi, {v['severityCounts'].get('media',0)} di gravità media e {v['severityCounts'].get('lieve',0)} lievi. «Bloccante» segnala un impedimento esplicito; anche i rilievi gravi possono impedire la pubblicazione. Le proposte facoltative restano nei §7 dei rapporti, fuori dal conteggio degli interventi necessari.

## 4. Osservazioni per capitolo

La seguente tabella permette di aprire il rapporto completo di ogni volume, che contiene le osservazioni per tutti i capitoli. Il numero dei rilievi misura voci aggregate, non una graduatoria di qualità fra volumi di estensione diversa.

| Volume e rapporto testuale | Capitoli letti | Rilievi testuali | Rapporto PDF | Problemi prioritari |
| --- | --- | --- | --- | --- |
{chr(10).join(rows)}

Completano il dossier il [rapporto comune sull'esportazione](EXPORT-COLLANA.md) e l'[analisi delle figure del VOL-05](FIGURE-VOL-05.md). Le figure degli altri volumi sono trattate nei rispettivi rapporti PDF.

## 5. Coerenza globale

Il primo intervento trasversale riguarda il **nucleo comune**: diversi specialistici rinviano al VOL-01 per conoscenze che nel base sono soltanto nominate. Va completata una sola spiegazione canonica, poi controllata la destinazione di ogni rinvio. Il perimetro specialistico deve aggiungere regole ed esempi del profilo senza duplicare il comune.

Il secondo riguarda il **Metodo BANDO**: devono restare costanti Bando, Aree, Nuclei, Diario, Output. Non sostituire le fasi con categorie diverse nelle tabelle e nelle figure. Separare obbligatorietà del programma, fase della prova e priorità personale: ridurre la priorità non autorizza a eliminare una materia richiesta.

Il terzo riguarda la **verifica dell'apprendimento**: quiz con chiavi discordanti, risposte banali, consegne prive dei dati necessari e soluzioni che ripetono la traccia non dimostrano preparazione. Occorrono prove risolvibili, soluzioni motivate, rubriche con punteggi possibili e casi completati.

L'**esportazione** può alterare il contenuto: EXP-01 documenta cinque nuclei universitari presenti nel sorgente ma eliminati dall'export e dal PDF; P06-03 e P03-04 documentano l'ordine errato dei capitoli. Una correzione al sorgente deve quindi essere seguita da controllo sul prodotto generato.

Gli **apparati visuali** devono spiegare relazioni corrette, con caratteri leggibili e spazi compilabili. I PDF mostrano tabelle troppo larghe, intestazioni ripetute, didascalie duplicate e materiale redazionale esposto. Il VOL-02 presenta anche un limite fisico di produzione documentato in P02-10: 867 pagine eccedono il massimo KDP verificato per il formato scelto.

## 6. Contenuto da verificare

Le fonti ufficiali consultate, i riscontri positivi e gli accessi falliti sono riportati nei §6 dei dodici rapporti e nei rapporti visuali pertinenti. Alcune pagine ufficiali hanno restituito protezioni, errori di accesso o soltanto contenuto indicizzato: questi limiti non autorizzano a dichiarare verificato il testo integrale corrente della norma.

Prima di incorporare le correzioni occorre consolidare nel wiki le nuove fonti rilevanti, distinguere norma vigente, decorrenza, regime transitorio e data del bando. Restano da chiudere i singoli punti esplicitamente indicati «da verificare», oltre al controllo esterno completo dei nuovi testi che verranno scritti. Le novità 2026 confermate nei rapporti non devono essere sostituite con regole precedenti per semplice familiarità.

La corrispondenza a uno specifico concorso futuro resta da verificare sul relativo bando: l'esaustività qui valutata è rispetto alla promessa e ai profili dichiarati dai volumi. Le esclusioni editoriali già concordate, comprese Campania e cultura generale nelle integrazioni precedenti, restano ferme.

## 7. Suggerimenti facoltativi (non errori)

Aggiungere percorsi di lettura per profilo e un indice tematico degli errori più ricorrenti. Sono scelte da valutare dopo aver colmato le lacune essenziali. Restano invece necessari gli interventi registrati sulla leggibilità e sulla compilabilità degli strumenti. Le preferenze di stile e le rifiniture facoltative specifiche sono nei §7 dei rapporti individuali.

## 8. Priorità degli interventi

1. Correggere errori sostanziali, clinici e normativi e le chiavi dei quiz; chiudere con fonte i punti incerti. Eliminare omissioni di export e materiali promessi assenti.
2. Completare la teoria e gli esempi necessari alla promessa di ogni volume, partendo dal comune e dai moduli con lacune strutturali. Risolvere la distribuzione editoriale del VOL-02 entro il limite di produzione senza comprimere i caratteri.
3. Riallineare metodo, ordine, numerazione, rinvii, matrici, esercizi, soluzioni e figure; controllare le ricorrenze della stessa correzione.
4. Rifinire linguaggio, tabelle, workbook e apparati; rigenerare i PDF e verificare celle, formule, paginazione, indice e assenza di residui redazionali.
5. Eseguire i gate applicabili attraverso il CLI, verificare le versioni e preparare il pacchetto finale con manifest; effettuare il controllo conclusivo di stampa prima della pubblicazione.

I gate precedenti restano evidenza tecnica separata: nella ricognizione iniziale 321 tentativi, 266 passati, 6 non passati e 49 non disponibili; altri 5 raccordi fuori dai target. Un esito positivo non prova correttezza normativa o sufficienza didattica. I sei deficit minimi di densità non vanno risolti aggiungendo parole di riempimento. Nessuno stato pipeline è stato modificato da questo audit.

## 9. Giudizio di pubblicabilità

**Non pubblicabile allo stato attuale**, per tutti i dodici volumi nel rispettivo perimetro di rilievi. Sono necessari interventi sostanziali e una verifica successiva delle parti corrette e del nuovo impaginato. Le carenze del nucleo comune incidono inoltre sui volumi che lo assumono come prerequisito.

La revisione richiesta è stata completata come diagnosi e raccolta di proposte. L'applicazione degli interventi è una fase successiva, secondo la richiesta dell'utente. Nessun file è stato dichiarato pronto, pubblicato o approvato automaticamente.

## 10. Limiti di questa revisione

- Lettura integrale del testo corrente, ma riscontro normativo e fattuale esterno selettivo: non una certificazione indipendente di ogni claim.
- Panorama di tutte le pagine dei PDF selezionati e dettagli mirati; non una seconda correzione di bozze a grandezza piena di ogni parola o una prova fisica su carta.
- Nessun collaudo operativo di attivazione digitale/QR, accessibilità con tecnologie assistive, diritti di riproduzione/licenze o metadati commerciali definitivi.
- I PDF candidati e i sorgenti correnti non sono assunti identici. Il controllo degli incipit è un rilevatore di omissioni, non una collazione integrale.
- Il ricettario digitale separato e i concorsi non inclusi nella promessa editoriale restano fuori perimetro.

La tracciabilità tecnica si trova in `artifacts/review-integrale-2026-10-02/`: dodici ledger, `complete-chapter-register.json`, `action-register.json`, `final-verification.json`, export, inventario PDF e manifest delle figure. I checksum collegano le osservazioni alla versione effettivamente letta. I rapporti preliminari del primo giro restano conservati come storico e sono superati, per lo stato della lettura integrale, da questo dossier.
'''
(reports/'README.md').write_text(content,encoding='utf8')
print('Global report written:',v['chapters'],'chapters;',v['actions'],'actions')
