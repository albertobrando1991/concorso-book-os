from pathlib import Path
import json,hashlib,re,shutil
A=Path(__file__).parent;B=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue')
rows=json.loads((A/'registro-applicazione.json').read_text(encoding='utf8'));selected=[r for r in rows if re.fullmatch(r'V09-\d+',r['id'])];assert len(selected)==38
fixes=[
'Ricomposte le tabelle dei capitoli 1, 5 e 9; titoli fuori dalle righe.',
'Domande, opzioni e risposte ricomposte; titoli dei nuclei descrittivi e collocati all’inizio della sezione.',
'Casi e fasi ricomposti; ridistribuzione dei capitoli 8, 13 e 14 in sei nuclei effettivi.',
'Eliminati i codici XX; 73 identificatori univoci nella matrice e nel testo.',
'Liquidazione, ordinazione e pagamento distinti nel modello degli enti locali.',
'Articoli 62–63 e allegato II.4: autonomia, qualificazione L/SF, livelli, requisiti e ricorso al soggetto qualificato.',
'Nomina e requisiti RUP, responsabili delle fasi, distinzione funzione DEC/nomina separata.',
'RACI compilata con modello dichiarato, valutazione, decisione e liquidazione distinte.',
'Programmazione triennale, aggiornamenti, soglie e riga di programma con CUI didattico.',
'Valore 234.000 euro comprensivo di opzioni, lotti e deroga massima 46.800 euro.',
'Cause di esclusione, self-cleaning, RTI, avvalimento, soccorso 5–10 giorni, OEPV; griglia risolta A 81,25/B 90,25.',
'Elementi dell’articolo 17 e atto annotato; modello compilabile nel laboratorio.',
'Valore e incorporazione dei documenti contrattuali esplicitati.',
'Soglie UE 2026, procedure nazionali e numero degli invitati; rotazione, interesse transfrontaliero e verifiche art.52.',
'Sotto soglia definito rispetto alle soglie UE; limiti nazionali distinti.',
'PAD, PCP, BDNCP, FVOE, pubblicità, trasparenza, guasti e CIG per lotto sviluppati.',
'Matrice obblighi ente/oggetto/importo; commi 449/450/510/512/516 e DPCM categorie 2026; eccezioni separate.',
'MePA Lavori include le nuove opere; distinto da SDA Lavori di manutenzione.',
'AQ, SDA e ASP sciolti e confrontati: durata, apertura, inviti e tempi.',
'Subappalto, varianti, sospensioni, penali, collaudo/CRE e CCT con presupposti, atti e tempi.',
'Revisione prezzi obbligatoria e regimi distinti; calcoli lavori 18.000 euro e servizi 2.400 euro.',
'Anticipazione 20% elevabile al 30%, annualità servizi e garanzia; esempio 40.000 euro oltre interessi.',
'Accesso digitale, primi cinque, oscuramento e termine speciale 10 giorni distinti dal ricorso.',
'Standstill 32 giorni e relative eccezioni, blocco cautelare, ricorso 30 giorni; rimedi esecutivi e ANAC.',
'Numero dichiarato degli elementi riallineato all’elenco.',
'RRF/PNRR, sette missioni, CID/OA, performance e chiusura 2026; scadenze trascorse indicate come tali.',
'Ruoli ReGiS e ciclo prevalidazione/validazione; scadenze DPO qualificate come esempio della misura.',
'Conti, comunicazioni, filiera, clausole, fatture e sanzioni; spesa 90.000 ammissibile e contributo 72.000.',
'Frode/irregolarità, conflitti e titolare effettivo; caso quote e doppio finanziamento risolti.',
'Art.17 tassonomia, regimi DNSH e scheda 3; venti notebook, prove e non pertinenza motivata.',
'Art.57 e CAM arredi DM254/2022: minimo cinque anni, ricambi, prove, imballaggi e premi 0/2/4/6/8.',
'Formazione parallela ai test ammessa nella rete dichiarata; dipendenze tecniche esplicitate.',
'Output/outcome e WBS uniformati; attività C resta bonifica dei dati anche nella simulazione.',
'WBS a tre livelli, Gantt datato, cammino critico A–B–D–F, margini e scenari 9/10/11 giorni.',
'Dieci tracce con dati, norme, atti, soluzioni e rubriche; università nel caso arredi sotto soglia.',
'Diario compilato, piani 30/60/90 e matrice reale di 73 nuclei; conteggi condivisi dichiarati.',
'Rimossa la promessa di appendici inesistenti; strumenti effettivi nei capitoli e kit finale.',
'Tre nuovi bandi ufficiali acquisiti: Ca’ Foscari, Bologna e Terre del Sole; limiti del campione espliciti.'
]
metrics=json.loads((A/'vol09-density.json').read_text(encoding='utf8'));assert all(not x['gate']['blockers'] and not x['gate']['warnings'] for x in metrics)
sources=sorted(Path('wiki/sources').glob('vol-09-*-2026-10-03.md'))
out='''# Report editoriale — VOL-09 Appalti, PNRR e fondi UE

## 1. Sintesi editoriale

Manuale specialistico per candidati ad appalti, procurement digitale, gestione PNRR e project management pubblico. Riesaminati i delta ai quattordici capitoli, quiz, casi, indice e matrice dopo la lettura integrale dell’audit iniziale. I 38 rilievi testuali sono applicati e verificati. La versione impaginata corrente deve ancora superare i controlli di produzione: questo report non autorizza la pubblicazione.

## 2. Punti applicati della checklist

Punti 1–4: indice reale, progressione e gerarchia. Punti 6–15: autonomia, coerenza, definizioni, regole, esempi e fonti. Punti 16–26 e 29: prosa, chiarezza, terminologia e correzione dei refusi nei delta. Punti 5 e 30: giudizio limitato al testo riesaminato. Punti 27–28: struttura Markdown controllata; impaginazione, leggibilità alle dimensioni finali e interruzioni restano alla prova PDF. Nessun controllo visuale del nuovo PDF è dichiarato svolto.

## 3. Tabella errori

Le posizioni originarie identificano i rilievi dell’audit del 2 ottobre, conservato immutato; dopo le integrazioni i numeri di riga sono cambiati.

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione applicata | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''
def cell(s):return re.sub(r'\s+',' ',s.replace('|','/')).strip()
for r in sorted(selected,key=lambda x:({'bloccante':0,'grave':1,'medio':2,'media':2,'lieve':3}.get(x['severity'].lower(),2),int(x['id'][-2:]))):
 fix=fixes[int(r['id'][-2:])-1]
 out+='| '+' | '.join(cell(str(v)) for v in [r['id'],r['position'],r['category'],r['severity'],r['description'],fix,'Verificato e chiuso nel testo; PDF separato'])+' |\n'
out+='\n### Registro di applicazione per ID\n\n| ID | File modificati | Fonte/evidenza | Stato finale |\n| --- | --- | --- | --- |\n'
for r in selected:
 files=[p for p in r['changedFiles'] if '/chapters/' in p];refs=[p for p in r['changedFiles'] if '/sources/' in p]
 out+='| '+r['id']+' | '+'; '.join(Path(p).name for p in files)+' | '+'; '.join(Path(p).stem for p in refs)+'; verifica esempi, matrice e gate | Testo verificato |\n'
out+='\n## 4. Osservazioni per capitolo\n\n'
observations=['Profili e bandi reali, confini fra famiglie e fasi contabili distinti.','Governance e qualificazione applicabili a casi; RACI dichiarata.','Fabbisogni, programmazione e valore completo calcolati.','Regole di gara e griglia OEPV risolta.','Soglie e procedure insegnate con eccezioni esplicite.','Flusso digitale e rettifiche con tracciabilità della versione.','Obblighi soggettivi e merceologici separati dagli strumenti.','Esecuzione insegnata con termini, presupposti e calcoli.','Accesso e tutela non confusi; decorrenze ed eccezioni distinte.','PNRR performance-based e chiusura storicamente corretta al 3 ottobre.','Spesa, pagamenti e controlli antifrode con quadri che riconciliano.','DNSH e CAM distinti; prove ambientali riferite all’oggetto.','Metodo PM² e rete con date e margini verificabili.','Dieci simulazioni autonome, rubrica, diario, calendario e kit.']
for n,x in enumerate(observations,1):out+=f'- Capitolo {n:02}: {x}\n'
out+='''
## 5. Coerenza globale

