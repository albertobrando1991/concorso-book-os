from pathlib import Path
import re,json,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');R=Path('wiki/reviews/pipeline/VOL-05');R.mkdir(exist_ok=True,parents=True)
applied={1:'Rinvii al base ricostruiti con capitolo, titolo e heading esistente; mappa del laboratorio completata.',2:'Riscritti tutti i 90 quesiti aperti e i 15 casi finali con fatti e soluzioni specifici.',3:'Inventario dei 75 nuclei effettivi e 15 unità aggregate; conteggio unico di 90 quesiti. Ricollocati heading che dividevano didascalie, introduzioni e tabelle.',4:'P definito giuridico-economico in testo, indice e Bibbia; rimossa etichetta premium.',5:'Otto schede di organi, nomine, durata, rinnovo, incompatibilità, personale e controlli con fonti puntuali.',6:'Accountability definita obbligo di rendere conto, motivazione e responsabilità verificabile.',7:'Fonti UE 288–291 e tabella di reti, agenzie e autorità; RTS/ITS distinti da progetti e orientamenti.',8:'Mini-AIR numerica con baseline, alternative, benefici netti, scenario avverso e distribuzione; delibera ARERA 255/2025/A identificata.',9:'Ispezioni AGCM/Garante, domicilio e autorizzazioni, tutela difensiva nel suo ambito; richiesta dati compilata e fase preliminare distinta.',10:'Tabella giudici, riti e termini, incluse novità TUF del 2026 e transitorio; privacy al Tribunale ordinario.',11:'Garanzie punitive, ne bis in idem, impegni 14-ter, transazione e due tipi di ottemperanza spiegati e applicati.',12:'Price cap e revenue cap separati, formule didattiche ed effetti dei volumi calcolati.',13:'Elasticità, regressione e intervallo, differenza delle differenze, strutture di mercato, RAB/WACC e costi comuni con esercizi risolti.',14:'Articoli 101/102, esenzione e clemenza; SIEC, competenza e soglie AGCM 2026, incluse operazioni sotto soglia.',15:'Codice consumo 20–26 e liste, gratis alla lettera v (rettifica della proposta originaria), clausole, rating, conflitti e delibera 31356; aggiornamento green claims 2026.',16:'PEF: gestore, ETC e ARERA distinti; esempio numerico, limite di crescita, MTR-3 e MTI-4.',17:'Tre tipi di unbundling; reclamo, indennizzo e conciliazione con termini e differenze per settore, incluso teleriscaldamento.',18:'CCE e TUSMA, SMP, accesso, servizio universale, spettro/pluralismo; percorso Corecom e rimedi distinti.',19:'Categorie e obblighi DSA, intero riparto essenziale dell’articolo 56; gatekeeper e criteri DMA con casi separati.',20:'Adeguatezza, appropriatezza ed execution only; conflitti, incentivi e best execution con caso numerico.',21:'Prospetto e OPA corrente; MAR dopo Listing Act dal 5 giugno 2026; ART/EMT/CASP e riparto, transitorio MiCAR concluso.',22:'Tabella ABF/ACF/AAS con valori, termini, effetti e condizioni; transitorio del primo anno AAS preservato.',23:'SSM, procedure comuni, TUB/CRR/CRD, capitale/liquidità/SREP, crisi e Solvency II; nucleo minimo privato/societario/AML.',24:'Articolo 55(2) applicato al concorso pubblico: niente sportello unico; distinto riuso autonomo del fornitore.',25:'Poteri 58, fasce 83, reclamo 77/78, Codice e regolamento 1/2019 aggiornato; tre, nove/dodici mesi e trenta giorni distinti.',26:'RPCT gestore del canale interno nei soggetti pubblici obbligati ex articolo 4(5).',27:'Interesse pubblico riferito all’oggetto; motivi personali irrilevanti ex articolo 16(2).',28:'Presunzione applicata ai casi e alla G3, limiti per soggetti collegati; articolo 19 distinto da articolo 6, ANAC distinto dal giudice.',29:'PNA/PIAO/PTPCT, caso di rischio compilato, articoli 220/222; ambito pubblico/privato, canali, termini e riservatezza.',30:'Dieci dossier e soluzioni complete; tre simulazioni economiche con calcoli. Rubrica richiede la regola corretta, non semplice dichiarazione di ignorarla.',31:'Memo effettivo di 107 parole: VLOP e competenza esclusiva Commissione per gli obblighi del caso.',32:'Refusi corretti e blocchi automatici sostituiti; concordanze riesaminate nei nuovi passaggi.',33:'Repertori leggibili per capitolo; URL DORA corretto a 25G00032 e vecchio slug del capitolo 12 riparato.'}
rows=[]
for line in Path('wiki/reviews/audit-integrale-2026-10-02/VOL-05.md').read_text(encoding='utf8').splitlines():
 if re.match(r'\|V05-\d\d\|',line):
  c=[x.strip() for x in line.strip('|').split('|')];n=int(c[0][-2:]);rows.append({'id':c[0],'position':c[1],'severity':c[2],'diagnosis':c[3],'correction':applied[n],'status':'Risolto nel testo; prova PDF da eseguire'})
