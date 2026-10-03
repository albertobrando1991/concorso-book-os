from pathlib import Path
import re,json,hashlib
B=Path('wiki/books/moduli/m-ir04-cultura-beni-culturali');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-06');C=Path('wiki/reviews/correzioni-collana-2026-10-02')
e={1:'Decoder del profilo e prodotto della prova; quattro percorsi distinti.',2:'Quattro dipartimenti e DG; SABAP, soprintendenze archivistiche, Archivi di Stato e autonomia.',3:'Art. 10 per categorie; presupposti e tutela interinale, verifica/dichiarazione, divieti.',4:'Compatibilità della valorizzazione e distinzione fra divieto e autorizzazione.',5:'Art. 21 aggiornato alla legge 40/2026; termini 30/60/180, alienazione e soglie 50.000/13.500.',6:'Metadati descrittivi, standard, master/derivati e doppio controllo integrità/corrispondenza.',7:'Diplomatica essenziale; ISAD/ISAAR, scheda multilivello, scarto, versamento e consultabilità.',8:'REICAT/ISBD/UNIMARC/SBNMARC; authority, soggetto, classificazione/collocazione, ILL/DD.',9:'US positive/negative e sequenza 10→12→13; ritrovamento entro 24 ore e custodia.',10:'Scheda Botticelli con cronologia, tecnica e incertezza; lettura e correzione guidata.',11:'Art. 29 e caso prevenzione/manutenzione/restauro; competenze professionali.',12:'Prova amministrativa distinta da tecnica; doppia consegna e atti del cantiere.',13:'Art. 20 D.Lgs. 81: lavoratore/addetto, piano locale e caso odore di bruciato.'}
repls={"perche'":'perché',"Perche'":'Perché',"puo'":'può',"Puo'":'Può',"piu'":'più',"cosi'":'così',"Così'":'Così',"gia'":'già',"Si'":'Sì',"si'":'sì',"e'":'è',"E'":'È',"ne'":'né',"qualita'":'qualità',"attivita'":'attività',"responsabilita'":'responsabilità',"proprieta'":'proprietà',"pubblicita'":'pubblicità',"capacita'":'capacità',"identita'":'identità',"possibilita'":'possibilità',"compatibilita'":'compatibilità',"accessibilita'":'accessibilità',"disponibilita'":'disponibilità',"titolarita'":'titolarità',"finalita'":'finalità',"autorita'":'autorità',"integrita'":'integrità',"continuita'":'continuità',"modalita'":'modalità',"eta'":'età',"antichita'":'antichità',"notorieta'":'notorietà',"facolta'":'facoltà',"opportunita'":'opportunità',"priorita'":'priorità',"comunita'":'comunità',"utilita'":'utilità',"fragilita'":'fragilità',"uniformita'":'uniformità',"complessita'":'complessità',"abilita'":'abilità',"leggibilita'":'leggibilità',"proporzionalita'":'proporzionalità',"necessita'":'necessità'}
stats=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');fm,body=t.split('\n---\n',1);c=int(p.name[:2])
 for a,b in repls.items():body=re.sub(r'(?<![\w])'+re.escape(a),b,body)
 body=body.replace('## Riferimenti consolidati','## Riferimenti essenziali').replace('richiamato con prudenza come Codice dei beni culturali e del paesaggio','Codice dei beni culturali e del paesaggio')
 body=body.replace('Le autorizzazioni servono invece a controllare interventi, modifiche, spostamenti o atti che possono incidere sul bene.','Autorizzazioni, denunce preventive e comunicazioni sono strumenti distinti di controllo sugli interventi e sugli atti che incidono sul bene; per gli spostamenti vale il regime illustrato dell’articolo 21 vigente.').replace('come un restauro o uno spostamento di un bene.','come un restauro; per lo spostamento si distingue invece la denuncia preventiva prevista dal testo vigente.')
 if c==12:
  body=body.replace('### N-IR04-12-04 · Cantieri e presidio amministrativo\n','''### N-IR04-12-04 · Cantieri e presidio amministrativo

**Controllo degli atti.** Una prescrizione richiede di documentare lo stato della superficie prima dell'allestimento. Nel fascicolo il controllo confronta prescrizione, verbale iniziale, fotografie identificate e successivi riscontri. L'assenza della documentazione non si sana dichiarando che il lavoro è stato eseguito bene: occorre registrare la carenza e attivare il responsabile competente. Il controllo amministrativo non sostituisce il giudizio tecnico, ma deve renderne rintracciabili presupposti ed esiti.
''')
 refs={2:'D.P.C.M. 15 marzo 2024, n. 57; D.M. 5 settembre 2024, n. 270; organigramma MiC e competenze DGA verificati il 3 ottobre 2026.',3:'D.Lgs. 42/2004, artt. 10, 12–14, 20–21.',4:'D.Lgs. 42/2004, artt. 20–21; tutela, valorizzazione e disciplina paesaggistica.',5:'D.Lgs. 42/2004, artt. 12–14, 20–21, 54–55, 59–61, 65 e 68, testo vigente verificato il 3 ottobre 2026; legge 17 marzo 2026, n. 40.',6:'ICDP, Linee guida per la digitalizzazione del patrimonio culturale, versione giugno 2022, §§3.1, 4.1, 4.7 e 9.',7:'ISAD(G), seconda edizione, regole 2.1–2.4; ISAAR(CPF); D.Lgs. 42/2004, artt. 21, 41, 122–123.',8:'ICCU, REICAT e protocollo SBNMARC; IFLA, ISBD; BNCF, Nuovo soggettario.',9:'D.Lgs. 42/2004, artt. 90–91; Università di Bologna, Archeologia dell’architettura, sezioni su unità e rapporti stratigrafici.',10:'Gallerie degli Uffizi, scheda Nascita di Venere di Daniela Parenti, consultata il 3 ottobre 2026.',11:'D.Lgs. 42/2004, art. 29, conservazione e qualificazioni professionali.',12:'D.Lgs. 42/2004, artt. 20–21 e disciplina paesaggistica; programma specifico del profilo tecnico.',13:'D.Lgs. 81/2008, art. 20; piano di emergenza e istruzioni del singolo istituto.'}
 if c in refs:body+='\n**Riferimenti per gli approfondimenti del capitolo.** '+refs[c]+'\n'
 sources=['sources/fonti-ufficiali-m-ir04-cultura-mic-2026-07-24']
 if c==8:sources+=['sources/biblioteche-universitarie-cataloghi-sbn-risorse-open-access-2026-08-05']
 for field in ['source_refs','last_compiled_from']:
  line=field+': '+json.dumps(sources,ensure_ascii=False);fm=re.sub(rf'^{field}:.*$',lambda m:line,fm,flags=re.M)
 fm=re.sub(r'^topics:.*$', 'topics: ["topics/m-ir04-cultura-fonti-e-profili"]',fm,flags=re.M)
 fm=re.sub(r'^entities:.*$', 'entities: ["entities/ministero-cultura"]',fm,flags=re.M)
 for field,val in [('updated_at','2026-10-03'),('draft_stage','corrections-applied'),('review_required','true')]:fm=re.sub(rf'^{field}:.*$',field+': '+val,fm,flags=re.M)
 t=fm+'\n---\n'+body;t='\n'.join(l.rstrip() for l in t.splitlines())+'\n';p.write_text(t,encoding='utf8')
 nuclei=[{'id':n.split(' · ')[0],'words':len(re.findall(r'\b[\w’]+\b',s.split('\n## ')[0])),'heading':n} for n,s in re.findall(r'^### (N-[^\n]+)\n(.*?)(?=^### N-|\Z)',body,re.M|re.S)]
 assert len(nuclei)==5 and min(n['words'] for n in nuclei)>=600,p
 assert len(re.findall(r'\*\*Quiz \d+',body))==6,p
 assert not re.search(r'\[\[(sources|topics|entities|raw|planning|reviews)/',body),p
 stats.append({'path':p.as_posix(),'chapter':c,'words':len(re.findall(r'\b[\w’]+\b',body)),'nuclei':nuclei,'quiz':6})
