from pathlib import Path
import json,re,hashlib
R=Path('wiki/reviews/pipeline/VOL-07');B=Path('wiki/books/moduli');A=Path('artifacts/correzioni-collana-2026-10-02');changes=json.loads((A/'VOL-07-changes.json').read_text(encoding='utf8'))['changes']
modules=[('M-SA02','m-sa02-professioni-sanitarie',list(range(14,28))+[29]),('M-SA03','m-sa03-dirigenza-medica-sanitaria',list(range(28,35))+[41])]
details={
'M-SA02':'''Responsabilità: struttura ed esercente distinti, art. 7 L. 24/2017 e art. 590-sexies senza immunità generale; regola temporanea 2026 espressamente condizionata alla grave carenza di personale. Consenso: capacità, minore/interdetto, rappresentanza, DAT e pianificazione non sono sinonimi; emergenza circoscritta. Assistenza: diagnosi infermieristica distinta da diagnosi medica, prevenzione ICA e osservazioni senza attribuire diagnosi all’OSS.

NEWS2: caso e somme riesaminati; scala 2 riservata all’insufficienza respiratoria ipercapnica confermata con obiettivo documentato, non alla sola BPCO; esclusi minori di 16 anni e gravidanza come uso generale. Triage: 5 priorità con immediatezza, 15/60/120/240 minuti e rivalutazione; tempi di accesso, non durata dell’intero percorso. BLS/ALS/NLS: riconoscimento, distinzione ritmi e cause reversibili, centralità della ventilazione neonatale; nessuna dose o manovra invasiva prescritta dal manuale.

DM 77: standard nazionali distinti da effettiva implementazione; IFeC riferito al complesso dei setting. PASSI: scarti 0,4/0,2/0,3 superiori alla tolleranza da arrotondamento 0,15, causa non dimostrata; corretto anche il limite inferenziale del rapporto 39,3/47,4. PREMAL: art. 5 letto nel fascicolo GU, differenza 12/24 ore e 48 ore/7 giorni, senza inventare flussi locali. Screening: intervalli nazionali di riferimento, estensioni regionali e transizione HPV tenute distinte.

TPALL: L. 689/1981, D.Lgs. 758/1994 e parte VI-bis D.Lgs. 152/2006 restano percorsi differenti; termine 60 giorni di verifica delle prescrizioni distinto dai 30 di pagamento. Esempio 300–1200: minore fra un terzo del massimo (400) e doppio del minimo (600) = 400. AUA non sostituisce AIA; controperizia e controversia mantengono oggetto, termini e garanzie; verbale separa fatti osservati da qualificazione e seguito. I cinque nuovi casi professionali arrivano a un output verificabile senza attribuire competenze estranee.''',
'M-SA03':'''Quadro concorsuale: art. 37 D.Lgs. 165/2001 distingue obbligo generale di informatica/inglese e modalità del bando; DPR 483, articoli per medico, farmacista, biologo e psicologo, conferma schema ordinario 20 titoli e 80 prove, soglie 21/30 e 14/20. I casi speciali non sono ricondotti automaticamente al modello. DPR 220 è stato trattato nei moduli di personale non dirigente.

Programmazione: copia valida della relazione NSG ministeriale 2022 ospitata dalla Camera; riscontro diretto metodologia alle pp. PDF 19–20: soglia di sufficienza 60 in ciascuna area, senza compensazione. Il testo non usa il documento come risultato sanitario 2026. Il cruscotto è originale: 180/200 = 90%, 72/80 = 90%, 8/160 = 5%, target esplicitamente didattici e denominatori definiti.

Qualità: evento avverso, near miss ed evento sentinella distinti, SIMES e reporting interno collegati senza identificarli; RCA retrospettiva e FMEA proattiva applicate a un esempio. Autonomia medica: rimosso il divieto generale improprio; il manuale non sostituisce la responsabilità clinica del professionista. Caso differenziale: ipotesi esemplificative e dati discriminanti, nessuna diagnosi certa dalla sola associazione temporale col farmaco.

CNOP: pagina ufficiale del codice attualmente vigente confrontata con archivio 1 dicembre 2023–24 dicembre 2024. Letti i passaggi pertinenti su competenza, segreto, custodia, consenso e committenza, inclusi articoli 16–17, 24–25 e 32. Eliminata la falsa vigenza del testo 2023. Gli altri codici non sono stati sostituiti con fonti non controllate.'''}
for code,m,ids in modules:
 p=R/f'15-moduli-{m}.md';arc=R/'archive'/('pre-correzioni-'+p.name)
 if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
 rows=[]
 for n in ids:
  x=changes[f'V07-{n:02}'];rows.append(f"| V07-{n:02} | "+', '.join(Path(z).name for z in x['files'])+' | Audit specialistico | Come rilievo storico | '+x['change']+' | Riesame del delta e delle fonti consolidate descritto sotto | Verificato nel perimetro del modulo |')
 do='''
| ID | Dato operativo | Area automatica | Fonte e versione | Verifica | Esito |
| --- | --- | --- | --- | --- | --- |
| DO-SA02-05-NEWS2-ER-2024 | NEWS2 | clinico-assistenziale | Regione Emilia-Romagna settembre 2024; RCP dicembre 2017 | 2026-10-03 | chiuso: scala, popolazione, calcoli e limiti coerenti |
| DO-SA02-05-TRIAGE-2019 | Priorità e tempi triage | clinico-assistenziale | Ministero Salute, linee nazionali 2019, tabelle 1–2 | 2026-10-03 | chiuso: priorità, tempi di accesso e rivalutazione distinti |
''' if code=='M-SA02' else 'Nessun box Dato operativo rilevato dal contratto CLI nel modulo. Le tabelle didattiche sono dichiarate come tali.'
 t=f'''# {code} — Audit specialistico automatico delle correzioni

## 1. Sintesi editoriale

Concluso il riesame specialistico automatico dei delta richiesti dall’audit integrale. Le correzioni sono presenti, hanno teoria autonoma e verifiche coerenti. Questa conclusione riguarda il perimetro del modulo e non il PDF, gli apparati SA04 o la pubblicabilità dell’intero volume.

## 2. Punti applicati della checklist

Punti 1–26 e 28–30 verificati sui delta e sui raccordi, usando la lettura integrale diagnostica precedente come baseline. Non dichiarata una nuova lettura integrale dei passaggi invariati. Controllati contenuto, fonti, termini, confini professionali, casi, calcoli e soluzioni. Micro-revisione e Humanizer svolti sui passaggi sostanziali. Punto 27 rinviato al controllo effettivo dei nuovi PDF.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''+ '\n'.join(rows)+f'''

