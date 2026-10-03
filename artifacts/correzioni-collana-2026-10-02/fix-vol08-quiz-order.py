from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters')
questions={9:[
('Un utente autenticato apre la pratica di un altro cittadino cambiando l’ID nell’URL. Quale controllo manca?', ['Il rinnovo periodico del certificato TLS','L’autorizzazione sulla singola risorsa','La compressione della risposta','La verifica della sintassi JSON'],'B','L’identità accertata non dimostra il diritto a consultare ogni oggetto. TLS protegge il canale, non sostituisce la verifica della risorsa.'),
('Quale combinazione esprime due categorie di fattori?', ['Password e PIN','Due password di servizi diversi','Domanda segreta e password','Password e dispositivo di possesso verificato'],'D','Conoscenza e possesso sono categorie diverse. Due segreti ricordati rimangono nella stessa categoria; il recupero deve conservare protezione adeguata.'),
('Vuoi verificare pubblicamente l’origine di un documento e rilevarne modifiche. Quale meccanismo è pertinente?', ['Firma digitale crittografica verificabile con la chiave pubblica','Hash pubblicato nello stesso file senza fonte affidabile','Sola cifratura simmetrica','Codifica Base64'],'A','La firma lega l’integrità alla chiave del firmatario secondo lo schema e la fiducia adottati; non offre da sola riservatezza. Un hash sostituibile insieme al documento non autentica l’origine.'),
('Il SIEM produce un alert insolito. Qual è il primo uso corretto?', ['Dichiarare concluso l’incidente','Cancellare i log duplicati prima dell’analisi','Qualificarlo correlando fonti, contesto e impatto','Ripristinare subito tutti i sistemi'],'C','L’alert è un segnale da valutare. La classificazione guida contenimento ed escalation e conserva le evidenze.'),
('Una chiave è sospettata compromessa. Quale distinzione è corretta?', ['La rotazione prova che la vecchia chiave non è mai stata usata','La revoca ne invalida l’uso nel sistema pertinente; la sostituzione non cancella gli effetti pregressi','Revocare significa soltanto copiarla in un altro archivio','La scadenza futura rende superfluo intervenire'],'B','Si revocano o disabilitano le credenziali coinvolte, si sostituisce il materiale e si ricostruisce l’esposizione. La rotazione da sola non chiude sessioni o usi già avvenuti.'),
('Un soggetto già obbligato apprende lunedì alle 10 di un incidente NIS significativo. Nel regime ordinario quale termine massimo vale per la notifica, distinta dalla pre-notifica?', ['Martedì alle 10','Un mese dalla conoscenza','72 ore dopo la pre-notifica','Giovedì alle 10'],'D','Le 72 ore decorrono dalla medesima conoscenza dell’incidente, non dall’invio della pre-notifica. Rimane l’obbligo di agire senza ingiustificato ritardo e la disciplina speciale dei prestatori fiduciari.')],
10:[
('Chi decide finalità e priorità di qualità del dominio, nel modello organizzativo illustrato?', ['Il data owner nel perimetro delle proprie competenze','Il solo amministratore del database','Qualunque fruitore che possiede una copia','Il catalogo automatico'],'A','L’owner presidia le decisioni; steward e custodian curano rispettivamente significato/qualità e attuazione tecnica. I nomi del modello non creano nuovi poteri legali.'),
('Quale attività descrive meglio lo steward?', ['Approvare autonomamente qualsiasi nuovo trattamento','Sostituire il responsabile del procedimento','Curare glossario, metadati, regole ed eccezioni di qualità','Amministrare sempre l’infrastruttura fisica'],'C','Lo steward rende coerenti significati e regole e raccorda gli uffici. La decisione su nuovi usi resta alla funzione competente.'),
('Due indicatori diversi derivano apparentemente dallo stesso archivio. Quale controllo aiuta a ricostruire la differenza?', ['Confrontare soltanto il formato dei grafici','Verificare fonte, estrazione, trasformazioni e versioni tramite lineage','Scegliere automaticamente il risultato più recente','Eliminare uno dei dataset'],'B','Il lineage ricostruisce la provenienza e le trasformazioni; differenze di data, definizione o filtro possono spiegare valori diversi senza presumere un errore dell’altro ufficio.'),
('Un catalogo descrive un dataset riservato. Quale conclusione è corretta?', ['I record diventano aperti','Il dataset perde la classificazione','Ogni ente può interrogarlo senza finalità','La descrizione non equivale all’accesso ai record'],'D','Metadati e accesso sono piani diversi. La catalogazione rende reperibile e comprensibile una risorsa senza cancellarne limiti e autorizzazioni.'),
('Una regola di qualità prevede un codice ufficio valido in ogni pratica attiva. Quale indicatore è coerente?', ['Pratiche attive con codice valido diviso tutte le pratiche attive, con periodo, soglia e azione definiti','Dimensione totale del database in byte','Numero di utenti registrati','Percentuale di campi qualsiasi compilati'],'A','Numeratore e denominatore si riferiscono alla popolazione della regola. Occorre poi assegnare chi interviene sugli scarti; misure di volume non dimostrano quella qualità.'),
('Un CSV è scaricabile gratuitamente, ma vieta ogni riuso commerciale e non ha metadati. Rispetta già la definizione CAD di dati di tipo aperto?', ['Sì, basta la gratuità','Sì, basta l’estensione CSV','No: mancano condizioni di riuso e metadati richiesti','Solo se il file supera una dimensione minima'],'C','I requisiti CAD sono cumulativi: condizioni per l’uso anche commerciale, formato aperto elaborabile con metadati e regime economico previsto. La dimensione non sostituisce tali requisiti.')]
}
for n,rows in questions.items():
 p=next(B.glob(f'{n:02}-*.md'));s=p.read_text(encoding='utf8');q='### Sei quiz commentati\n\n'
 for i,(stem,opts,key,why) in enumerate(rows,1):
  q+=f'**Quiz {i}. {stem}**\n\n'+'\n'.join(f'{chr(65+j)}) {x}.' for j,x in enumerate(opts))+f'\n\n**Risposta corretta: {key}.** {why}\n\n'
 if n==9:s=re.sub(r'### Sei quiz commentati\n.*?(?=### Domanda da commissario)',q,s,flags=re.S)
 else:s=re.sub(r'\*\*Quiz 1\..*?(?=## Da sapere in 5 righe)',q,s,flags=re.S)
 p.write_text(s,encoding='utf8')
