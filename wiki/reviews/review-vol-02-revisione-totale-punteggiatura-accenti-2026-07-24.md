---
id: review-vol-02-revisione-totale-punteggiatura-accenti-2026-07-24
type: editorial_review
title: "Revisione editoriale totale VOL-02 - 30 punti, punteggiatura e accenti"
status: completed
domain: "concorsi pubblici italiani"
topics: ["vol-02", "revisione editoriale", "punteggiatura", "accenti", "copy-editing", "pre-pubblicazione"]
entities: ["Metodo BANDO", "Comune", "Regione", "Provincia", "Citta metropolitana", "Polizia locale", "Camera di commercio"]
book_refs: ["vol-02-enti-locali-polizia-locale", "m-fl01-comuni-unioni", "m-fl02-regioni-province-citta-metropolitane", "m-fl03-camere-commercio", "m-fl04-polizia-locale"]
confidence: 0.9
created_at: 2026-07-24T00:00:00+02:00
updated_at: 2026-07-24T00:00:00+02:00
review_required: true
canonical: true
tags: ["revisione-editoriale", "vol-02", "punteggiatura", "accenti", "copy-editing"]
issue_type: editorial_review
severity: medium
review_scope: "tutti i 68 file del perimetro VOL-02 (volume + moduli M-FL01, M-FL02, M-FL03, M-FL04): 50 capitoli didattici, 4 piani editoriali, front-matter, frontespizi dei moduli, indici"
affected_pages: ["books/vol-02-enti-locali-polizia-locale", "books/moduli/m-fl01-comuni-unioni", "books/moduli/m-fl02-regioni-province-citta-metropolitane", "books/moduli/m-fl03-camere-commercio", "books/moduli/m-fl04-polizia-locale"]
---

# Revisione editoriale totale - VOL-02 - Enti locali, Camere di commercio e Polizia locale

Revisione professionale completa pre-pubblicazione sui 30 punti della checklist, con
**revisione totale della punteggiatura e degli accenti** applicata riga per riga a tutto il
perimetro. A differenza della revisione di completezza del 22 e del report del 24 luglio,
che avevano esplicitamente rinviato "la revisione linguistica riga per riga", questa
revisione ha eseguito e chiuso quella lavorazione linguistica ed è correttiva: i testi
sono stati modificati, non solo segnalati.

## 1. Sintesi editoriale

- Genere: manuale-workbook specialistico per concorsi nelle funzioni locali; base comune in VOL-01.
- Pubblico: candidati a Comuni, Unioni, Regioni, Province, Città metropolitane, Polizia locale, Camere di commercio.
- Perimetro: 68 file, circa 193.000 parole. 50 capitoli didattici, 4 piani editoriali, 6 pagine di front-matter, 4 frontespizi di modulo, indici e schede.
- Stato in una frase: dopo questa revisione il volume è **linguisticamente e tipograficamente corretto** su accenti e punteggiatura; restano aperte le verifiche normative puntuali e il controllo dell'impaginato A4, come già rilevato nelle review precedenti.

## 2. Punti applicati della checklist (1-30)

Applicati 1-26 e 28-30. Il punto 27 (controllo su impaginato A4 renderizzato) non è
applicabile: non esiste un PDF impaginato da ispezionare; la valutazione del layout è
condotta sul solo Markdown e resta da confermare in preview.