Matrice riallineata a 73 nuclei effettivi, con citazioni estratte dai manoscritti e conteggi Q/C/E condivisi per capitolo: non sono 73 apparati indipendenti. Tutti i 14 gate di copertura sono superati. Densità senza blocker o warning; nessuna immagine mancante né wikilink staff nel corpo. Corretto anche il richiamo della simulazione 10: C è sempre preparazione/bonifica dei dati. Verificati 23 calcoli e il calendario lavorativo; l’esito automatico prova queste proprietà, non la verità di tutta la normativa.

## 6. Contenuto verificato e fonti

Riscontri primari puntuali consolidati nelle source notes seguenti, con raw, articoli, date e limiti di acquisizione. Le risposte vuote/di errore non sono usate come prova. Per i commi finanziari sono state acquisite anche le pagine successive dell’articolo, evitando di scambiare la prima pagina per il testo dei commi 449–516.

'''
out+=''.join(f'- [[sources/{p.stem}]]\n' for p in sources)
out+='''
Norme consolidate: Codice dei contratti e allegati pertinenti; soglie UE 2026; obblighi Consip e categorie del DPCM 2026; tracciabilità e identificativi; regolamento finanziario 2024/2509; RRF e tassonomia; CAM arredi. Fonti operative: ANAC/Consip, Guida DNSH 2024, istruzioni di chiusura PNRR 16 aprile 2026, esempio DPO e PM² 3.1. Non viene presentata come adottata una proposta di modifica del PNRR priva del relativo atto del Consiglio verificato.

