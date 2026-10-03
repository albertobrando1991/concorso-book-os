---
id: vol-01-text-freeze-manifest
type: text_freeze_manifest
title: Text freeze - Il Metodo BANDO, integrazioni nazionali
status: frozen
book_id: il-metodo-bando
volume_code: VOL-01
module_code: M-PA01
pipeline_target: il-metodo-bando
freeze_date: 2026-10-02
reference_commit: 38a03176d279cd58236ac60f19c0a32cebce6594
updated_at: 2026-10-02
created_at: 2026-08-21
review_required: false
canonical: true
tags: [text-freeze, vol-01, m-pa01, pipeline-step-16, delta-integrazioni]
---

# Text freeze — Il Metodo BANDO

## Esito e perimetro

Nuovo congelamento testuale dopo le integrazioni INT01–04 nei capitoli 05, 06 e 12. Il manifest fotografa 32 sezioni e tre file di governo del volume; i nuovi controlli specialistici riguardano il delta, non una ricertificazione al 2 ottobre dell'intero volume. Il confronto SHA-256 con il manifest del 21 agosto conferma 29 capitoli identici; cambiano soltanto 05, 06 e 12.

Il precedente manifest è conservato in [[reviews/pipeline/VOL-01/archive/16-il-metodo-bando-pre-integrazione-2026-10-02]]. I precedenti cut-off e le evidenze storiche restano identificabili; non viene ereditata alcuna certificazione visiva del PDF dopo le modifiche.

## Riferimento di versione

- Commit di base del workspace: 38a03176d279cd58236ac60f19c0a32cebce6594. Gli hash sotto descrivono i file effettivi modificati nel worktree, non pretendono che siano già contenuti nel commit.
- Algoritmo: SHA-256 sui byte dei file.
- Cut-off dell'audit aggiuntivo: 2 ottobre 2026, solo INT01–04; audit storico restante: 21 agosto 2026.
- Fonti puntuali, eccezioni e limiti di lettura: report15 e note fonte citate. Nessuna certificazione generale di tutti i testi normativi consolidati.
- La review_required generale dei capitoli resta distinta dalla chiusura della revisione del delta e dal congelamento; non viene trasformata in dichiarazione di prodotto pubblicabile.

## Condizioni verificate

| Condizione | Evidenza effettiva | Esito |
|---|---|---|
| Presenza e indice | 32 target dichiarati, 32 file presenti, 32 riferimenti nell'indice | superata |
| Copertura | Gate canonico runCoverageGate: passed=true, zero blocker/warning; 21 nuclei completi, nessuno parziale/solo-nominato/mancante | superata |
| Rinvii e fonti | Gate rinvii dei tre capitoli passato; source_refs e last_compiled_from tutti esistenti | superata nel delta; resto immutato |
| Contratto studente | Lint legacy cap05/06/12: passed=true, zero blocker/warning, nessuna promozione formato2 | superata |
| Humanizer | Controllo manuale assistito sui nuovi passaggi: audit_base per05/06 e main per12; micro-revisioni e verifica indipendente. Non un nuovo step11 integrale | superata nel delta |
| Errori obbligatori | Report14 e15 passati via CLI, zero blocker/warning; RB01 e C12-01–03 risolti | superata |
| Audit specialistico | Report15 e due review indipendenti: nessun rilievo grave o medio residuo nel perimetro | superata nel delta |
| Tabelle | Due tabelle storiche da quattro colonne suddivise con chiave comune; cap05/06/12 massimo tre colonne, dati invariati | superata sul Markdown |
| Integrità | git diff --check senza errori; 29 hash di capitolo identici al precedente freeze | superata |
| Gate automatico freeze | Risposta reale CLI: gate-not-implemented per text-freeze | non automatizzato; accettazione manuale motivata dopo i controlli |

## File congelati

Percorsi relativi a wiki/books/il-metodo-bando. Frozen significa contenuto testuale sotto controllo delle modifiche, non PDF pronto.

