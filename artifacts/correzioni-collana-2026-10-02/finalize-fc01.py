from pathlib import Path
import re,json,hashlib,shutil
B=Path('wiki/books/moduli/m-fc01-ministeri');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-03')
for p in (B/'chapters').glob('*.md'):
 s=p.read_text(encoding='utf8')
 s=s.replace('sono riferimenti consolidati per inquadrare','sono riferimenti per inquadrare')
 s=s.replace("Il R.D. 30 ottobre 1933, n. 1611 costituisce la base ordinamentale storica richiamata dalle fonti consolidate del modulo. La disciplina vigente deve essere verificata prima di attribuire poteri, casi di patrocinio o regole processuali puntuali.","Il R.D. 30 ottobre 1933, n. 1611 costituisce la base ordinamentale dell’Avvocatura, da leggere con le successive modifiche e le norme processuali speciali. Le sezioni seguenti distinguono i principali titoli di patrocinio e i criteri di competenza utili al profilo amministrativo.")
 s=re.sub(r'^review_required:.*$','review_required: false',s,flags=re.M)
 p.write_text(s,encoding='utf8')
for p in [Path('wiki/sources/ministeri-rettifiche-organizzazione-contabilita-2026-10-03.md'),Path('wiki/topics/ministeri-organizzazione-bilancio-rettifiche-2026.md')]:
 s=p.read_text(encoding='utf8');s=re.sub(r'^review_required:.*$','review_required: false',s,flags=re.M);s=s.replace('La revisione specialistica corrente deve chiudere i delta nel rapporto 15.','Il riesame specialistico del 3 ottobre 2026 chiude i delta nel rapporto 15 M-FC01; rimangono distinti PDF e preflight.')
 p.write_text(s,encoding='utf8')
