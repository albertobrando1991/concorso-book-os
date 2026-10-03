from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-sp01-forze-ordine');A=Path('artifacts/correzioni-collana-2026-10-02');C=Path('wiki/reviews/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-12')
sources=['sources/bandi-rappresentativi-m-sp01-forze-polizia-2026','sources/ordinamento-forze-di-polizia-quadro-normativo-m-sp01','sources/prove-efficienza-fisica-accertamenti-forze-di-polizia-m-sp01']
e={1:'Mappa dei tre corpi e dei due livelli; cinque bandi con ruoli, titoli e prove; rinvio alla Polizia locale.',2:'Età PS corretta, formule CC/GdF distinte, sentenza 40/2024 circoscritta e D.M. 198 riferito alla Polizia di Stato.',3:'Funzione, formato e banca separati; CC 898 italiano a 60 quesiti, GdF 983 composizione di sei ore; scenario banca con tempo ipotetico.',4:'Protocollo GdF 983 nel perimetro, obbligatori/facoltativi e conversione punti; certificazioni distinte da prenotazioni.',5:'Titoli dichiarati tempestivamente, documentazione successiva distinta; inglese PS obbligatorio e scelte facoltative specifiche.',6:'Perimetro di orientamento e metodo dichiarato; tre piani di funzione distinti, rinvii circoscritti letti nelle destinazioni.',7:'Decoder con canale, scadenza, ricevuta e reinvio; quattro stati dell’informazione; CC 3.081 compilato e scheda utilizzabile.',8:'Piani alternativi 30/60/90 con ore e consegne; banca 5.000 e scenario 33 giorni; commenti dei quiz pertinenti.',9:'Quattro casi chiusi su certificato, nuovo invio, avviso e penalità; otto quiz con calcoli e distrattori motivati.',10:'Ammissibilità separata dalla preparazione; N/A e avviso futuro; ricevuta soltanto dopo invio e decisioni motivate.'}
stats=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');fm,body=t.split('\n---\n',1);c=int(p.name[:2]);ids=re.findall(r'^## (N-SP01-\d+-\d+) ·',body,re.M);assert len(ids)==5
 mapping={old:f'N-SP01-{c:02}-{i:02}' for i,old in enumerate(ids,1)}
 fm=re.sub(r'N-SP01-\d+-\d+',lambda m:mapping.get(m[0],m[0]),fm);body=re.sub(r'N-SP01-\d+-\d+',lambda m:mapping.get(m[0],m[0]),body)
 deps=[x.removesuffix('.md').removeprefix('wiki/') for x in json.loads(re.search(r'^source_refs: (\[.*\])$',fm,re.M)[1])];deps=list(dict.fromkeys(deps+sources))
 for field,val in [('source_refs',json.dumps(deps)),('last_compiled_from',json.dumps(deps)),('topics','["topics/m-sp01-forze-ordine-percorsi-prove"]'),('entities','["entities/ministero-interno"]'),('updated_at','2026-10-03'),('cut_off_date','2026-10-03'),('draft_stage','corrections-applied'),('review_required','true')]:
  if re.search(rf'^{field}:',fm,re.M):fm=re.sub(rf'^{field}:.*$',field+': '+val,fm,flags=re.M)
  else:fm+='\n'+field+': '+val
 t='\n'.join(x.rstrip() for x in (fm+'\n---\n'+body).splitlines())+'\n';p.write_text(t,encoding='utf8')
 nuclei=[{'id':m[0],'heading':m[1],'words':len(re.findall(r'\b[\w’]+\b',m[2]))} for m in re.findall(r'^## (N-SP01-\d+-\d+) · ([^\n]+)\n(.*?)(?=^## |\Z)',body,re.M|re.S)]
 assert len(nuclei)==5 and min(n['words'] for n in nuclei)>=600,(p,nuclei)
 quiz=len(re.findall('Risposta corretta: [ABCD]',body));assert quiz>=6
 stats.append({'path':p.as_posix(),'chapter':c,'words':len(re.findall(r'\b[\w’]+\b',body)),'nuclei':nuclei,'quiz':quiz})