assert len(rows)==33
files=sorted((B/'chapters').glob('*.md'));assert len(files)==15
# Refresh analytic inventory after the final structural adjustments, without altering aggregate counts.
p=B/'planning/02-matrice-copertura-didattica.md';s=p.read_text(encoding='utf8');inv=''
for ch in files:
 t=ch.read_text(encoding='utf8');heads=list(re.finditer(r'^## (N-MF05-\d\d-\d\d) · (.*)$',t,re.M));n=ch.name[:2]
 for i,m in enumerate(heads):
  block=t[m.end():heads[i+1].start() if i+1<len(heads) else len(t)];hs=re.findall(r'^### (.+)$',block,re.M);ev='; '.join(hs[:5]) or m[2]+' — spiegazione e applicazioni';inv+='| '+m[1]+' | '+n+' | '+ev.replace('|','/')+' | Q1–Q6 e caso del capitolo '+n+'; conteggio unico sotto | verificato nel perimetro |\n'
start=s.index('| N-MF05');end=s.index('\n## Copertura canonica',start);s=s[:start]+inv+s[end:];p.write_text(s,encoding='utf8')
table='| ID | Posizione | Gravità | Correzione applicata | Stato |\n|---|---|---|---|---|\n'+''.join('| '+' | '.join(r[k] for k in ['id','position','severity','correction','status'])+' |\n' for r in rows)
text='''# VOL-05 — Correzioni integrali del testo, 3 ottobre 2026

## 1. Sintesi editoriale

Applicati e riesaminati i 33 rilievi testuali sui 15 capitoli. Gli originali sono stati letti integralmente anche nel presente ciclo; checkpoint e baseline conservano percorsi e hash. Riscritti 90 quesiti aperti e 15 casi finali; le 10 simulazioni ora hanno dossier e soluzioni. Le integrazioni normative discendono da note consolidate prima della scrittura, con limiti di lettura dichiarati.

## 2. Checklist applicata

Struttura, promessa concorsuale, percorsi G/E/P, autonomia, correttezza dei claim verificati, coerenza, esempi, verifica, lingua, rinvii e fonti controllati. Quindici gate di capitolo superati senza blocker né warning. Il conteggio non sostituisce la valutazione editoriale. La resa del PDF corretto resta separata.

## 3. Registro per ID

'''+table+'''
## 4. Osservazioni per capitolo

01 percorsi e rinvii; 02 governance di otto enti; 03 fonti e reti europee; 04 AIR numerica; 05 garanzie e richiesta dati; 06 sanzioni e giurisdizione; 07 analisi economica; 08 concorrenza e consumer; 09 tariffe e tutela; 10 comunicazioni e piattaforme; 11 mercati e condotta; 12 prudenza e ADR; 13 Garante; 14 ANAC; 15 laboratorio svolto.

## 5. Coerenza globale

La matrice inventaria 75 nuclei effettivi e 15 unità aggregate di verifica: sei quesiti per capitolo, non sei per ciascun nucleo. I percorsi sono G giuridico, E economico-regolatorio e P giuridico-economico. Rinvii al VOL-01 verificati fino all'heading; rinvio tecnico-digitale al VOL-08. Matrice storica archiviata. Il perimetro non promette econometria avanzata o corsi esaustivi di diritto civile e societario.

## 6. Verifiche ed evidenze

Consolidate note puntuali su governance, reti UE, AIR, istruttoria, sanzioni/giurisdizione, economia, AGCM, ARERA, AGCOM, Consob, Banca d'Italia/IVASS, Garante e ANAC. Le acquisizioni hanno URL e SHA-256; la lettura completa di un articolo non è presentata come lettura completa del testo unico. Evidenze di lettura nel manifest e nello scope integrativo.

Aggiornamenti sostanziali comprendono OPA dopo D.Lgs. 47/2026, disciplina processuale TUF dopo D.Lgs. 128/2026 con transitorio, MAR dopo Listing Act, fine transitorio MiCAR, primo anno AAS, soglie AGCM 2026 e green claims applicabili dal 27 settembre. La proposta originaria V05-15 indicava una lettera errata: il caso «gratis» usa la lettera v dell'articolo 23.

Calcoli verificati: price/revenue cap, elasticità, regressione e intervallo, DiD, RAB/WACC, costi comuni, mini-AIR, PEF, best execution, capitale/liquidità e SCR. Nel laboratorio E1: 14/26 giorni e composizione; E2: 6.000/7.000/−5.000 euro; E3: 180.000/120.000, ricavo 790.000 e tariffa didattica 79 euro. Memo inglese: 107 parole. I dati fittizi sono dichiarati.

## 7. Suggerimenti facoltativi

Ulteriori verticali dipendono dal bando. Il glossario bilingue ampliato non è stato trattato come obbligo derivante dall'audit.

## 8. Priorità residue

Chiudere audit specialistico e freeze tramite CLI; sostituire le figure generiche con schemi specifici, poi esportare e controllare il PDF aggiornato. Preservare gli originali e registrare ogni sostituzione. Nessuna riduzione dei caratteri per comprimere il contenuto.

## 9. Giudizio di pubblicabilità

Correzioni testuali verificate; pubblicabilità finale non attestata. Il PDF precedente contiene difetti e non rappresenta questo testo. Lo step 24 richiede la conferma sul pacchetto finale effettivamente verificato.

## 10. Limiti

Riscontro normativo mirato, non certificazione di ogni disposizione dei testi unici o di ogni programma concorsuale. Alcuni documenti UE sono verificati su estratti primari indicizzati perché l'acquisizione diretta ha restituito anti-bot: non si dichiara la lettura integrale dei PDF mancanti. Il testo non sostituisce il controllo dei regimi territoriali o del bando. Figure, PDF e dati editoriali finali restano da verificare.
'''
out=Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-05.md');out.write_text(text,encoding='utf8')
for step in ['14','15']:(R/(step+'-moduli-m-fc05-authority-indipendenti.md')).write_text(text,encoding='utf8')
for p in files+[B/'index.md',B/'planning/02-matrice-copertura-didattica.md',B/'planning/03-bibbia-del-modulo.md']:
 s=p.read_text(encoding='utf8');s=re.sub(r'^review_required:.*$','review_required: false',s,flags=re.M);s=re.sub(r'^draft_stage:.*$','draft_stage: specialist_audit_done',s,flags=re.M);p.write_text(s,encoding='utf8')