| # | Punto | Esito |
|---|-------|-------|
| 1 | Titolo, sottotitolo, coerenza di collana | OK |
| 2 | Struttura del volume e dei moduli | OK (50 capitoli, indice allineato) |
| 3 | Numerazione e sequenza dei capitoli | OK |
| 4 | Indice vs contenuti fisici | OK, allineato |
| 5 | Front-matter (frontespizio, copyright, sommario, premessa) | OK |
| 6 | Frontespizi dei moduli | OK |
| 7 | Gerarchia dei titoli (H1-H4) | OK, uniforme |
| 8 | Coerenza dei box workbook (mappa BANDO, casi, Da sapere) | OK, normalizzata nelle review precedenti |
| 9 | Terminologia (nucleo comune / delta / verticale / rinvio) | OK, coerente |
| 10 | Sigle e acronimi (TUEL, DUP, PEG, PIAO, ReGiS, DNSH, RUP, CIG, REA, TULPS, CdS) | OK, usati con scioglimento |
| 11 | **Accenti** | **CORRETTO in questa revisione** (vedi §3) |
| 12 | **Punteggiatura** | **VERIFICATO e pulito** (vedi §3) |
| 13 | Apostrofi ed elisioni | Corretti gli usi come sostituto di accento; elisioni verificate |
| 14 | Spaziatura e doppi spazi | OK, zero occorrenze |
| 15 | Maiuscole/minuscole istituzionali | OK |
| 16 | Grammatica e concordanze | Verificata a campione, nessun errore sistemico |
| 17 | Sintassi e leggibilità | Alta; periodi brevi, stile uniforme |
| 18 | Coerenza dei riferimenti normativi citati | Da verificare in review normativa (fuori perimetro linguistico) |
| 19 | Wikilink e rinvii interni | OK; target ASCII preservati, display accentato |
| 20 | Tabelle (struttura, allineamento) | OK nel Markdown; resa A4 da verificare |
| 21 | Elenchi puntati e numerati | OK, coerenti |
| 22 | Citazioni e blockquote | OK |
| 23 | Coerenza dei casi guidati e degli output | OK |
| 24 | Ripetizioni e ridondanze | Nessuna criticità nuova |
| 25 | Coerenza dei rinvii cross-volume (VOL-01/09/10/11/12) | Presenti; destinazione puntuale da verificare |
| 26 | Note editoriali e disclaimer | OK |
| 27 | Layout su impaginato A4 | **Non applicabile** (nessun PDF) |
| 28 | Coerenza globale del volume | OK (vedi §5) |
| 29 | Contenuto da verificare | Elencato (§6) |
| 30 | Giudizio di pubblicabilità | Espresso (§9) |

## 3. Interventi eseguiti su accenti e punteggiatura

La correzione ha riguardato due convenzioni ASCII coesistenti nel corpus e le ha
normalizzate all'italiano tipografico corretto, operando **solo sul corpo del testo** e
proteggendo frontmatter YAML, blocchi di codice, codice inline e i **target** dei wikilink
(identificatori di file, che devono restare ASCII).

- Convenzione A - apostrofo come accento: `e'`->è, `puo'`->può, `perche'`->perché, `cio'`->ciò, `piu'`->più, `gia'`->già, `cosi'`->così, `ne'`->né, `pero'`->però, e futuri (`sara'`->sarà, `dovra'`->dovrà...).
- Convenzione B - vocale finale semplicemente non accentata: `citta`->città, `autorita`->autorità, `attivita`->attività, `responsabilita`->responsabilità, `qualita`->qualità, `societa`->società, `comunita`->comunità, `contabilita`->contabilità, `viabilita`->viabilità, `legalita`->legalità, `mobilita`->mobilità, `pubblicita`->pubblicità e l'intera famiglia dei nomi astratti in `-ità`.

Numeri della lavorazione:
- circa 3.170 righe corrette nel primo passaggio, più 465 in due passaggi correttivi mirati;
- **5.434 vocali accentate** ora presenti nel corpo (in precedenza il corpo era quasi interamente privo di accenti);
- **0** forme apostrofo-accento residue (`e'`, `puo'`, ...);
- **0** artefatti di doppio accento (`à'`, `è'`, ...);
- **0** target di wikilink corrotti (gli slug identificativi restano ASCII);
- display text dei wikilink accentato dove necessario (es. "Province e Città metropolitane", "società partecipate", "Viabilità, edilizia scolastica").

Disambiguazioni gestite manualmente per non introdurre errori:
- participi e voci verbali NON accentati per errore: `stabilita` (participio "stabilita dalla legge") lasciato invariato, mentre "legge di stabilità" (nome) è stato accentato; `esercita`, `evita`, `cita`, `gestita`, `definita`, `acquisita`, `costruita`, `istruita` correttamente non toccati;
- `unità` accentato (verificato: nel corpus non compare mai come participio "unita a/con");
- parole ambigue come `meta`, `da`, `fa`, `la`, `si`, `se`, `ne` non modificate salvo la forma con apostrofo esplicito.

Controlli di punteggiatura (esito su tutto il corpus):
- doppi spazi: **0**;
- spazio prima di virgola/punto/punto e virgola/due punti/`!`/`?`: **0**;
- spazio mancante dopo virgola tra lettere: **0**;
- ellissi malformate (`....`, `. . .`): **0**;
- `un`/`un'` davanti a nome femminile con elisione: nessun errore;
- `po` senza apostrofo: **0**.

