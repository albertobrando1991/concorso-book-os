from pathlib import Path
import re,shutil,json
root=Path.cwd();base=root/'wiki/books/moduli/m-fc02-agenzie-fiscali/chapters';art=root/'artifacts/correzioni-collana-2026-10-02';removed=[]
biblio={
'01':'D.Lgs. 300/1999, artt. 57 e seguenti; D.L. 193/2016, art. 1; bandi e avvisi pubblicati nei portali istituzionali AE, ADM, AdER e inPA.',
'02':'D.P.R. 487/1994, come modificato dal D.P.R. 82/2023; testo, allegati e avvisi del bando cui si riferisce il decoder.',
'03':'D.Lgs. 300/1999, artt. 57–74; D.L. 193/2016, art. 1; statuti e regolamenti di amministrazione di Agenzia delle entrate, ADM e AdER.',
'04':'Costituzione, artt. 23 e 53; D.P.R. 917/1986 (TUIR); D.P.R. 633/1972 (IVA); legge 212/2000; direttiva 2006/112/CE; regolamento (UE) 952/2013.',
'05':'D.P.R. 600/1973, artt. 32–41; legge 212/2000, artt. 6-bis, 10-quater e 10-quinquies; D.Lgs. 218/1997; D.Lgs. 128/2015; circolare AE 6/E del 6 agosto 2026. Per i casi internazionali, convenzione bilaterale pertinente e linee guida OCSE sui prezzi di trasferimento.',
'05a':'D.Lgs. 471/1997, D.Lgs. 472/1997 e D.Lgs. 74/2000, coordinati con il D.Lgs. 87/2024 e i correttivi applicabili; D.L. 200/2025, art. 4, convertito dalla legge 26/2026, per il rinvio al 2027 del TU 173/2024.',
'06':'D.P.R. 917/1986 (TUIR), artt. 6, 25–71, 72–83 e 109; D.P.R. 633/1972; D.P.R. 322/1998; D.Lgs. 241/1997. Gli esempi numerici assumono espressamente dati didattici: non sostituiscono aliquote o istruzioni dei modelli annuali.',
'07':'D.P.R. 602/1973, in particolare artt. 19, 77 e 86; D.Lgs. 112/1999; D.Lgs. 110/2024; istruzioni AdER su rateizzazione e procedure cautelari ed esecutive.',
'08':'Regolamento (UE) 952/2013 (CDU); regolamenti delegato (UE) 2015/2446 e di esecuzione (UE) 2015/2447; D.Lgs. 141/2024 e correttivi; istruzioni ADM sulle procedure doganali.',
'09':'D.Lgs. 504/1995 (TUA); direttiva (UE) 2020/262; istruzioni ADM sul sistema EMCS; D.Lgs. 41/2024 per il riordino dei giochi a distanza e disposizioni di settore sulle concessioni.',
'10':'Codice civile, artt. 2643 e seguenti e 2808; R.D.L. 652/1939; D.P.R. 650/1972; D.M. 701/1994; guide tecniche dell’Agenzia delle entrate su catasto, pubblicità immobiliare e osservatorio OMI.',
'11':'Codice civile, artt. 2423 e seguenti; principi OIC 11, 12, 13, 16, 24 e altri pertinenti, con emendamenti applicabili; TUIR per il raccordo tra risultato civilistico e imponibile.',
'12':'Codice civile: obbligazioni e contratti, garanzie, impresa e società; D.Lgs. 14/2019 (Codice della crisi) per le definizioni e gli assetti richiamati. Le regole tributarie e doganali speciali restano distinte.',
'13':'D.P.R. 487/1994 e D.P.R. 82/2023; bandi, allegati e avvisi delle singole procedure. Le simulazioni di questo capitolo sono esercizi didattici, non quesiti attribuiti a una banca dati ufficiale.',
'14':'TUIR; D.P.R. 600/1973 e 602/1973; legge 212/2000; D.Lgs. 471/1997, 472/1997, 74/2000 e 546/1992 nel regime 2026; CDU; TUA; regolamento (UE) 2016/679. I capitoli indicati nelle tavole sviluppano le relative regole e applicazioni.'}
words='ammissibilita centralita disponibilita esecutivita formalita genericita gravita imputabilita incapacita integrita intensita invalidita irregolarita legalita neutralita nullita redditivita unita velocita abitualita annullabilita applicabilita attendibilita autenticita capacita conformita contabilita credibilita densita detraibilita difformita effettivita elasticita entita esigibilita fiscalita idoneita illegalita illegittimita immunita imparzialita imponibilita impossibilita inattivita indetraibilita irreparabilita irretroattivita liquidita luminosita normalita oralita ordinarieta parita parziarieta passivita penalita pluralita priorita probatorieta progressivita pubblicita punibilita recuperabilita responsabilita riferibilita severita societa solidarieta solidita specialita stagionalita sussidiarieta tempestivita territorialita tipicita titolarita verificabilita modalita qualita realta attivita autorita difficolta volonta potesta affinche poiche finche perche cosi pero cio piu puo gia neanche'.split()
accent={w:w[:-1]+('é' if w.endswith('che') else 'ì' if w=='cosi' else 'ò' if w in ['pero','cio','puo'] else 'ù' if w=='piu' else 'à') for w in words if w!='neanche'}
def language(t):
 for w,v in accent.items():
  t=re.sub(r'\b'+w+r'\b',v,t);t=re.sub(r'\b'+w.capitalize()+r'\b',v.capitalize(),t)
 t=re.sub(r'([àèéìòù])\x27',r'\1',t)
 t=re.sub(r'\be\x27\b','è',t) if False else t
 for a,b in [(" e' ",' è '),("E' ",'È '),(" ne' ",' né '),(" cosi'",' così'),('disciplina stabilità','disciplina stabilita'),('funzione stabilità','funzione stabilita'),('documentazione stabilità','documentazione stabilita'),('priorità stabilità','priorità stabilita'),('S.r.l., stabilità a Bologna','S.r.l., stabilita a Bologna'),("l'operatore necessità","l'operatore necessita"),('Sarà sta preparando','Sara sta preparando'),('Sarà pensa','Sara pensa'),('Sarà corregge','Sara corregge'),('Sarà non ha','Sara non ha'),("infiltra l'offerta con controlli pubblici","presidia l'offerta con controlli pubblici")]:t=t.replace(a,b)
 return t