## 7. Suggerimenti facoltativi

Ulteriori esercizi per singoli bandi possono ampliare il testo. Non sono necessari per sanare i rilievi qui chiusi e non si promette copertura universale di ogni concorso.

## 8. Priorità degli interventi

Concludere audit specialistico e freeze tramite CLI; rigenerare il PDF e verificare tabelle, formule, grafico, titoli, indice, quiz, campi compilabili e preliminari. Gli eventuali rilievi della nuova prova riaprono il testo interessato.

## 9. Giudizio di pubblicabilità

**Pubblicabile dopo intervento medio di produzione e verifica dell’impaginato.** I 38 rilievi testuali sono risolti nel perimetro esaminato; non sono ancora chiusi i rilievi PDF. Nessuna approvazione finale o pubblicazione esterna è stata effettuata.

## 10. Limiti di questa revisione

Le verifiche normative sono puntuali, datate 3 ottobre 2026, e non certificano ogni futura modifica o atto applicativo. Il campione bandi è qualitativo, non statistico. Il PDF precedente non rappresenta i manoscritti integrati. Il nuovo Gantt è stato visionato come asset, ma occorre verificarlo nell’impaginato finale. Le prove sono conservate in VOL-09-verifica-esempi.json, VOL-09-gates.json, vol09-density.json e nel manifest della matrice; i report originari restano immutati.
'''
p=Path('wiki/reviews/pipeline/VOL-09/14-moduli-m-tr02-appalti-pnrr-fondi-ue.md');backup=A/'before-text/VOL-09/14-report-luglio.md'
if not backup.exists():shutil.copy2(p,backup)
p.write_text(out,encoding='utf8');Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-09.md').write_text(out,encoding='utf8')
for r in selected:
 r['status']='applicato-verificato-testo';r['textVerified']=True;r['finalPublicationVerified']=False
 r['verification']=['38 rilievi testuali ricontrollati; rapporto step14','14 gate copertura passati; 73 nuclei, densità senza blocker/warning','23 calcoli e calendario; nessun asset mancante o wikilink staff nel corpo','PDF corrente e produzione ancora da verificare']
 r['fileHashes']={p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in r['changedFiles'] if Path(p).exists()}
(A/'registro-applicazione.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print({'reported':len(selected),'sources':len(sources),'words':sum(x['metrics']['chapterWords'] for x in metrics),'finalPublicationVerified':False})
