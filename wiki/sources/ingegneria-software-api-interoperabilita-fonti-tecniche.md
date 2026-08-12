---
id: source-ingegneria-software-api-interoperabilita-fonti-tecniche
type: source
title: "Ingegneria software, API e interoperabilità — fonti tecniche e istituzionali"
status: processed
domain: "informatica specialistica e PA digitale"
topics: ["ingegneria software", "api", "interoperabilità", "PDND"]
entities: ["IEEE Computer Society", "IETF", "OpenAPI Initiative", "AgID", "PDND", "Unione europea"]
source_refs: ["sources/pa-digitale-cad-identita-documenti-servizi-dati", "sources/d-lgs-7-marzo-2005-n-82-amministrazione-digitale", "sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026"]
book_refs: ["m-tr01-ict-trasformazione-digitale"]
confidence: 0.91
updated_at: 2026-07-29
created_at: 2026-07-29
review_required: true
canonical: true
tags: ["source", "vol-08", "software-engineering", "api", "interoperabilita", "pdnd"]
source_type: "technical_standards_and_official_documentation"
source_url: "https://www.agid.gov.it/it/linee-guida"
source_date: 2026-07-29
authority_level: alta
---

# Ingegneria software, API e interoperabilità — fonti tecniche e istituzionali

## Uso

Nota consolidata per il capitolo 6 di VOL-08. Sostiene requisiti, progettazione, qualità, test, gestione della configurazione, contratti HTTP API, descrizioni OpenAPI e quadro istituzionale di ModI, PDND e interoperabilità europea. Le scelte operative di una specifica amministrazione e l’applicazione puntuale delle regole PDND restano soggette a verifica sulle versioni vigenti e a review specialistica.

## Fonti primarie e istituzionali

- **Guide to the Software Engineering Body of Knowledge, SWEBOK V4.0a**, IEEE Computer Society, release settembre 2025: <https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf>. Organizza le aree di conoscenza relative, fra l’altro, a requisiti, progettazione, costruzione, test, qualità, processi e gestione della configurazione.
- **Software Engineering Body of Knowledge — Knowledge Areas**, IEEE Computer Society, consultato il 29 luglio 2026: <https://www.computer.org/education/bodies-of-knowledge/software-engineering/topics>.
- **RFC 9110 — HTTP Semantics**, IETF/RFC Editor: <https://www.rfc-editor.org/rfc/rfc9110>. Riferimento per metodi, semantica delle richieste, codici di stato, proprietà safe e idempotent e rappresentazioni HTTP.
- **RFC 8259 — The JavaScript Object Notation (JSON) Data Interchange Format**, IETF/RFC Editor: <https://www.rfc-editor.org/rfc/rfc8259>.
- **RFC 9457 — Problem Details for HTTP APIs**, IETF/RFC Editor: <https://www.rfc-editor.org/rfc/rfc9457>. Modello standard per rappresentare dettagli di errore in risposte HTTP.
- **OpenAPI Specification**, OpenAPI Initiative, versione pubblicata più recente consultata il 29 luglio 2026: <https://spec.openapis.org/oas/latest.html>. Definisce una descrizione standard e indipendente dal linguaggio per API HTTP.
- **SOAP Version 1.2 Part 1: Messaging Framework**, W3C Recommendation: <https://www.w3.org/TR/soap12-part1/>.
- **Linee guida sull’interoperabilità tecnica delle Pubbliche Amministrazioni** e allegati, AgID: <https://www.agid.gov.it/it/linee-guida>. Definiscono tecnologie, pattern di interazione, pattern di sicurezza, profili e governance del Modello di interoperabilità.
- **Il nuovo Modello di interoperabilità**, AgID, consultato il 29 luglio 2026: <https://www.agid.gov.it/it/infrastrutture/sistema-pubblico-connettivita/il-nuovo-modello-interoperabilita>. Richiama versionamento, documentazione, throttling, logging, accounting, livelli di servizio e scalabilità delle API.
- **Linee guida sull’infrastruttura tecnologica della PDND per l’interoperabilità dei sistemi informativi e delle basi di dati** e allegati, AgID, disponibili nel catalogo delle linee guida: <https://www.agid.gov.it/it/linee-guida>.
- **Piano Triennale per l’informatica nella PA 2024-2026**, sezione e-service in interoperabilità tramite PDND, documentazione Italia: <https://docs.italia.it/italia/piano-triennale-ict/pianotriennale-ict-doc/it/2024-2026/capitolo-3_servizi/e-service-in-interoperabilit%C3%A0-tramite-pdnd.html>.
- **Regolamento (UE) 2024/903 — Interoperable Europe Act**, EUR-Lex: <https://eur-lex.europa.eu/eli/reg/2024/903/oj>. Inquadra misure per un livello elevato di interoperabilità del settore pubblico nell’Unione.
- **New European Interoperability Framework**, Commissione europea: <https://ec.europa.eu/isa2/eif_en/>. Quadro concettuale per interoperabilità giuridica, organizzativa, semantica e tecnica.

## Decisioni editoriali

- Presentare il ciclo di vita come insieme di attività correlate, non come una sequenza universale e immutabile.
- Distinguere bisogno, requisito, vincolo e criterio di accettazione.
- Collegare ogni requisito verificabile a una o più evidenze di test.
- Descrivere architetture e attributi di qualità mediante compromessi, evitando la formula «una tecnologia è sempre migliore».
- Trattare l’API come contratto osservabile prima che come codice o prodotto.
- Usare REST come stile architetturale e SOAP come protocollo di messaggistica, senza presentarli come semplici formati alternativi.
- Limitare OpenAPI alla descrizione delle API HTTP e non attribuirgli l’implementazione del servizio.
- Distinguere compatibilità del contratto, versione dell’API e versione della specifica OpenAPI.
- Presentare ModI e PDND per ruoli, finalità e processo logico, senza inventare dettagli operativi mutevoli.
- Distinguere interoperabilità da pubblicazione open data e accesso indiscriminato.
- Trattare protezione dei dati, autorizzazione e sicurezza come requisiti trasversali, rinviando l’approfondimento ai capitoli dedicati.

## Limiti e review

- Terminologia e processi PDND possono evolvere: verificare linee guida e manuali operativi vigenti prima del text freeze.
- SWEBOK organizza la disciplina ma non sostituisce gli standard specifici né le procedure dell’ente.
- Gli esempi HTTP e OpenAPI devono essere validati da un API designer.
- La classificazione dei livelli di interoperabilità deve essere verificata rispetto al quadro europeo e al ModI vigente.
- Ruoli, finalità, autorizzazioni, basi giuridiche e dati personali richiedono review giuridico-organizzativa e privacy.
- Metodologie, linguaggi, framework e piattaforme richiesti devono essere validati sui singoli bandi.

## Collegamenti

- [[sources/pa-digitale-cad-identita-documenti-servizi-dati]]
- [[sources/d-lgs-7-marzo-2005-n-82-amministrazione-digitale]]
- [[sources/agid-piano-triennale-informatica-pa-2024-2026-aggiornamento-2026]]
- [[topics/open-data-interoperabilita-cloud-pa]]
- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]]
- [[books/moduli/m-tr01-ict-trasformazione-digitale/chapters/06-ingegneria-software-api-interoperabilita-pa]]