(A/'M-IR04-surface-counts.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf8')
p=B/'planning/02-matrice-copertura-didattica.md';t=p.read_text(encoding='utf8');archive=C/'archive/IR04-matrice-pre-correzioni.md'
if not archive.exists():archive.write_text(t,encoding='utf8')
t=t.split('## Totali e blocker')[0];t=t.replace('status: planned_complete','status: text-reconciled').replace('updated_at: 2026-07-29','updated_at: 2026-10-03').replace('`Completo` attesta la progettazione con teoria, applicazione e verifica in un capitolo preciso; non equivale a capitolo redatto o pubblicabile.','Matrice riconciliata con il testo effettivo. Completo riguarda il perimetro dei nuclei indicati, non ogni specializzazione del profilo; PDF e audit di volume restano separati.').replace('mini-progetto | progetto conservativo','caso di classificazione e competenza | decisione conservativa motivata').replace('Cantieri avanzati rinviati VOL-10','Quadro amministrativo; rinvio puntuale ai livelli di progettazione sotto')
t+='''## Evidenze correnti e dimensioni didattiche

Per ciascun nucleo la collocazione è l'heading riportato nel capitolo. Definizione, funzione, distinzioni e conseguenze sono nel nucleo; caso, output, errore e verifica sono nel nucleo o negli apparati del medesimo capitolo. Le evidenze sintetiche sotto descrivono l'integrazione effettiva, senza certificare specializzazioni esterne. Q:6 C:1 E:1 indica il minimo riscontrato per capitolo, non sei quiz per ogni nucleo.

| Capitolo | Nucleo ID | Titolo/evidenza teorica | Applicazione e output | Verifica | Stato |
| --- | --- | --- | --- | --- | --- |
'''
for row in stats:
 for n in row['nuclei']:t+=f"| {row['chapter']:02} | {n['id']} | {n['heading'].split(' · ',1)[1]} | {e[row['chapter']]} | Q:6 C:1 E:1 nel capitolo | completo nel perimetro |\n"
