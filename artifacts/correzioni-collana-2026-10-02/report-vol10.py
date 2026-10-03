from pathlib import Path
import re,json,hashlib,shutil,math,datetime
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-tr03-tecnico-ingegneristico');R=Path('wiki/reviews/pipeline/VOL-10');R.mkdir(exist_ok=True)
applied={1:'Stato editoriale eliminato; rinvio funzionale al volume 9, capitoli 3–6 e 10–12.',2:'Conferenze istruttoria, decisoria e preliminare distinte per funzione e presupposti, con esempi e verifica; regole tecniche sviluppate nei capitoli pertinenti.',3:'Vincoli piani, tre gradi di libertà, reazioni e trave L=4 m, q=10 kN/m con equilibrio, taglio, momento, segni e due figure.',4:'Vita nominale, classi I–IV, coefficienti e V_R; stati sismici e combinazioni, esercizio da 135 kN.',5:'Intervento locale, miglioramento e adeguamento: campo, condizioni, ζ_E, esempi e collaudo.',6:'Risposta distinta per nuove costruzioni e valutazione delle esistenti, con eccezione SLE della classe IV.',7:'Zone A–F, standard e articolazioni, esercizio da 7.200 m²; vincolo quinquennale, decadenza e reiterazione.',8:'Permesso come titolo, conclusione espressa o tacita; art. 20 aggiornato dalla legge 182/2025, assensi formali di tutela già acquisiti.',9:'Categorie definite; CILA, SCIA e alternativa con tempi; artt. 34-bis, 36 e 36-bis; tre casi con dati e qualificazione.',10:'Avvio ordinario distinto da anticipato e urgente ex artt. 17 e 50, con requisiti e responsabilità.',11:'Eliminato assoluto che rinviava le cautele; CSE sospende subito le lavorazioni nei presupposti dell’art. 92.',12:'Fattispecie dell’art. 120, soglie non sufficienti da sole, quinto; sospensione DL/RUP e ripresa; nomine CSP/CSE.',13:'Tempi e carattere del collaudo; soglie ed esclusioni CRE, DL/RUP; manuali e programma manutentivo con esempio.',14:'Analisi 126,50 €/m², quadro economico 150.000 euro, sicurezza/manodopera, TOL, riserve e calendario SAL/certificato/pagamento.',15:'Classi stradali A–F-bis, livelli ponti 0–5 e cinque classi di attenzione; scheda P17 senza diagnosi inventate.',16:'BIM 2 milioni e soglia beni culturali, CI/OGI/PGI e ruoli; raster/vettori e 50 m; PREGEO/DOCFA/voltura; beni pubblici.',17:'Rinvio cartaceo a due sezioni effettive del capitolo 15, R19 dichiarato digitale opzionale.',18:'Dossier S1/D1/D2/R1/F01/E1, planimetria e illustrazione, traccia di 50 minuti, modello e computo 864 euro, rubrica di 30 punti didattici.'}
rows=[]
for line in Path('wiki/reviews/audit-integrale-2026-10-02/VOL-10.md').read_text(encoding='utf8').splitlines():
 if re.match(r'\| V10-\d\d \|',line):
  c=[x.strip() for x in line.strip('|').split('|')];n=int(c[0][-2:]);rows.append({'id':c[0],'position':c[1],'category':c[2],'severity':c[3],'diagnosis':c[4],'correction':applied[n],'status':'Applicato e riesaminato nel testo; PDF da verificare'})
