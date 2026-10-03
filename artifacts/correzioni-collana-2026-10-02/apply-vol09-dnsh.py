from pathlib import Path
import importlib.util
s=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
u.BASE=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters');u.REF='sources/vol-09-dnsh-cam-casi-verificati-2026-10-03.md'
slug='12-dnsh-cam-procurement-sostenibile';t=u.read(slug)
t=t.replace('## N-TR02-12-01 · Obiettivo del capitolo','## N-TR02-12-01 · DNSH: obiettivi e regimi')
t=t.replace('## N-TR02-12-02 · Strumenti e applicazioni','## N-TR02-12-02 · CAM: obblighi minimi e criteri premianti')
t=t.replace('## N-TR02-12-04 · Controlli e casi','## N-TR02-12-04 · Fascicolo ambientale e non conformità')
t=t.replace('Le regole puntuali dipendono dalla misura, dal settore, dall\'oggetto del contratto e dai documenti ufficiali vigenti. Per questo il manuale lavora sul metodo: non fissa soglie mobili, non inventa requisiti tecnici e non sostituisce la verifica dei testi applicabili al caso concreto.','Le regole puntuali dipendono dalla misura, dal settore e dall’oggetto del contratto. Il capitolo sviluppa due applicazioni distinte: una fornitura di notebook per la verifica DNSH e una fornitura di arredi per i CAM. I criteri indicati riguardano questi oggetti; prima di riutilizzarli occorre verificarne la pertinenza alla nuova procedura.')
t=u.replace(t,'Per il RUP e per la stazione appaltante il DNSH entra almeno in quattro momenti.','''### Che cosa costituisce danno significativo

L’articolo 17 del regolamento (UE) 2020/852 specifica il contenuto del danno. Per la mitigazione rilevano emissioni significative di gas a effetto serra. Per l’adattamento rileva l’aumento degli effetti avversi del clima sull’attività, sulle persone, sulla natura o sui beni. Per le acque e le risorse marine rileva il pregiudizio allo stato o al potenziale dei corpi idrici e al buono stato delle acque marine.

Per l’economia circolare rilevano, fra l’altro, inefficienze significative nell’uso delle risorse e aumenti rilevanti di rifiuti, incenerimento o smaltimento, considerando gli effetti di lungo periodo. Per l’inquinamento si considera l’aumento significativo delle emissioni in aria, acqua e suolo. Per biodiversità ed ecosistemi si valuta il danno alla loro condizione, resilienza e conservazione, compresi habitat e specie.

L’analisi guarda al **ciclo di vita**: produzione, utilizzo e fine vita del prodotto o servizio. Un bene a basso consumo può quindi richiedere anche verifiche sui materiali e sulla gestione dei rifiuti. La sola riduzione della CO₂ non dimostra il rispetto di tutti e sei gli obiettivi. L’articolo 5, paragrafo 2, del regolamento RRF 2021/241 ammette il sostegno soltanto alle misure che rispettano il principio.

### Regime 1 e Regime 2

La Guida operativa RGS, terza edizione del 2024, distingue due regimi. Nel **Regime 1** l’intervento deve contribuire sostanzialmente all’obiettivo ambientale previsto e rispettare il DNSH rispetto agli altri obiettivi. Nel **Regime 2** deve rispettare il DNSH senza che gli sia attribuito quel contributo sostanziale. Regime 2 non significa assenza di controlli o tolleranza di danni significativi.

Il regime deriva dagli impegni della misura e dagli atti del Piano. Il soggetto attuatore non può scegliere quello meno impegnativo. La guida contiene mappature e schede tecniche; l’amministrazione titolare le applica e le adatta in coerenza con la misura e con la decisione di esecuzione del Consiglio. Le mappature aiutano a individuare le attività, ma non sostituiscono l’esame dell’intervento. La terza edizione considera anche contributi sostanziali relativi ad acque ed economia circolare: non bisogna identificare sempre il Regime 1 con la sola mitigazione climatica.

Se una misura non ha una scheda associata, non nasce un’esenzione automatica. Occorre considerare i sei obiettivi e motivare l’eventuale assenza di impatti rilevanti, secondo le indicazioni dell’amministrazione titolare. Anche una conclusione di non pertinenza deve avere un oggetto preciso: può riguardare una componente della fornitura senza estendersi ai lavori edilizi compresi nello stesso progetto.

Per il RUP e per la stazione appaltante il DNSH entra almeno in quattro momenti.''')
t=u.replace(t,'La parola "minimi" non deve trarre in inganno. Non significa che siano irrilevanti o facoltativi quando la disciplina li rende applicabili. Significa che individuano una base ambientale da considerare per quella categoria. La stazione appaltante deve verificare se per l\'oggetto esiste un CAM pertinente, quale versione è vigente e quali parti si applicano alla procedura concreta.','''L’articolo 57, comma 2, del d.lgs. 36/2023 impone di inserire nella documentazione progettuale e di gara **almeno le specifiche tecniche e le clausole contrattuali** dei CAM pertinenti. I decreti di categoria possono differenziare le prescrizioni in relazione al valore dell’appalto o della concessione. I criteri premianti sono inoltre tenuti in considerazione nella predisposizione dell’offerta economicamente più vantaggiosa richiamata dall’articolo 108, commi 4 e 5.

La distinzione produce una conseguenza: il requisito minimo non può essere reso facoltativo attribuendogli pochi punti. Prima si verifica la conformità alle prescrizioni obbligatorie; poi si valuta l’eventuale miglioramento secondo la griglia. Il punteggio non compensa la mancanza del minimo. La stazione appaltante individua categoria, decreto vigente, prescrizione e mezzo di prova, senza copiare una versione storica del CAM soltanto perché richiamata in una vecchia guida.''')
t=u.replace(t,'### ▣ Verifica 1','''### CAM arredi: una clausola completa sulla garanzia

Per la fornitura di arredi interni, il decreto 23 giugno 2022 n. 254, pubblicato nella Gazzetta Ufficiale n. 184 dell’8 agosto 2022, contiene un criterio verificabile: il punto **4.2.2** richiede una garanzia di almeno **cinque anni dall’acquisto** e la disponibilità dei pezzi di ricambio per almeno cinque anni.

La verifica richiede un documento scritto che precisi durata della garanzia, impegno relativo ai ricambi e contatti. Se i ricambi sono offerti gratuitamente, ciò deve risultare; se non lo sono, il costo deve essere stabilito preventivamente e rapportato al valore del prodotto. Non è corretto aggiungere al criterio una gratuità generalizzata che il testo non impone.

Una clausola didattica può quindi specificare: «Per gli arredi forniti è assicurata una garanzia di almeno cinque anni dall’acquisto. L’operatore consegna il documento di garanzia, l’impegno sulla disponibilità quinquennale dei ricambi, i contatti del servizio e le condizioni economiche dei ricambi previste dal criterio 4.2.2». La clausola va coordinata con gli altri criteri del decreto e con il contratto: da sola non esaurisce i CAM arredi.

Il punto **4.2.1** disciplina invece il ritiro degli imballaggi alla consegna per destinarli al riutilizzo o al riciclo. La prova comprende la dichiarazione sulla destinazione finale, i soggetti coinvolti e gli accordi sottoscritti. Se gli arredi non vengono disimballati subito, l’amministrazione organizza il successivo ritiro e i relativi costi secondo quanto previsto dal criterio. Nel verbale di consegna si registra quindi anche l’esito del ritiro o la gestione concordata del disimballaggio differito.

### Esercizio: minimo obbligatorio e premio

Il criterio **4.3.8** premia l’estensione della garanzia rispetto ai cinque anni minimi. Il CAM prevede frazioni del punteggio massimo: 0,25 per un anno aggiuntivo, 0,50 per due, 0,75 per tre e l’intero punteggio per almeno quattro anni aggiuntivi. Supponiamo che la gara assegni a questo criterio un massimo di **8 punti**; è una scelta dell’esempio, non un punteggio fisso imposto dal decreto.

| Garanzia totale offerta | Anni oltre il minimo | Punti dell’esempio |
|---|---|---|
| 5 anni | 0 | 0 |
| 6 anni | 1 | 2 |
| 7 anni | 2 | 4 |
| 8 anni | 3 | 6 |
| 9 anni o più | Almeno 4 | 8 |

Un concorrente offre tre anni, un altro sette. Il secondo, se rispetta anche le altre condizioni, ottiene 4 punti. Il primo non è semplicemente un’offerta da zero punti: propone una durata inferiore al minimo obbligatorio. Il suo difetto non si supera facendo modificare dopo la scadenza il contenuto sostanziale dell’offerta tecnica da tre a cinque anni. La questione va valutata alla luce degli atti e dei limiti dell’articolo 101 sul soccorso istruttorio, sviluppati nel capitolo 4.

### ▣ Verifica 1''')
anchor='## N-TR02-12-04 · Fascicolo ambientale e non conformità'
t=u.replace(t,anchor,'''### Caso DNSH: venti notebook nuovi

La misura del caso richiede di applicare la **scheda 3** della Guida operativa RGS a una fornitura di venti notebook nuovi. È un’ipotesi esplicita della traccia: non si sceglie la scheda perché il progetto contiene genericamente una componente digitale. Prima si confrontano misura, attività e prescrizioni dell’amministrazione titolare.

Per questa scheda la guida individua il Regime 2 anche quando l’investimento complessivo ricade in Regime 1. Il regime della singola attività va quindi letto nella scheda pertinente, senza cancellare gli altri impegni dell’investimento. Adattamento, acque e biodiversità risultano non pertinenti nel perimetro della scheda 3; questa conclusione non si estende automaticamente, per esempio, alla ristrutturazione dei locali che ospiteranno i computer.

Il controllo energetico può utilizzare un’etichetta ambientale di tipo I, conforme alla ISO 14024 e pertinente al requisito. La guida ammette anche le alternative previste, quali Energy Star o la prova del consumo energetico tipico Etec entro il massimo Etecmax determinato secondo i criteri GPP richiamati. Non esiste nel capitolo una soglia unica in kWh valida per ogni apparecchiatura: categoria e caratteristiche incidono sul calcolo.

Per la circolarità si verificano le evidenze pertinenti su durata, riparabilità e gestione a fine vita, compresi gli adempimenti RAEE applicabili ai soggetti coinvolti. Per l’inquinamento occorrono prove coerenti con le prescrizioni su sostanze e apparecchiature: REACH, RoHS e compatibilità elettromagnetica, secondo la scheda. Un marchio o una certificazione generica dell’impresa non provano automaticamente le caratteristiche del modello offerto.

Il fascicolo contiene la seguente scheda didattica. Non sostituisce la checklist ufficiale o le istruzioni della misura; rende visibili i collegamenti da costruire.

| Controllo | Evidenza identificata | Esito da registrare |
|---|---|---|
| Perimetro | Misura, prescrizione e scheda 3 | Attività e modelli a cui si applica |
| Energia | Prova ammessa riferita al modello A | Requisito coperto, versione e validità |
| Circolarità | Documenti su riparazione e fine vita | Prescrizioni coperte e lacune |
| Inquinamento | Dichiarazioni e prove pertinenti | Collegamento al prodotto e al requisito |
| Consegna | Elenco modelli e verbale | Corrispondenza ai beni verificati |

Prima dell’acquisto l’istruttoria ha verificato il modello A. Alla consegna arrivano diciotto A e due B. Il fornitore dichiara che B è «più recente e quindi più ecologico». Il controllo non può chiudersi positivamente per tutti e venti i beni sulla base della documentazione di A. Si registra la difformità, si verifica se la sostituzione è contrattualmente ammissibile e si acquisiscono le evidenze specifiche di B. Se non dimostrano la conformità o se la sostituzione non è ammessa, si attiva il rimedio previsto, compresa la sostituzione dei beni quando dovuta.

**Soluzione ragionata.** Il difetto non è il numero di documenti: è l’assenza del collegamento fra documento e bene effettivo. Il verbale identifica i due notebook, l’esito ancora aperto e l’azione richiesta. La chiusura registra la prova acquisita o la sostituzione effettuata. Le verifiche ex ante previste dalla scheda restano distinte da questo controllo contrattuale alla consegna: il secondo accerta che il bene fornito sia proprio quello valutato. Nessun esito viene retrodatato per far apparire conforme la consegna originaria.

'''+anchor)
t=u.replace(t,'| Requisito | Prova | Responsabile | Momento | Conseguenza |\n|---|---|---|---|---|\n| Che cosa chiedo? | Come lo dimostro? | Chi controlla? | Quando controllo? | Che cosa accade se manca? |','''| Prescrizione e prova | Verifica e seguito |
|---|---|
| Requisito: che cosa chiedo? | Responsabile: chi controlla? |
| Prova: come si dimostra? | Momento: quando si controlla? |
| Esito: quale evidenza è accettata? | Conseguenza: quale rimedio si attiva se manca? |''')
t=t.replace('DNSH significa non arrecare un danno rilevante agli obiettivi ambientali applicabili.','DNSH significa non arrecare danno significativo ai sei obiettivi, valutando gli impatti pertinenti al ciclo di vita.')
t+='''
### Riferimenti per i due casi

Regolamento (UE) 2020/852, art. 17; regolamento (UE) 2021/241, art. 5; Guida operativa RGS sul DNSH, terza edizione, circolare n. 22 del 14 maggio 2024, parte introduttiva e scheda 3; d.lgs. 36/2023, artt. 57, 101 e 108; decreto 23 giugno 2022 n. 254 sui CAM arredi, criteri 4.2.1, 4.2.2 e 4.3.8. Per un oggetto diverso, si ricercano il CAM e la scheda pertinenti: il criterio degli arredi non si trasferisce ai notebook e la scheda informatica non si applica agli arredi.
'''
u.save(slug,t,['V09-30','V09-31'],u.REF);u.record()