# Move the seven introductory application blocks after their definitions.
p=next(B.glob('10-*.md'));s=p.read_text(encoding='utf8');markers=['Un dato è una rappresentazione','I nomi data owner','Il ciclo di vita del dato inizia','Inventario, catalogo, glossario','La qualità del dato è','Gli open data sono','L\'interoperabilità']
changes=[]
for i,marker in enumerate(markers,1):
 start=s.index(f'## N-TR01-10-{i:02}');end=s.find('\n## ',start+1)
 if end<0:end=len(s)
 section=s[start:end]; lines=section.split('\n',1);body=lines[1]
 # The definition phrase is an exact anchor; for interoperability locate stable alternative.
 if marker not in body:
  candidates=[p for p in body.split('\n\n') if p.startswith(('Interoperabilità','L’interoperabilità'))]
  assert candidates,(i,marker)
  marker=candidates[0]
 cut=body.index(marker);intro=body[:cut].strip();core=body[cut:].strip()
 assert intro.startswith('### ')
 # Applications follow definition/theory, before the error/example closure when present.
 pos=core.find('**Errore tipico:**')
 if pos<0:pos=len(core)
 body=core[:pos].rstrip()+'\n\n'+intro+'\n\n'+core[pos:].lstrip()+'\n'
 s=s[:start]+lines[0]+'\n\n'+body+s[end:];changes.append({'nucleus':i,'action':'definitions and theory before existing application block; no unique content removed'})
s=s.replace('Per essere effettivo, il riuso richiede almeno condizioni comprensibili: i tre requisiti cumulativi','La definizione richiede i tre requisiti cumulativi')
p.write_text(s,encoding='utf8')
Path('artifacts/correzioni-collana-2026-10-02/VOL-08-quiz-review.json').write_text(json.dumps({'rewritten':questions,'answerDistribution':{'A':3,'B':3,'C':3,'D':3},'checked':'12 stems, alternatives and explanations resolved independently; correct option matches comment','ordering':changes},ensure_ascii=False,indent=2),encoding='utf8')
print('12 quiz risolti e rimappati; sette nuclei data governance riordinati.')