assert len(rows)==18
table='| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |\n| --- | --- | --- | --- | --- | --- | --- |\n'+''.join('| '+' | '.join([r['id'],r['position'],r['category'],r['severity'],r['diagnosis'],r['correction'],r['status']])+' |\n' for r in rows)
# Supersede historical blanket attestations without erasing their history.
p=B/'planning/02-matrice-copertura-didattica.md';s=p.read_text(encoding='utf8');s=s.replace('audit specialistico concluso il 21 agosto 2026; restano variabili solo bando e disciplina territoriale applicabile','Riesame del 3 ottobre 2026: evidenze e delta nella sezione finale; PDF separato');s=s.replace('# Matrice di copertura didattica M-TR03','# Matrice di copertura didattica M-TR03\n\nLe attestazioni storiche dello step 07 e i delta del 2026-08-21 sono conservati come traccia; il riesame corrente è quello del 3 ottobre 2026 in fondo alla matrice. I richiami storici a “Note di review” rinviano ora all’archivio staff `planning/revisioni-2026-10-03/`, non al libro.');s=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',s,flags=re.M).replace('review_required: false','review_required: true');s=re.sub(r'^source_refs: \[(.*)\]$',lambda m:'source_refs: ['+m[1]+', "sources/vol-10-tecnico-rettifiche-2026-10-03"]',s,flags=re.M)
s+='\n## Riesame di copertura — 3 ottobre 2026\n\nLe diciotto lacune o imprecisioni documentate nell’audit integrale sono trattate come obblighi di contenuto. La fonte corrente `vol-10-tecnico-rettifiche-2026-10-03` e il topic collegato sostengono i delta, insieme al riscontro esecutivo del volume 9. Nessuna riduzione della promessa per aggirare i rilievi.\n\n| ID | Collocazione e contenuto | Evidenza | Stato |\n| --- | --- | --- | --- |\n'
for r in rows:s+='| '+r['id']+' | '+r['position']+' | '+r['correction']+' | Verificato nel testo; PDF da controllare |\n'
s+='\nIl capitolo 7 include inoltre un caso CAM edilizia con transitorio del D.M. 24 novembre 2025. Il perimetro rimane introduttivo e concorsuale: non si promette il dimensionamento completo di un’opera né la copertura di ogni bando. Tredici capitoli legacy: `retrofit-dovuto` non bloccante fuori dagli step 08–12; gli avvisi di squilibrio dei nuclei non sono occultati e non si aggiunge testo riempitivo.\n';p.write_text(s,encoding='utf8')
# Resolve explicit base-volume destinations while preserving printed labels.
p=next((B/'chapters').glob('10-*.md'));s=p.read_text(encoding='utf8').replace('in `VOL-01`, capitolo `Contratti pubblici essenziali`, sezione `10. Documenti di gara: bando, disciplinare e capitolato`','nel volume 1, capitolo Contratti pubblici essenziali, [[books/il-metodo-bando/chapters/contratti-pubblici-essenziali#10. Documenti di gara: bando, disciplinare e capitolato|sezione 10 — Documenti di gara: bando, disciplinare e capitolato]]');p.write_text(s,encoding='utf8')
p=next((B/'chapters').glob('13-*.md'));s=p.read_text(encoding='utf8');s=s.replace('capitolo **La prova orale**, sezione *Risposte da due minuti*','capitolo La prova orale, [[books/il-metodo-bando/chapters/la-prova-orale#Risposte da due minuti|Risposte da due minuti]]')
for h in ['Versione lampo: 30 secondi','Versione standard: 2 minuti','Versione estesa: 5 minuti']:s=s.replace('*'+h+'*','[[books/il-metodo-bando/chapters/appendice-e-schema-universale-risposta-orale#'+h+'|'+h+']]')
p.write_text(s,encoding='utf8')
# Narrow corroboration of a garbled number in the Camera copy.
p=Path('wiki/sources/vol-10-tecnico-rettifiche-2026-10-03.md');s=p.read_text(encoding='utf8');s=s.replace('## Collegamenti','''## Riscontri aggiuntivi circoscritti

Art. 4 D.M. 1444/1968: il limite mancante nella copia Camera per i nuovi complessi in comuni oltre 10.000 abitanti è 1 m³/m² di densità fondiaria. Riscontro nel testo ufficiale indicizzato del [D.D.G. Sicilia 73/2022](https://www.regione.sicilia.it/sites/default/files/2022-03/ddg%2073%202022.pdf) e nell'[allegato del Comune di Monte San Pietrangeli](https://monte-san-pietrangeli-api.cloud.municipiumapp.it/system/attachments/attachment/attachment/1/1/5/6/0/linee_guida_aree.pdf). Il download del primo restituisce la pagina “non trovata”, non il decreto: raw escluso, verifica limitata agli estratti ufficiali indicizzati, concordanti. Non è una lettura integrale dei due allegati.

Letto integralmente anche II.14 art. 12: documenti contabili, firme e cronologia, SAL e certificato RUP, conto finale; sommario facoltativo, contabilità digitale con formati aperti, autenticità e provenienza. Il termine per la firma del conto è non superiore a trenta giorni; la regola dell’art. 7 è esposta insieme al termine assegnato, non come facoltà di ignorarlo.

## Collegamenti''');p.write_text(s,encoding='utf8')
p=next((B/'chapters').glob('05-*.md'));s=p.read_text(encoding='utf8').replace("il decreto contempla anche l'ipotesi dei nuovi complessi a bassa densità nei comuni maggiori",'la stessa dotazione di 12 m² si applica nei comuni maggiori ai nuovi complessi con densità fondiaria non superiore a 1 m³/m²');p.write_text(s,encoding='utf8')
p=next((B/'chapters').glob('10-*.md'));s=p.read_text(encoding='utf8').replace('Il sommario del registro ordina','Il sommario, se previsto, ordina').replace('La piattaforma digitale facilita la tracciabilità e la trasmissione dei dati.','L’Allegato II.14, art. 12, richiede programmi di contabilità digitale con formati aperti non proprietari e garanzie di autenticità, sicurezza e provenienza dei dati. Il DL esterno usa programmi previamente accettati dal RUP. La piattaforma facilita tracciabilità e trasmissione.').replace('la firma è richiesta entro **trenta giorni dall\'invito del RUP**','la firma è richiesta nel termine assegnato dal RUP, **non superiore a trenta giorni**, coordinando gli artt. 7 e 12');p.write_text(s,encoding='utf8')
calculations={'beam':{'L':4,'q':10,'RA':20,'RB':20,'points':[{'x':x,'V':20-10*x,'M':20*x-5*x*x} for x in range(5)]},'NTC':100+20+.3*50,'VR':50*1.5,'standards':{'total':400*18,'parts':[400*x for x in [4.5,2,9,2.5]],'deficit':400*18-6800},'price':(40+45+10+5)*1.15*1.1,'quantity20':20*126.5,'QE':100000+5000+2000+10000+6000+2000+25000,'payment':str(datetime.date(2026,6,10)+datetime.timedelta(days=30)),'GIS':math.hypot(30,40),'dossier':{'area':6*6,'cost':36*24,'underestimate':(36-30)*24,'haloWrongScope':2*24},'rubric':sum([4,6,8,6,6]),'relationWords':len(re.search(r'\*\*Relazione\.\*\* «(.+?)»',next((B/'chapters').glob('13-*.md')).read_text(encoding='utf8'))[1].split())}
assert math.isclose(calculations['price'],126.5) and calculations['relationWords']<=250 and calculations['rubric']==30
(A/'VOL-10-calculations.json').write_text(json.dumps(calculations,ensure_ascii=False,indent=2),encoding='utf8')
text='''# VOL-10 — Correzioni del testo, 3 ottobre 2026

## 1. Sintesi editoriale

Applicati e riesaminati tutti i diciotto rilievi testuali dell’audit integrale. Letti tutti i tredici originali e la matrice; ricontrollati i passaggi aggiunti, casi, formule, risposte e riferimenti. Quattro figure didattiche sono inserite e visionate come asset; questo controllo non sostituisce il PDF impaginato.

## 2. Punti applicati della checklist

Controllati promessa, progressione, autonomia, accuratezza, casi e verifiche, terminologia, rinvii, apparati e tracciabilità. Applicati i punti testuali 1–26 e 28–30. Il punto 27 resta alla verifica del candidato PDF corrente; le precedenti tavole non rappresentano queste integrazioni. Prosa riesaminata per eliminare formule generiche dove occorreva insegnare la regola, conservando le cautele specifiche del caso reale.

## 3. Registro per ID

'''+table+'''
## 4. Osservazioni per capitolo

01 rinvio di famiglia; 02 conferenze; 03 statica risolta; 04 NTC e categorie di intervento; 05 standard e vincolo; 06 categorie e regimi edilizi; 07 CAM e transitorio; 08 esecuzione e sicurezza; 09 collaudo e manutenzione; 10 analisi e contabilità; 11 classificazioni e ponti; 12 gestione informativa, catasto e patrimonio; 13 dossier autonomo. I documenti staff rimossi dal corpo sono archiviati, non distrutti.

## 5. Coerenza globale e copertura

Indice e matrice riallineati ai contenuti e allo stato corrente, senza conservare l’attestazione anticipata di impaginazione completata. I delta storici restano identificati come precedenti. La famiglia conserva il proprio confine: il diritto comune e i metodi di prova hanno destinazioni precise nel volume base; la simulazione è utilizzabile con i soli documenti cartacei forniti.

## 6. Contenuto verificato e prove

Fonte `vol-10-tecnico-rettifiche-2026-10-03` e topic collegato; riuso del riscontro sui contratti `vol-09-esecuzione-verifica-2026-10-03`. URL, raw validi e limiti sono espliciti. Normattiva: articoli edilizi, conferenze, sicurezza, Codice e allegati, strade e beni pubblici pertinenti. GU: NTC §§ 2.4, 2.5.3 e 8.3–8.4, modifiche 2023, legge 182/2025 e CAM 2025. Linee guida ponti: § 1.3, non tutti i 92 fogli. Verificati conti di statica, 135 kN, 7.200 m², 126,50 €/m², quadro da 150.000 euro, calendario, 50 m e computo da 864 euro; artifact `VOL-10-calculations.json`.

Tredici gate di capitolo superati senza blocker, con avviso legacy `retrofit-dovuto` su tutti e `squilibrio-nuclei` su undici. Gli avvisi sono dichiarati: la revisione degli step 14–16 non riapre il ciclo 08–12 e non attribuisce retroattivamente Format 2. Non si comprimono né si allungano artificialmente i nuclei per soddisfare una soglia diversa. Zero rinvii wikilink irrisolti nel corpo. Nuove figure coerenti con calcoli, quote, segni e natura illustrativa; dimensioni finali da controllare nel PDF.

## 7. Suggerimenti facoltativi

Nessun suggerimento facoltativo usato per eludere le lacune. Ulteriori esercizi o approfondimenti dipendono dai bandi; il testo non promette un corso universitario completo o una progettazione esecutiva professionale.

## 8. Priorità residue

Concludere audit 15 e freeze 16 tramite CLI; poi figure/impaginato corrente, revisione visuale e preflight. Controllare tabelle con formule, apici e simboli, planimetria, diagrammi e campi compilabili, senza ridurre la tipografia.

## 9. Giudizio di pubblicabilità

Le diciotto correzioni sono applicate e verificate nel testo. La pubblicabilità finale resta non dichiarata finché non si controllano il PDF rigenerato e i gate di produzione. L’esito non è una certificazione professionale delle opere descritte negli esempi.

## 10. Limiti della revisione

Riscontri puntuali datati 3 ottobre 2026, non lettura integrale di ogni raccolta normativa o di tutti gli allegati CAM. Il PDF EUR-Lex scaricato vuoto, le risposte Normattiva errate e il download Sicilia “pagina non trovata” sono esclusi dalle prove. La soglia UE è confermata dalla pagina Commissione; il limite di densità urbanistica è corroborato da estratti ufficiali indicizzati, con limite dichiarato nella fonte. Nessun revisore umano fittizio o approvazione finale simulata. PDF precedente, indice storico e hash non certificano il nuovo impaginato.
'''
for target in [R/'14-moduli-m-tr03-tecnico-ingegneristico.md',Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-10.md')]:
 if target.exists() and not (A/'before-text/VOL-10'/target.name).exists():shutil.copy2(target,A/'before-text/VOL-10'/target.name)
 target.write_text(text,encoding='utf8')
(A/'VOL-10-applied.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print('18 ID recorded, matrix updated, calculations passed; relation words',calculations['relationWords'])
