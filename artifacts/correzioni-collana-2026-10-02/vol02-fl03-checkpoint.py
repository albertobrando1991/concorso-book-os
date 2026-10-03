from pathlib import Path
import json,re,hashlib
art=Path('artifacts/correzioni-collana-2026-10-02');base=Path('wiki/books/moduli/m-fl03-camere-commercio')
src=Path('wiki/sources/vol-02-camerale-verifica-2026-10-03.md')
t=src.read_text(encoding='utf-8').replace('sources/vol-02-documentazione-elettorale-verifica-2026-10-03','sources/d-p-r-28-dicembre-2000-n-445-documentazione-amministrativa')
if '# Documentazione e scenari' not in t:
 t+='''\n# Documentazione e scenari didattici\n\nPer artt. 40 e 43 D.P.R. 445/2000 si riusa il nucleo consolidato di [[sources/d-p-r-28-dicembre-2000-n-445-documentazione-amministrativa]]: certificazioni nei rapporti privati, dichiarazioni sostitutive e acquisizione d'ufficio nei rapporti con PA e gestori. La fonte conserva review su altri nuclei: qui si usa soltanto la verifica puntuale della decertificazione documentata.\n\nGli esempi di bando dei capitoli 01 e 05 sono riclassificati come compositi, senza attribuire a una specifica selezione materie o frequenze. Non costituiscono un nuovo campione empirico né modificano i bandi storici acquisiti.\n'''
src.write_text(t,encoding='utf-8')
state=json.loads((art/'VOL-02-changes.json').read_text(encoding='utf-8'))
data=[('V02-35',['02'],'Sezioni e soggetti, pubblicità dichiarativa/costitutiva/notizia, eccezione agricola, conservatore e rimedi 8/15 giorni, ComUnica e decertificazione PA.','33 articoli nel manifest normattiva-fl03; casi su art. 2193, rimedi e quiz 7–8; fonte camerale consolidata.'),('V02-36',['03'],'Mediazione e arbitrato distinti per esito; protesti: pagamento, cancellazione, riabilitazione e ricorso; metrologia: soggetti, termini ed eccezione camerale 2026; rimosso rinvio a step interno.','Casi risolti su controversia, cambiale 8/14 mesi e bilancia; quiz 7–8; D.M. 93 art. 4 vigente verificato.'),('V02-37',['04'],'Quattro organi con formazione, funzioni e durata; distinto segretario generale; CCNL 23 febbraio 2026, quattro aree, incarichi EQ e progressioni.','Tabella e caso programma/pratica; quiz 7–8; L. 580 artt. 9–20 e ARAN 2022/2026.'),('V02-38',['01','04','05'],'Esempi camerali dichiarati compositi; distinta pubblicità del Registro da accesso al fascicolo istruttorio; variante risolta del caso di laboratorio.','Letti integralmente cap. 01 e 05 correnti; cap. 04 già letto; nessun interesse qualificato imposto alla visura pubblica. Resta parte FL04/01.')] 
for fid,nums,change,evidence in data:
 state['changes'][fid]={'files':[next((base/'chapters').glob(n+'-*.md')).as_posix() for n in nums],'change':change,'evidence':evidence,'status':'applicato; audit 15 da eseguire' if fid!='V02-38' else 'parziale: M-FL03 applicato, resta M-FL04/01'}