for p in sorted(base.glob('*.md')):
 s=p.read_text(encoding='utf-8');bk=art/'before-text/VOL-03'/p.name
 if not bk.exists():shutil.copy2(p,bk)
 prefix,fm,body=s.split('---',2);code=p.name.split('-')[0]
 # The Decoder also has a short source block BEFORE legitimate chapter text.
 body=re.sub(r'(?ms)^### Riferimenti consolidati\n(?:(?!^#{1,3} ).)*?(?=^## Dal bando al piano di studio)', '', body)
 matches=list(re.finditer(r'(?m)^#{2,3} Riferimenti consolidati',body))
 m=re.search(r'(?s).*',body[matches[-1].start():]) if False else None
 if matches:m=re.search(r'(?ms)^#{2,3} Riferimenti consolidati.*',body[matches[-1].start():])
 tail_start=matches[-1].start() if matches else None
 if m:
  removed.append({'file':str(p),'removedStaffTail':m.group(0)});body=body[:tail_start].rstrip()+'\n\n## Riferimenti essenziali\n\n'+biblio[code]+'\n'
 # Protect URLs, image destinations and wiki targets while editing ordinary prose.
 chunks=re.split(r'(\[\[[^\]]+\]\]|\]\([^\n)]+\))',body)
 for i in range(0,len(chunks),2):chunks[i]=language(chunks[i])
 body=''.join(chunks)
 body=body.replace('La pubblicazione o l\'applicazione a una fattispecie reale richiede una review giuridica specifica.',"La soluzione del caso richiede di verificare la disposizione applicabile e i suoi presupposti.")
 body=body.replace('Il quadro e il metodo derivano da [[sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18]].','Il quadro si fonda sulla direttiva IVA 2006/112/CE e sul Codice doganale dell’Unione, regolamento (UE) 952/2013.')
 body=body.replace('se nessuna destinazione consolidata è pronta, registra un gap editoriale: non sostituirlo con un rinvio generico.','se una materia richiesta non è trattata nel percorso individuato, segnala nel piano di studio l’integrazione necessaria e scegli un testo specialistico pertinente al programma.')
 body=body.replace('apri un gap di copertura e abbina una fonte dedicata prima della scrittura','integra con un manuale di statistica o analisi dei dati adeguato al livello della prova')
 body=body.replace('[[books/moduli/architettura-moduli-specialistici#Regola madre di copertura v4 - vincolante]]','Programma tecnico del bando e relativo manuale specialistico')
 body=body.replace('Se manca una destinazione consolidata, annota `gap da consolidare` e non promettere copertura.','Se manca un contenuto richiesto, annota `integrazione da studiare`, con il testo scelto e la data di verifica.')
 body=body.replace('le procedure avanzate richiedono una fonte dedicata','per procedure avanzate espressamente richieste dal bando, integra con un testo specialistico aggiornato')
 replacements={'sources/regolamento-ue-2016-679-gdpr-protezione-dati-personali':'regolamento (UE) 2016/679 (GDPR)','sources/sanzioni-amministrative-tributarie-aggiornamento-2026-07-18':'D.Lgs. 471/1997 e 472/1997','sources/reati-tributari-dlgs-74-2000-aggiornamento-2026-07-18':'D.Lgs. 74/2000','sources/processo-tributario-dlgs-175-2024-aggiornamento-2026-07-18':'D.Lgs. 546/1992, regime 2026','sources/diritto-ue-fiscale-doganale-iva-cdu-2026-07-18':'direttiva 2006/112/CE e regolamento (UE) 952/2013','sources/prove-concorsuali-quiz-scritto-orale-dpr-487-1994':'(D.P.R. 487/1994)'}
 for a,b in replacements.items():body=body.replace('[['+a+']]',b)
 body=re.sub(r' \[\[(?:sources/m-fc02-dossier-redazionale-agenzie-fiscali|sources/bandi-rappresentativi-m-fc02-agenzie-fiscali-2023-2026|topics/banca-dati-ufficiale-quiz|topics/profili-agenzie-fiscali)\]\]','',body)
 fm=fm.replace('status: final','status: revised_draft').replace('draft_stage: text_frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('"text-frozen", ','').replace(', "text-frozen"','')
 fm=re.sub(r'updated_at: [^\n]+','updated_at: 2026-10-03',fm,count=1)
 fm=re.sub(r'(?m)^title: (.*)$',lambda m:'title: '+language(m[1]),fm)
 fm=fm.replace('processo-tributario-dlgs-175-2024-aggiornamento-2026-07-18.md','processo-tributario-regime-2026-rettifica-2026-10-03.md')
 if code=='05':fm=fm.replace('"sources/dogane-accise-rettifiche-2026-10-03", ','').replace('"wiki/sources/dogane-accise-rettifiche-2026-10-03.md", ','')
 p.write_text(prefix+'---'+fm+'---'+body,encoding='utf-8')
(art/'VOL-03-FC02-staff-tail-archive.json').write_text(json.dumps(removed,ensure_ascii=False,indent=2),encoding='utf-8')
print('16 capitoli: accenti contestuali e riferimenti pubblici; '+str(len(removed))+' code staff archiviate')
