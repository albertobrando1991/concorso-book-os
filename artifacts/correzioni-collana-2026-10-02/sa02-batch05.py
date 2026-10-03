from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-sa02-professioni-sanitarie');S=Path('wiki/sources')
p=S/'tpall-sicurezza-ambiente-vigilanza-sanzioni.md';s=p.read_text(encoding='utf-8');s+='''
## Riscontri puntuali per le correzioni del 3 ottobre 2026

Gli HTML Normattiva del lotto iniziale contengono l'indice e il primo articolo: non sono prova di lettura dell'atto intero. Per i nuclei aggiunti sono stati consultati gli articoli e i riscontri ufficiali seguenti.

- L. 689/1981, artt. 14, 16–18: contestazione immediata ove possibile; notifica ordinaria entro 90 giorni ai residenti in Italia e 360 all'estero dall'accertamento; pagamento ridotto entro 60 giorni; scritti e richiesta di audizione entro 30 giorni; rapporto e ordinanza motivata o archiviazione. [Testo ufficiale riprodotto dalla CCIAA Marche](https://www.marche.camcom.it/tutela-impresa-e-consumatore/sanzioni-amministrative/legge-24-novembre-1981-n-689.pdf), versione 2020, confrontata con l'indice temporale Normattiva acquisito: gli artt. 14, 17 e 18 risultano originari. Per l'art. 16 resta il criterio nazionale generale, fatte salve deroghe settoriali.
- D.Lgs. 758/1994, artt. 20–24, riprodotti nelle note al [D.Lgs. 81/2008 in GU](https://www.gazzettaufficiale.it/eli/gu/2008/04/30/101/so/108/sg/pdf): verifica entro 60 giorni dalla scadenza della prescrizione, pagamento entro 30 giorni di un quarto del massimo dell'ammenda dopo adempimento; comunicazioni al PM e condizioni per l'estinzione. L'indice Normattiva acquisito non indica modifiche degli artt. 20–24.
- D.Lgs. 152/2006, parte VI-bis: [Arpae, quadro aggiornato settembre 2026](https://www.arpae.it/it/attivita-e-servizi/vigilanza-e-controllo/asseverazioni/prescizioni-e-asseverazioni) conferma ambito contravvenzionale e assenza di danno o pericolo concreto e attuale, asseverazione tecnica e adempimento. [Pagamento e oneri](https://www.arpae.it/it/attivita-e-servizi/vigilanza-e-controllo/asseverazioni/asseverazioni-pagamenti-sanzioni-importi-dm-2025): 30 giorni e quarto del massimo, oltre agli oneri di prescrizione/asseverazione del D.M. 8 ottobre 2025, pubblicato nella [GU del 16 febbraio 2026](https://www.gazzettaufficiale.it/eli/gu/2026/02/16/38/sg/pdf). Non estendere ai delitti o a tutte le violazioni sui rifiuti.
- D.Lgs. 27/2021, artt. 7–8: [atto in GU](https://www.gazzettaufficiale.it/eli/id/2021/03/11/21G00034/sg), coordinato con [L. 71/2021, allegato, art. 1-bis](https://www.gazzettaufficiale.it/eli/id/2021/05/22/21G00081/sg): soppressa l'esclusione dell'art. 223 D.Lgs. 271/1989. Controperizia documentale richiesta entro 15 giorni, controversia documentale entro 30 dalla comunicazione dell'esito sfavorevole; ulteriore fase analitica distinta. Le garanzie processuali non sono cancellate dalle due procedure.
- D.Lgs. 81/2008, artt. 17, 28–29: [Ministero del lavoro, obblighi del datore](https://www.lavoro.gov.it/sportello-unico-digitale/salute-e-sicurezza-sul-luogo-di-lavoro/obblighi-del-datore-di-lavoro), valutazione/DVR e nomina RSPP non delegabili. Collaborazione con RSPP e medico competente nei casi previsti, previa consultazione RLS.
- D.P.R. 59/2013: [testo ufficiale Ministero del lavoro](https://www.lavoro.gov.it/documenti-e-norme/normative/Documents/2013/Decreto_del_Presidente_della_Repubblica_13_marzo_2013_n59), AUA e rapporto con AIA. Regolamenti CE 178/2002, artt. 18–19, e 852/2004, art. 5: rintracciabilità, ritiro/richiamo, procedure basate sui principi HACCP, da leggere nel corpus sui controlli ufficiali collegato.

Gli esempi compilati sono originali e dichiaratamente didattici. Non attestano un'ispezione reale né una sanzione accertata.
''';p.write_text(s,encoding='utf-8')
p=B/'chapters/09-controlli-tpall-verbalizzazione-campionamento-sanzioni.md';s=p.read_text(encoding='utf-8')
s=s.replace('Termini, pagamento in misura ridotta, autorità competente e modalità dipendono dalla fattispecie e dalla disciplina vigente. Non vanno inventati quando la traccia non indica la norma violata.', '''Lo schema generale della L. 689/1981, salvo regole speciali, è il seguente.

| Fase | Regola generale | Punto da controllare |
| --- | --- | --- |
| Contestazione/notifica, art. 14 | contestazione immediata ove possibile; altrimenti notifica entro 90 giorni ai residenti in Italia, 360 all'estero, dall'accertamento | accertamento e commissione del fatto non coincidono necessariamente |
| Pagamento ridotto, art. 16 | entro 60 giorni dalla contestazione o notifica; un terzo del massimo oppure, se previsto e più favorevole, doppio del minimo, oltre alle spese | ammissibilità e deroghe settoriali |
| Difese, art. 18 | entro 30 giorni dalla contestazione/notifica, scritti, documenti e richiesta di audizione | autorità destinataria competente |
| Rapporto, art. 17 | se non è effettuato il pagamento ridotto, trasmissione del rapporto con prova della contestazione/notifica | distinto dalla notizia di reato |
| Decisione, art. 18 | esame degli atti e delle difese, audizione se richiesta; ordinanza-ingiunzione motivata o archiviazione | distinto dal verbale di accertamento |

**Esempio aritmetico.** Una fattispecie didattica ammette il pagamento ridotto e prevede da 300 a 1.200 euro: un terzo del massimo è 400, il doppio del minimo è 600. La misura più favorevole è 400 euro, oltre alle spese. Il calcolo non dimostra da solo che l'art. 16 sia applicabile al caso: occorre prima verificare la disciplina speciale.''')
s=s.replace('### Funzioni di polizia giudiziaria e notizia di reato','''### Dalla prescrizione all'estinzione: confronto dei regimi

Nel D.Lgs. 758/1994 l'organo di vigilanza impartisce una prescrizione per eliminare la contravvenzione e fissa il tempo tecnicamente necessario. Resta l'obbligo di riferire la notizia di reato al pubblico ministero. Entro 60 giorni dalla scadenza verifica l'adempimento: se positivo, ammette al pagamento, entro 30 giorni, di un quarto del massimo dell'ammenda. Adempimento e pagamento nei termini fondano l'estinzione; il pagamento isolato non sana l'omessa regolarizzazione. Il procedimento penale segue la disciplina di sospensione e le comunicazioni previste dagli artt. 21–24; l'organo di vigilanza non emette una sentenza di assoluzione.

La parte VI-bis del D.Lgs. 152/2006 riguarda invece determinate **contravvenzioni ambientali**, in assenza di danno o pericolo concreto e attuale di danno alle risorse protette. Non è applicabile ai delitti ambientali e non basta che il responsabile dichiari di avere riparato. La prescrizione richiede asseverazione tecnica dell'ente specializzato; seguono verifica entro 60 giorni dalla scadenza e, in caso di adempimento, ammissione al pagamento entro 30 giorni di un quarto del massimo dell'ammenda, con gli ulteriori oneri previsti per prescrizione e asseverazione. Il D.M. 8 ottobre 2025, pubblicato il 16 febbraio 2026, disciplina questi oneri e i versamenti.

| Elemento | Sicurezza del lavoro | Ambiente |
| --- | --- | --- |
| Fonte | D.Lgs. 758/1994 e raccordo art. 301 D.Lgs. 81/2008 | D.Lgs. 152/2006, parte VI-bis |
| Primo controllo | contravvenzione compresa nell'ambito applicabile | natura contravvenzionale, pena e condizioni dell'art. 318-bis |
| Prescrizione | organo di vigilanza, termine tecnicamente necessario | prescrizione con asseverazione tecnica |
| Esito favorevole ordinario | adempimento e pagamento nei termini | adempimento e pagamento nei termini, inclusi oneri applicabili |
| Errore | considerarla una multa amministrativa ordinaria | estenderla a qualsiasi danno ambientale o delitto |

### Funzioni di polizia giudiziaria e notizia di reato''')
s=s.replace('L\'**autorizzazione unica ambientale (AUA)** ha presupposti e campo propri. AIA e AUA non sono sinonimi.', '''L'**autorizzazione unica ambientale (AUA)**, regolata dal D.P.R. 59/2013, riunisce i titoli ambientali indicati dal regolamento per le imprese e gli impianti nel suo ambito, non soggetti ad AIA. La domanda passa dal SUAP; l'autorità competente adotta il provvedimento secondo il riparto applicabile. Non sostituisce qualsiasi autorizzazione né trasforma un impianto AIA in impianto AUA. L'AIA, disciplinata dalla parte II del D.Lgs. 152/2006, considera in modo integrato gli impatti dell'installazione e le migliori tecniche disponibili (BAT). I BAT-AEL sono livelli di emissione associati alle BAT nelle condizioni indicate: non vanno scambiati con un limite numerico universale per qualunque impianto. AIA e AUA non sono sinonimi.''')
anchor='## Verbale, rapporto e non conformità'
block='''## Sicurezza del lavoro e sicurezza alimentare

Nel luogo di lavoro il **DVR** rende documentata la valutazione dei rischi. Il datore di lavoro non può delegare tale valutazione e la conseguente elaborazione del documento, né la designazione del RSPP. RSPP e medico competente, nei casi previsti, collaborano; il RLS è consultato, non sostituisce il datore nella valutazione. Dirigenti e preposti hanno obblighi propri legati alle rispettive funzioni. In un sopralluogo non basta trovare un fascicolo intitolato DVR: si confrontano mansioni, rischi reali, misure, formazione, sorveglianza sanitaria e aggiornamento.

Nel settore alimentare l'operatore è responsabile delle procedure basate sui principi **HACCP**: analisi dei pericoli, punti critici, limiti, monitoraggio, azioni correttive, verifica e registrazioni proporzionate. Il controllo ufficiale verifica il sistema e le evidenze, non redige al posto dell'operatore il suo autocontrollo. La **rintracciabilità** permette di risalire ai fornitori e individuare i destinatari professionali; il **ritiro** rimuove dalla filiera un prodotto non sicuro, mentre il **richiamo** raggiunge anche il consumatore quando necessario. Il semplice ritrovamento di una scheda incompleta non dimostra automaticamente un alimento pericoloso, ma impone di valutarne rilevanza e conseguenze.

### Controperizia e controversia

Per i controlli ufficiali nel campo del D.Lgs. 27/2021, la controperizia dell'art. 7 consente all'operatore, a proprie spese, un esame documentale da parte di un esperto qualificato; la richiesta va presentata entro 15 giorni dalla comunicazione dell'esito sfavorevole. Può comprendere l'analisi dell'aliquota disponibile presso un laboratorio accreditato di fiducia. Se dopo la controperizia permane il dissenso, l'art. 8 prevede la controversia documentale davanti all'ISS, da attivare entro 30 giorni dalla comunicazione dell'esito sfavorevole; l'eventuale fase analitica ha istanza e termine distinti, decorrenti dalla valutazione documentale ISS.

Non sono sinonimi di una generica «seconda analisi». Aliquote, riproducibilità, deperibilità e motivazione delle eventuali limitazioni vanno considerate fin dal campionamento. La L. 71/2021 ha rimosso le disposizioni che escludevano le garanzie dell'art. 223 D.Lgs. 271/1989: non si deve quindi affermare che controperizia e controversia cancellino ogni garanzia processuale. Le misure urgenti per contenere il rischio sanitario restano possibili.

'''
s=s.replace(anchor,block+anchor)
s=s.replace('### Verbale, rapporto di prova e rapporto ispettivo','''### Estratto di verbale compilato: esempio didattico

**Verbale n. 12/2026 — dati interamente fittizi.** Il 3 ottobre 2026, dalle 9:15 alle 10:10, presso il laboratorio alimentare Alfa, gli operatori del servizio competente Rossi e Bianchi, alla presenza della responsabile Verdi, verificano registrazioni di autocontrollo e rintracciabilità del lotto L0310.

**Fatti osservati.** Il registro delle temperature del frigorifero F2 non presenta annotazioni per il turno precedente. La procedura aziendale HACCP, revisione 3, prevede una rilevazione a ogni turno. Sono acquisiti copia della pagina del registro (allegato A), procedura pertinente (B) e documento di ingresso del lotto (C). Non sono state eseguite analisi né accertate temperature retrospettive.

**Dichiarazione attribuita.** La responsabile riferisce che «il controllo è stato fatto, ma non registrato». La dichiarazione è distinta dal fatto verificabile: l'assenza della registrazione. Non dimostra quale fosse la temperatura del prodotto.

**Valutazione e seguito.** È rilevato uno scostamento documentale dalla procedura; il servizio valuta rischio, altri dati disponibili e disciplina applicabile prima di qualificare l'illecito o disporre misure. Sono richiesti i registri digitali eventualmente disponibili e il collegamento del lotto ai destinatari. Il verbale è letto, sottoscritto e consegnato secondo le modalità del servizio. Questo estratto non contiene una sanzione presunta né un esito analitico inventato.

### Verbale, rapporto di prova e rapporto ispettivo''')
p.write_text(s,encoding='utf-8')
p=B/'chapters/10-prova-pratica-casi-professionali.md';s=p.read_text(encoding='utf-8');anchor='## Costruire una risposta orale efficace'
block='''## Cinque casi completi: dall'obiettivo alla verifica

I dati seguenti sono simulati. Ciascun caso richiede una decisione professionale motivata e un esito controllabile; non basta scrivere «avviso il referente».

### Infermiere: recuperare autonomia nell'igiene

**Traccia.** Una persona clinicamente stabile dopo un ictus comprende le istruzioni, muove l'arto superiore destro e richiede aiuto per igiene e vestizione. Il piano segnala deficit motorio a sinistra, rischio di caduta e necessità di assistenza nei trasferimenti. Riferisce imbarazzo quando viene aiutata. Imposta l'assistenza mattutina.

**Soluzione.** Distinguo la diagnosi medica dal bisogno infermieristico: deficit nella cura di sé, con risorse residue e rischio di perdita di autonomia. Concordo un obiettivo osservabile: eseguire personalmente le parti dell'igiene raggiungibili in sicurezza e scegliere l'abbigliamento. Preparo ambiente, privacy e materiali accessibili; verifico dolore e tolleranza, assisto nelle attività non sicure, proteggo la cute e coinvolgo l'OSS con indicazioni coerenti con piano e competenze. Evito di sostituirmi in tutto alla persona soltanto per finire prima. Registro attività svolte autonomamente, aiuto necessario, integrità cutanea e risposta emotiva. Alla rivalutazione confronto questi dati con il giorno precedente e adeguo il piano con l'équipe.

### OSS: una sequenza sicura di assistenza quotidiana

**Traccia.** Il piano assistenziale prevede igiene al lavabo con una persona vigile, collaborante, che può stare seduta e necessita di aiuto nei trasferimenti. Gli ausili prescritti sono disponibili e verificati. Descrivi l'intervento e la consegna.

**Soluzione.** Confermo identità, consegna e collaborazione; spiego l'attività e tutelo riservatezza. Preparo materiali, ambiente e ausili, eseguo igiene delle mani e uso i dispositivi necessari al rischio. Collaboro al trasferimento con personale e tecnica previsti, senza improvvisare sollevamenti. Lascio svolgere alla persona ciò che riesce a fare, aiuto nelle parti indicate e osservo cute, dolore e affaticamento. Al termine assicuro comfort, abbigliamento, campanello e sistemazione dell'ambiente. Riferisco, per esempio, «igiene del viso eseguita autonomamente; comparso arrossamento persistente al tallone sinistro, segnalato all'infermiere», senza diagnosticare una lesione. L'esito si valuta su partecipazione, comfort e assenza di eventi avversi, non sul solo completamento del compito.

### Ostetrica: dimissione dopo puerperio fisiologico

**Traccia.** Donna al secondo giorno dopo parto vaginale non complicato, condizioni stabili, neonato seguito nel percorso ordinario. Chiede quali cambiamenti osservare a domicilio e come organizzare il sostegno.

**Soluzione.** Rivaluto benessere, dolore, perdite, eliminazione, riposo, vissuto emotivo e avvio dell'allattamento secondo il percorso. Concordo un piano di continuità con recapiti e contatti previsti. Spiego che sanguinamento improvviso abbondante, dispnea, dolore toracico, convulsioni o rapido peggioramento richiedono soccorso urgente; febbre associata a malessere, dolore crescente, cefalea intensa o disturbi visivi richiedono tempestiva valutazione. Non presento una perdita normale come garanzia che non possano comparire complicanze. Verifico la comprensione chiedendo alla donna di descrivere come agirebbe in due scenari e chi può aiutarla. Documento bisogni, informazioni condivise, contatto successivo e criticità ancora aperte. Il neonato conserva il proprio percorso di valutazione e sorveglianza.

### Fisioterapista: obiettivo funzionale e misura dell'esito

**Traccia.** Persona stabile in riabilitazione dopo ricovero, con indicazioni mediche disponibili e nessun nuovo allarme. Cammina per 20 metri con ausilio e supervisione; desidera raggiungere il bagno, distante 12 metri, in sicurezza. Definisci un piano breve.

**Soluzione.** Valuto trasferimenti, equilibrio, forza, tolleranza e barriere ambientali; verifico ausilio, precauzioni e bisogni della persona. L'obiettivo condiviso è completare il percorso letto-bagno nelle condizioni concordate, riducendo l'aiuto quando possibile. Programmo attività graduate e pertinenti: passaggi posturali, cammino sul percorso reale o simulato e gestione dell'ausilio, con dose individualizzata e criteri di interruzione. Non deduco l'autonomia dal solo fatto che 20 sia maggiore di 12: svolte, alzata, soglie e affaticamento possono cambiare il compito. Registro distanza, tipo di aiuto, pause, sintomi e qualità del movimento. Rivaluto con la stessa modalità e raccordo il risultato con équipe e caregiver.

### TPALL: dalla verifica documentale alla conclusione motivata

**Traccia.** Nel controllo AIA il punto E2 è stato identificato senza ambiguità, l'accesso è sicuro e la prescrizione richiede una misura annuale. Il gestore produce il rapporto relativo all'anno precedente e nessuna evidenza dell'anno corrente, il cui termine è già scaduto. Non sono disponibili misure per affermare un superamento emissivo.

**Soluzione.** Acquisisco autorizzazione, prescrizione, termine e documenti prodotti; verifico eventuali modifiche o proroghe. Distinguo mancata dimostrazione dell'autocontrollo da superamento del limite: solo la prima è sostenuta dai dati. Registro richieste, risposte e allegati e completo gli accertamenti necessari. L'autorità competente qualifica la violazione della prescrizione alla luce della norma applicabile e dispone il seguito; un eventuale campionamento ufficiale risponde a un quesito distinto. La verifica finale accerta l'esecuzione degli adempimenti richiesti e l'esito del procedimento, senza trasformare una nuova misura conforme nella prova che l'obbligo passato fosse stato rispettato.

''';s=s.replace(anchor,block+anchor);p.write_text(s,encoding='utf-8')
for p in [S/'tpall-sicurezza-ambiente-vigilanza-sanzioni.md',*list((B/'chapters').glob('09-*')),*list((B/'chapters').glob('10-*'))]:
 s=p.read_text(encoding='utf-8');s=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',s,flags=re.M);s=re.sub(r'^review_required:.*$','review_required: true',s,flags=re.M);s=re.sub(r'^draft_stage:.*$','draft_stage: revision-in-progress',s,flags=re.M);p.write_text(s,encoding='utf-8')
batch={}
for n,desc,ch in [(25,'Esposte fasi e termini L689, prescrizione D758 e parte VI-bis ambientale con differenze, condizioni e oneri vigenti.',9),(26,'Integrati AIA/AUA, DVR e ruoli, HACCP/rintracciabilità, controperizia/controversia e verbale compilato originale.',9),(27,'Aggiunti cinque casi completi specifici per infermiere, OSS, ostetrica, fisioterapista e TPALL, con obiettivi, decisioni e verifica.',10)]:
 batch[f'V07-{n:02}']={'change':desc,'files':[next((B/'chapters').glob(f'{ch:02}-*')).as_posix(),(S/'tpall-sicurezza-ambiente-vigilanza-sanzioni.md').as_posix()] if ch==9 else [next((B/'chapters').glob('10-*')).as_posix()],'evidence':'Rilettura del delta, riscontri ufficiali consolidati e risoluzione dei casi. Step 15 e PDF pendenti.','status':'applicato'}
Path('artifacts/correzioni-collana-2026-10-02/VOL-07-batch05.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf-8')