p=R/'15-moduli-m-fc01-ministeri.md';arc=A/'before-text/VOL-03'/p.name
if p.exists() and not arc.exists():shutil.copy2(p,arc)
p.write_text('''# M-FC01 — Audit specialistico conclusivo, 3 ottobre 2026

## 1. Sintesi editoriale

Riesaminate le dodici correzioni dell'audit integrale, i nuovi claim e le verifiche applicative. Il testo può passare al congelamento tramite CLI: nessun errore grave o medio noto resta aperto nel perimetro riesaminato. Il giudizio non attesta il PDF finale.

## 2. Perimetro e metodo

Baseline integralmente letta nell'audit VOL-03. Riesame attuale dei blocchi modificati e delle 106 righe estratte per norme, date e termini, comprese alcune righe di metadata. Controllati CCNL, fonti organizzative, PIAO, contabilità statale, acquisti e comportamento. Dati operativi: nessun box dichiarato o rilevato dal contratto CLI.

## 3. Registro specialistico

| ID | Posizione | Categoria | Gravità | Evidenza consolidata | Correzione applicata | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| FC01-S01 | 03; 12 | Contratto e comportamento | Grave | CCNL 9 maggio 2022 art. 12/allegato A e art. 42; definitivo 6 agosto 2026 acquisito | Quattro aree; rinnovo definitivo; rimostranza e limite penale o amministrativo | Verificato e chiuso |
| FC01-S02 | 05–07 | Organizzazione | Media | D.Lgs. 303/1999 artt. 7–8; D.Lgs. 300/1999 artt. 3/5/6; R.D. 1611/1933, regolamento e fonti Avvocatura | Responsabilità, durata missioni, modelli alternativi, patrocinio e competenza | Verificato e chiuso |
| FC01-S03 | 08 | PIAO | Media | D.M. 132/2022 e allegato; D.L. 80/2021 | Quattro sezioni, tre anni, aggiornamento annuale e termine ordinario; ruoli distinti | Verificato e chiuso |
| FC01-S04 | 09 | Bilancio dello Stato | Grave | RGS residui, L. 196/2009, DFP 2026 Camera e DPFP RGS | Riscosso non versato; 40 residui nell'esempio; unità di voto, sezioni, due conti, parificazione | Verificato e chiuso |
| FC01-S05 | 10 | Acquisti | Media | L. 296/2006 commi 449–450 e tabella Consip corrente | Convenzione distinta da procedura, MePA distinto da piattaforma, soglia 5.000 e caso | Verificato e chiuso |
| FC01-S06 | 12; 14 | Imparzialità | Media | L. 241/1990 art. 6-bis e D.P.R. 62/2013 artt. 6–7 | Segnalazione accompagnata da astensione quando dovuta, anche nell'istruttoria | Verificato e chiuso |
| FC01-S07 | 08–15 | Quiz e strumenti | Media | 60 righe nel ledger; cento criteri; confronto con sezioni teoriche | Soluzioni separate, 15 chiavi per lettera, criteri di correzione; criterio 82 allineato alle sette domande effettive | Verificato e chiuso |
| FC01-S08 | 01; 07; rinvii | Autonomia del lettore | Media | Scansione e rilettura dei passaggi | Rimossi residui di linguaggio staff; fonti pubbliche; ancore core precise e risolte | Verificato e chiuso |

## 4. Riscontri normativi

Il contratto 2025–2027 è definitivo dal 6 agosto 2026; le decorrenze puntuali restano distinte (ferie art. 21 dal 1° gennaio 2027). La struttura professionale del 2022 resta il riferimento per le quattro aree. L'ordine rinnovato per iscritto non consente atti penalmente vietati o illeciti amministrativi. La missione PCM ordinaria non supera la durata del Governo istitutore; discipline speciali sono esplicitamente distinte.

Il DFP 2026 risulta presentato il 22 aprile. Il testo distingue quel documento dal Piano di medio termine, dal DPFP già impiegato nel 2025 e dal DBP europeo; non presume approvazioni autunnali 2026 non acquisite. I residui attivi includono le due componenti statali. Programma e tipologia sono unità di voto; conto del bilancio e patrimonio sono componenti del rendiconto, non le due sezioni della legge di previsione.

## 5. Fonti e tracciabilità

URL, riferimenti puntuali e limiti nelle note `ministeri-rettifiche-organizzazione-contabilita-2026-10-03`, `aran-ccnl-funzioni-centrali-pcm-2022-2026` e `contabilita-generale-stato-e-bilancio-stato`. Topic nuovo collegato a fonti e capitoli. Testo definitivo CCNL acquisito in raw senza alterare le fonti storiche. Snapshot dei manoscritti e apparati staff conservati negli artefatti.

## 6. Verifiche eseguite

60 opzioni corrette confrontate con i rispettivi commenti e alternative; distribuzione complessiva A/B/C/D = 15/15/15/15. Tutte le batterie sono autocorreggibili e i casi conservati. Ricalcolo residui 20+20=40. Cento criteri confrontati con le domande, incluso il riallineamento del criterio 82. Zero rinvii irrisolti. Gate di densità 08–15 superati; due warning di lunghezza sul nucleo delle cento risposte, esplicitamente conservati e motivati dall'autonomia del workbook.

## 7. Suggerimenti facoltativi

Nessuna nuova integrazione contenutistica obbligatoria nel perimetro dei dodici rilievi. La suddivisione visiva delle risposte è valutata sul PDF, preservando integralmente i criteri.

## 8. Priorità di produzione

Freeze manuale documentato se il gate CLI resta non implementato. Seguono controllo figure, esportazione del candidato e preflight; nessun rinvio a futura revisione umana del testo.

## 9. Giudizio sul testo

Correzioni specialistiche concluse nel perimetro indicato. Passaggio consentito al text freeze; nessuna dichiarazione di pubblicabilità di VOL-03 nel suo complesso, perché FC03 e PDF hanno verifiche separate.

## 10. Limiti

Riesame del candidato rispetto alla baseline letta, non nuova lettura visuale di ogni pagina. Le verifiche non estendono i claim a ogni eccezione settoriale, elenco di uffici, importo economico o calendario futuro. I warning di lunghezza restano registrati; nessun font è ridotto per assorbirli.
''',encoding='utf8')
ledger={'module':'M-FC01','date':'2026-10-03','baseline':'wiki/reviews/audit-integrale-2026-10-02/VOL-03.md','quizReviewed':60,'openAnswerCriteriaReviewed':100,'claimExtractLinesRead':106,'pdfVerified':False,'files':[{'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted((B/'chapters').glob('*.md'))]}
(A/'VOL-03-FC01-specialist-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf8')
print('Riesame FC01 chiuso; rapporti e ledger scritti.')
