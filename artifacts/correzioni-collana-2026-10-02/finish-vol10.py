from pathlib import Path
import json,re,hashlib,shutil,datetime
A=Path('artifacts/correzioni-collana-2026-10-02'); B=Path('wiki/books/moduli/m-tr03-tecnico-ingegneristico')
source=Path('wiki/sources/vol-10-tecnico-rettifiche-2026-10-03.md')
s=source.read_text(encoding='utf8').replace('## Collegamenti\n\n','').replace('[[entities/codice-contratti-pubblici]]','[[entities/codice-dei-contratti-pubblici]]')
pos=s.index('- [[topics/tecnico-ingegneristico')
s=s[:pos]+'''## CAM edilizia, soglia UE e modifiche NTC

[D.M. 24 novembre 2025, GU 281 del 3 dicembre 2025](https://www.gazzettaufficiale.it/eli/id/2025/12/03/25A06516/sg): verificati artt. 1–4 sul PDF GU integrale già acquisito in `artifacts/correzioni-collana-2026-10-02/gu-2025-281-legge182.pdf`, pagine stampate 85–86, SHA-256 `d7372a1e2e6e06c5418fcbfc5251dbd64f0b63e82216b15fbbb9366434aeecad`. Efficacia dopo 60 giorni dalla pubblicazione: 2 febbraio 2026. Si applica ai nuovi affidamenti di servizi indicati, ai lavori basati su progetti validati in vigenza e alla progettazione interna non ancora validata. Il precedente D.M. 256/2022, modificato nel 2024, conserva applicazione nei casi dell'art. 2: PFTE per integrato o esecutivo per soli lavori validati nel precedente regime, con pubblicazione bando/avviso o invio invito entro tre mesi dalla validazione. Non letto integralmente l'allegato tecnico CAM separato; nessuna sua percentuale prestazionale introdotta.

[Commissione europea, soglie 2026–2027](https://single-market-economy.ec.europa.eu/single-market/public-procurement/legal-rules-and-implementation/thresholds_en?prefLang=fr): tabella della direttiva 2014/24/UE letta il 3 ottobre 2026, lavori 5.404.000 euro, rinvio al regolamento delegato (UE) 2025/2152. Il tentativo raw `reg-ue-2025-2152.pdf` ha prodotto un file vuoto; escluso dalle prove, non dichiarato letto. La cifra è corroborata dalla pagina ufficiale della Commissione, non dal download fallito.

[D.M. 9 marzo 2023, GU 69 del 22 marzo 2023, articolo 1](https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticoloDefault/originario?atto.codiceRedazionale=23A01847&atto.dataPubblicazioneGazzetta=2023-03-22&atto.tipoProvvedimento=DECRETO): letti transitorio di sette anni e sospensioni dei punti 11.4.2 e 11.5.2 fino al 22 marzo 2025. Non modifica i valori dei capitoli 2 e 8 utilizzati negli esempi. Riscontro puntuale, non attestazione di lettura integrale della circolare applicativa.

## Collegamenti

'''+s[pos:];source.write_text(s,encoding='utf8')
# Source consolidation precedes the editorial addition.
p=next((B/'chapters').glob('07-*.md'));s=p.read_text(encoding='utf8')
anchor='## N-TR03-07-05 · Soggetti e responsabilità'
addition='''### CAM edilizia e scelta della disciplina applicabile

I criteri ambientali minimi entrano nei requisiti del progetto e nei documenti di affidamento: non sono una certificazione generica da richiedere a fine lavori. Per gli interventi edilizi il riferimento è il **D.M. 24 novembre 2025**, efficace dal **2 febbraio 2026**, con le disposizioni transitorie dell'articolo 2. Occorre individuare oggetto dell'affidamento, data di validazione del progetto e data di bando o invito.

Per l'appalto integrato il transitorio considera il PFTE validato nel precedente regime; per i soli lavori, il progetto esecutivo. Il D.M. 256/2022, modificato nel 2024, continua ad applicarsi nei casi previsti soltanto se il bando o invito interviene entro tre mesi dalla validazione. Un incarico interno precedente non basta a mantenere il vecchio regime se la progettazione non è ancora validata all'entrata in vigore del nuovo decreto.

**Caso:** un progetto esecutivo validato il 15 gennaio 2026 secondo il precedente regime, con bando per soli lavori pubblicato il 10 marzo, rientra nel termine trimestrale; lo stesso progetto con bando del 20 maggio non vi rientra. Non basta copiare il riferimento CAM dalla relazione precedente: va verificata e aggiornata la coerenza di requisiti, specifiche e mezzi di prova. L'esempio riguarda il transitorio, non sostituisce l'applicazione dei singoli criteri pertinenti all'opera.

'''
assert anchor in s;s=s.replace(anchor,addition+anchor);p.write_text(s,encoding='utf8')
refs={
1:'Il bando e i suoi allegati definiscono requisiti, materie, prove e criteri della singola procedura. Il volume 9 approfondisce contratti e servizi; il volume 1 contiene metodo e materie comuni.',
2:'Legge 241/1990, in particolare articolo 14 sulle conferenze di servizi; D.Lgs. 165/2001 per organizzazione e responsabilità della PA; legge 20/1994 per responsabilità amministrativo-contabile, nei rispettivi testi vigenti.',
3:'Equazioni di equilibrio della statica piana e principi della meccanica dei solidi. Gli esempi numerici sono originali e didattici; per il quadro prestazionale si veda il D.M. 17 gennaio 2018, NTC, e il capitolo 4.',
4:'D.M. 17 gennaio 2018, Norme tecniche per le costruzioni, capitoli 2, 6, 7, 8 e 9; circolare 21 gennaio 2019 n. 7 C.S.LL.PP. per istruzioni applicative; D.M. 9 marzo 2023 per modifiche e transitori. Per i valori illustrati: §§ 2.4, 2.5.3 e 8.3–8.4.',
5:'D.M. 2 aprile 1968 n. 1444, articoli 2–5; D.P.R. 327/2001, articoli 9 e 39 per durata e reiterazione del vincolo; D.Lgs. 42/2004 per beni culturali e paesaggio. Applicare anche legge regionale e strumenti urbanistici pertinenti.',
6:'D.P.R. 380/2001, articoli 3, 6, 6-bis, 9-bis, 10, 20, 22–24, 27 e seguenti, 34-bis, 36 e 36-bis, nel testo vigente; legge 241/1990, articolo 19; legge 182/2025, articolo 40. I casi precisano i presupposti nazionali senza sostituire la disciplina territoriale.',
7:'D.Lgs. 36/2023, articolo 41 e Allegato I.7 per progettazione e controlli; articolo 43 e Allegato I.9 per gestione informativa; D.M. 24 novembre 2025, CAM edilizia, articoli 1–4 e allegato tecnico pertinente.',
8:'D.Lgs. 36/2023, articoli 17, 50, 114–115, 120–121 e Allegato II.14; D.Lgs. 81/2008, in particolare articoli 90, 92, 100 e allegati di sicurezza applicabili.',
9:'D.Lgs. 36/2023, articolo 116 e Allegato II.14, in particolare articolo 28; Allegato I.7, articolo 27; NTC 2018 per collaudo statico e costruzioni esistenti.',
10:'D.Lgs. 36/2023, articoli 41, 60, 108 e 125; Allegato I.7, articoli 5 e 31; Allegato II.14, articoli 7 e 12; Allegato II.2-bis per revisione prezzi. D.D. MIT 743 del 30 marzo 2026 per gli indici TOL. Prezzario vigente del territorio per i prezzi professionali.',
11:'D.Lgs. 285/1992, articolo 2; D.M. 204/2022 e Linee guida per classificazione e gestione del rischio, valutazione della sicurezza e monitoraggio dei ponti esistenti, § 1.3 per i livelli; NTC 2018 per la valutazione della singola opera.',
12:'D.Lgs. 36/2023, articolo 43 e Allegato I.9; regolamento delegato (UE) 2025/2152 e tabella ufficiale della Commissione sulle soglie 2026–2027; Agenzia delle Entrate, documentazione PREGEO, DOCFA e voltura; Codice civile, articoli 822–823 e 826–828.',
13:'Bando e criteri ufficiali della procedura per durata, strumenti ammessi e valutazione. I dati del dossier e la griglia qui forniti sono didattici; per le regole tecniche si vedano i capitoli 2–12 e per la metodologia il volume 1, capitolo 15.'}
archive=B/'planning/revisioni-2026-10-03';archive.mkdir(exist_ok=True)
for p in sorted((B/'chapters').glob('*.md')):
 n=int(p.name[:2]);s=p.read_text(encoding='utf8');pos=s.index('## Riferimenti consolidati')
 (archive/p.name).write_text('# Archivio degli apparati precedenti — '+p.name+'\n\nMateriale staff storico, sostituito nel libro il 3 ottobre 2026. Le attestazioni precedenti non certificano le correzioni correnti.\n\n'+s[pos:],encoding='utf8')
 s=s[:pos]+'## Riferimenti normativi e professionali\n\n'+refs[n]+'\n'
 fm,body=s.split('---',2)[1:]
 for field,value in [('status','revision-in-progress'),('review_required','true'),('updated_at','2026-10-03'),('draft_stage','revision-in-progress')]:fm=re.sub(r'^'+field+r':.*$',field+': '+value,fm,flags=re.M)
 for field,value in [('source_refs','sources/vol-10-tecnico-rettifiche-2026-10-03'),('topics','topics/tecnico-ingegneristico-rettifiche-2026')]:fm=re.sub(r'^'+field+r': \[(.*)\]$',lambda m:field+': ['+m[1]+', "'+value+'"]',fm,flags=re.M)
 fm=re.sub(r'^last_compiled_from:.*$','last_compiled_from: ["sources/vol-10-tecnico-rettifiche-2026-10-03", "topics/tecnico-ingegneristico-rettifiche-2026"]',fm,flags=re.M)
 body=body.replace('subtotal appalto','subtotale appalto')
 p.write_text('---'+fm+'---'+body,encoding='utf8')
