---
id: review-vol-07-step-16-m-sa01-text-freeze
type: review
title: Manifest di text freeze M-SA01 — integrazioni nazionali
status: complete
updated_at: 2026-10-02
created_at: 2026-08-04
review_required: false
canonical: false
book_refs: [m-sa01-sanita-amministrativa, vol-07-sanita-amministrativa-professioni-sanitarie]
source_refs: [sources/ssn-organizzazione-aziende-standard-lea, sources/contabilita-budget-aziende-sanitarie, sources/integrazione-sociosanitaria-accreditamento-quadro-nazionale-2026, sources/lea-aggiornamenti-pubblicati-settembre-2026]
tags: [pipeline-step-16, text-freeze, integrazioni-nazionali]
---

# Manifest di text freeze — M-SA01

## Esito e ambito

Versione testuale del 2 ottobre 2026: integrate INT-05–08 nei capitoli 04 e 09. Gli altri tre capitoli sono identici al precedente manifest e conservano l'audit al cut-off storico 28 luglio 2026. Non si dichiara una nuova verifica integrale di tutto il volume. Escluse Campania/ASL Caserta e cultura generale.

Il gate automatico restituisce `gate-not-implemented`: non è stato presentato come verde. Le condizioni sono controllate manualmente con le evidenze qui sotto; chiusura CLI mediante `--accept` motivato. Questo è un freeze del testo, non un'approvazione di PDF, impaginazione o pubblicazione.

## Condizioni verificate

| Condizione | Evidenza al 2 ottobre | Esito |
| --- | --- | --- |
| Capitoli presenti | Target 04, 05, 06, 09, 10; 5/5 file presenti | Superata |
| Copertura | Matrice 12 righe complete; coverage gate passed, zero blocker e warning | Superata |
| Rinvii e forma | Chapter lint legacy e verified-referral su tutti i cinque capitoli: zero blocker e warning | Superata |
| Humanizer | Step11 storici conservati; controllo del delta documentato nel nuovo report14 | Superata |
| Errori gravi e medi | Report14/15 correnti; revisione indipendente delle integrazioni senza rilievi residui | Superata |
| Audit specialistico | Step15 ricalcolato e passato; scope e limiti dichiarati nel report | Superata |
| Indice | Tutti i collegamenti risolti; cinque capitoli presenti e numerazione tecnica preservata | Superata |
| Fonti | 48 riferimenti dichiarati complessivi nei cinque capitoli; zero file mancanti | Superata |
| Stati | Tutti i cinque capitoli review_required:false; indice, piano e Bibbia coerenti | Superata |

Revisione indipendente: [[reviews/integrazione-sanita-verifica-indipendente-2026-10-02]]. I report14/15 precedenti sono conservati in archive; il manifest precedente resta in [[reviews/pipeline/VOL-07/archive/16-m-sa01-pre-integrazione-2026-10-02]].

## File identificati

Gli SHA-256 individuano i byte effettivi, anche in worktree non committata. La data identifica il pacchetto e non attribuisce una nuova verifica normativa ai capitoli invariati.

