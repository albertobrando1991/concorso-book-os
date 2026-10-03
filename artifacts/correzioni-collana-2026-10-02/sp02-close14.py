from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-sp02-vigili-fuoco');A=Path('artifacts/correzioni-collana-2026-10-02');C=Path('wiki/reviews/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-12')
e={1:'Ruoli distinti: ispettore antincendi e tecnico-scientifico; D.M. 49/2022 circoscritto.',2:'Termini, riserve, limiti di età, condotta, visus e parametri con unità e limiti della valutazione preliminare.',3:'Diario tablet del 28 settembre; valore atteso e omissione; mantenimento dello studio e comprensione.',4:'Regolazione sbarra, media dei moduli, trave 30/25/21, tempi e titoli; casi con dati coerenti.',5:'Mappa istituzionale e procedurale prevenzione incendi; progetto, SCIA, controlli e caso categoria B.',6:'Rinvii a heading letti del volume base; Decoder e controlli in parallelo.',7:'Percorsi 30/60/90, ore e consegne coerenti; 8 risposte settimanali per obiettivo mensile 30.',8:'Andrea: punteggi e margini risolti; Francesca: pressione, scaletta e rubrica; checklist distinta da idoneità.'}
stats=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');fm,body=t.split('\n---\n',1);c=int(p.name[:2]);ids=re.findall(r'^## (N-SP02-\d+-\d+) ·',body,re.M);assert len(ids)==5
 mapping={old:f'N-SP02-{c:02}-{i:02}' for i,old in enumerate(ids,1)}
 for partname in ['fm','body']:
  v=locals()[partname];v=re.sub(r'N-SP02-\d+-\d+',lambda m:mapping.get(m[0],m[0]),v)
  if partname=='fm':fm=v
  else:body=v
 if c==3:
  body=body.replace('Il capitolo *Informatica, PA digitale e competenze digitali* tratta l\'informatica come la trattano i concorsi amministrativi: amministrazione digitale, documento informatico, identità digitale, protocollo, conservazione. È l\'informatica **giuridica** della pubblica amministrazione.','Il capitolo *Informatica, PA digitale e competenze digitali* comprende sia aspetti giuridici sia competenze d’uso. Per il bando operativo seleziona file, applicazioni, rete e sicurezza di base; il capitolo 6 di questo modulo indica le destinazioni precise.').replace('Sono due programmi diversi che portano lo stesso nome.','Sono oggetti distinti all’interno dell’area digitale.').replace('un margine sopra la linea di ammissione, non massimizzare un punteggio che verrà azzerato.','una preparazione equilibrata con richiami: la soglia reale dipende anche dagli altri candidati.')
  body=body.replace('**È la formula con cui','È la formula con cui')
 if c==5:body+='\n**Riferimenti essenziali.** Bando 38 vice direttori dell’11 giugno 2025 e programma; D.M. 49/2022 per ispettore tecnico-scientifico; D.M. 166/2019, artt. 1–2; D.Lgs. 139/2006, art. 13; D.P.R. 151/2011, artt. 3–4, testi correnti controllati il 3 ottobre 2026.\n'
 if c==7:body=body.replace('Il piano è pronto quando sa reagire senza perdere il vincolo dominante: superare il filtro e presentare una prestazione fisica affidabile.','Il controllo finale associa a ogni risultato il protocollo usato, la data e il limite osservato. Questi dati consentono di modificare il piano se cambia una convocazione o una prestazione diventa instabile.')
 if c==8:body=body.replace('Il suo esito resta aperto, come deve essere un caso serio. Il metodo migliora la qualità della decisione; non garantisce il posto.','Il totale calcolato consente il confronto aritmetico; la posizione richiede invece i risultati effettivi della procedura. Andrea conserva distinti questi due esiti nella scheda.')
 sources=['sources/bandi-e-ordinamento-corpo-nazionale-vigili-del-fuoco-m-sp02']
 if c in [2,4]:sources.append('sources/parametri-fisici-concorsi-dpr-207-2015-vol-12')
 for field,val in [('source_refs',json.dumps(sources)),('last_compiled_from',json.dumps(sources)),('topics','["topics/m-sp02-vigili-fuoco-percorsi-prove"]'),('entities','["entities/ministero-interno"]'),('updated_at','2026-10-03'),('cut_off_date','2026-10-03'),('draft_stage','corrections-applied'),('review_required','true')]:
  if re.search(rf'^{field}:',fm,re.M):fm=re.sub(rf'^{field}:.*$',field+': '+val,fm,flags=re.M)
  else:fm+='\n'+field+': '+val
 t=fm+'\n---\n'+body;t='\n'.join(x.rstrip() for x in t.splitlines())+'\n';p.write_text(t,encoding='utf8')
 nuclei=[{'id':m[0],'heading':m[1],'words':len(re.findall(r'\b[\w’]+\b',m[2]))} for m in re.findall(r'^## (N-SP02-\d+-\d+) · ([^\n]+)\n(.*?)(?=^## |\Z)',body,re.M|re.S)]
 assert len(nuclei)==5 and min(n['words'] for n in nuclei)>=600,p
 assert len(re.findall('Risposta corretta: [ABCD]',body))==6,p
 stats.append({'path':p.as_posix(),'chapter':c,'words':len(re.findall(r'\b[\w’]+\b',body)),'nuclei':nuclei,'quiz':6})