p=next((B/'chapters').glob('13-*.md'));s=p.read_text(encoding='utf8');s=s.replace('**La lettura della traccia** e **Lo schema base: definizione, riferimento, funzione, esempio, conclusione**','[[books/il-metodo-bando/chapters/prova-scritta-teorico-pratica#La lettura della traccia|La lettura della traccia]] e [[books/il-metodo-bando/chapters/prova-scritta-teorico-pratica#Lo schema base: definizione, riferimento, funzione, esempio, conclusione|Lo schema base: definizione, riferimento, funzione, esempio, conclusione]]');p.write_text(s,encoding='utf8')
p=B/'index.md';s=p.read_text(encoding='utf8');s=s.replace('publication_candidate','revision-in-progress');s=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',s,flags=re.M).replace('review_required: false','review_required: true');s=re.sub(r'^- Stato:.*$','- Stato: tredici capitoli in verifica dopo le correzioni dei diciotto rilievi del 2 ottobre 2026. Nuove fonti, casi e quattro figure inseriti; il PDF aggiornato richiede verifica separata.',s,flags=re.M);s=s.replace('Il testo resta congelato salvo errori documentati.','Il precedente freeze è riaperto per le correzioni documentate.');p.write_text(s,encoding='utf8')
p=A/'VOL-10-reading-checkpoint.json';d=json.loads(p.read_text(encoding='utf8'))
for r in d:r['readComplete']=True
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
for suffix in ['gates','links']:
 s=(A/f'check-vol08-{suffix}.py').read_text(encoding='utf8').replace('VOL-08','VOL-10').replace('M-TR01','M-TR03').replace('TR01','TR03').replace('m-tr01-ict-trasformazione-digitale','m-tr03-tecnico-ingegneristico');(A/f'check-vol10-{suffix}.py').write_text(s,encoding='utf8')
print('Source, CAM, 13 reader references, staff archives, metadata and checkpoint updated.')
