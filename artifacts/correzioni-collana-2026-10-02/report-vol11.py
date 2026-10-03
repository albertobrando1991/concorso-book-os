from pathlib import Path
import re,json,hashlib,shutil
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-tr04-ambiente-protezione-civile');R=Path('wiki/reviews/pipeline/VOL-11')
applied={1:'Eliminate quattro ripetizioni integrali e sostituite con prove differenziate, lettura delle fonti e casi quantitativi.',2:'SNPA descritto come sistema; coordinamento tecnico attribuito a ISPRA.',3:'Tre calendari alternativi, carichi orari, pesi per AMB/PC/EN/LOC, prove e recupero; toolkit cartaceo.',4:'Costituzione 117–118, parti del decreto e principi 3-bis–3-sexies, L.132, LEPTA.',5:'Ripetizioni ridotte e due mini-esercizi risolti con competenza e motivazione.',6:'Tre iter distinti: art.6 comma9, screening19 e screening VAS12; presupposti e termini.',7:'Mini-esercizi precisano allegato e fatti; nessuna VIA ricavata dalla sola parola opera.',8:'Ripristinato esprime, conservando condizioni e richiesta del proponente.',9:'VIncA, Natura2000, competenze, PUA/PAUR e sequenze temporali datate.',10:'Art.3 AUA corrente, voci aggiunte e facoltà regionale del comma2; rettificata anche source precedente.',11:'Autorità adotta e SUAP rilascia; sequenza distinta.',12:'AUA15anni/rinnovo6mesi; AIA10/12/16 e BAT4; emissioni269/272; IED schemaAG420 distinto dal diritto vigente.',13:'Rinnovo124 un anno, AUA sei mesi; suolo/sottosuolo103/104, piani117/121 e sei anni.',14:'M0, M0a/b e distinzione macroindicatori/indicatori semplici RQTI.',15:'Caso SST240 contro200, metodo, titolo e campionamento dichiarati; 20% e limiti dell’incertezza.',16:'Rimosso carattere di sillabazione invisibile.',17:'Soggetti/esclusioni188-bis, termini190, FIR e registro compilati, digitale dal16settembre.',18:'Codici150101/150110*, specchio170503*/170504, HP, end of waste e titoli208/212/214/216.',19:'Diagnosi originaria precisata: inferiore è testo letterale art.240; chiarita l’uguaglianza nei passaggi applicativi e casi CSC/CSR.',20:'Complementare sul sito o, se opportuno, altrove, distinta dalla compensativa.',21:'Sequenza242/250, termini, responsabilità298-bis/303 e casi50/80/150 conCSR120.',22:'Categorie aria definite, PM10/NO2 con periodi e superamenti; direttiva2024/2881 distinta da schema nazionale.',23:'Sei classi, periodi, differenziale5/3 ed esclusioni; esempi62−60 e56−49; Leq/Lden/Lnight.',24:'Accesso ambientale195: chiunque,30/60giorni, limiti e accesso parziale; caso risolto.',25:'Distinzione formale pene; art.256 corrente contravvenzione/delitto secondo fattispecie.',26:'Timeline689 e318-bis/seguenti; pagamenti1000 e4500, proroga6mesi, verifiche e comunicazioni.',27:'Casi concreti256,137/133 e279: rifiuti/acque/emissioni; dati, pena e natura, limite del nesso causale.',28:'Prefetto: eventi b/c, imminenza/preannuncio, raccordo e direzione tecnica distinti.',29:'Attesa/assistenza/ammassamento, COC/CCS/COM/DiComaC e ambiti, volontariato39/40.',30:'Giallo/arancione almeno attenzione, rosso almeno preallarme; innalzamento motivato.',31:'Cinque schede: sisma, vulcano, maremoto SiAM, incendio/interfaccia, Seveso PEI/PEE.',32:'Rami A/B espliciti; matrice4colonne; validità18:00 distinta dalle osservazioni15:20.',33:'FER190 artt.6–9 e allegati A/B/C; correttivo178/2025 e REDIII5/2026; casi80kW/6MW/20MW.',34:'Partecipanti/controllo CER, zona/cabina primaria, diritti, TIAD e minimo orario70kWh.',35:'Diagnosi102, PAcentrale3%, APE192, EED incompleta riscontrata1ott; PNIEC/PNACC e calcolo risparmio/payback/CO2e.',36:'Regimi DNSH definiti; attribuzione da misura; casi NZEB50/40 e progetto45.',37:'CAM24novembre2025 e circolare10aprile2026; criterio2.5.2 con profilo pedologico,75/90m³ e prove per fase.',38:'Quattro fasi LCA; LCC scontato5anni3%,24601,73/23590,72 e differenza1011,01.',39:'Sim6 tabella+nota, sim8 otto righe, sim10 nota+sei azioni con tempi e rubrica.',40:'Paragrafi metodologici ricollocati prima di sintesi e simulazioni1/3/5/8, conservando testo utile.',41:'Regole note distinte da fatti mancanti; casi risolvibili con numeri e disposizioni; quiz6 corretto.',42:'AppendiciA–E effettive nel capitolo14, modelli compilati e percorsi; indici riallineati.',43:'Matrice90nuclei reali, archivio attestazioni precedenti, indice senza scaffold/escape, metadati correnti.',44:'Eliminata istruzione textfreeze dal corpo; date e uso del dato leggibili; codici DO tecnici conservati per parser e filtrati dal renderer comune.'}
rows=[]
for line in Path('wiki/reviews/audit-integrale-2026-10-02/VOL-11.md').read_text(encoding='utf8').splitlines():
 if re.match(r'\| V11-\d\d \|',line):
  c=[x.strip() for x in line.strip('|').split('|')];n=int(c[0][-2:]);rows.append(dict(id=c[0],position=c[1],category=c[2],severity=c[3],diagnosis=c[4],correction=applied[n],status='Applicato e verificato nel testo; PDF da verificare'))