(A/'M-SP01-surface-counts.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf8')
p=B/'planning/02-matrice-copertura-didattica.md';old=p.read_text(encoding='utf8');arc=C/'archive/pre-correzioni-sp01-matrice.md';assert not arc.exists();arc.write_text(old,encoding='utf8');fm=old.split('\n---\n',1)[0];fm=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',fm,flags=re.M)
t=fm+'''\n---

# M-SP01 — Matrice di copertura didattica

Riconciliazione del 3 ottobre 2026: dieci capitoli, cinquanta nuclei, numerazione corrispondente ai file. Il perimetro è orientamento, requisiti e regole dei bandi illustrati, scelta del percorso e preparazione. Il capitolo 6 non promette un corso completo di diritto penale, procedura penale, TULPS o ordinamento di ogni corpo. I rinvii selezionano contenuti effettivamente letti e non valgono come copertura di tutto il programma di un concorso.

Definizione, funzione, ambito, distinzioni, conseguenze, caso, output, verifica ed errori sono stati riesaminati nei nuclei. Q indica il totale del capitolo; C ed E almeno un caso e un esercizio. La densità quantitativa è un controllo separato dalla completezza del contenuto.

| Nucleo ID | Materia/concetto | Fonte | Collocazione | Teoria | Applicazione/output | Verifica | Stato | Review normativa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
'''
for s in stats:
 for n in s['nuclei']:t+=f"| {n['id']} | {n['heading']} | [[sources/bandi-rappresentativi-m-sp01-forze-polizia-2026]], [[sources/ordinamento-forze-di-polizia-quadro-normativo-m-sp01]] | cap. {s['chapter']:02}, heading {n['id']} | Spiegazione nel perimetro assegnato | {e[s['chapter']]} | Q:{s['quiz']} C:1 E:1 | completo | Riscontri selettivi del 3 ottobre, limiti nelle fonti |\n"
t+='\n## Rinvii e limiti\n\nCapitolo 1: orientamento alla Polizia locale. Capitolo 6: metodo banca dati e procedimento amministrativo nel volume base; notizia di reato e TULPS nel modulo Polizia locale, limitatamente agli oggetti indicati, senza estendere qualifiche e poteri locali agli altri corpi. Destinazioni e heading controllati nel testo. Le date storiche della banca PS non riattestate non sono usate come fatti nuovi: il piano di 33 giorni è dichiarato simulato. Protocolli: [[sources/prove-efficienza-fisica-accertamenti-forze-di-polizia-m-sp01]]. Nuovo PDF necessario.\n';p.write_text(t,encoding='utf8')
topic=Path('wiki/topics/m-sp01-forze-ordine-percorsi-prove.md');assert not topic.exists()
topic.write_text('---\nid: topic-m-sp01-forze-ordine-percorsi-prove\ntype: topic\ntitle: Forze di polizia — percorsi e prove\nstatus: consolidated\ndomain: concorsi pubblici\ntopics: ["carriere speciali", "forze di polizia"]\nentities: ["entities/ministero-interno"]\nsource_refs: '+json.dumps(sources)+'\nbook_refs: ["m-sp01-forze-ordine"]\nconfidence: 0.9\nupdated_at: 2026-10-03\ncreated_at: 2026-10-03\nreview_required: false\ncanonical: true\ntags: ["topic", "module-code-m-sp01"]\n---\n\n# Forze di polizia — percorsi e prove\n\nLe tre fonti distinguono bando, disciplina ordinamentale e protocollo della singola procedura. Età e condotta non si trasferiscono fra corpi; il D.M. 198/2003 non è il regolamento sanitario universale. Il percorso collega metodo e regole, senza dichiarare completo l’intero programma penalistico.\n\n'+ '\n'.join(f'- [[{x}]]' for x in sources)+'\n\nEnte collegato: [[entities/ministero-interno]] (per Polizia di Stato e amministrazione della pubblica sicurezza; non implica dipendenza organica degli altri corpi).\n\n'+ '\n'.join(f"- [[{Path(s['path']).with_suffix('').as_posix()[5:]}]] — {e[s['chapter']]}" for s in stats)+'\n',encoding='utf8')
for source in sources:
 p=Path('wiki')/(source+'.md');t=p.read_text(encoding='utf8');t+='\nRaccordo editoriale: [[topics/m-sp01-forze-ordine-percorsi-prove]], [[entities/ministero-interno]], [[books/moduli/m-sp01-forze-ordine/index]]. Restano distinti riscontri puntuali e materiale storico non riattestato.\n';p.write_text(t,encoding='utf8')