| File | Data pacchetto | SHA-256 |
| --- | --- | --- |
| `wiki/books/moduli/m-sa01-sanita-amministrativa/index.md` | 2026-10-02 | `3d5c03dc1a32cfda03e48d63da073c7e02dac2f9bfd0e5146812d8597b546fc0` |
| `wiki/books/moduli/m-sa01-sanita-amministrativa/planning/00-piano-editoriale.md` | 2026-10-02 | `e31c8397d5009c2fab94c3a772da8d5fd5bb9b84a50fd86ed965300bb41d2177` |
| `wiki/books/moduli/m-sa01-sanita-amministrativa/planning/02-matrice-copertura-didattica.md` | 2026-10-02 | `a149b4a69a6a54191f22e7d9708cc96416c17559c9ab0a0682beb2a2c7bf0a92` |
| `wiki/books/moduli/m-sa01-sanita-amministrativa/planning/09-bibbia-del-modulo.md` | 2026-10-02 | `eb890676a8d626d621bc719e346cc2cd8f733d922ca35462570eec1e857cf6e8` |
| `wiki/books/moduli/m-sa01-sanita-amministrativa/chapters/04-atti-procedimenti-flussi-informativi.md` | 2026-10-02 | `d60498e040922b51ee29eb29dcea2cc5138f29ec484d3359e5e4b47a7e60a94f` |
| `wiki/books/moduli/m-sa01-sanita-amministrativa/chapters/05-documentazione-accesso-conservazione.md` | 2026-10-02 | `2f65a3a2df0a527dde81dbdce6a78ecebea8c65c18bea21e416fd8a33da4072f` |
| `wiki/books/moduli/m-sa01-sanita-amministrativa/chapters/06-front-office-comunicazione-utenza.md` | 2026-10-02 | `9e7d97cd00646b04a14114c10422b3aa79c82dbb3f1818343ffb963c0d73c1ea` |
| `wiki/books/moduli/m-sa01-sanita-amministrativa/chapters/09-contabilita-budget-controllo-gestione.md` | 2026-10-02 | `acbb8642654bc16160e9759bceb46d79be98380959df4a79dab584a2b5486fa8` |
| `wiki/books/moduli/m-sa01-sanita-amministrativa/chapters/10-procurement-farmaci-dispositivi-magazzino.md` | 2026-10-02 | `40a40721cd64a171fb0a349c32c7a4739f595a112a125c8295478050616aa5b1` |
| `wiki/reviews/pipeline/VOL-07/13-moduli-m-sa01-sanita-amministrativa.md` | 2026-10-02 | `33ac419890cc6d06cdb38045ac444d586f79154deb661f82e62fb9810e677e79` |
| `wiki/reviews/pipeline/VOL-07/14-moduli-m-sa01-sanita-amministrativa.md` | 2026-10-02 | `354d89d5961a77616b4767e5dc1ce3c49a3f938c590ede2819e2a4d72c4b120f` |
| `wiki/reviews/pipeline/VOL-07/15-moduli-m-sa01-sanita-amministrativa.md` | 2026-10-02 | `bec4f0edab18be80ab4454c012cb1e9cd000c1edfc468ba0f5cb0b048e0a9419` |

## Recupero tracciato della pipeline

Una nota inserita tra il titolo Moduli e la tabella ha alterato l'associazione del parser. Il sync ha temporaneamente rimosso 157 record di stato, senza modificare i capitoli. Spostata la nota prima di Moduli e verificati quattro moduli e 25 capitoli; recuperato soltanto il run-state dai byte HEAD, identici all'index e privi di modifiche preesistenti. Nuovo sync: nessun target aggiunto o rimosso. Riaperti 14–23 pertinenti via CLI e rieseguiti realmente i gate14/15, senza inventare timestamp né alterare JSON a mano. I 169 target e lo storico estraneo all'integrazione sono preservati.

## Lavori successivi e controllo delle modifiche

Necessari controllo immagini, PDF rigenerato, ottimizzazione del layout, preflight e conferma umana finale24. Preferenza permanente dell'utente: verificare sempre anche spazi bianchi, tabelle, quiz, interruzioni, titoli orfani e leggibilità delle pagine. Il precedente PDF non rappresenta questo pacchetto. Ogni modifica sostanziale successiva riapre i gate10–15; le correzioni puramente tipografiche devono essere tracciate e riverificate.

## Correzione tipografica controllata successiva al freeze

Il 2 ottobre, su richiesta esplicita dell'utente sul layout, suddivise sette tabelle nei capitoli04/09 in blocchi collegati con massimo tre colonne. Nessuna modifica sostanziale di teoria, casi, quiz o soluzioni; conservate 114/114 tuple chiave-intestazione-cella, heading e frontmatter invariati. Lint e rinvii nuovamente superati. Evidenza: [[reviews/integrazione-layout-tabelle-sanita-2026-10-02]].

Gli hash della tabella sono aggiornati alla correzione controllata. Prima della suddivisione: cap04 `1b54fe0bf0bfb3c1dea69c628987d66883dd5f60f1858c85b752b0ad36320215`; cap09 `628883f2c2b67ca00abb66eb3a9bd74d7e9ce663e913fc9cbaee7416a4074a5d`. Nel successivo controllo visivo l'etichetta «Evidenze ed esiti» risultava isolata in fondo pagina: questa e la parallela «Azioni condizionate» sono state promosse a sottotitoli H4 sotto l'H3 esistente. Identico testo e identiche celle, nessuna nuova nozione; lint e rinvii rieseguiti e passati. L'hash intermedio del cap09 dopo le sole tabelle era `ef6c8325b44eb325af173e07786e2f524e7a69f4e93e6f858aed8a8f0232a2e5`. Non viene dedotta una nuova verifica normativa dall'intervento tipografico. Il controllo del PDF rimane distinto e pendente.
