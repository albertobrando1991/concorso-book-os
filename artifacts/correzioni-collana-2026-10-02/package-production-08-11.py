from pathlib import Path
import json,hashlib,shutil,re,sys
A=Path(__file__).parent;W=Path('wiki/reviews/correzioni-collana-2026-10-02')
load=lambda p:json.loads(p.read_text(encoding='utf8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
def prose_spacing(text):
 parts=re.split(r'(`[^`]*`)',text)
 for i in range(0,len(parts),2):
  parts[i]=re.sub(r'(?<=[a-zàèéìòù])(?=\d)',' ',parts[i])
  parts[i]=re.sub(r'(?<=\d)(?=[a-zàèéìòù])',' ',parts[i])
  parts[i]=parts[i].replace('tutteviste','tutte viste').replace('PDF244','PDF 244').replace('accettazioneKDP','accettazione KDP').replace('fascicoloKDP','fascicolo KDP').replace('payloadAPI','payload API')
  parts[i]=re.sub(r'\b(pp?|n)\.(?=\d)',r'\1. ',parts[i])
  parts[i]=re.sub(r'([;:])(?=\d)',r'\1 ',parts[i])
 return ''.join(parts)
spec={
'08':{'mod':'01','chapters':13,'nuclei':82,'label':'vol-08-release-20261003','title':'ICT, digitale, cybersecurity e dati','extra':'Pseudocodice e SQL sono leggibili in Consolas a circa9,49pt. La timeline procurement alle pp.163–164 e il diario a p.237 usano gruppi collegati di colonne; l’avvertenza finale è integrata nella p.244. Nessuna immagine raster presente.','rows':[
('P08-01','Indice, pp.6–8','Tipografia','medio','Indice storico a6,75pt.','Corpo minimo9,5pt e95destinazioni reali verificate.'),
('P08-02','Timeline, pp.163–164','Tabelle','grave','Parole spezzate e intestazioni ripetute sulla stessa pagina.','Gruppi di colonne collegati, sequenza delle fasi e responsabili leggibili.'),
('P08-03','Diario, p.237','Usabilità','grave','Otto colonne troppo strette per compilare.','Tre gruppi4/4/2 con campi brevi e righe vuote leggibili.'),
('P08-04','Aperture, controllo p.222','Gerarchia','medio','Titoli duplicati senza distinzione gerarchica.','Titolo capitolo distinto dalla prima sezione e riflusso verificato.'),
('P08-05','Chiusura, p.244','Ritmo','lieve','Avvertenza isolata nella pagina finale.','Avvertenza integrata con checklist e riferimenti.') ]},
'09':{'mod':'02','chapters':14,'nuclei':73,'label':'vol-09-final-20261003','title':'Appalti, PNRR e procurement','extra':'Il kit14.6 alle pp.265–267 ricolloca gli strumenti necessari nei capitoli e aggiunge schede compilabili: non vengono dichiarate cinque appendici autonome inesistenti. Il Gantt a p.240 distingue percorso critico A–B–D–F, nove giorni lavorativi e margine di un giorno per C/E; la tabella seguente esplicita i valori. Il delta finale corregge i due campi della scheda senza cambiare norme o casi.','rows':[
('P09-01','Tabella, p.13','Formattazione','grave','Tabella Markdown non resa nella prova storica.','Tabella completa con nove righe, intestazioni e celle leggibili.'),
('P09-02','Quiz, pp.106–107,157,212–213','Gerarchia','medio','Titoli interferivano con le alternative.','Unità domanda/alternative/soluzione distinte e continue.'),
('P09-03','Sezione13.1, p.227','Residui interni','medio','N-TR02-XX-04 visibile al lettore.','Titolo descrittivo e numerazione13.1 nel PDF.'),
('P09-04','Kit14.6, pp.265–267','Apparati','grave','Promesse di appendici non presenti.','Rinvii puntuali ai capitoli e schede effettive; promessa riallineata.'),
('P09-05','Indice, pp.6–7','Tipografia','medio','Indice troppo piccolo.','Corpo9,5pt e87destinazioni verificate.'),
('P09-06','Tabelle nel volume','Continuità','medio','Frammenti sulla stessa pagina.','Intestazioni regolari e gruppi semantici collegati senza perdita di righe.'),
('P09-07','Scheda affidamento, p.266','Refuso','medio','Segno+ univa Controlli svolti e Risorse.','Eliminato il segno e separati i due campi in paragrafi; delta verificato nel nuovo PDF.') ]},
'10':{'mod':'03','chapters':13,'nuclei':88,'label':'vol-10-final-20261003','title':'Tecnico-ingegneristico','extra':'Quattro immagini alle pp.28,31,122,123. Le tre tavole sono state renderizzate da PDF realmente vettoriali, con54/87/89tracciati e zero bitmap:1950pixel, circa371,4ppi alla dimensione effettiva. La fotografia illustrativa conserva292,6ppi, valore dichiarato senza attestare300ppi o interpolare l’immagine. Planimetria e caso distinguono misure, discordanza documentale, zona non ispezionata e causa non accertata; la soluzione calcola36m²,864euro e differenza144euro.','rows':[
('P10-01','Figure pp.28,31,122–123; dossier pp.121–126','Completezza visuale','grave','Mancavano diagrammi e documenti effettivi del caso.','Quattro figure e dossier con dati, consegna, elaborato modello e griglia; corrispondenza figura/testo verificata.'),
('P10-02','Tabelle, pp.79–80 e125–126','Continuità','medio','Frammenti e intestazioni ripetute nella prova storica.','Continuazioni regolari tra pagine con intestazione, contenuti integri e celle leggibili.'),
('P10-03','Tre tavole, pp.28,31,122','Risoluzione','medio','Prima rasterizzazione a247,6ppi effettivi.','Rendering dei PDF vettoriali a371,4ppi; composizione immutata e tre pagine ricontrollate.') ]},
'11':{'mod':'04','chapters':14,'nuclei':90,'label':'vol-11-final-20261003','title':'Ambiente, protezione civile e sostenibilità','extra':'Le appendici A–E sono realmente presenti alle pp.247–250 come schede operative nel capitolo14. Le matrici dense sono suddivise in gruppi collegati per la stessa chiave. Due codici DO sono stati tolti dalla pagina pubblica e conservati nei metadati audit con fonte, ambito, versione, data e posizione. L’appendice B esplicita il divisore1.000 nella conversione7.500kg=7,5t.','rows':[
('P11-01','Matrici, pp.149,167,184,206–207,225,227','Tabelle','grave','Nove/undici colonne spezzavano parole e sigle.','Gruppi collegati fino a quattro colonne; intestazione Responsabile / funzione ora va a capo tra parole.'),
('P11-02','Dati operativi, pp.91,179–180,191','Residui interni','medio','ID e istruzioni audit apparivano nel testo pubblico.','ID conservati nel frontmatter strutturato e rimossi dal corpo; fonti, date e limiti leggibili.'),
('P11-03','Appendici A–E, pp.247–250','Apparati','grave','Appendici promesse assenti nella prova storica.','Inserite schede operative di protezione civile, energia, ambiente locale, registri e toolkit; esaminate tutte.'),
('P11-04','Indice, pp.6–8','Tipografia','medio','Indice a6,75pt.','Corpo minimo9,5pt e104destinazioni verificate.'),
('P11-05','Matrice conclusiva, p.149','Continuità','medio','Frammentazione patologica e parole troncate.','Due proiezioni semantiche collegate dalla colonna Fatto; righe e intestazioni integre.'),
('P11-06','Appendice B, p.248','Calcolo e unità','medio','30.000×0,25=7,5t ometteva la conversione kg/t.','Esplicitati kWh,kg/kWh e divisione per1.000; formula ricalcolata e PDF ricontrollato.') ]}}

for num in sys.argv[1:] or list(spec):
 s=spec[num];vol=f'VOL-{num}';label=s['label'];D=Path(f'delivery/{vol}/candidate-2026-10-03');v=load(A/(label+'-verification.json'));sub=load(A/(label+'-index-subentries.json'));dom=load(A/(label+'-proof-metrics.json'));geometry=load(A/(label+'-proof-audit')/'metrics.json');vis=load(A/f'{vol}-production-visual.json');payload=load(A/f'{vol}-production-payload.json');fpath=A/f'M-TR{s["mod"]}-freeze.json';freeze=load(fpath)
 assert v['pageCountMatch'] and v['allFontsEmbedded'] and not any(v[k] for k in ['indexMismatches','overflowPages','internalLeaks','replacementGlyphs','missingImages'])
 assert len(v['indexEntries'])==s['chapters'] and len(sub['entries'])==s['nuclei'] and not sub['mismatches']
 assert vis.get('finalPdfSha256',vis['pdfSha256'])==v['sha256'] and vis['allContactSheetsViewed']
 assert all(sha(Path(r['path']))==r['sha256'] for r in freeze['files'])
 assert not any(p['textOutsidePage'] for p in geometry['pagesData'])
 chapterpaths=[c['path'] for c in payload['chapters'] if '/chapters/' in c['path']];assert len(chapterpaths)==s['chapters'] and all(any(p['path']==c for p in dom['pages']) for c in chapterpaths)
 table='| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |\n|---|---|---|---|---|---|---|\n'+'\n'.join('| '+' | '.join(r)+' | Corretto e verificato localmente |' for r in s['rows'])
 total=s['chapters']+s['nuclei'];coverage=f"Tutte le {len(vis['contactSheets'])} tavole contatto della release ({v['pages']} pagine) e {len(vis['zoomPagesViewed'])} pagine ingrandite, elencate nel registro visuale."
 if num!='08':coverage+=' '+vis['finalCoverage']
 report=f'''# Revisione dell’impaginato corrente — {vol}

## 1. Sintesi

Prova del3ottobre2026: **{v['pages']} pagine**, {s['chapters']}capitoli e {s['nuclei']}nuclei. Interno tecnico revisionato; servizi digitali e dati editoriali comuni restano dipendenze aperte. Nessun signoff24.

PDF SHA-256: `{v['sha256']}`.

## 2. Punti di forza

Il volume {s['title']} conserva la progressione dei capitoli, gli apparati e i casi del freeze testuale. L’indice distingue capitoli e nuclei e porta alle pagine effettive. Le tabelle dense sono leggibili per gruppi collegati; nessuna riduzione del corpo è stata usata per accorciare il volume.

## 3. Interventi verificati

{table}

## 4. Macrostruttura e completezza

Presenti tutti i{s['chapters']}master e i{s['nuclei']}nuclei attesi. Il payload esportabile, gli snapshot e gli hash del freeze sono conservati nel pacchetto. Confrontati {len(freeze['files'])}file del freeze con le sorgenti correnti: nessuna divergenza non registrata. La revisione testuale integrale e le correzioni sostanziali restano documentate nel rapporto VOL-{num}.md; questa fase non dichiara una nuova rilettura parola per parola dell’intero manuale.

## 5. Contenuti, figure e rinvii

{s['extra']}

La verifica grafica non certifica nuovamente ogni norma o fonte. I delta testuali di produzione sono tracciati separatamente con copie precedenti e confronto degli hash; quiz e casi restano quelli verificati dal responsabile testuale, salvo le correzioni puntuali esplicitate sopra.

## 6. Tipografia e geometria

Formato6,69×9,61pollici,481,92×691,92pt. Corpo Garamond circa11pt; tabelle e indice circa9,5pt. Font incorporati; zero overflow DOM, testo oltre pagina, glifi sostitutivi e immagini mancanti. Conteggio DOM e PDF coincidente. Le continuazioni normali di tabella possono attraversare il foglio con intestazione ripetuta; non sono confuse con la frammentazione patologica storica.

## 7. Secondo controllo e copertura

{coverage} Le tavole contatto verificano ritmo, densità, salti e geometria; non equivalgono alla lettura di ogni parola del raster a piena risoluzione. L’estrazione diretta del PDF conferma tutte le{total}destinazioni d’indice ({s['chapters']}capitoli+{s['nuclei']}nuclei). Registri geometrici e DOM coprono ogni pagina. Nessuna perdita di contenuto osservata nelle verifiche dichiarate.

## 8. Giudizio finale

**Non pubblicabile allo stato attuale per dipendenze editoriali comuni aperte.** Il candidato interno supera i controlli locali descritti. La promessa digitale di pagina1 non è stata collaudata; dati editoriali commerciali, copertina, prova fisica e accettazioneKDP non sono attestati. Step21 resta in corso;22–24 non chiusi da questo rapporto.

## 9. Produzione e artefatti

Il conteggio di{v['pages']}pagine rientra nel limite828per questo formato in nero su carta bianca, documentato nel fascicoloKDP di VOL-02 ([specifica ufficiale](https://kdp.amazon.com/it_IT/help/topic/GVBQ3CMEQW3W2VL6)). Non occorre dividere l’interno o ridurre il carattere. Pacchetto: `delivery/{vol}/candidate-2026-10-03/README.md`, con PDF, payload, snapshot, verifiche, registri e immagini di controllo. Nessun upload o pubblicazione eseguito.

## 10. Priorità residue

Risoluzione delle dipendenze comuni sul digitale e sui dati editoriali; eventuale aggiornamento del front matter e nuova verifica del delta; copertina e prova fisica; completamento dei gate nell’ordine del CLI. Le fonti normative restano quelle consolidate nei dossier testuali. Il PDF è un candidato revisionabile, non un file approvato alla pubblicazione.
'''
 # Normalize compact number/word drafting in prose, preserving paths and identifiers.
 report=prose_spacing(report)
 W.mkdir(parents=True,exist_ok=True);rp=W/f'PDF-{vol}.md';rp.write_text(report,encoding='utf8')
 canonical=Path(f'wiki/reviews/pipeline/{vol}/21-vol-{num}.md');archive=A/f'{vol}-step21-before-production.md'
 if canonical.exists() and not archive.exists():shutil.copy2(canonical,archive)
 canonical.write_text('---\nstatus: review\nreview_required: true\nupdated: 2026-10-03\n---\n\n'+report,encoding='utf8')
 production={'volume':vol,'pages':v['pages'],'pdfSha256':v['sha256'],'report':rp.as_posix(),'visualReview':(A/f'{vol}-production-visual.json').as_posix(),'indexEntriesVerified':total,'finalSignoff':False,'findings':[dict(zip(['id','position','category','severity','diagnosis','correction'],r),status='Corretto e verificato localmente') for r in s['rows']]}
 ledgerpath=A/f'{vol}-ledger.json'
 if ledgerpath.exists():
  ledger=load(ledgerpath)
  for row in ledger.get('files',[]):
   if Path(row['path']).is_file():row['sha256']=sha(Path(row['path']));row['pdfReview']='Tecnica completa e copertura visiva dichiarata nel rapporto di produzione.'
  ledger['limitations']=[x for x in ledger.get('limitations',[]) if 'PDF e figure aggiornati ancora da verificare' not in x]
  ledger['limitations'].append('Produzione locale verificata; dipendenze comuni digitali/editoriali aperte. Nessun signoff24.')
  ledger['limitations']=list(dict.fromkeys(ledger['limitations']))
  for row in ledger.get('findings',[]):
   if row.get('status')=='Testo verificato e congelato; PDF da verificare':row['status']='Testo verificato e congelato; PDF verificato nella copertura dichiarata; dipendenze comuni aperte'
 else:ledger={'volume':vol,'note':'Registro di produzione; audit testuale nel rapporto VOL-09.md e manifest M-TR02-freeze.json.'}
 ledger['production']=production;ledger['finalVerified']=False;save(ledgerpath,ledger)
 textreport=W/f'{vol}.md';t=textreport.read_text(encoding='utf8').replace('Testo verificato e congelato; PDF da verificare','Testo verificato e congelato; PDF verificato nella copertura dichiarata; dipendenze comuni aperte');marker='\n## Verifica di produzione del 3 ottobre 2026\n';t=t.split(marker)[0]+marker+f'\nProva corrente di {v["pages"]} pagine verificata. Rilievi grafici e delta nel rapporto [PDF-{vol}](PDF-{vol}.md); {total} destinazioni d’indice corrette. Copertura panoramica completa e ingrandimenti mirati dichiarati nel registro. Dipendenze editoriali comuni aperte; nessun signoff 24.\n';textreport.write_text(t,encoding='utf8')
 freeze['pdfChecked']={'sha256':v['sha256'],'pages':v['pages'],'method':'Tutte le pagine in contatti; zoom mirati; confronto raster dei delta; geometria e indice completi.','finalSignoff':False};save(fpath,freeze)
 for subdir in ['reports','snapshot','reproduction','visual/release','visual/final']: (D/subdir).mkdir(parents=True,exist_ok=True)
 shutil.copy2(A/(label+'-proof.pdf'),D/f'vol-{num}-interior-kdp.pdf')
 for src,name in [(A/f'{vol}-production-payload.json','payload.json'),(A/(label+'-proof-metrics.json'),'dom-metrics.json'),(A/(label+'-verification.json'),'verification.json'),(A/(label+'-index-subentries.json'),'index-subentries.json'),(A/(label+'-proof-audit')/'metrics.json','pdf-geometry.json'),(A/f'{vol}-production-visual.json','visual-review.json')]:shutil.copy2(src,D/name)
 snapshots={Path(r['path']) for r in freeze['files']}
 snapshots.update(p for c in payload['chapters'] if (p:=Path('wiki')/c['path']).is_file())
 snapshots.update(Path('wiki')/r['path'] for r in payload.get('assets',[]) if (Path('wiki')/r['path']).is_file())
 if num=='10':snapshots.update(Path(r['source']) for r in load(A/'VOL-10-vector-render-delta.json'))
 snapshots.update(Path('wiki/sources')/(ref.removeprefix('sources/')+'.md') for c in payload['chapters'] for ref in c.get('sourceRefs',[]) if (Path('wiki/sources')/(ref.removeprefix('sources/')+'.md')).is_file())
 volume_index=next(Path('wiki/books/volumi').glob(f'vol-{num}-*/index.md'));snapshots.add(volume_index)
 for src in sorted(snapshots):dest=D/'snapshot'/src;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
 save(D/'source-hashes.json',[{'path':p.as_posix(),'sha256':sha(p),'snapshot':(Path('snapshot')/p).as_posix()} for p in sorted(snapshots)])
 for src in [rp,textreport,ledgerpath,fpath]:shutil.copy2(src,D/'reports'/src.name)
 for src in A.glob(f'{vol}-*delta.json'):shutil.copy2(src,D/'reports'/src.name)
 if num!='08':shutil.copy2(A/f'{vol}-final-render-comparison.json',D/'render-comparison.json')
 release=A/f'vol-{num}-release-20261003-proof-audit'
 for name in vis['contactSheets']:shutil.copy2(release/name,D/'visual/release'/name)
 for n in vis['zoomPagesViewed']:shutil.copy2(release/f'zoom-{n:03}.png',D/'visual/release'/f'zoom-{n:03}.png')
 for n in vis.get('finalChangedPagesViewed',[]):shutil.copy2(A/(label+'-proof-audit')/f'zoom-{n:03}.png',D/'visual/final'/f'zoom-{n:03}.png')
 if num!='08':
  for p in (A/(label+'-proof-audit')).glob('contact-*.png'):shutil.copy2(p,D/'visual/final'/p.name)
 pageledger=[{'page':p['page'],'path':dom['pages'][p['page']-1]['path'],'contactViewed':True,'zoomViewed':p['page'] in vis['zoomPagesViewed'] or p['page'] in vis.get('finalChangedPagesViewed',[]),'textOutsidePage':p['textOutsidePage'],'overflow':dom['pages'][p['page']-1]['overflows'],'method':'Panoramica completa; geometria automatica; ingrandimento solo se zoomViewed.','status':'Nessun difetto geometrico bloccante rilevato; limiti generali nel rapporto.'} for p in geometry['pagesData']];save(D/'page-ledger.json',pageledger)
 rendererfiles=[Path('src/book/pagination.ts'),Path('src/server/book/book-preview.ts'),Path('scripts/book-studio-pdf-export-core.mjs'),Path('scripts/book-studio-layout-options.mjs')]+list(Path('app').rglob('*.css'))+list(Path('app').rglob('*book*.tsx'))
 save(D/'renderer-source-hashes.json',[{'path':p.as_posix(),'sha256':sha(p)} for p in rendererfiles if p.is_file()])
 script=(A/'export-proof.mjs').read_text(encoding='utf8').replace("from '../../scripts/","from '../../../../scripts/").replace("import path from 'node:path'","import path from 'node:path'\nimport {fileURLToPath} from 'node:url'")
 script=script.replace("const bookId=process.argv[2]||'volumi/vol-12'",f"const bookId='volumi/vol-{num}'").replace("const label=process.argv[3]||bookId.split('/').at(-1)",f"const label='vol-{num}-reproduced'").replace("const out=path.resolve('artifacts/correzioni-collana-2026-10-02')","const out=fileURLToPath(new URL('../reproduced/',import.meta.url))\nawait fs.mkdir(out,{recursive:true})\nconst payload=JSON.parse(await fs.readFile(new URL('../payload.json',import.meta.url),'utf8'))")
 script=script.replace('try {\n  await page.goto',"try {\n  await page.route('**/api/book-studio?**',route=>route.fulfill({status:200,contentType:'application/json',body:JSON.stringify(payload)}))\n  await page.goto")
 (D/'reproduction/export-frozen.mjs').write_text(script,encoding='utf8')
 readme=f'''# {vol} — candidato interno del 3 ottobre 2026

**{v['pages']} pagine; nessuna autorizzazione alla pubblicazione.** Servizi digitali e dati editoriali comuni restano aperti. Step21 in corso;22–24 non chiusi. Destinazione prevista: nero su carta bianca,6,69×9,61pollici.

PDF: `vol-{num}-interior-kdp.pdf`\nSHA-256: `{v['sha256']}`.

Controlli: {total}destinazioni d’indice corrette, DOM=PDF, font incorporati, zero overflow e testo fuori pagina. Copertura: tutte le pagine in tavole contatto; ingrandimenti mirati e confronto raster dei delta. Il controllo delle miniature non è lettura di ogni parola a piena risoluzione. Metodo e limiti in `reports/PDF-{vol}.md` e `visual-review.json`.

Il pacchetto contiene PDF, payload congelato, snapshot di master/fonti/asset, hash, rapporti, contatti e zoom. Le sorgenti normative raw complete restano nel repository: le note fonte incluse ne documentano provenienza e limiti. Non sono inclusi copertina, prova fisica o collaudo della piattaforma digitale.

Riproduzione nell’attuale repository: server Book Studio su3020, dipendenze installate e renderer corrispondente a `renderer-source-hashes.json`; poi `node delivery/{vol}/candidate-2026-10-03/reproduction/export-frozen.mjs`. L’helper intercetta il payloadAPI con quello congelato e scrive una cartella `reproduced`, preservando il candidato. Gli asset devono corrispondere agli hash e agli snapshot. Dipende dal repository e dai font installati: non è un export autonomo e l’identità binaria del PDF non è garantita. Qualunque nuova prova richiede verifica visiva e geometrica.
'''
 (D/'README.md').write_text(prose_spacing(readme),encoding='utf8')
 save(D/'package-manifest.json',{'volume':vol,'date':'2026-10-03','pdfSha256':v['sha256'],'finalSignoff':False,'files':[{'path':p.relative_to(D).as_posix(),'sha256':sha(p)} for p in sorted(D.rglob('*')) if p.is_file() and p.name!='package-manifest.json']})
 manifest=load(D/'package-manifest.json');assert all(sha(D/r['path'])==r['sha256'] for r in manifest['files'])
 print(json.dumps({'volume':vol,'pages':v['pages'],'indexDestinations':total,'packageFiles':len(manifest['files']),'package':D.as_posix(),'hashMismatches':0}))
