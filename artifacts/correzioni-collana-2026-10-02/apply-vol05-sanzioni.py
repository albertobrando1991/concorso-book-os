from pathlib import Path
import json
B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');O=Path('artifacts/correzioni-collana-2026-10-02')
t=Path('wiki/topics/authority-rettifiche-2026.md');t.write_text(t.read_text(encoding='utf8')+'\n\n## Sanzioni e giurisdizione\n\n[[sources/vol-05-sanzioni-giurisdizione-verifica-2026-10-03]] registra la riforma TUF 128/2026 e le decorrenze differenziate. Per la tutela si distinguono autorità, tipo di sanzione e data di avvio del procedimento; il nome CONSOB non identifica più da solo il giudice.\n',encoding='utf8')
p=B/'chapters/06-sanzioni-impegni-rimedi-controllo-giurisdizionale.md';s=p.read_text(encoding='utf8')
pos=s.index('Il candidato deve distinguere almeno quattro elementi:')
s=s[:pos]+'''### Le garanzie delle sanzioni punitive

Legalità e tipicità richiedono di individuare condotta, destinatari e conseguenze consentite prima di applicare la misura. Le sanzioni sostanzialmente punitive, anche se chiamate amministrative, richiamano garanzie costituzionali e convenzionali: determinatezza, divieto di retroattività sfavorevole, difesa, presunzione d'innocenza e proporzionalità. La disciplina più favorevole richiede l'esame della natura della sanzione, delle norme di successione e delle eventuali deroghe, secondo la giurisprudenza costituzionale; non si applica automaticamente a ogni misura amministrativa.

**Ne bis in idem.** Se la stessa persona è già stata oggetto di decisione definitiva per i medesimi fatti in un procedimento di natura penale in senso sostanziale, una seconda risposta punitiva richiede il controllo del divieto. Cambiare nome all'illecito o autorità competente non rende diversi i fatti. Nel diritto UE, un eventuale cumulo ammesso deve rispettare condizioni rigorose: base prevedibile, obiettivi complementari, coordinamento effettivo, vicinanza temporale e onere complessivo proporzionato. La sentenza bpost, C-117/20, mostra perché non basta rispondere «due autorità, due multe»; neppure ogni misura correttiva e sanzione costituisce automaticamente un bis punitivo.

**Distinzione delle funzioni.** L'ufficio che raccoglie e valuta gli elementi formula la proposta; l'organo competente decide secondo la disciplina dell'ente, considerando le difese. Il modello deve rendere effettivo il confronto, senza trasformare la contestazione in decisione già presa. L'accesso necessario alla difesa si coordina con segreti e riservatezza, non viene sostituito dalla pubblicazione del solo dispositivo.

'''+s[pos:]
s=s.replace("entro il termine previsto dopo l'apertura dell'istruttoria", "entro **tre mesi dalla notifica dell'apertura dell'istruttoria**")
pos=s.index('Il candidato deve usare questa distinzione per ordinare gli istituti:')
s=s[:pos]+'''**Sequenza degli impegni AGCM.** Avvio e notifica → proposta dell'impresa nel termine → valutazione d'idoneità e consultazione del mercato → eventuale decisione che li rende obbligatori → monitoraggio. La decisione può avere durata determinata. L'inadempimento può comportare sanzione fino al 10% del fatturato mondiale dell'esercizio precedente e riapertura nei casi previsti: «senza accertare l'infrazione» non significa «senza obblighi». Non si assume che l'offerta debba essere accettata.

La **transazione antitrust**, art. 14-quater, è diversa: discussioni con l'Autorità, eventuale proposta che riconosce partecipazione e responsabilità, conclusione del procedimento con accertamento e sanzione ridotta. Nella comunicazione AGCM del 16 maggio 2023, n. 30629, la riduzione è del 10% nei cartelli segreti e del 20% negli altri casi contemplati. Non è una trattativa libera sull'esistenza dell'illecito; l'Autorità può interrompere le discussioni. La clemenza per chi collabora alla scoperta di un cartello segue ancora un'altra disciplina, ripresa nel capitolo 8.

**Tempi della difesa antitrust.** Nel DPR 217/1998, aggiornato dal DPR 214/2024, le risultanze istruttorie sono comunicate almeno **45 giorni** prima della chiusura. Memorie e documenti possono essere presentati sino a **10 giorni prima**; la richiesta di audizione al Collegio va proposta entro **10 giorni dal ricevimento** delle risultanze. Sono tre decorrenze differenti, non tre termini da sommare. La sequenza riguarda questo procedimento: non la si trapianta nel Codice privacy o nel TUF.

'''+s[pos:]
s=s.replace('### Misure correttive, monitoraggio e ottemperanza amministrativa','### Misure correttive e adempimento del provvedimento')
pos=s.index('### Il controllo giurisdizionale: una tutela da mappare')
s=s[:pos]+'''Il controllo dell'adempimento da parte dell'Autorità non è il **giudizio di ottemperanza** degli artt. 112 e seguenti CPA. Quest'ultimo serve a dare attuazione a pronunce giurisdizionali e titoli previsti dalla legge, davanti al giudice competente. Se un'impresa disobbedisce a un ordine AGCM si applica il regime amministrativo dell'inottemperanza; se l'amministrazione non esegue una sentenza, può aprirsi il diverso problema dell'ottemperanza giudiziale.

'''+s[pos:]
old='Il Codice del processo amministrativo disciplina, fra l’altro, azioni, tutela cautelare, impugnazioni e ottemperanza.'
a=s.index("Il Codice del processo amministrativo disciplina, fra l'altro")
b=s.index('\n\n![Figura 6.5',a)
s=s[:a]+'''### Mappa compilata dei ricorsi al 3 ottobre 2026

La tabella riguarda i provvedimenti indicati, non qualsiasi lite che coinvolga l'ente. Il rito abbreviato dell'art. 119 CPA **non dimezza in primo grado il termine per notificare il ricorso introduttivo**: per l'azione di annullamento ordinaria resta il termine di 60 giorni dell'art. 29. Altri termini sono dimezzati secondo le eccezioni della disposizione; controversie sugli appalti, lavoro e altre azioni richiedono il proprio regime.

| Atto e perimetro | Giudice | Rito e termine introduttivo essenziale |
| --- | --- | --- |
| Provvedimenti AGCM e AGCOM devoluti al giudice amministrativo | TAR Lazio, Roma; CPA art. 135 | Art. 119; annullamento: notifica entro 60 giorni |
| Provvedimenti ARERA nell'esercizio dei suoi poteri | TAR Lombardia, Milano; CPA art. 14, comma 2 | Art. 119; annullamento: notifica entro 60 giorni |
| Provvedimenti autoritativi e sanzionatori ANAC e IVASS nel perimetro CPA | TAR Lazio, Roma; artt. 133 e 135 | Art. 119; annullamento: notifica entro 60 giorni, salvi specifici regimi di altra controversia |
| Sanzioni previste dal TUF, art. 195, comma 7, nel nuovo regime temporale descritto sotto | TAR Lombardia, Milano; giurisdizione esclusiva | Art. 119; annullamento: notifica entro 60 giorni; ricorso non sospensivo da solo |
| Sanzioni CONSOB/Banca d'Italia per disposizioni esterne al TUF che richiamano art. 195, nel regime del comma 8 | Corte d'appello della sede della società/ente; se criterio inapplicabile, luogo della violazione | Notifica all'Autorità entro 30 giorni dalla comunicazione, 60 per ricorrente all'estero; deposito entro 30 giorni dalla notifica |
| Sanzioni Banca d'Italia ex art. 145 TUB | Corte d'appello di Roma | Notifica entro 30 giorni dalla comunicazione, 60 all'estero; deposito entro 30 giorni dalla notifica |
| Provvedimenti Garante, art. 10 D.Lgs. 150/2011 | Tribunale ordinario: alternativamente sede/residenza del titolare o residenza dell'interessato | Rito del lavoro con regole speciali; ricorso entro 30 giorni dalla comunicazione, 60 per residente all'estero; sentenza non appellabile |

**La riforma TUF richiede una linea del tempo.** Il D.Lgs. 25 giugno 2026, n. 128, è entrato in vigore il **7 agosto 2026**. L'art. 10 differisce di nove mesi varie disposizioni procedimentali, ma esclude da quel differimento i commi 7–8 dell'art. 195 sul giudice. Il comma 4 collega le nuove disposizioni ai procedimenti sanzionatori avviati dopo la rispettiva data di applicazione, anche se riguardano fatti anteriori. Al 3 ottobre 2026 non è quindi corretto dire né «CONSOB sempre corte d'appello» né «ogni vecchio procedimento passa al TAR». Si annotano fonte della violazione, data di avvio, regime applicabile e data di comunicazione del provvedimento. Per i procedimenti anteriori si ricostruisce la disciplina precedente; gli altri istituti differiti non si anticipano.

**Sindacato e cautela.** Il giudice verifica fatti, diritto, ragionamento tecnico e proporzionalità nei limiti della domanda e del rito; l'art. 134, comma 1, lettera c), estende al merito la cognizione sulle sanzioni pecuniarie devolute al giudice amministrativo. Questa previsione non gli attribuisce tutte le sanzioni del sistema. Il ricorso non equivale da solo a sospensione dell'efficacia: occorre la misura cautelare secondo i presupposti della disciplina applicabile.''' +s[b:]
s=s.replace('Mappa della tutela senza termini non verificati','Mappa di atto, giudice, rito, decorrenza e termine').replace('Nel privacy,','Nella protezione dei dati,')
a=s.index("### Checklist per una nota d'ufficio")
s=s[:a]+'''## N-MF05-06-05 · Consolidamento e verifica

### ▣ Verifica ragionata

**Quesito 1.** AGCM rende obbligatori impegni idonei ex art. 14-ter. Ha necessariamente accertato l'infrazione e concesso uno sconto?

**Risposta corretta:** no. La decisione può chiudere senza accertamento; lo sconto legato al riconoscimento della responsabilità appartiene alla diversa transazione dell'art. 14-quater. Gli impegni restano vincolanti e controllabili.

**Quesito 2.** Il rito abbreviato contro una delibera ARERA riduce automaticamente a 30 giorni la notifica del ricorso introduttivo di annullamento?

**Risposta corretta:** no. L'art. 119 esclude dal dimezzamento quel termine in primo grado: resta 60 giorni. Il foro funzionale è TAR Lombardia, Milano. Non va confuso con il diverso rito degli appalti.

**Quesito 3.** Un provvedimento Garante è comunicato a un destinatario residente in Italia. La mappa corretta è TAR Lazio e 60 giorni?

**Risposta corretta:** no. Tribunale ordinario, rito del lavoro con regole speciali, ricorso entro 30 giorni dalla comunicazione; la competenza territoriale segue le alternative dell'art. 10 D.Lgs. 150/2011.

**Quesito 4.** Una sanzione TUF deriva da un procedimento avviato il 1° settembre 2026. Basta ricordare Corte cost. 162/2012 per scegliere la corte d'appello?

**Risposta corretta:** no. Per il procedimento nuovo si applica l'art. 195, comma 7, come riformato dal D.Lgs. 128/2026: TAR Lombardia, Milano, rito art. 119. Il controllo della data di avvio e della fonte distingue questo caso dai procedimenti anteriori e dalle violazioni esterne al TUF.

**Quesito 5.** Due autorità applicano sanzioni punitive alla stessa persona per gli stessi fatti; il diverso nome delle norme elimina il problema del ne bis in idem?

**Risposta corretta:** no. Occorre verificare identità materiale dei fatti, soggetto, natura delle misure e definitività, oltre alle condizioni rigorose di un eventuale cumulo previsto dal diritto applicabile. La diversità delle autorità non è una giustificazione sufficiente.

**Quesito 6.** Un'impresa non rispetta gli impegni AGCM. Il funzionario può chiamare il proprio controllo «giudizio di ottemperanza»?

**Risposta corretta:** no. Verifica l'adempimento e applica il procedimento di inottemperanza previsto dalla norma. Il giudizio di ottemperanza è una tutela giurisdizionale per dare esecuzione ai titoli contemplati dall'art. 112 CPA.

### Caso ragionato di chiusura

**Traccia.** Arrivano tre provvedimenti: sanzione AGCM antitrust; sanzione Banca d'Italia ex art. 145 TUB; sanzione CONSOB per violazione del TUF in procedimento avviato il 15 settembre 2026. Il destinatario, residente in Italia, propone per tutti «ricorso al TAR Lazio entro 30 giorni, con sospensione automatica». Correggi la nota.

**Soluzione.** AGCM: TAR Lazio, Roma, rito art. 119 e termine di notifica dell'annullamento di 60 giorni. TUB: corte d'appello di Roma, notifica entro 30 giorni dalla comunicazione e deposito entro 30 dalla notifica. TUF nel procedimento nuovo: TAR Lombardia, Milano, art. 195, comma 7, rito art. 119 e termine introduttivo di 60 giorni. In nessuno dei tre casi la mera proposizione del ricorso equivale alla sospensione: si verifica e, se giustificata, si chiede la tutela cautelare. Le date esatte di scadenza richiedono conoscenza delle comunicazioni e applicazione delle regole di computo; non si inventano dal nome dell'Autorità.

**Autovalutazione:** quattro punti, uno per ciascuna mappa corretta e uno per la distinzione fra ricorso e cautela. Per il TUF è necessario citare anche il criterio temporale della riforma.

**Riferimenti normativi e professionali.** L. 287/1990, artt. 14-ter e 14-quater; DPR 217/1998, art. 14; AGCM, delibera 30629/2023; CPA artt. 14, 29, 112, 119, 133–135; TUF artt. 187-septies e 195, coordinati con [D.Lgs. 128/2026](https://www.gazzettaufficiale.it/eli/id/2026/07/23/26G00145/sg), art. 10; TUB art. 145; D.Lgs. 150/2011 art. 10. Corte cost. 63/2019, 169/2023 e 73/2026; CGUE, bpost, C-117/20, 22 marzo 2022. Quadro e transitorio verificati il 3 ottobre 2026.
'''
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('source_refs: [','source_refs: ["sources/vol-05-sanzioni-giurisdizione-verifica-2026-10-03.md", "sources/vol-05-istruttoria-verifica-2026-10-03.md", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/vol-05-sanzioni-giurisdizione-verifica-2026-10-03.md", "wiki/topics/authority-rettifiche-2026.md", ',1)
p.write_text(s,encoding='utf8')
f=O/'VOL-05-progress.json';d=json.loads(f.read_text(encoding='utf8'));d['chaptersApplied']=[1,2,3,4,5,6];d['chaptersReadThisCycle']=[1,2,3,4,5,6];d['findingsFullyApplied']+=['V05-10','V05-11'];f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
f=O/'VOL-05-reading-checkpoint.json';d=json.loads(f.read_text(encoding='utf8'));d['files'][5]['readComplete']=True;f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
f=O/'norme-vol05/cpa-manifest.json';d=json.loads(f.read_text(encoding='utf8'))
for r in d:r['readComplete']=True;r['verifiedAt']='2026-10-03'
f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
print('Applied chapter 6; TUF 2026 transition and distinct jurisdictions documented.')
