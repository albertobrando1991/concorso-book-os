from pathlib import Path
import re,shutil
p=next(Path('wiki/books/moduli/m-sp03-magistratura-avvocatura-notariato/chapters').glob('04-*.md'));a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-sp03-04.md');assert not a.exists();shutil.copyfile(p,a);t=p.read_text(encoding='utf8')
t=t.replace('Prima della domanda | Pratica','Alla scadenza della domanda | Pratica')
t=t.replace('“Se la pratica è compiuta entro la domanda,','“Se la pratica è compiuta entro la scadenza della domanda,')
t=t.replace('Nel bando studiato la pratica deve essere già compiuta al momento della domanda e deve essere dichiarata.','Nel bando studiato la pratica deve essere compiuta entro la scadenza per la domanda. Un invio anticipato non anticipa il termine sostanziale: la dichiarazione deve indicare correttamente il periodo e il compimento entro quel termine, secondo il modulo.')
t=t.replace('concorsi notarili banditi dopo il 2009','concorsi notarili banditi dopo l’entrata in vigore della legge 69/2009')
t=t.replace('concorsi banditi dopo il 2009','concorsi banditi dopo l’entrata in vigore della legge 69/2009')
t=t.replace('espulsione durante le prove scritte','espulsione dopo la dettatura del tema durante le prove scritte')
t=t.replace('espulsione durante gli scritti','espulsione dopo la dettatura del tema durante gli scritti')
t=t.replace('Espulsione durante gli scritti','Espulsione dopo la dettatura del tema durante gli scritti')
t=t.replace('Il riferimento ai concorsi banditi dopo il 2009','Il riferimento ai concorsi banditi dopo l’entrata in vigore della legge 69/2009')
start=t.index('**Scenario.** Marta');end=t.index('## N-SP03-09-01',start)
t=t[:start]+'''**Caso A — prima candidatura.** Marta si iscrive nel registro dei praticanti il 1 luglio 2024 durante l’ultimo anno universitario, nel regime che consente il periodo anticipato; consegue la laurea il 20 dicembre 2024. La pratica prosegue senza interruzioni fino al 30 gennaio 2026. Non ha partecipato a precedenti concorsi notarili e non invoca riduzioni. Considera acquisita nel caso la regolarità dei periodi certificabili dal Consiglio notarile.

**Consegna.** Verifica separatamente durata totale, periodo anticipato, anno continuativo dopo la laurea, limite di completamento e momento del certificato.

**Soluzione.** Alla scadenza indicata dalla scheda ministeriale, 30 gennaio 2026 ore 12.00, sono trascorsi più di diciotto mesi dall’iscrizione. Il periodo prima della laurea è inferiore a sei mesi; quello successivo supera un anno ed è continuo. La pratica è terminata entro trenta mesi dall’iscrizione. I dati soddisfano quindi le condizioni temporali ordinarie considerate. Marta dichiara periodo e Consiglio nella domanda; il certificato non è richiesto come allegato iniziale, ma dopo il superamento dell’orale, entro trenta giorni dalla notifica della richiesta prevista dagli artt. 10 e 11 del bando. Questo esito riguarda i requisiti esaminati: gli altri requisiti vanno comunque controllati.

**Variante — invio anticipato.** Luca, senza riduzioni, si laurea e inizia regolare pratica il 20 luglio 2024. La compie senza interruzioni il 20 gennaio 2026. Prepara la domanda il 10 gennaio: non deve scrivere di aver già completato diciotto mesi quel giorno. Il termine sostanziale resta però la scadenza della candidatura, non il giorno scelto per l’invio. Deve rappresentare correttamente le date secondo il modulo e verificare l’effettivo compimento entro il termine; un certificato rilasciato più tardi non può sanare una pratica terminata dopo la scadenza.

**Caso B — precedenti esiti.** Andrea ha completato regolarmente la pratica nel 2012. Alla pubblicazione del bando del 30 dicembre 2025 risultano documentati, in cinque distinte procedure bandite dopo l’entrata in vigore della legge 69/2009: tre dichiarazioni di non idoneità, un’espulsione dopo la dettatura del tema e l’annullamento di una prova. Tutti gli esiti sono già intervenuti alla data di pubblicazione.

**Soluzione.** L’art. 2, comma 2, e l’art. 4, comma 2, del bando impongono di computare i cinque esiti, comprese le fattispecie equiparate. Andrea è escluso per questo limite. Pratica regolare, età o migliore preparazione non neutralizzano il vincolo. La data da usare per questo controllo è la pubblicazione del bando; per la pratica, invece, rileva la scadenza della candidatura. Distinguere i due candidati evita di attribuire cinque precedenti concorsi a chi ha appena completato il percorso iniziale.

**Applicazione alla prova.** Marta si allena su tre consegne: disposizioni mortis causa, trasferimento fra privati e operazione societaria. Non sceglie la materia più gradita: applica rispettivamente il protocollo testamentario, quello dell’atto tra vivi civile e quello commerciale, svolgendo anche i principi collegati. L’idoneità documentale permette di concorrere; non dimostra ancora la capacità di redigere.

**Materiali.** Per la tornata studiata i testi sono consegnati durante l’identificazione, prima degli scritti, per il controllo della commissione; non sono accettati nuovi testi nei giorni delle prove. Codici non commentati e fotocopie della Gazzetta contenenti norme rientrano nelle categorie previste, ma devono rispettare tutte le condizioni dell’art. 7. Per una nuova tornata Marta legge nuovamente bando e avvisi. La biblioteca di studio non coincide automaticamente con i materiali d’aula.

''' +t[end:]
t=t.replace('Il bando esclude chi sia stato dichiarato non idoneo in cinque precedenti concorsi notarili', 'Il bando esclude chi, alla data della sua pubblicazione, sia stato dichiarato non idoneo in cinque precedenti concorsi notarili')
t=t.replace('Esempio: un candidato dice di avere quattro “bocciature”.','Esempio: un candidato ricorda cinque partecipazioni e parla genericamente di “bocciature”.')
t=t.replace('Solo dopo può sapere se il limite è raggiunto.','Se i tre giudizi di non idoneità e l’annullamento rientrano nel periodo indicato dal bando, sono quattro esiti computabili; la mera mancata consegna, senza un distinto provvedimento equiparato, non aggiunge automaticamente il quinto. La ricostruzione va conclusa sugli atti, non sul numero di iscrizioni.')
t=t.replace('Le soglie verificate sono trentacinque punti per ciascuna prova scritta e trentacinque punti per ciascun gruppo orale, con idoneità complessiva non inferiore a 210 punti su 300.','Il giudizio di idoneità agli scritti comporta almeno 35 punti per ciascun elaborato; occorrono poi almeno 35 punti per ciascun gruppo orale e non meno di 210 punti su 300 nel complesso. L’art. 8 prevede inoltre due punti aggiuntivi per ciascuna precedente idoneità, per chi abbia conseguito tutti i minimi. Esempio senza incrementi: 38 + 37 + 40 negli scritti e 36 + 35 + 37 all’orale danno 223; i sei minimi sono rispettati. Un voto orale di 34 impedisce il superamento, anche se la somma supera 210. Preferenze a parità di merito e incrementi per precedenti idoneità hanno funzioni diverse e non vanno confusi.')
t=t.replace('Decreto ministeriale 16 dicembre 2025','Decreto dirigenziale 16 dicembre 2025')
p.write_text(t,encoding='utf8')
s=Path('wiki/sources/bandi-magistratura-avvocatura-notariato-m-sp03.md');x=s.read_text(encoding='utf8');x+='''

### Riscontro notariato del 3 ottobre 2026

Riletti integralmente gli artt. 2–14 nel PDF GU locale `notariato-bando-400-posti.pdf`, pagine PDF 7–11 (stampate 1–5). L’art. 2 distingue requisiti entro il termine della domanda e cinque precedenti non idoneità alla pubblicazione. L’espulsione conta dopo la dettatura del tema. Gli artt. 10–11 separano pratica sostanziale, certificato dopo l’orale e documentazione successiva. Art. 8: minimi 35, totale 210/300 e incremento di due punti per precedente idoneità alle condizioni previste.

La [scheda ministeriale SCE1485302](https://www.giustizia.it/giustizia/it/mg_1_6_1.page?contentId=SCE1485302), nuovamente acquisita tramite ricerca ufficiale il 3 ottobre 2026, conferma finestra telematica 30 dicembre 2025 ore 12.00–30 gennaio 2026 ore 12.00. Il dato operativo è attribuito alla scheda e non ricavato con un computo autonomo dei trenta giorni. Gli aggiornamenti della correzione pubblicati in ottobre non sono usati per previsioni di esito o probabilità individuali.
''';s.write_text(x,encoding='utf8')
print('SP03/04 corrected')
