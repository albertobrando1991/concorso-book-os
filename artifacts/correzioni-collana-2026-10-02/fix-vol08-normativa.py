from pathlib import Path
import re
B=Path('wiki/books/moduli/m-tr01-ict-trasformazione-digitale/chapters')
def patch(n,fn):
 p=next(B.glob(f'{n:02}-*.md'));s=p.read_text(encoding='utf8');p.write_text(fn(s),encoding='utf8')
def before(s,marker,extra):
 assert marker in s
 return s.replace(marker,extra.strip()+'\n\n'+marker,1)
def cloud(s):
 s=s.replace('Il quadro consolidato comprende il Regolamento unico adottato nel 2024 e il catalogo dei servizi qualificati.', 'Il riferimento è il Regolamento unico ACN adottato con decreto direttoriale 21007/24 del 27 giugno 2024, applicabile nel regime ordinario dal 1 agosto 2024. La qualificazione riguarda lo specifico servizio e il relativo livello, non ogni prodotto del fornitore; la validità e il mantenimento dei requisiti si controllano nel catalogo e nel provvedimento.')
 return before(s,'### Assessment','''### Impatto e classe: tre distinzioni

| Classe | Conseguenza della compromissione | Esempio didattico di valutazione |
| --- | --- | --- |
| Strategica | Impatto sulla sicurezza nazionale e sulle funzioni essenziali dello Stato | Sistema la cui indisponibilità compromette una funzione essenziale di sicurezza nazionale |
| Critica | Pregiudizio ai servizi rilevanti per società, salute, sicurezza e benessere economico/sociale | Servizio sanitario la cui interruzione impedisce prestazioni rilevanti |
| Ordinaria | Dati e servizi non ricadenti nei livelli precedenti secondo la valutazione d’impatto | Informazioni di consultazione con impatto limitato, senza dipendenze critiche nascoste |

Gli esempi non assegnano una classe automatica a tutti i sistemi di quel settore. Un portale informativo può dipendere da un servizio critico; un dato già pubblico può richiedere elevata integrità. La classificazione considera riservatezza, integrità, disponibilità e conseguenze, mentre la qualificazione dimostra requisiti dell’offerta cloud. Il responsabile censisce dati e servizi, motiva la classe, controlla la compatibilità della destinazione e conserva l’esito; una generica certificazione commerciale non sostituisce questi passaggi. La strategia, il regolamento e il catalogo svolgono funzioni diverse: il primo orienta, il secondo regola, il terzo permette di verificare l’offerta corrente.''')
patch(7,cloud)
def nis(s):
 marker='## N-TR01-09-06 · PA, ACN, CSIRT, NIS2 e privacy'
 a=s.index(marker);b=s.index('\n## ▣ Verifica',a)
 s=s[:a]+marker+'''

### Soggetti, governance e misure

Il d.lgs. 138/2024 recepisce NIS2. Il campo si verifica mediante articolo 3, settori degli allegati, dimensioni ed eccezioni: non basta che un’organizzazione usi un computer o sia pubblica. L’articolo 6 distingue **essenziali** e **importanti**. Fra gli essenziali rientrano, alle condizioni previste, grandi soggetti dell’allegato I, soggetti critici, determinati operatori digitali e le PA centrali dell’allegato III; gli altri soggetti nel campo che non sono essenziali sono importanti. L’individuazione ACN e la comunicazione di inserimento permettono di fissare gli adempimenti del soggetto. “Importante” non significa facoltativamente protetto.

Gli organi di amministrazione e direttivi approvano le modalità di attuazione delle misure, ne sovrintendono l’implementazione e rispondono delle violazioni nei termini dell’articolo 23. Seguono formazione cyber e promuovono quella del personale. La funzione tecnica realizza e documenta i controlli, ma non assorbe questa responsabilità. L’articolo 24 richiede misure tecniche, operative e organizzative proporzionate: analisi dei rischi, gestione degli incidenti, continuità e backup, fornitori, sviluppo e vulnerabilità, verifica dell’efficacia, igiene/formazione, crittografia, accessi e autenticazione quando appropriata. L’ente conserva decisioni, responsabili ed evidenze di efficacia, non soltanto acquisti di prodotti.

### Quando e come notificare

Per l’articolo 25 è significativo l’incidente che causa o può causare grave perturbazione operativa/perdite finanziarie, oppure ripercussioni considerevoli materiali o immateriali su altri. La valutazione applica le specifiche ACN pertinenti al soggetto e al servizio; un alert isolato non è automaticamente un incidente significativo. ACN è autorità nazionale competente; CSIRT Italia riceve le notifiche e svolge i compiti di risposta e supporto previsti.

| Passaggio ordinario NIS | Termine massimo e contenuto |
| --- | --- |
| Pre-notifica | Senza ingiustificato ritardo, entro 24 ore dalla conoscenza dell’incidente significativo; possibile origine malevola e impatto transfrontaliero |
| Notifica | Entro 72 ore dalla stessa conoscenza; prima valutazione di gravità/impatto e indicatori disponibili |
| Relazione intermedia | Su richiesta del CSIRT |
| Relazione finale | Entro un mese dalla notifica: descrizione, causa probabile, mitigazioni e impatto transfrontaliero noto |

Se l’incidente è ancora in corso, si trasmette una relazione mensile sui progressi e quella finale entro un mese dalla conclusione della gestione. Per i prestatori di servizi fiduciari interessati dal caso, la notifica ha il termine speciale di 24 ore. I massimi non autorizzano ritardi ingiustificati né si calcolano dalla fine dell’indagine. Informazioni incomplete si aggiornano secondo la procedura, invece di aspettare una ricostruzione perfetta.

### Decorrenze al 3 ottobre 2026

La determinazione ACN 379907/2025, applicabile dal 15 gennaio 2026, sostituisce la 164179/2025: allegati 1/2 per misure degli importanti/essenziali, 3/4 per incidenti significativi di base. La 127434/2026, applicabile dal 30 aprile, distingue le coorti.

| Coorte | Notifiche di base | Misure di base |
| --- | --- | --- |
| Inseriti nel 2025 e permanenti nel 2026 | Nove mesi dalla comunicazione di inserimento | Diciotto mesi dalla stessa comunicazione |
| Inseriti per la prima volta nel 2026 | Dal 1 gennaio 2027 | Entro 31 luglio 2027 |

Si conserva dunque la data della comunicazione: il reinserimento annuale non riavvia automaticamente i termini. Queste decorrenze non sospendono altri obblighi già applicabili, né cancellano le misure previgenti degli operatori per i quali il regime transitorio ne impone il mantenimento.

### Legge 90/2024 e protezione dei dati

La legge 90/2024, articolo 1 aggiornato anche dalla legge 132/2025, ha una platea e una tassonomia proprie: comprende, fra gli altri soggetti indicati, PA centrali, regioni, città metropolitane, comuni oltre 100.000 abitanti e capoluoghi di regione, ASL e determinati trasporti/società in house. Prevede segnalazione entro 24 ore e notifica completa entro 72 dalla medesima conoscenza dell’incidente, tramite le procedure ACN. Campo, esclusioni del comma 7 e coordinamento con NIS/altre discipline vanno verificati: non si sommano moduli indiscriminatamente perché due norme usano numeri uguali.

Un incidente cyber può compromettere un servizio senza dati personali; un data breach può derivare anche da un invio errato non ostile. Il GDPR richiede al titolare notifica al Garante senza ingiustificato ritardo e, ove possibile, entro 72 ore dalla conoscenza, salvo che sia improbabile un rischio per diritti e libertà; se il rischio è elevato, valuta la comunicazione agli interessati secondo l’articolo 34 e le sue eccezioni. Il responsabile del trattamento informa il titolare senza ingiustificato ritardo. I presupposti restano distinti e ogni violazione è documentata; il DPO informa e consiglia, mentre la decisione compete al titolare.

**Caso svolto.** Un ente già obbligato apprende lunedì alle 10 di un incidente NIS significativo. Senza attendere il massimo se può agire prima, pre-notifica entro martedì alle 10 e notifica entro giovedì alle 10; il mese della relazione finale decorre dalla notifica. Se emerge anche esfiltrazione di dati, il titolare attiva una valutazione GDPR distinta. Il coordinatore conserva timeline, fonti, decisioni, turni e sostituzioni; il ripristino è autorizzato dopo verifica di causa, privilegi e integrità, non solo perché il portale risponde.

''' + s[b:]
 return before(s,'## N-TR01-09-04', '''### Chiavi, impronte e fiducia

| Meccanismo | Chi conserva quale chiave | Proprietà ed esempio |
| --- | --- | --- |
| Cifratura simmetrica | Mittente e destinatario condividono un segreto | Protegge un archivio; chi ottiene la chiave può decifrare |
| Cifratura asimmetrica | Coppia pubblica/privata del destinatario | Si protegge per il destinatario con la pubblica; soltanto la privata consente il recupero previsto dallo schema |
| Firma crittografica | Il firmatario custodisce la privata; la pubblica verifica | Consente di verificare origine e integrità, non nasconde il documento |
| Hash | Nessuna chiave per l’hash ordinario | Impronta per confrontare integrità; non dimostra da sola l’identità dell’autore |

Nei protocolli reali si combinano meccanismi: la cifratura asimmetrica non è descritta come soluzione efficiente per ogni grande archivio. Le firme non sono una generica “cifratura con la chiave privata”: algoritmi, codifiche e verifiche seguono schemi specifici. Un MAC usa invece un segreto condiviso per autenticità/integrità e non permette di attribuire pubblicamente la firma a uno solo dei titolari del segreto.

Un hash crittografico deve rendere impraticabile ricavare una preimmagine, trovare una seconda preimmagine per un messaggio dato o costruire collisioni. Le collisioni esistono matematicamente perché l’output è finito; resistenza non significa unicità assoluta. Per le password, un hash veloce non basta: si usano funzioni dedicate con salt individuale e costo regolato, senza memorizzare la password reversibile. Il salt non è una password segreta e ostacola il riuso di tabelle precalcolate; non compensa password deboli o controlli di accesso assenti.

Un **certificato** associa una chiave pubblica a un’identità secondo una politica, con firma dell’emittente e periodo di validità. La PKI gestisce emissione, catena di fiducia, rinnovo e revoca. Il client TLS verifica catena, identità del server atteso, validità e condizioni applicabili, non soltanto la presenza di un certificato. TLS protegge il canale e negozia chiavi di sessione; non prova che ogni contenuto del sito sia corretto né autorizza l’utente sulle pratiche.

**Esempio.** L’ufficio firma un documento con la propria privata e il destinatario verifica con la pubblica associata al firmatario. Per inviare lo stesso documento riservatamente serve anche cifratura/canale protetto. Un attaccante che sostituisse documento e semplice digest potrebbe far coincidere i due: manca una fonte affidabile dell’impronta. Certificati e firme crittografiche vanno inoltre distinti dalla qualificazione giuridica delle firme elettroniche nel quadro eIDAS.''')
patch(9,nis)
def data(s):
 s=s.replace('formato aperto e leggibile meccanicamente quando pertinente, metadati, licenza o condizioni d\'uso, canale di accesso, aggiornamento e documentazione.', 'i tre requisiti cumulativi dell’articolo 1, lettera l-ter, CAD: una licenza o previsione normativa che permetta a chiunque l’uso anche commerciale in forma disaggregata; accessibilità con tecnologie ICT in formato aperto adatto all’elaborazione automatica e con metadati; gratuità o costi marginali di riproduzione/divulgazione, salvo la disciplina dell’articolo 7 del d.lgs. 36/2006. Si aggiungono aggiornamento e documentazione necessari a usare correttamente la risorsa.')
 s=s.replace('requisiti che possono includere leggibilità meccanica, API e download massivo.', 'formati leggibili meccanicamente e disponibilità tramite API, oltre al download massivo dove indicato nell’allegato. Si pubblicano termini d’uso, criteri di qualità e documentazione delle API e un contatto; i metadati identificano il dataset come HVD. Le condizioni di riuso seguono CC0, CC BY 4.0 o licenza equivalente/meno restrittiva secondo l’allegato, con il regime di gratuità ed eventuali deroghe applicabili.')
 s=s.replace('Per contratti API, ruoli di erogatore e fruitore, procedure di adesione e dettagli di piattaforma il rinvio è', 'Per contratti API, ruoli di erogatore e fruitore e il percorso concettuale di adesione/fruizione il rinvio è')
 return s