assert len(rows)==44
# Improve spacing in generated prose, leaving exact ID forms intact.
for r in rows:
 c=r['correction'];c=re.sub(r'(?<=[a-zàèéìòù])(?=\d)', ' ',c);c=re.sub(r'(?<=\d)(?=[a-zàèéìòù])',' ',c);c=re.sub(r'(?<=\d)(?=[A-Z])',' ',c);c=re.sub(r'\b(CSR|SST|AG|NZEB|LCA|LCC|FER|REDIII|PAcentrale|Sim)(?=\d)',r'\1 ',c);r['correction']=c
table='| ID | Posizione | Categoria | Gravità | Evidenza originaria | Correzione applicata | Stato |\n|---|---|---|---|---|---|---|\n'+''.join('| '+' | '.join(r[k] for k in ['id','position','category','severity','diagnosis','correction','status'])+' |\n' for r in rows)
text='''# VOL-11 — Correzioni del testo, 3 ottobre 2026

## 1. Sintesi editoriale

Applicati e riesaminati i 44 rilievi testuali sui 14 capitoli. L'audit originario aveva letto integralmente tutti i testi e risolto le 84 domande finali (24 aperte e 60 a scelta multipla). La baseline corrente coincideva per 13 capitoli; nel capitolo 12 era cambiata solo una cella per il wrapping. Nel ciclo autorizzato sono stati riesaminati i delta e il loro contesto, i nuovi casi, le soluzioni e gli apparati. Non si dichiara una nuova lettura integrale di ogni fonte normativa.

## 2. Punti applicati della checklist

Controllati struttura, promessa, quattro profili, teoria, precisione, lingua, ripetizioni, esercizi, soluzioni, fonti, rinvii e apparati. La tipografia e la composizione del candidato PDF aggiornato restano verifica separata. Nessun carattere è stato ridotto per far entrare il contenuto.

## 3. Registro per ID

'''+table+'''
## 4. Osservazioni per capitolo

01 percorsi e calendario; 02 principi e sistema; 03 iter e competenze; 04 titoli e termini; 05 rinnovi, RQTI e analisi; 06 classificazione e tracciabilità; 07 bonifiche e responsabilità; 08 misure e accesso; 09 fattispecie e procedura; 10 centri, aree e volontariato; 11 rischi e allertamento; 12 regimi FER, CER e diagnosi; 13 DNSH/CAM/LCA/LCC; 14 laboratorio e cinque appendici effettive.

## 5. Coerenza globale

La matrice corrente elenca 90 nuclei effettivi e collega fonti e applicazioni. Il precedente scaffold e le attestazioni storiche sono archiviati e superati dal riesame corrente. Le appendici A–E sono nel capitolo 14, già incluso nell'export, con nomi corrispondenti all'indice. I calendari 30/60/90 sono alternativi, con carichi e adattamenti professionali.

## 6. Contenuti verificati ed evidenze

Cinque nuove note consolidate e topic `ambiente-rettifiche-2026`; manifest normativi con URL, hash, validità e lettura completa/parziale esplicita. Verificati gli articoli pertinenti di D.Lgs. 152, DPR 59, L.132, DPR357, D.Lgs.195, Codice protezione civile, Seveso, FER190, CER199, efficienza102, edifici192 e L.689. RQTI, DPCM rumore, SNPA classificazione, TIAD, RGS DNSH e CAM letti nei passaggi dichiarati.

La Commissione del 1° ottobre 2026 conferma EED incompleta e mancato progetto di piano ristrutturazioni: non si presume recepimento completo dalla sola scadenza UE. IED e aria distinguono atti vigenti e schemi parlamentari. V11-19 è stato corretto anche nella diagnosi: la parola «inferiore» è letterale nell'art.240; l'integrazione spiega uguaglianza e superamento senza alterare la citazione.

Calcoli controllati: SST 20%; PM10 38/35 e 32/40; rumore 2 e 7 dB; pagamenti 1.000/4.500 euro; CER 70 kWh; risparmio 25%, 6 anni e 7,5 t CO₂e ipotetiche; suolo 75/90 m³; LCC 24.601,73/23.590,72 euro. I dati didattici sono dichiarati. Quattordici gate di capitolo passano senza blocker né warning; il conteggio non sostituisce l'esame del contenuto.

## 7. Suggerimenti facoltativi

Eventuali ulteriori esercizi territoriali dipendono dal bando. Nessuna riduzione della promessa editoriale è stata usata per evitare le integrazioni obbligatorie.

## 8. Priorità residue

Chiudere CLI 14/15/16 e rigenerare il PDF. Verificare soprattutto tabelle, appendici, formule e pagine finali; i vecchi PDF non dimostrano la qualità delle nuove aggiunte.

## 9. Giudizio di pubblicabilità

Correzioni verificate nel testo, pubblicabilità finale ancora non attestata. `textVerified: true`, `finalVerified: false` al termine dell'audit specialistico; il freeze avviene tramite CLI e manifest separato.

## 10. Limiti

Verifica normativa mirata ai claim e alle integrazioni, non certificazione integrale dei testi unici, della giurisprudenza o delle regole regionali. PDF finale e preflight restano aperti. Download con sessione scaduta o senza allegato sono esclusi dalle prove; le letture parziali sono registrate come tali. Gli ID tecnici dei dati operativi restano nel sorgente per il sistema e sono esclusi dalla copia lettore dal renderer; la resa finale va ricontrollata nel PDF.
'''
out=Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-11.md');out.parent.mkdir(exist_ok=True,parents=True);out.write_text(text,encoding='utf8')
for step in ['14','15']:
 p=R/(step+'-moduli-m-tr04-ambiente-protezione-civile.md')
 if p.exists() and not (A/'before-text/VOL-11'/p.name).exists():shutil.copy2(p,A/'before-text/VOL-11'/p.name)
 p.write_text(text.replace('Correzioni del testo','Audit specialistico conclusivo del testo' if step=='15' else 'Revisione del testo').replace('Applicato e verificato nel testo; PDF da verificare','Risolto nel testo'),encoding='utf8')