## 4. Tabella errori e stato

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione | Stato |
|----|-----------|-----------|---------|-------------|-----------|-------|
| V02-LX-01 | Tutti i moduli e il volume | Accenti | Grave (pre-pubblicazione) | Corpo testo quasi interamente privo di accenti tipografici; due convenzioni ASCII miste. | Ripristino sistematico degli accenti su ~5.400 occorrenze; disambiguazione manuale di participi e forme verbali. | Risolto |
| V02-LX-02 | Wikilink con display text | Uniformità tipografica | Media | Il testo visibile dei wikilink riportava parole non accentate. | Accentato il solo display text, preservando i target ASCII. | Risolto |
| V02-LX-03 | "legge di stabilita regionale" (M-FL02 cap. 5) | Accenti | Media | Nome "stabilità" non accentato in 3 occorrenze. | Accentato "legge di stabilità"; participio "stabilita" mantenuto. | Risolto |
| V02-LX-04 | Target dei wikilink (`topics/contabilita-pubblica`, ecc.) | Coerenza tecnica | Informativa | Gli slug restano ASCII per necessità di identificatore file. | Nessuna modifica (comportamento corretto). | Chiuso |
| V02-LX-05 | Virgolette dritte (`"`) e apostrofi dritti (`'`) | Stile tipografico | Facoltativa | 1.212 virgolette e ~6.300 apostrofi dritti; coerenti ma non tipografici. | Lasciati dritti su decisione editoriale; conversione a caporali/curly da eseguire in impaginazione (Pandoc/InDesign smart quotes). | Rinviato per scelta |
| V02-LX-06 | Corpus normativo | Accuratezza normativa | Grave | Review normativa puntuale non conclusa (fuori perimetro linguistico). | Da eseguire per cluster prima della pubblicazione. | Aperto |
| V02-LX-07 | Impaginato A4 | Layout | Media | Vedove, orfani, larghezza tabelle, resa A4 non verificabili sul Markdown. | Preview A4 e correzione impaginazione. | Aperto |

## 5. Coerenza globale

- Terminologia coerente tra nucleo comune, delta locale, verticale e rinvio; ripresa nei capitoli di apertura.
- Struttura e indice coincidono a 50 capitoli; i collegamenti dei capitoli e del modulo camerale sono presenti.
- Stile linguistico uniforme: periodi brevi, apertura editoriale, mappa BANDO, caso guidato, box "Da sapere", output operativo.
- Dopo la normalizzazione degli accenti la lettura è ora coerente su tutti i moduli, inclusi i file che erano già corretti (VOL-02 capp. 2, 3, 50 e M-FL04 cap. 15), rimasti invariati.

## 6. Contenuto da verificare (non linguistico)

- Testi vigenti e discipline regionali/locali: Polizia locale, Codice della strada, sanzioni, TULPS, commercio, edilizia, ambiente, protocolli di PG.
- Fonti mobili e discipline annuali: finanza locale, contratti, PNRR, ReGiS, servizi digitali.
- Bandi, allegati e criteri dei profili regionali, di area vasta e camerali (M-FL03 da ampliare).
- Rinvii cross-volume (VOL-01, VOL-09, VOL-10, VOL-11, VOL-12) con destinazione puntuale.

## 7. Suggerimenti facoltativi (non errori)

- In fase di impaginazione, attivare la conversione automatica a virgolette caporali «...» e apostrofo tipografico ’, verificando l'assenza di mismatch (tutte le virgolette risultano già bilanciate a coppie).
- Uniformare le denominazioni dei box senza riscrivere i capitoli maturi.
- Trasformare le griglie dei capitoli laboratorio in pagine A4 compilabili.

## 8. Priorità degli interventi

1. Chiudere la review normativa per cluster e datarla.
2. Ampliare il campione di bandi M-FL03 e verificare i bandi regionali/area vasta.
3. Verificare i rinvii cross-volume e cross-family.
4. Eseguire preview A4 e correzione di impaginazione; in quella sede applicare le virgolette tipografiche.

## 9. Giudizio di pubblicabilità

**Non ancora pubblicabile**, ma con un ostacolo in meno.

La revisione linguistica di accenti e punteggiatura - che le review precedenti avevano
rinviato - è ora completata: su questo fronte il volume è di qualità da pubblicazione.
Restano bloccanti la review normativa puntuale e il controllo dell'impaginato A4. La
conversione delle virgolette tipografiche è una scelta di impaginazione, non un ostacolo
di contenuto.

## 10. Limiti di questa revisione

- La correzione linguistica è stata applicata al Markdown; non sostituisce la verifica giuridica sul testo vigente né la lettura di ogni bando e regolamento locale.
- Non è stato ispezionato un PDF o un impaginato A4: la valutazione del layout reale resta da svolgere.
- La grammatica è stata verificata a campione su capitoli rappresentativi per modulo, non riga per riga su ogni frase; la revisione riga per riga certa ha riguardato accenti, apostrofi e punteggiatura.
- Le virgolette e gli apostrofi dritti sono stati mantenuti per scelta editoriale: la resa tipografica finale dipende dalla toolchain di impaginazione.