patch(10,data)
patch(6,lambda s:before(s,'## ▣ Verifica', '''### PDND: dall’adesione alla chiamata autorizzata

L’ente aderisce alla PDND sottoscrivendo l’accordo e assegna i ruoli abilitati. L’erogatore pubblica nel catalogo l’e-service con contratto, versione, attributi richiesti e condizioni. Il fruitore presenta la richiesta di fruizione, dimostra gli attributi pertinenti e dichiara finalità e analisi del rischio richieste; l’erogatore valuta/abilita secondo le condizioni del servizio. Si configurano client e chiavi e si ottiene il voucher da usare nella chiamata all’API dell’erogatore. Quest’ultimo verifica voucher e autorizzazioni: la piattaforma abilita uno scambio controllato, non rende pubblici tutti i dati né crea da sola la base giuridica.

**Esempio.** Un ufficio deve verificare un solo requisito per una pratica. Specifica finalità, attributi minimi e soggetto autorizzato, invece di richiedere l’intero archivio. Prova risposta positiva, requisito assente, voucher non valido ed e-service indisponibile; registra correlazione ed esito senza riversare il contenuto personale nei log. Revoca della fruizione, cambio di versione e variazione della finalità richiedono un riesame. Le schermate correnti sono nella documentazione PagoPA; il flusso appena descritto permette di comprenderle senza dipendere da un pulsante o nome di menu.'''))
print('Cloud, NIS, crittografia, open data e PDND integrati.')