t+='\nRinvio per i livelli di progettazione: [[books/moduli/m-tr03-tecnico-ingegneristico/chapters/07-progettazione-opere-pubbliche#N-TR03-07-03 · I livelli della progettazione]]. Non promette copertura di ogni tecnica di restauro o progettazione specialistica.\n\n13 capitoli, 65 nuclei, 78 quiz. Review normativa selettiva documentata nella fonte; dati e standard verificati nelle parti dichiarate. Nuovo PDF e controllo finale ancora necessari.\n';p.write_text(t,encoding='utf8')
p=B/'index.md';t=p.read_text(encoding='utf8').replace('M-IR04 -','M-IR04 —').replace('status: text_frozen','status: corrections-applied').replace('module_status: text_frozen','module_status: editorial_revision').replace('draft_stage: text-frozen','draft_stage: corrections-applied').replace('updated_at: 2026-07-29','updated_at: 2026-10-03').replace('Stato: text freeze completato dopo audit editoriale e specialistico.','Stato: correzioni testuali applicate; audit specialistico e nuovo PDF da completare.').replace('## Fonti da consolidare','## Fonti del modulo').replace('## Prossimo passo\nConsolidare il text freeze dopo gli audit automatici di modulo e di volume.','## Prossimo passo\nAudit specialistico sul testo corretto, text freeze e verifica del nuovo PDF.');t+='\n## Capitoli per il lettore\n\n'+'\n'.join(f"- [[{Path(x['path']).with_suffix('').as_posix()[5:]}|{x['chapter']:02} — {Path(x['path']).stem[3:].replace('-',' ')}]]" for x in stats)+'\n';p.write_text(t,encoding='utf8')
topic=Path('wiki/topics/m-ir04-cultura-fonti-e-profili.md');topic.write_text('''---
id: topic-m-ir04-cultura-fonti-e-profili
type: topic
title: Cultura e MiC — fonti e profili
status: consolidated
domain: beni culturali
topics: ["beni culturali", "archivi", "biblioteche"]
entities: ["entities/ministero-cultura"]
source_refs: ["sources/fonti-ufficiali-m-ir04-cultura-mic-2026-07-24", "sources/biblioteche-universitarie-cataloghi-sbn-risorse-open-access-2026-08-05"]
book_refs: ["m-ir04-cultura-beni-culturali"]
confidence: 0.9
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: ["topic", "module-code-m-ir04"]
---

# Cultura e MiC — fonti e profili

La fonte [[sources/fonti-ufficiali-m-ir04-cultura-mic-2026-07-24]] raccoglie la verifica selettiva del Codice corrente, assetto MiC, standard e casi. Distingue dati normativi da esempi originali e documenta le parti lette. Il quadro bibliografico è collegato a [[sources/biblioteche-universitarie-cataloghi-sbn-risorse-open-access-2026-08-05]]. Ente: [[entities/ministero-cultura]].

'''+ '\n'.join(f"- [[{Path(x['path']).with_suffix('').as_posix()[5:]}]]: {e[x['chapter']]}" for x in stats)+'\n',encoding='utf8')
entity=Path('wiki/entities/ministero-cultura.md')
assert not entity.exists(),'Entità già presente: preservare e integrare'
entity.write_text('''---
id: entity-ministero-cultura
type: entity
title: Ministero della cultura
status: consolidated
domain: beni culturali
topics: ["topics/m-ir04-cultura-fonti-e-profili"]
entities: []
source_refs: ["sources/fonti-ufficiali-m-ir04-cultura-mic-2026-07-24"]
book_refs: ["m-ir04-cultura-beni-culturali"]
confidence: 0.9
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: ["entity", "ministero"]
---

# Ministero della cultura

Ministero competente nei settori culturali secondo la disciplina di attribuzione. Assetto D.P.C.M. 57/2024 e D.M. 270/2024 verificato il 3 ottobre 2026: quattro dipartimenti, direzioni generali, uffici territoriali e istituti autonomi. Le competenze vanno individuate per funzione, bene e territorio, senza equiparare SABAP, soprintendenze archivistiche e Archivi di Stato.

Fonti e limiti: [[sources/fonti-ufficiali-m-ir04-cultura-mic-2026-07-24]]. Collegamenti: [[topics/m-ir04-cultura-fonti-e-profili]]; [[books/moduli/m-ir04-cultura-beni-culturali/index]].
''',encoding='utf8')
p=Path('wiki/sources/fonti-ufficiali-m-ir04-cultura-mic-2026-07-24.md');t=p.read_text(encoding='utf8');t+='\nDiplomatica introduttiva: ICAR, Glossario archivistico, voce scrittore, riscontro del solo estratto indicizzato il 3 ottobre 2026 (pagina completa non acquisita): https://icar.cultura.gov.it/ICARWEB/20161214144029/http%3A/www.icar.beniculturali.it/index.php?it%2F189%2Fglossario-archivistico= . Distingue autore, destinatario e scrittore. Definizioni generali di originale/copia e autenticità sono impiegate nel loro significato introduttivo, senza attribuire efficacia probatoria a specifici documenti.\n';p.write_text(t,encoding='utf8')
report='''# M-IR04 — Correzioni del 3 ottobre 2026

## 1. Sintesi editoriale

Applicati i rilievi testuali del modulo; tredici capitoli, 65 nuclei e 78 quiz disciplinari. Pubblicabilità non attestata prima del nuovo PDF.

## 2. Checklist

Copertura, autonomia, definizioni, categorie e termini normativi, competenze dei profili, dati e ipotesi, casi risolti, quiz e spiegazioni, rinvii, stile e superficie. Impaginazione separatamente da verificare.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''
rows=[('V06-25','02','Organigramma e competenze'),('V06-26','03–05','Categorie, procedimenti e termini'),('V06-27','03–04','Usi incompatibili vietati'),('V06-28','06','Catalogazione come metadati descrittivi'),('V06-29','07','ISAD, ISAAR, scarto, consultazione e diplomatica'),('V06-30','09–11','Stratigrafia, opera concreta e art. 29'),('V06-31','12','Prova tecnica distinta da amministrativa'),('V06-32','13','Obblighi lavoratore, addetti e piano locale'),('V06-11 quota IR04','06–08','Standard, catalogazione e preservazione'),('V06-33/35/36 quota IR04','Tutti','Superficie, matrice e 78 quiz disciplinari')]
for id,where,desc in rows:report+=f'| {id} | {where} | Testo e didattica | Media | {desc} | Integrazione e raccordo applicati | Corretto |\n'
report+='\n## 4. Osservazioni per capitolo\n\n'+'\n\n'.join(f'{c:02}: {v}' for c,v in e.items())+'''