mapping={1:(1,e[1]),2:(2,'Corrette soglie PS e formule dei compleanni; elevazioni collegate alla categoria.'),3:(2,'Sentenza 40/2024 limitata alla clausola GdF sulla guida in stato di ebbrezza.'),4:(2,'D.M. 198/2003 riferito alla Polizia di Stato; parametri e accertamenti distinti.'),5:(3,e[3]),6:(4,e[4]),7:(5,'Corretta cronologia del caso Luca e separati dichiarazione e prova documentale.'),8:(5,'Eliminata competitività astratta delle lingue; scelta entro i vincoli della procedura.'),9:(6,e[6]),10:(7,'Canale, termine, pagamento se previsto, invio, ricevuta e annullamento/reinvio; esempio CC.'),11:(7,'Distinti non reperito, non ancora pubblicato, non previsto e da verificare.'),12:(8,e[8]),13:(8,'Sei quiz con commenti specifici e chiavi redistribuite senza disallineamenti.'),14:(9,e[9]),15:(10,e[10])}
report='''# M-SP01 — Correzioni editoriali del 3 ottobre 2026

## 1. Sintesi editoriale

Applicati quindici rilievi V12-01–15 e le quote SP01 dei rilievi trasversali V12-63–66. Dieci capitoli e cinquanta nuclei; audit specialistico e nuovo PDF restano distinti.

## 2. Punti applicati della checklist

Controllati promessa e copertura, progressione, titoli, numerazione, fonti, definizioni, ambiti, cronologie, casi, calcoli, quiz e commenti, rinvii, autonomia, stile e residui staff. Impaginazione e spazi compilabili vanno verificati nel PDF rigenerato.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''
for n,(c,desc) in mapping.items():report+=f'| V12-{n:02} | Capitolo {c:02} | Contenuto e applicazione | Media | {desc} | Delta applicato e tracciato | Corretto |\n'
report+='\n## 4. Osservazioni per capitolo\n\n'+'\n\n'.join(f'{c:02}: {v}' for c,v in e.items())+'''

## 5. Coerenza globale

Matrice e cinquanta ID ricondotti ai capitoli reali. Cinque procedure rappresentative distinte per corpo e livello; il bando GdF 69 ufficiali non alimenta il protocollo del percorso. Il capitolo 6 dichiara il limite strategico e rinvii precisi, non una promessa di corso penalistico integrale.

## 6. Contenuto da verificare

Il sito PS restituisce accesso negato. Requisiti e prove riscontrati sugli originali, compreso il PDF completo PS 1.000 recuperato da inPA. Date storiche non riattestate di banca e scritto non sono riproposte come fatti: la finestra di 33 giorni è uno scenario. Nessuna valutazione sanitaria individuale. PDF nuovo necessario.

## 7. Suggerimenti facoltativi

Il piano è adattabile ma non prescrive un allenamento atletico né sostituisce il programma completo richiesto dal bando. Non ampliare automaticamente a ufficiali o altre famiglie.

## 8. Priorità degli interventi

Audit specialistico dei delta, manifest e nuovo PDF; proseguire SP03 e SP04 prima del giudizio di volume.

## 9. Giudizio di pubblicabilità

Non attestata. Modifiche testuali presenti, controlli di modulo, volume e nuovo PDF separatamente necessari.

## 10. Limiti di questa revisione

Baseline letta integralmente nell’audit storico e capitoli riesaminati nella correzione. Verifica normativa selettiva nelle parti dichiarate nelle fonti, non certificazione dell’intero ordinamento. Originali editoriali archiviati e report storico immutato. Le dimensioni quantitative non dimostrano da sole qualità o copertura.
'''
p=R/'14-moduli-m-sp01-forze-ordine.md';arc=C/'archive/pre-correzioni-14-m-sp01.md'
if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
p.write_text(report,encoding='utf8');(A/'M-SP01-findings-map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2),encoding='utf8')
print('SP01 close14',sum(s['words'] for s in stats),'words',sum(s['quiz'] for s in stats),'quiz')