(A/'M-SP02-surface-counts.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf8')
p=B/'planning/02-matrice-copertura-didattica.md';old=p.read_text(encoding='utf8');arc=C/'archive/pre-correzioni-sp02-matrice.md'
if not arc.exists():arc.write_text(old,encoding='utf8')
fm=old.split('\n---\n',1)[0];fm=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',fm,flags=re.M)
t=fm+'''\n---

# M-SP02 — Matrice di copertura didattica

Riconciliazione del testo corretto del 3 ottobre 2026: otto capitoli e quaranta nuclei con ID associati al capitolo reale. La copertura riguarda orientamento, regole selettive, requisiti, protocolli illustrati e metodo. Non dichiara un corso completo di storia, chimica, fisica o delle specializzazioni ingegneristiche: queste aree sono delimitate nel programma e nei percorsi di studio. I rinvii comuni sono circoscritti alle destinazioni effettive.

Per ciascun nucleo sono state riesaminate definizione/funzione, ambito, distinzioni, conseguenze, applicazione, output e controllo. Q:6 C:1 E:1 indica il minimo verificato nel capitolo, non sei quiz dentro ogni nucleo. Le quantità e i casi non sostituiscono il giudizio didattico.

| Nucleo ID | Materia/concetto | Fonte | Collocazione | Teoria | Applicazione/output | Verifica | Stato | Review normativa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
'''
for s in stats:
 for n in s['nuclei']:t+=f"| {n['id']} | {n['heading']} | [[sources/bandi-e-ordinamento-corpo-nazionale-vigili-del-fuoco-m-sp02]] | cap. {s['chapter']:02}, heading {n['id']} | Spiegazione nel perimetro dichiarato | {e[s['chapter']]} | Q:6 C:1 E:1 | completo | Riscontri selettivi nella fonte, 3 ottobre 2026 |\n"
t+='\n## Rinvii e limiti\n\nIl capitolo 6 collega cinque heading esistenti di VOL-01, letti nelle parti rinviate: connettivi e condizioni; file e cartelle; produttività Office; reading; nozioni costituzionali. Non equivalgono alla copertura integrale di ogni materia specialistica. Il diario VVF del 28 settembre aggiorna tablet e calendario; le comunicazioni del 7 ottobre sono future al controllo. Nuovo PDF e verifica di volume restano necessari.\n';p.write_text(t,encoding='utf8')
topic=Path('wiki/topics/m-sp02-vigili-fuoco-percorsi-prove.md');assert not topic.exists()
topic.write_text('''---
id: topic-m-sp02-vigili-fuoco-percorsi-prove
type: topic
title: Vigili del fuoco — percorsi e prove
status: consolidated
domain: concorsi pubblici
topics: ["concorsi VVF"]
entities: ["entities/ministero-interno"]
source_refs: ["sources/bandi-e-ordinamento-corpo-nazionale-vigili-del-fuoco-m-sp02", "sources/parametri-fisici-concorsi-dpr-207-2015-vol-12"]
book_refs: ["m-sp02-vigili-fuoco"]
confidence: 0.9
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: ["topic", "module-code-m-sp02"]
---

# Vigili del fuoco — percorsi e prove

Fonti: [[sources/bandi-e-ordinamento-corpo-nazionale-vigili-del-fuoco-m-sp02]]; [[sources/parametri-fisici-concorsi-dpr-207-2015-vol-12]]. Ente: [[entities/ministero-interno]]. Requisiti sanitari e prove motorie sono discipline distinte; il diario ufficiale del 28 settembre 2026 aggiorna la preselezione. I riscontri normativi sono selettivi e documentati, senza prognosi sanitarie individuali.

'''+ '\n'.join(f"- [[{Path(s['path']).with_suffix('').as_posix()[5:]}]] — {e[s['chapter']]}" for s in stats)+'\n',encoding='utf8')
for name in ['bandi-e-ordinamento-corpo-nazionale-vigili-del-fuoco-m-sp02','parametri-fisici-concorsi-dpr-207-2015-vol-12']:
 p=Path('wiki/sources')/(name+'.md');t=p.read_text(encoding='utf8');t+='\nRaccordo aggiornato: [[topics/m-sp02-vigili-fuoco-percorsi-prove]], [[entities/ministero-interno]], [[books/moduli/m-sp02-vigili-fuoco/index]]. Le rettifiche del 3 ottobre prevalgono sulle descrizioni storiche di acquisizione sopra riportate.\n';p.write_text(t,encoding='utf8')