(art/'VOL-02-changes.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
matrix=base/'planning/02-matrice-copertura-didattica.md';t=matrix.read_text(encoding='utf-8')
t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,count=1,flags=re.M)
marker='## Delta correttivo del 3 ottobre 2026'
if marker in t:t=t.split(marker)[0]
t+='''\n## Delta correttivo del 3 ottobre 2026

La dichiarazione storica di completezza non copriva i dettagli rilevati nell'audit integrale. Le righe seguenti la integrano e prevalgono sui riepiloghi precedenti per i nuclei interessati. Fonte: [[sources/vol-02-camerale-verifica-2026-10-03]], topic [[topics/vol-02-camerale-registro-servizi-organi]].

| Nucleo ID | Materia e integrazione | Teoria e conseguenze | Applicazione/output | Verifica | Stato | Review |
| --- | --- | --- | --- | --- | --- | --- |
| N-FL03-01-05 | Bando composito | Natura simulata, non prova empirica | Decoder su avviso didattico | Q:6 C:2 E:1 | completo | Riesame correttivo 2026 |
| N-FL03-02-01 | Sezioni ed effetti | Art. 2193; costitutiva 2331; eccezione agricola | Opponibilità al terzo | Q:2 C:1 E:1 | completo | 33 articoli acquisiti, fonte consolidata |
| N-FL03-02-02 | REA | Attività economica non principale e distinzione soggetti | Classificazione della richiesta | Q:1 C:1 E:1 | completo | Fonte Registro istituzionale |
| N-FL03-02-03 | Conservatore, giudice, rimedi | Artt. 2189/2192 e D.L. 76 art. 40 | Rifiuto su domanda vs cancellazione d'ufficio | Q:1 C:2 E:1 | completo | Termini diversi 8/15 |
| N-FL03-02-04 | Documenti e PA | Decertificazione artt. 40/43 | Acquisizione d'ufficio | Q:2 C:1 E:1 | completo | Nucleo DPR445 consolidato |
| N-FL03-02-05 | ComUnica | Enti, modelli, ricevuta condizionata e termini | Pratica mista SUAP | Q:2 C:2 E:1 | completo | Art. 9 vigente |
| N-FL03-03-03 | ADR e protesti | Accordo/lodo; cancellazione/riabilitazione/rimedi | Cambiale pagata 8/14 mesi | Q:4 C:3 E:1 | completo | Norme puntuali consolidate |
| N-FL03-03-04 | Metrologia | Organismi, Camera, Unioncamere, titolare; termini | Segnalazione bilancia | Q:1 C:2 E:1 | completo | Inclusa eccezione art. 4, c. 1-bis |
| N-FL03-04-01 | Organi e SG | Formazione, poteri, durata | Programma/avviso/pratica | Q:2 C:2 E:1 | completo | L. 580 vigente |
| N-FL03-04-02 | Personale | Aree, EQ, progressioni | Tre esiti distinti | Q:2 C:1 E:1 | completo | CCNL 2026 e rinvii 2022 |
| N-FL03-04-04 | Accesso | Registro pubblico/fascicolo istruttorio | Visura vs allegati contributo | Q:1 C:1 E:1 | completo | Riesame del caso |
| N-FL03-05-05 | Laboratorio | Regime dati pubblici e riservati | Variante risolta, nessun diniego generico privacy | Q:6 C:2 E:1 | completo | Scenario composito |

Le integrazioni esplicitano definizione, funzione, inquadramento, elementi, distinzioni, conseguenze, casi, uso nella prova, errore, verifica e fonti. Non viene attestato un nuovo controllo integrale delle soglie di 600 parole per ogni nucleo: la revisione correttiva opera nello step 14 e conserva il formato dichiarato. La resa impaginata richiede il nuovo PDF.
'''
matrix.write_text(t,encoding='utf-8')
index=base/'index.md';t=index.read_text(encoding='utf-8');t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,count=1,flags=re.M);index.write_text(t,encoding='utf-8')
report=Path('wiki/reviews/pipeline/VOL-02/14-moduli-m-fl03-camere-commercio.md');old=art/'VOL-02-step14-M-FL03-prima-correzioni.md'
if report.exists() and not old.exists():old.write_bytes(report.read_bytes())
lines=['# Correzioni autorizzate — M-FL03','','## 1. Sintesi editoriale','','Applicati V02-35–37, parte camerale di V02-38 e refusi pertinenti di V02-53 nei cinque capitoli. Le lacune normative sono integrate con regole, esempi e verifiche. V02-38 resta aperto nel modulo di polizia locale.','','## 2. Punti applicati della checklist','','Riesaminati contenuti, promesse, norme, esempi, quiz, coerenza terminologica e leggibilità dei passaggi modificati. Le figure restano oggetto di verifica del PDF successivo. Applicate Professional Writer, Humanizer nei passaggi e checklist del Revisore Editoriale Totale.','','## 3. Tabella errori','','| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |','| --- | --- | --- | --- | --- | --- | --- |']
for fid,nums,change,evidence in data:lines.append('| '+' | '.join([fid,'Capitoli '+', '.join(nums),'Normativa/didattica','Grave',evidence,change,'Applicato nel modulo; audit 15 successivo'])+' |')
lines+=['| V02-53 | Capitolo 05 | Lingua | Lieve | Necessità usato come verbo; segnalo anziché imperativo | Corrette necessita e segnalalo; punteggiatura quiz 6 | Applicato nel perimetro camerale |','','## 4. Osservazioni per capitolo','','01: esplicitata natura simulata del bando. 02: effetti e rimedi ora studiabili, inclusa decertificazione. 03: servizi distinti con presupposti ed esiti; metrologia aggiornata. 04: organi e personale con casi e quiz. 05: laboratorio composito e dati pubblici/fascicolo distinti.','','## 5. Coerenza globale','','Numerazione volume dei cinque file riallineata a 30–34. Il Registro pubblico non è trattato come fascicolo riservato. Lodo rituale e accordo di mediazione distinti. Le scadenze della verificazione metrologica distinguono richiesta ed esecuzione. Il nuovo CCNL non è confuso con un’ipotesi di accordo.','','## 6. Contenuto da verificare','','Eseguire audit 15 prima del freeze. Fonte: [[sources/vol-02-camerale-verifica-2026-10-03]]; manifest con 33 articoli validi letti e 16 risposte URN incongrue escluse. Capitoli non derivati dalle acquisizioni errate.','','## 7. Suggerimenti facoltativi (non errori)','','Non aggiunto un catalogo di bandi senza prove verificabili; le simulazioni sono dichiarate originali.','','## 8. Priorità degli interventi','','Gate 14, audit 15 e freeze CLI; poi produzione e verifica del nuovo PDF.','','## 9. Giudizio di pubblicabilità','','Testo corretto nel perimetro dei rilievi camerali; nessuna dichiarazione di pubblicabilità del VOL-02.','','## 10. Limiti di questa revisione','','Lettura attuale dei cinque capitoli svolta durante il riesame, con rilettura delle integrazioni e soluzioni. Non verificato il PDF successivo. Le fonti sono verificate per gli articoli elencati, non per tutti i testi unici completi. Il controllo dimensionale del formato 2 non sostituisce quello didattico e non è simulato.']
report.write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Ledger, matrice e report 14 aggiornati')