## 5. Coerenza globale

Cinque nuclei per capitolo; verifica unica con sei quiz commentati, casi e richiami alla fonte leggibili. Originali archiviati; rimosse equivalenze false, promesse di esenzione dalla prova tecnica e appiattimenti sulle autorizzazioni. Rinvio ai livelli di progettazione con heading esistente.

## 6. Fonti

Letti 19 articoli del Codice e art. 20 D.Lgs. 81, organigramma e competenze DGA; ISAD nelle pagine dichiarate, ISAAR e linee guida digitalizzazione; standard bibliografici già consolidati, scheda Uffizi e sezioni universitarie sulla stratigrafia. L'art. 21 e le soglie dell'art. 65 recepiscono le modifiche del 2026. La nota documenta limiti e acquisizioni.

## 7. Suggerimenti facoltativi

Nessun ampliamento indiscriminato a ogni tecnica professionale. I casi specialistici coprono il perimetro dichiarato del modulo.

## 8. Priorità

Audit specialistico, manifest testuale e nuovo PDF, con controllo dell'ordine dei capitoli e delle bibliografie.

## 9. Pubblicabilità

Non attestata: testo corretto, ma nuova produzione PDF e verifiche di volume necessarie.

## 10. Limiti

Audit integrale della baseline già svolto; ora controllo dei delta e raccordi, non nuova lettura integrale dichiarata delle parti invariate. Normativa e standard verificati selettivamente, non certificati integralmente. Nessun record MARC eseguibile o progetto tecnico professionale completo simulato. Le definizioni introduttive di diplomatica non sono un corso specialistico completo.
'''
p=R/'14-moduli-m-ir04-cultura-beni-culturali.md';archive=C/'archive/pre-correzioni-14-m-ir04.md'
if p.exists() and not archive.exists():archive.write_bytes(p.read_bytes())
p.write_text(report,encoding='utf8');print('IR04 close14',sum(x['words'] for x in stats),'parole')
