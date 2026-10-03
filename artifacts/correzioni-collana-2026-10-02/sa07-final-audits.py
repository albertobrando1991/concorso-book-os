from pathlib import Path
import json,re
A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-07');B=Path('wiki/books/moduli')
changes=json.loads((A/'VOL-07-changes.json').read_text(encoding='utf8'))['changes'];audit=json.loads(Path('artifacts/review-integrale-2026-10-02/VOL-07-ledger.json').read_text(encoding='utf8'));sev={x['id']:x['severity'] for x in audit['findingsDetails']}
details={
'M-SA01':'''Capitolo 04: titolo riallineato in testo, indice e scheda; mantenute le integrazioni INT già riesaminate separatamente. Capitolo 05: divieto di accesso civico generalizzato ai dati sanitari, bilanciamento dell’accesso documentale, termini 7/30 giorni dell’art. 4 L. 24/2017 e distinzione FSE/dossier. Il termine per integrare non viene sommato automaticamente al primo termine. Capitolo 06: rubrica con errori critici su competenza, riservatezza e sicurezza che impediscono l’esito sufficiente anche con somma favorevole; esempio completo di delega e richiesta documentale.

Capitolo 09: risolti i calcoli di variazione (−4,44%), quota di ammortamento e sterilizzazione (20.000 euro, residuo 80.000). Il caso distingue contributo in conto capitale da contributo in conto esercizio; lettura integrale dei consolidati degli artt. 26, 29, 31 e 32 D.Lgs. 118/2011: documenti e scadenze 30 aprile, 31 maggio e 30 giugno confermati. La riconciliazione 8−6 = 2 milioni delle integrazioni preesistenti resta preservata.

Capitolo 10: AIC e rimborsabilità separate, classi A/H/C/C(nn), confini farmaco/dispositivo, FEFO/FIFO, quarantena e catena del freddo. Calcolo di riordino con disponibilità utilizzabile 530 dopo esclusione di 150 unità in quarantena. Il D.P.C.M. 11 febbraio 2026 è recepito dalla fonte ufficiale consolidata dal coordinamento: decorrenza, categorie, soglia farmaci 40.000 euro e regola della gara pluriennale non sono estesi impropriamente a ogni acquisto. NSO resta distinto da contratto, piattaforma e fatturazione.

Riscontri ufficiali selettivi nei capitoli e nelle source pertinenti; non attestata una nuova lettura di ogni articolo di tutto il corpus sanitario. Le prove sono concorsuali e documentali, non autorizzano una pratica clinica.''',
'M-SA04':'''Capitolo 01: obbligo generale inglese/informatica distinto dal formato del bando; DPR 220/2001 con schema e soglie dei profili pertinenti. Capitolo 02: principi analitici selezionati, microbiologia e vitalità, ematologia/emostasi, immunologia e istocitologia; distinte sensibilità analitica e diagnostica, precisione ed esattezza, calibrazione e controllo qualità. Serie 100–107 con media 100 e deviazione standard 2: z = 0; 0,5; 1; 1,5; 2; 2,5; 3; 3,5. Grafico originale coerente con la tabella; trend identificato senza dichiarare un criterio universale di accettazione. Gruppi biologici e livelli di contenimento non sono sinonimi; art. 275 D.Lgs. 81/2008 confrontato con la copia INL gennaio 2026, cappe e rifiuti descritti nel perimetro didattico.

Capitolo 03: CTDIvol in mGy, DLP in mGy·cm, DAP in Gy·cm²; esempio DLP 8×30 + 8×10 = 320 mGy·cm. Indicatori distinti dalla dose individuale. Letti integralmente i consolidati Normattiva degli artt. 146 e 166 del D.Lgs. 101/2020: lavoratori esposti 20 mSv dose efficace, 20 cristallino, 500 pelle/estremità; popolazione 1/15/50, con media su 1 cm² per la pelle. Nessun limite di dose applicato al paziente. Gravidanza/allattamento e RM distinti; D.M. 14 gennaio 2021 e marcature degli impianti preservano le verifiche professionali. Apparati movimento e rumore inseriti con domande e soluzioni; nel primo i contorni sono allargati e sfocati, nel secondo il contrasto medio è costante. Gli originali sono stati ispezionati dal coordinamento; la composizione PDF è un controllo successivo.

Capitolo 04: classi MDR I/IIa/IIb/III e IVDR A/B/C/D distinte, UDI distinto dal numero inventariale, FSCA distinta da FSN; incidente grave comprende anche deterioramento temporaneo grave e potenzialità dell’esito. Termini di segnalazione dell’operatore mantenuti senza confonderli con quelli del fabbricante. Fonti EUR-Lex con challenge non utilizzate come se fossero state lette; riscontri specifici documentati nelle fonti ministeriali e istituzionali. Il controllo non certifica il fascicolo tecnico di un dispositivo.'''}
for code,m,nums in [('M-SA01','m-sa01-sanita-amministrativa',range(1,15)),('M-SA04','m-sa04-tecnici-sanitari-prevenzione',[28,29,35,36,37,38,39,40,41])]:
 p=R/f'15-moduli-{m}.md';arc=R/'archive'/('pre-correzioni-'+p.name)
 if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
 rows=[]
 for n in nums:
  fid=f'V07-{n:02}';x=changes[fid];rows.append('| '+' | '.join([fid,', '.join(Path(f).name for f in x['files'] if f.endswith('.md')),'Audit specialistico',sev[fid],x['change'],'Riesame dei delta e riscontri specifici descritti nelle sezioni 4 e 6','Corretto'])+' |')
 text=f'''# {code} — Audit specialistico automatico delle correzioni, 3 ottobre 2026

## 1. Sintesi editoriale

Riesaminati i delta dell’audit integrale e i relativi raccordi. Non risultano errori testuali gravi o medi aperti nei claim effettivamente insegnati e verificati. La lettura integrale diagnostica precedente costituisce la baseline; non si dichiara una nuova lettura integrale delle parti invariate. Nessuna dichiarazione di pubblicabilità dell’intero volume.

## 2. Punti applicati della checklist

Punti 1–26 e 28–30 pertinenti: accuratezza, fonti, definizioni, autonomia, ambito professionale, casi, calcoli, risposte, lessico e raccordi. Micro-revisione e Humanizer sui delta. Punto 27 ancora da controllare nel nuovo PDF.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''+ '\n'.join(rows)+f'''