| File | Stato | Data | SHA-256 |
|---|---|---|---|
| index.md | frozen | 2026-10-02 | 1a8e62335f09b76b65652d095cdfcfb370f8d61674450978ec642e170335a388 |
| planning/00-scheda-pipeline.md | frozen | 2026-10-02 | 4ebb8ac2c53342b0cc8693acf001824591171c8666bfd4b20335b8429f940686 |
| planning/02-matrice-copertura-didattica.md | frozen | 2026-10-02 | 0a48ec6e7fd843e89e801671b8828dd6d2ddc23caf69565ac125acf3ed49db84 |
| chapters/introduzione.md | frozen | 2026-10-02 | 14029d77081c45687cc6bd7bca84531e554c1cb22cb4aef1b73ab47c7b1f281d |
| chapters/il-nuovo-candidato-pubblico.md | frozen | 2026-10-02 | dcebc7ec82dda3e7cf46a355751c4f6fafaf4858e071311d3a99fc249af81457 |
| chapters/anatomia-del-bando.md | frozen | 2026-10-02 | 2c583598b7ef05694bce6d0e359a71f9c4534f29baab8db8af3ffd9b4f03ab57 |
| chapters/il-metodo-bando.md | frozen | 2026-10-02 | 6cf59171517f02c66e549ff5018e9edaa69e77d019b0e20d7329f2313834dd1a |
| chapters/costituzione-e-ordinamento-dello-stato.md | frozen | 2026-10-02 | db7781d7e0f8d5d3b73f7f81375fe23ed3090f5be3b64d09e44375506e3e55fd |
| chapters/diritto-amministrativo-per-candidati.md | frozen | 2026-10-02 | cef0c0465d4b63ed21e5791d0a5c058f10be1b855d4ce17cdcaf6422a01846ab |
| chapters/pubblico-impiego-e-organizzazione-pa.md | frozen | 2026-10-02 | d54aace2050b3cf307c95636c69151756c894a95feb3c0c3c055e97682435238 |
| chapters/trasparenza-anticorruzione-privacy.md | frozen | 2026-10-02 | 526d9c0e9531f452b93ecfd55f083f36554f5899caabe6be17f9a5d2e2276b08 |
| chapters/contabilita-pubblica-essenziale.md | frozen | 2026-10-02 | 428766e3fcd4057ea89afa1cc089b87623f34a2afebccbf98c066875aa268e61 |
| chapters/contratti-pubblici-essenziali.md | frozen | 2026-10-02 | 5866365c772967f8a112b5cf6377070fc144886e5b6ad2422ff28487102d29c4 |
| chapters/informatica-pa-digitale-competenze-digitali.md | frozen | 2026-10-02 | 49cbc58790d33130d3576f0e197cbbc17fa1aa6b2a8977c854b5437f31265912 |
| chapters/inglese-concorsuale-essenziale.md | frozen | 2026-10-02 | 162bb71bf3a4ea4603eda7e912ead4f377b352c026daf471e44150b34f38ac34 |
| chapters/logica-comprensione-ragionamento.md | frozen | 2026-10-02 | 8cc12a4724844e97573eabd7a679e7e22759ec06198b071409681a871e752c06 |
| chapters/metodo-di-studio-per-concorsi.md | frozen | 2026-10-02 | 09fafc7c6bdac8e0fa0c63aa78d3084f58a31eee3f16692eddc279abef8c644b |
| chapters/la-prova-a-quiz.md | frozen | 2026-10-02 | 0f15c4ed6a524a4b0c2da6ba0ca13e085b84f437fa166871d8cc0083d0a1b559 |
| chapters/prova-scritta-teorico-pratica.md | frozen | 2026-10-02 | 935208474037ef0662244d5b00e9adc2559dc30e5149bb85d974be1ee5cdd592 |
| chapters/la-prova-orale.md | frozen | 2026-10-02 | 3ddc6426f19b6cf459adc7e3a836d2d79f1ad3ebdedeb64b8e90a3269b99b484 |
| chapters/casi-pratici-problem-solving-amministrativo.md | frozen | 2026-10-02 | c8df450a98b85d27ccb4ab2525e5eb53b5fd46cd7fe583bd3efd619de4391f08 |
| chapters/quesiti-situazionali-soft-skills.md | frozen | 2026-10-02 | 0bdf584ff8e88f230848faf925084799de6dc4e8cd29f09388d9b8af4f3c0c6d |
| chapters/famiglie-concorsi-pubblici.md | frozen | 2026-10-02 | 123d361784708dcfb7a1612f1171f78fa50abdf0deb3b0d5e5a5e0ea6a26248a |
| chapters/mappe-profilo-cosa-resta-comune-cosa-cambia.md | frozen | 2026-10-02 | e5e97be6f8f7a41a513fdbe21c36df52cda9935fbff88faee0f7d677cc9b2b08 |
| chapters/scegliere-moduli-integrativi.md | frozen | 2026-10-02 | 47529ac0c6096750654262ca1d0f6f62fa41f57e23fc103587491e54b7a73d59 |
| chapters/sistema-adattabile.md | frozen | 2026-10-02 | ea89bafd5fb34030ed7a731206e5a2eb64d8facd1230bb3a03f59f3f965c2c53 |
| chapters/diario-degli-errori.md | frozen | 2026-10-02 | 2f996ebccb38f936a9d5dcd4ee38a8c25dd0c8d6cee2e43cd6e5fe3708cb0f85 |
| chapters/checklist-operative.md | frozen | 2026-10-02 | e1f50a6edd32bd766a8451d957a542bca950c69de5a4daa7e0b506000d2c71a0 |
| chapters/conclusione.md | frozen | 2026-10-02 | d44706c3f780f315aa3c346c5040d8e350ee5a9b4dacfed152b625fe87496d3d |
| chapters/appendice-a-glossario-essenziale-pa.md | frozen | 2026-10-02 | 2ccb807654e06b5aec101b66ea8bdf5e1df415c824973c021efe4333e2c0ce05 |
| chapters/appendice-b-100-parole-chiave-concorsi.md | frozen | 2026-10-02 | 0bf33370b7fa86cec50041ea8099433ae2ddfe73867fda6c1ebd13da0e6bcfd5 |
| chapters/appendice-c-template-bando-decoder.md | frozen | 2026-10-02 | c72c59f4af164c773cd30ad8a2fa50c2b3631766bf784efd11d4142915d3b2e0 |
| chapters/appendice-d-piano-studio-personale.md | frozen | 2026-10-02 | ef5cfdb87093583ba32128f8060e399f8228dea6f3e43fdd31f44cfb90eb7565 |
| chapters/appendice-e-schema-universale-risposta-orale.md | frozen | 2026-10-02 | d5faac47aa336405fd79175db6d7ffd7824677ec09388d5a898617889dcd84d8 |
| chapters/appendice-f-matrice-materie-profili.md | frozen | 2026-10-02 | 1a8c4b1d43bd2a0aef5bfea5ef18c8e377339dd019c9129d5d7db4681b6e2298 |

## Produzione ancora pendente

La nuova impaginazione deve essere sempre ottimizzata, secondo la preferenza dell'utente. Devono ancora essere verificati layout reale, nuova paginazione, immagini, tabelle in pagina, indice paginato e nuovo PDF; seguono preflight, confezionamento e conferma umana finale. Nessuno di questi esiti è dichiarato completato qui. Gli step17 e successivi non sono avviati da questo ciclo di chiusura.

## Regola dopo il congelamento

Solo correzioni controllate. Ogni modifica sostanziale a teoria, fonti, esempi, esercizi o struttura riapre i gate10–15. Anche una correzione tipografica richiede aggiornamento degli hash e nuova verifica tecnica pertinente. Non modificare silenziosamente i capitoli dopo il presente manifest.