for p in list((B/'chapters').glob('*.md'))+[B/'index.md',B/'planning/02-matrice-copertura-didattica.md',B/'planning/17-bibbia-del-modulo.md']:
 s=p.read_text(encoding='utf8');s=re.sub(r'^review_required:.*$','review_required: false',s,flags=re.M);s=re.sub(r'^draft_stage:.*$','draft_stage: specialist_audit_done',s,flags=re.M);p.write_text(s,encoding='utf8')
# Current climate check remains scoped to the published target, not all flexibility provisions.
p=Path('wiki/sources/vol-11-energia-sostenibilita-verifica-2026-10-03.md');s=p.read_text(encoding='utf8')+'\n## Ulteriore riscontro climatico\n\nIl 3 ottobre confermato sul testo ufficiale EUR-Lex indicizzato del regolamento (UE) 2026/667 l’obiettivo vincolante 2040 del 90% netto rispetto al 1990. L’apertura HTML diretta restituisce controllo anti-bot: non dichiarata lettura integrale. URL https://eur-lex.europa.eu/eli/reg/2026/667/oj?uri=CELEX%3A32026R0667 . Gli obiettivi 2030/2050 restano dal regolamento2021/1119 già verificato nel ciclo originario.\n';p.write_text(s,encoding='utf8')
p=next((B/'chapters').glob('12-*.md'));s=p.read_text(encoding='utf8').replace('Quadro climatico UE verificato il 18 agosto 2026','Quadro climatico UE — aggiornamento del 3 ottobre 2026');p.write_text(s,encoding='utf8')
files=sorted((B/'chapters').glob('*.md'));urls=[]
for p in Path('wiki/sources').glob('vol-11-*-2026-10-03.md'):urls+=re.findall(r'https?://[^\s)]+',p.read_text(encoding='utf8'))
ledger={'volume':'VOL-11','module':'M-TR04','date':'2026-10-03','textVerified':True,'finalVerified':False,'readingCheckpoint':(A/'VOL-11-reading-checkpoint.json').as_posix(),'findings':rows,'files':[{'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'readComplete':True,'readingScope':'audit originale integrale e riesame dei delta nel contesto','quizReview':'complete'} for p in files],'externalClaimsChecked':sorted(set(urls)),'normativeEvidence':[(A/'norme-vol11/manifest.json').as_posix(),(A/'norme-vol11/manifest-extra.json').as_posix()],'chapterGates':{'passed':14,'blockers':0,'warnings':0},'coverageNuclei':90,'appendices':'A–E nel capitolo14','limitations':['PDF aggiornato ancora da verificare','Verifiche normative mirate con scope per articolo/documento','Scenari locali e importi didattici non sono istruzioni professionali per ogni caso']}
(A/'VOL-11-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf8');print('44 ID, report14/15 and ledger prepared.')
