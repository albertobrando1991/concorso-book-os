---
id: source-iam-crittografia-logging-incident-response-fonti-primarie
type: source_note
title: "IAM, gestione delle chiavi, logging e incident response — fonti primarie"
status: consolidated
domain: "cybersicurezza e pubblica amministrazione"
topics: ["iam", "crittografia", "key management", "logging", "incident response", "nis2"]
entities: ["NIST", "Agenzia per la cybersicurezza nazionale", "CSIRT Italia"]
source_refs: []
book_refs: ["m-tr01-ict-trasformazione-digitale"]
confidence: 0.9
updated_at: 2026-07-30
created_at: 2026-07-30
review_required: true
canonical: true
tags: ["source", "iam", "crittografia", "logging", "incident-response"]
source_type: "official-guidance-and-legislation"
source_url: "https://csrc.nist.gov/pubs/sp/800/63/4/final"
source_date: 2026-07-30
authority_level: "primary"
---

# IAM, gestione delle chiavi, logging e incident response — fonti primarie

## Perimetro

La nota consolida fonti ufficiali utili al capitolo 09 di M-TR01. Le pubblicazioni NIST sono riferimenti tecnici trasferibili, non norme italiane. Il decreto legislativo 4 settembre 2024, n. 138 costituisce invece il riferimento nazionale per il recepimento NIS2; platea, procedure, tassonomie, termini e canali applicabili devono essere verificati sul testo vigente e sugli atti ACN al momento della pubblicazione.

## Identità digitale

NIST SP 800-63-4, pubblicata in versione finale nel luglio 2025, sostituisce SP 800-63-3. La suite tratta gestione del rischio dell'identità digitale, identity proofing ed enrollment, autenticazione e gestione degli autenticatori, federazione e asserzioni. Distingue tre dimensioni di assurance: identità, autenticazione e federazione. Il trasferimento al manuale riguarda le distinzioni concettuali e il principio di selezionare controlli proporzionati al rischio; non implica recepimento automatico dei livelli NIST nella PA italiana.

SP 800-63A-4 riguarda prova dell'identità ed enrollment; SP 800-63B-4 autenticazione e ciclo degli autenticatori; SP 800-63C-4 federazione e asserzioni. La suite conferma che identificazione, autenticazione e federazione sono funzioni diverse e che autenticare un soggetto non determina da sola le autorizzazioni applicative.

## Crittografia e gestione delle chiavi

NIST SP 800-57 Part 1 rev. 5, finale dal maggio 2020, fornisce indicazioni generali sul materiale crittografico, sui servizi di sicurezza e sulle funzioni di key management. La protezione effettiva dipende non soltanto dall'algoritmo, ma anche da generazione, distribuzione, conservazione, uso, rotazione, revoca, recupero, archiviazione e distruzione delle chiavi.

Nel manuale si usano distinzioni funzionali: la cifratura protegge principalmente la riservatezza; l'hash produce un'impronta e non è cifratura reversibile; il MAC combina un segreto con il controllo di integrità e autenticità; la firma digitale impiega una chiave privata per consentire verifiche con la corrispondente chiave pubblica. Algoritmi, lunghezze e periodi crittografici richiedono una fonte tecnica aggiornata e una scelta di architettura: non vengono prescritti nel capitolo.

## Logging

NIST SP 800-92, finale dal settembre 2006, descrive il log management come capacità organizzativa e tecnica: generazione, trasmissione, conservazione, accesso, analisi e dismissione dei dati di log. La rev. 1, pubblicata come initial public draft nel 2023, alla data di consultazione non è finale. Può orientare il tema della pianificazione, ma non va presentata come versione vigente definitiva.

Un log è un record di eventi prodotti da asset informatici. La sua utilità dipende da scopo, copertura delle sorgenti, qualità dei campi, tempo coerente, protezione da modifiche e accessi non autorizzati, conservazione governata e capacità di analisi. La presenza di molti log non garantisce rilevazione né ricostruzione.

## Incident response

NIST SP 800-61 rev. 3, finale dall'aprile 2025, sostituisce la rev. 2 e integra l'incident response nella gestione del rischio descritta dal NIST CSF 2.0. Preparazione e miglioramento coinvolgono tutte le funzioni del CSF; Detect, Respond e Recover sostengono le attività operative durante l'incidente. Il ciclo non va ridotto a una sequenza rigida indipendente da governance, asset, rischi e continuità.

La risposta comprende capacità organizzative, ruoli, escalation, analisi, contenimento, ripristino, comunicazione, conservazione delle evidenze e apprendimento. L'azione tecnica più rapida non è sempre quella corretta: occorre bilanciare impatto sul servizio, propagazione, sicurezza delle persone, disponibilità delle evidenze e obblighi applicabili.

## Quadro italiano e NIS2

Il decreto legislativo 4 settembre 2024, n. 138 recepisce la direttiva (UE) 2022/2555. ACN svolge le funzioni nazionali attribuite dal decreto e CSIRT Italia opera nel sistema di gestione e notifica degli incidenti. Gli obblighi dipendono dall'inquadramento del soggetto e dalla significatività dell'incidente.

Il capitolo può affermare con sicurezza che:

- la governance della cybersicurezza non è delegabile alla sola funzione tecnica;
- i soggetti interessati devono predisporre processi di rilevazione, escalation e notifica coerenti con la disciplina applicabile;
- una notifica cyber e una notifica di violazione dei dati personali rispondono a presupposti diversi e possono concorrere;
- il playbook interno deve indicare chi verifica platea, significatività, canale e tempistica usando la fonte ufficiale vigente.

Il capitolo non fissa procedure, tassonomie o scadenze operative, perché tali dettagli richiedono controllo degli atti ACN vigenti e review giuridico-istituzionale al text freeze.

## Claim sostenuti

- IAM governa identità e accessi lungo il ciclo di vita.
- Identificazione, autenticazione, autorizzazione e accounting sono funzioni distinte.
- Crittografia efficace richiede governo delle chiavi.
- Log management è un processo, non la sola installazione di un SIEM.
- Evento, alert e incidente non sono sinonimi.
- Incident response è parte della gestione del rischio e richiede preparazione, risposta, recupero e miglioramento.
- Gli adempimenti NIS2 e privacy devono essere valutati separatamente sul caso concreto.

## Limiti e review

- Verificare al text freeze eventuali nuove revisioni delle pubblicazioni NIST.
- Verificare testo vigente del d.lgs. 138/2024 e determinazioni ACN applicabili.
- Far validare la parte IAM da un identity architect, la parte crittografica da uno specialista key management, logging e incident response da SOC/CSIRT, la parte normativa da esperto ACN/NIS2 e DPO.

## Fonti ufficiali

- NIST SP 800-63-4 e parti A/B/C: https://csrc.nist.gov/pubs/sp/800/63/4/final
- NIST SP 800-57 Part 1 rev. 5: https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final
- NIST SP 800-92 finale: https://csrc.nist.gov/pubs/sp/800/92/final
- NIST Log Management Project, stato della rev. 1: https://csrc.nist.gov/Projects/log-management
- NIST SP 800-61 rev. 3: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- NIST CSF 2.0: https://www.nist.gov/cyberframework
- D.lgs. 4 settembre 2024, n. 138: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024;138

## Collegamenti

- [[topics/sicurezza-informatica]]
- [[topics/ict-digitale-cybersecurity-dati-concorsi-pa]]
- [[entities/agenzia-cybersicurezza-nazionale]]
- [[books/moduli/m-tr01-ict-trasformazione-digitale/chapters/09-iam-crittografia-logging-incident-response]]
