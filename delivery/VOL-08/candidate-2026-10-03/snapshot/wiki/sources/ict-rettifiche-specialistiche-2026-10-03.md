---
id: source-ict-rettifiche-specialistiche-2026-10-03
type: source_note
title: "ICT: riscontri per le correzioni specialistiche del 3 ottobre 2026"
status: consolidated
domain: concorsi pubblici italiani
topics: ["ict-rettifiche-specialistiche-2026", "sicurezza-informatica"]
entities: ["ACN", "AgID", "Unione europea", "PostgreSQL", "NIST"]
source_refs: []
book_refs: ["m-tr01-ict-trasformazione-digitale"]
confidence: 0.95
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: ["fonti-primarie", "rettifiche-audit", "VOL-08"]
source_type: official_documents_and_technical_research
source_url: mixed:primary-sources-below
source_date: 2026-10-03
authority_level: primary
---

# Riscontri ICT del 3 ottobre 2026

## NIS2 e calendario ACN

Acquisiti gli originali dal [catalogo normativo ACN](https://www.acn.gov.it/portale/nis/la-normativa). La [determinazione 379907/2025](https://www.acn.gov.it/portale/documents/d/guest/detacn_obblighi_2511-v3_signed), articolo 3, fissa diciotto mesi dalla comunicazione per le misure e nove per le notifiche; distingue negli allegati soggetti importanti ed essenziali. La [determinazione 127434/2026](https://www.acn.gov.it/portale/documents/d/guest/detacn_misuresicurezza-v4_post), articolo 1, stabilisce per i nuovi inseriti 2026 misure entro 31 luglio 2027 e notifiche dal 1 gennaio 2027; per i soggetti 2025 che permangono conserva le scadenze precedenti. Letti integralmente i due provvedimenti di cinque e tre pagine, esclusi gli allegati separati non acquisiti; non si inventano soglie tecniche degli allegati.

Copie immutabili in `wiki/raw/correzioni-vol08-2026-10-03/`. Il download diretto ufficiale è riuscito anche quando il lettore web restituiva 403.

## AI Act: modifiche vigenti

[Regolamento (UE) 2026/1744, testo ufficiale PDF](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32026R1744), pubblicato il 24 luglio e in vigore dal 27 luglio 2026. Acquisito il testo, letti i passaggi pertinenti (non attestazione di lettura integrale dei 41 fogli): art. 1, punti 5, 13, 39 e 40. Il nuovo art. 4 richiede misure che sostengano lo sviluppo dell’alfabetizzazione, senza garantire un livello individuale specifico. Capo III, sezioni 1–3, salvo art. 6(5): allegato III dal 2 dicembre 2027; art. 6(1)/allegato I dal 2 agosto 2028. Il rinvio non riguarda indistintamente tutto il regolamento. Per i sistemi generativi immessi sul mercato prima del 2 agosto 2026, il nuovo art. 111(4) differisce al 2 dicembre 2026 il solo art. 50(2). Regime separato art. 111(2) per alto rischio già immesso/in servizio: modifiche significative e termine PA 2 agosto 2030. Il manuale non confonde questo transitorio con una proroga generale per tutti i nuovi sistemi PA.

[Commissione, calendario aggiornato](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) e [entrata in vigore](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force) corroborano le date. [Legge 132/2025, art. 14](https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.codiceRedazionale=25G00143&art.dataPubblicazioneGazzetta=2025-09-25&art.flagTipoArticolo=0&art.idArticolo=14&art.idGruppo=2&art.idSottoArticolo=1&art.idSottoArticolo1=10&art.progressivo=0&art.versione=1): conoscibilità e tracciabilità, supporto alla decisione con responsabilità umana, misure tecniche/organizzative/formative. Si distingue la legge dal documento strategico e dalle bozze di linee guida.

## Cloud e acquisti

[DTD, Strategia Cloud Italia](https://innovazione.gov.it/dipartimento/focus/strategia-cloud-italia/) e [percorso di qualificazione](https://cloud.italia.it/qualificazione-servizi-cloud/): regolamento ACN 21007/24 del 27 giugno 2024, regime ordinario dal 1 agosto 2024; classificazione dell’amministrazione distinta dalla qualificazione del servizio. Il catalogo del singolo servizio è un dato corrente: nessuna qualifica nominativa è garantita da questa nota.

[AgID, valutazione comparativa](https://docs.italia.it/italia/developers-italia/lg-acquisizione-e-riuso-software-per-pa-docs/it/stabile/acquisizione-software/valutazione-comparativa.html), §§ 2.3–2.5 e [tabella sinottica](https://docs.italia.it/italia/developers-italia/lg-acquisizione-e-riuso-software-per-pa-docs/it/stabile/attachments/allegato-e-tabella-sinottica-degli-elementi-necessari-al-percorso-decisionale.html): CAD 68–69, sei famiglie, TCO inclusa uscita, interoperabilità, sicurezza/privacy e servizio; accertare riuso/open source prima della soluzione proprietaria e motivare l’impossibilità. Il riuso del sorgente non rende gratuiti manutenzione, migrazione e formazione.

## Fondamenti tecnici verificati

- David Goldberg, *What Every Computer Scientist Should Know About Floating-Point Arithmetic*, 1991, riprodotto nella [documentazione Oracle](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html): significando, esponente, arrotondamento e intervallo distinti. Esempi binari e complemento a due del capitolo sono calcoli originali verificabili.
- Pat Morin, *Open Data Structures*, versione Python, [§ 1.3 Mathematical Background](https://opendatastructures.org/ods-python/1_3_Mathematical_Background.html): notazione asintotica; distinguere limite O e ordine stretto Theta. Gli esercizi dichiarano input e memoria ausiliaria.
- [PostgreSQL 18, § 13.2 Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html): quattro livelli SQL; PostgreSQL assimila Read Uncommitted a Read Committed e il suo Repeatable Read impedisce anche i phantom, ma non ogni anomalia di serializzazione. La tabella del manuale separa garanzie minime SQL e implementazione.
- [RFC 9114, HTTP/3](https://www.rfc-editor.org/rfc/rfc9114.html): HTTP/3 usa QUIC; non estendere TCP a ogni versione HTTP.
- Roy T. Fielding, *Architectural Styles and the Design of Network-based Software Architectures*, 2000, [capitolo 5](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm): client/server, stateless, cache, interfaccia uniforme, livelli e code-on-demand opzionale. Un semplice endpoint JSON non prova il rispetto di tutti i vincoli REST.

## Riscontri integrativi

- [D.lgs. 138/2024, Gazzetta ufficiale](https://www.gazzettaufficiale.it/eli/gu/2024/10/01/230/sg/pdf), artt. 6 e 23–25 letti nel PDF acquisito: essenziali/importanti; responsabilità e formazione degli organi; misure proporzionate; significatività e sequenza 24/72 ore/mese. Il mese decorre dalla notifica, non dall’incidente; relazione mensile durante l’incidente ancora aperto, finale entro un mese dalla conclusione. Eccezione dei prestatori fiduciari: notifica entro 24 ore. Nessuna lettura integrale dell’intera Gazzetta dichiarata.
- [MEF, legge 90/2024 art. 1, vigente dal 10 ottobre 2025](https://def.finanze.it/DocTribFrontend/executePrintArticolo.do?articolo=Articolo+1&codiceOrdinamento=0000000000000010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&id=%7BAA11E7C0-AFF2-4925-B787-55C9CF7A0C55%7D): letto articolo completo, due pagine. Platea e tassonomia proprie, segnalazione 24 ore/notifica 72 dalla medesima conoscenza, esclusioni comma 7. La legge 132/2025 ha aggiornato il riferimento alla tassonomia: non usare solo la legge 90 originaria.
- [CAD, art. 1 l-ter, edizione 20 aprile 2026](https://docs.italia.it/italia/piano-triennale-ict/codice-amministrazione-digitale-docs/it/v2026-04-20/_rst/capo1_sezione1_art1.html): tre requisiti cumulativi; uso di chiunque anche commerciale in forma disaggregata; formati aperti utilizzabili automaticamente con metadati; gratuità/costi marginali salvo art. 7 d.lgs. 36/2006.
- [Regolamento UE 2023/138](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32023R0138), artt. 1–4: dataset dell’allegato nel campo della direttiva; formati leggibili meccanicamente e API obbligatori, bulk dove indicato; documentazione, condizioni, contatto e metadati HVD. Licenza CC0/CC BY 4.0 o equivalente/meno restrittiva secondo allegato. Le esclusioni del quadro informativo non scompaiono.
- [ANAC, parere su incentivi e DEC](https://www.anticorruzione.it/documents/91439/d65e8b95-df51-493e-a7ed-896e801e07d7): testo indicizzato ufficiale conferma art. 114(8), allegato II.14 artt. 31–32 aggiornato dal 209/2024: funzione in capo al RUP salvo particolare importanza con DEC distinto. Il download ha restituito errore, conservato come tale; non è una copia normativa acquisita né base per soglie non lette.
- [MEF, legge 208/2015 comma 516](https://def.finanze.it/DocTribFrontend/getAttoNormativoDetail.do?ACTION=getArticolo&codiceOrdinamento=0000000000000010000000000000000000000000005160000000000000000000000000000000000000000000000000000000000000000000000000000000000000&id=%7B87A9A68D-F316-4522-97DB-D295E5E1FB14%7D), testo indicizzato: autorizzazione motivata del vertice per indisponibilità/inidoneità o necessità e urgenza per continuità. L’acquisto ICT non si esaurisce nel solo confronto del prezzo.
- [PagoPA, glossario PDND](https://developer.pagopa.it/pdnd-interoperabilita/guides/manuale-operativo-pdnd-interoperabilita/riferimenti-tecnici/glossario) e [AgID, FAQ SUAP](https://www.agid.gov.it/en/domande-frequenti/suap): adesione, erogazione/fruizione, finalità e voucher. Il capitolo spiega il percorso concettuale, non replica pulsanti/versioni dell’interfaccia né attribuisce alla PDND il potere di creare una base giuridica.
- Scikit-learn, documentazione tecnica ufficiale: [alberi decisionali § 1.10](https://scikit-learn.org/stable/modules/tree.html), [k-means § 2.3](https://scikit-learn.org/stable/modules/clustering.html#k-means). Metodi e limiti; dati e calcoli nel manuale sono esempi originali, non benchmark o risultati empirici della PA.
- NIST: [gestione chiavi](https://csrc.nist.gov/projects/key-management/key-management-guidelines) distingue rev. 5 finale e rev. 6 in bozza; [log management](https://csrc.nist.gov/Projects/log-management) riporta rev. 1 ancora in lavorazione e [800-92](https://csrc.nist.gov/pubs/sp/800/92/final) finale 2006. Non presentare bozze come norme italiane.

[[topics/ict-rettifiche-specialistiche-2026]] · [[books/moduli/m-tr01-ict-trasformazione-digitale/index]]. Questa nota consolida claim puntuali al 3 ottobre 2026: non promuove automaticamente le raccolte storiche né certifica ogni versione tecnica menzionata nel volume.

Verificato nuovamente il testo integrale dell’articolo 14 della legge 132/2025 sulla Gazzetta ufficiale: quattro commi, nessuna delega della decisione provvedimentale al sistema. Esempi di albero, k-means, metriche, TCO e SLA ricalcolati con dati didattici originali.