## 4. Osservazioni per capitolo

{details[code]}

## 5. Coerenza globale

Il percorso mantiene i limiti di profilo e i rinvii agli altri moduli. Matrici e topic sono raccordati al contenuto aggiunto; i precedenti esiti sono storici. Nessun conteggio di righe viene usato come prova autonoma di completezza. I claim mobili conservano fonte e ambito.

## 6. Contenuti verificati

Evidenze e URL sono nelle source note del modulo e nel [[reviews/correzioni-collana-2026-10-02/VOL-07|registro per ID]]. Il precedente ostacolo di accesso Normattiva è superato per gli articoli elencati nella sezione 4, scaricati in `wiki/raw/correzioni-collana-2026-10-02/`. Sono controlli selettivi, non una certificazione integrale dei corpus. Nessun box «Dato operativo» è stato rilevato dal contratto CLI del modulo: non vi sono righe obbligatorie omesse.

## 7. Suggerimenti facoltativi

Nessun ampliamento estraneo ai rilievi necessario per questo passaggio.

## 8. Priorità degli interventi

Superare il gate CLI e registrare il freeze del testo; quindi generare e verificare effettivamente il nuovo PDF, compresi apparati, tabelle e spazi di risposta. Non trasformare il gate del report in una verifica visiva.

## 9. Giudizio di pubblicabilità

Testo del modulo idoneo al freeze nel perimetro concorsuale dichiarato. Pubblicabilità del volume non attestata: PDF, preflight e conferma conclusiva restano separati.

## 10. Limiti di questa revisione

Audit automatico editoriale con riscontri esterni puntuali; non parere professionale per casi reali, validazione clinica o controllo di ogni norma territoriale. Gli esempi numerici originali non diventano standard. Le immagini originali hanno verifica distinta dal loro futuro impaginato. I report storici restano archiviati.
'''
 p.write_text(text,encoding='utf8')
 for p in (B/m/'chapters').glob('*.md'):
  t=p.read_text(encoding='utf8');t=re.sub(r'^review_required:.*$','review_required: false',t,flags=re.M);t=re.sub(r'^draft_stage:.*$','draft_stage: specialist-audit-complete',t,flags=re.M);p.write_text(t,encoding='utf8')
 p=B/m/'planning/02-matrice-copertura-didattica.md';t=p.read_text(encoding='utf8');t+='\n### Riesame automatico del 3 ottobre 2026\n\nDelta normativi, specialistici e casi riesaminati nel report 15 corrente del modulo. I rilievi testuali pertinenti risultano corretti; per SA04 i tre apparati originali sono inseriti. Il controllo del nuovo PDF e il preflight restano da svolgere: il presente esito riguarda il testo.\n';t=re.sub(r'^review_required:.*$','review_required: false',t,flags=re.M);p.write_text(t,encoding='utf8')
print('Audit 15 SA01/SA04 e metadata scritti; gate da eseguire.')