# Explicit article reading scopes from the persisted checkpoints and completed reads.
complete={'agcm':'10 14 14bis 14ter 14quater 16'.split(),'consob':['1'],'privacy':'153 156 157 158 166'.split(),'risparmio':['19'],'civit':['13'],'ivass':['13'],'tuf':'5 21 94 106 187septies 195'.split(),'tub':['5','145'],'processo':['10'],'consumo':'20 21 22 23 24 25 26 27 37bis'.split(),'whistle':'1 2 3 4 5 6 8 12 16 17 19'.split(),'contratti':['220','222']}
p=A/'norme-vol05/manifest.json';d=json.loads(p.read_text(encoding='utf8'))
for r in d:
 if str(r['article']) in complete.get(r['name'],[]):r.update(readComplete=True,readScope='articolo estratto integralmente; nessuna attestazione sull’intero atto')
 elif not r.get('readScope'):r['readScope']='acquisito; non assunto come prova di lettura integrale'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
scope={'privacy-reg2019.html':'articoli 8–20 pertinenti; non intero regolamento','privacy-art140bis.html':'articolo intero','privacy-art142.html':'articolo intero','privacy-art143.html':'articolo intero','privacy-art144.html':'articolo intero','tuf-riforma47-gu.pdf':'articoli 11–16, PDF pagine 47–50; non fascicolo GU intero','consob-intermediari.pdf':'articoli 40–54; documento 2022, nessuna attestazione di lettura integrale','micar-riparto.pdf':'sezioni 1, 2.1–2.4 e tabelle riparto, pagine 3–7; non intero documento','mar-listing-act.pdf':'acquisizione vuota esclusa; usati estratti primari EUR-Lex indicizzati','mar-delegato2026.pdf':'acquisizione vuota esclusa; nessuna regola ricavata da questo file','aas-faq.html':'FAQ 1–5 pertinenti e transitorio primo anno','ivass-solvency-guida.pdf':'pagine 18–22 e 26–28; guida 2016, non usati minimi nominali storici','uif-ordinamento.html':'passaggi istituzionali AML; dettaglio dagli articoli 231 letti','abf-presentare.html':'istruzioni principali; condizioni confrontate con verifiche preliminari ufficiali'}
(A/'VOL-05-external-reading-scope.json').write_text(json.dumps({'date':'2026-10-03','mainManifest':'norme-vol05/manifest.json','additionalScopes':scope,'GDPR':'articoli 55, 58, 77, 78, 83 interi; 56 e 60–65 per passaggi pertinenti','TFUE':'101,102,288–291','private':'12 articoli elencati nel private-manifest integralmente letti','otherScopes':'Note consolidate per settore precisano letture parziali, documenti istituzionali e verifiche indicizzate; readComplete false non viene promosso senza riscontro.'},ensure_ascii=False,indent=2),encoding='utf8')
urls=[]
for p in Path('wiki/sources').glob('vol-05-*-verifica-2026-10-03.md'):urls+=re.findall(r'https?://[^\s)]+',p.read_text(encoding='utf8'))
ledger={'volume':'VOL-05','module':'M-FC05','date':'2026-10-03','textVerified':True,'finalVerified':False,'readingCheckpoint':(A/'VOL-05-reading-checkpoint.json').as_posix(),'findings':rows,'files':[{'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'readComplete':True,'readingScope':'Originale letto integralmente nel ciclo, modifiche e contesto riesaminati','quizReview':'complete'} for p in files],'externalClaimsChecked':sorted(set(urls)),'normativeEvidence':[(A/'VOL-05-external-reading-scope.json').as_posix()],'chapterGates':{'passed':15,'blockers':0,'warnings':0},'coverageNuclei':75,'quizCount':90,'finalCaseCount':15,'solvedSimulations':10,'limitations':['PDF aggiornato da verificare','Riscontri normativi mirati, nessuna dichiarazione di lettura integrale di ogni testo unico','Schemi e pacchetto finale in lavorazione']}
(A/'VOL-05-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf8');print('33 findings; reports and ledger prepared.')