## 4. Osservazioni per capitolo

{details[code]}

## 5. Coerenza globale

Nessun conflitto noto residuo nei delta del modulo. I nuovi esempi usano dati sufficienti e non trasformano il manuale in una procedura clinica o aziendale. Frontmatter e matrici vengono aggiornati all’esito del riesame; la baseline storica resta distinguibile. Registro per ID: [[reviews/correzioni-collana-2026-10-02/VOL-07]].

## 6. Contenuti verificati

Le evidenze sono nelle source note dei capitoli, aggiornate prima del testo, e negli artifact del 3 ottobre. Riscontri selettivi su fonti ufficiali, con esclusione delle risposte challenge. Il controllo non certifica ogni articolo di ogni corpus né procedure locali mai fornite. Non restano richieste di futura revisione umana come prerequisito del testo.

{do}

## 7. Suggerimenti facoltativi

Nessun ampliamento facoltativo necessario alla chiusura dei rilievi assegnati al modulo.

## 8. Priorità degli interventi

Completare il gate CLI, poi text freeze del modulo. A livello di volume restano gli apparati di SA04 e i nuovi PDF: devono essere realmente verificati, non sostituiti dall’esito di questo audit.

## 9. Giudizio di pubblicabilità

Testo del modulo idoneo al successivo freeze nel perimetro concorsuale dichiarato. Nessuna autorizzazione alla pubblicazione del volume: la resa editoriale e gli apparati richiedono il nuovo candidato PDF e il controllo conclusivo.

## 10. Limiti di questa revisione

Audit automatico editoriale e specialistico, non certificazione clinica o parere professionale per casi reali. I confronti esterni sono selettivi e documentati. Nessun dato clinico individuale, prova strumentale reale o legge regionale viene validato per uso operativo. Le parti mobili conservano data e ambito.
'''
 if code=='M-SA02':t+='\nGate del capitolo pilota rieseguiti: densità e copertura entrambi passed, zero blocker/warning, due DO estratti correttamente. Artifact: `artifacts/correzioni-collana-2026-10-02/SA02-05-gates.json`.\n'
 p.write_text(t,encoding='utf8')
 for p in (B/m/'chapters').glob('*.md'):
  s=p.read_text(encoding='utf8');s=re.sub(r'^review_required:.*$','review_required: false',s,flags=re.M);s=re.sub(r'^draft_stage:.*$','draft_stage: specialist-audit-complete',s,flags=re.M);p.write_text(s.rstrip()+'\n',encoding='utf8')
 p=B/m/'planning/02-matrice-copertura-didattica.md';s=p.read_text(encoding='utf8');s+='\n### Esito del riesame automatico del 3 ottobre 2026\n\nI delta del modulo sono stati riesaminati nello [[reviews/pipeline/VOL-07/15-moduli-'+m+'|step 15 corrente]]: nessun errore testuale noto residuo nel perimetro. Il nuovo freeze segue il gate CLI; apparati degli altri moduli e PDF di volume restano separati.\n';s=re.sub(r'^review_required:.*$','review_required: false',s,flags=re.M);s=re.sub(r'^status:.*$','status: reviewed',s,flags=re.M);p.write_text(s,encoding='utf8')
print('Report 15 SA02/SA03 redatti e metadati raccordati al riesame sostanziale; esito CLI ancora da eseguire.')
