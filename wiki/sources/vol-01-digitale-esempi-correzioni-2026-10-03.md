---
id: source-vol-01-digitale-esempi-correzioni-2026-10-03
type: source
title: "VOL-01: CAD, documenti, dati ed esempi informatici verificati"
status: consolidated
domain: concorsi pubblici italiani
topics: ["pa digitale", "informatica", "competenze digitali", "privacy"]
entities: ["CAD", "AgID", "Garante", "Microsoft", "PostgreSQL"]
source_refs: ["sources/pa-digitale-cad-identita-documenti-servizi-dati.md", "sources/database-programmazione-formati-concorsi.md"]
book_refs: ["il-metodo-bando"]
confidence: 0.96
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: ["correzioni-collana", "fonti-primarie"]
source_type: official-documentation
source_url: https://docs.italia.it/italia/piano-triennale-ict/codice-amministrazione-digitale-docs/it/v2026-04-20/_rst/capo1_sezione1_art1.html
source_date: 2026-04-20
authority_level: primary
---

# Consolidamento puntuale

## CAD e privacy

Il [CAD, art. 1, versione 20 aprile 2026](https://docs.italia.it/italia/piano-triennale-ict/codice-amministrazione-digitale-docs/it/v2026-04-20/_rst/capo1_sezione1_art1.html) comprende nella categoria documentale anche le copie informatiche da analogico. Domicilio digitale: PEC oppure recapito certificato qualificato, non email ordinaria. Open data: requisiti cumulativi di riuso, formato/elaborabilità/metadati e condizioni economiche. Il formato aperto da solo non basta.

L'[art. 22](https://docs.italia.it/italia/piano-triennale-ict/codice-amministrazione-digitale-docs/it/v2026-04-20/_rst/capo2_sezione1_art22.html) distingue le copie e la loro efficacia probatoria: non confondere natura informatica, conformità all'originale e sottoscrizione. Una scansione può essere copia per immagine; non diventa per questo un documento firmato digitalmente.

Raw: `wiki/raw/correzioni-collana-2026-10-02/cad-art1-versione20260420.html` e `cad-art22-versione20260420.html`. Versione esplicita della fonte, senza dedurre un aggiornamento normativo successivo dalla sola data di consultazione.

Il [documento di indirizzo Garante sul RPD pubblico](https://www.garanteprivacy.it/documents/10160/0/Documento%2Bdi%2Bindirizzo%2Bsu%2Bdesignazione%2C%2Bposizione%2Be%2Bcompiti%2Bdel%2BResponsabile%2Bdella%2Bprotezione%2Bdei%2Bdati%2B%28RPD%29%2Bin%2Bambito%2Bpubblico.pdf/04f7e00d-548d-9c2c-8582-79219dfa1838?download=true&version=1.0) spiega il conflitto con incarichi che determinano finalità o modalità del trattamento. Nel glossario il RPD informa, consiglia e sorveglia; la scelta delle finalità e dei mezzi compete al titolare. Il concetto di dato personale riguarda persone fisiche (GDPR art. 4, già consolidato nelle fonti del cap. 7).

## Esempi originali e riferimenti tecnici

- [Microsoft, riferimenti relativi/assoluti/misti](https://support.microsoft.com/it-it/office/modificare-il-tipo-di-riferimento-relativo-assoluto-o-misto-dfec08cd-ae65-4f56-839e-5f0d8d0baca9): nella copia i riferimenti senza dollaro variano; il dollaro blocca la coordinata cui precede. Esempio originale: B2=10, B3=20, B4=30, E1=10%; C2=`=B2*$E$1` copiata dà 1, 2, 3.
- [Microsoft, stampa unione](https://support.microsoft.com/it-it/word/use-mail-merge-to-personalize-letters): documento modello, origine dati, campi, anteprima e unione. Esempio originale con due convocazioni fittizie.
- [PostgreSQL, foreign key](https://www.postgresql.org/docs/current/tutorial-fk.html), [JOIN](https://www.postgresql.org/docs/current/tutorial-join.html), [ORDER BY](https://www.postgresql.org/docs/17/queries-order.html): vincolo referenziale distinto dall'operazione di collegamento; ordinamento esplicito necessario per un ordine garantito. Esempio originale con uffici 10/20 e dipendenti 1/2/3; JOIN filtrata su Anagrafe restituisce Bianchi e Verdi.

## Collegamenti

[[topics/pa-digitale]], [[topics/informatica]], [[topics/competenze-digitali]], [[topics/privacy]]. Capitolo 10 e appendici A/B del VOL-01; V01-25/26/27/28/29/45/47. Gli esempi software sono piccoli casi di calcolo/lettura, non istruzioni a operare su dati personali reali.