mapping={16:(1,'Separati ispettore antincendi e tecnico-scientifico e ambito D.M. 49/2022.'),17:(2,'Visus isolato non dimostra idoneità ad altri ruoli né prognosi permanente; quiz 5 risolto.'),18:(2,'Termini di maturazione distinti dalla pubblicazione e cronologie 22–23 anni corrette.'),19:(2,'Elevazione militare e limite volontari distinti da requisiti della riserva.'),20:(2,'Residuo nominale distinto da contingente garantito; graduatoria e devoluzione.'),21:(2,'Condotta generale distinta dalla singola causa di condanna irrevocabile.'),22:(2,'Unità, operatori, art. 3 comma 2 DPR 207 e valutazione competente; costo visita eliminato.'),23:(3,'Valore atteso e omissione con formula e controesempio numerico.'),24:(3,'Diario ufficiale tablet acquisito; eliminata lettura ottica presunta e ordine rigido.'),25:(3,'Comprensione e mantenimento; simulazioni provvisorie etichettate e nessuna esclusiva dei materiali.'),26:(4,'Braccia in alto per regolare sbarra, lungo i fianchi soltanto alla partenza.'),27:(4,'Media aritmetica con tutti i moduli sufficienti e casi risolti.'),28:(4,'Trave con esiti previsti; sesso specificato; punteggi intermedi non inventati.'),29:(4,'Rapporti non usati come misura del rendimento atletico; quiz 6 senza sovrapposizioni.'),30:(4,'Cronometraggio, ordine e certificato senza automatismi non previsti.'),31:(4,'Titoli acquisiti dopo scadenza non valutabili; patente senza promessa di esito.'),32:(5,'Prevenzione incendi: funzione, fonti, progetto, SCIA, controlli e caso B.'),33:(6,'Rinvii esistenti letti e preparazione in parallelo ai controlli formali.'),34:(7,'Otto risposte per settimana e percorsi 30/60 con ore e consegne.'),35:(8,'Andrea con punteggi/margini e Francesca con consegna, soluzione e griglia.')}
report='''# M-SP02 — Correzioni editoriali del 3 ottobre 2026

## 1. Sintesi editoriale

Applicati venti rilievi specifici V12-16–35 e le quote SP02 dei rilievi trasversali V12-63–66. Otto capitoli, quaranta nuclei, 48 quiz; testo corretto, nuovo PDF e altri moduli separatamente necessari.

## 2. Punti applicati della checklist

Riesaminati per i delta: copertura e promessa, progressione, titoli/numerazione, collegamenti, autonomia, definizioni, dati, fonti, casi, calcoli, opzioni e commenti, termini, stile, ripetizioni, refusi e apparati. Controllo dell’impaginazione riservato al nuovo PDF. Il conteggio delle parole non attesta da solo completezza.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''
for n,(c,desc) in mapping.items():report+=f'| V12-{n:02} | Capitolo {c:02} | Contenuto e applicazione | Media | {desc} | Delta applicato con fonte e caso pertinenti | Corretto |\n'
report+='| V12-63–66, quota SP02 | Tutti | Superficie e verifica | Media | Rimossi residui staff individuati, commenti generici sostituiti, nuclei rinumerati e casi resi concreti | Raccordo matrice/testo | Corretto nel modulo |\n'
report+='\n## 4. Osservazioni per capitolo\n\n'+'\n\n'.join(f'{c:02}: {v}' for c,v in e.items())+'''

## 5. Coerenza globale

Numerazione ricondotta agli otto capitoli effettivi e matrice riconciliata; fonti e topic nel frontmatter. Rinvii al volume base letti per l’oggetto dichiarato. Nessuna teoria universitaria completa promessa dal solo percorso metodologico. Gli originali sono archiviati e l’audit storico resta immutato.

## 6. Contenuto da verificare

Le ulteriori comunicazioni VVF annunciate per il 7 ottobre sono future al controllo del 3 ottobre: il libro distingue il diario acquisito da contenuti non ancora noti. Nuovo PDF necessario per layout e numerazione visibile. Verifica normativa selettiva, non certificazione dell’intero ordinamento.

## 7. Suggerimenti facoltativi

Nessun ampliamento automatico a ogni specializzazione tecnica o protocollo sanitario. Conservati i limiti del modulo e le precauzioni per apnea e attività in quota.

## 8. Priorità degli interventi

Audit specialistico dei delta, manifest del testo e nuovo PDF. Proseguire gli altri tre moduli del volume prima della revisione globale.

## 9. Giudizio di pubblicabilità

Non attestata allo stato attuale: le correzioni testuali del modulo sono presenti, ma restano gli audit e i controlli di volume e del PDF rigenerato.

## 10. Limiti di questa revisione

La baseline era stata letta integralmente nell’audit storico. Questa fase riesamina gli otto capitoli e i delta, con verifiche esterne nelle parti dichiarate: bando e allegati VVF, requisiti medici, diario, tre articoli sulla prevenzione. Nessuna diagnosi personale, previsione di assunzione o progetto tecnico eseguibile. Il controllo visivo precedente non vale sul nuovo testo.
'''
p=R/'14-moduli-m-sp02-vigili-fuoco.md';arc=C/'archive/pre-correzioni-14-m-sp02.md'
if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
p.write_text(report,encoding='utf8');(A/'M-SP02-findings-map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2),encoding='utf8')
print('SP02 close14',sum(s['words'] for s in stats),'parole')
