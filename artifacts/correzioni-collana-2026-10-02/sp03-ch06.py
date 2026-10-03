from pathlib import Path
import shutil
p=next(Path('wiki/books/moduli/m-sp03-magistratura-avvocatura-notariato/chapters').glob('06-*.md'));a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-sp03-06.md');assert not a.exists();shutil.copyfile(p,a);t=p.read_text(encoding='utf8')
t=t.replace('Una pagina corretta male insegna più di trenta pagine lette senza verifica','Una pagina scritta male e corretta bene può insegnare più di trenta pagine lette senza verifica')
t=t.replace('limite dei trentacinque anni non compiuti secondo il bando','limite di non aver superato il trentacinquesimo anno alla scadenza, secondo il bando e gli eventuali benefici applicabili')
t=t.replace('Il limite dei trentacinque anni non compiuti previsto dal bando.','Il limite di non aver superato il trentacinquesimo anno alla scadenza, salve le elevazioni applicabili.')
t=t.replace('Elena è laureata in giurisprudenza e lavora in uno studio legale. Sta valutando i tre binari del modulo.','**Caso composito di confronto, letto dopo la pubblicazione delle tre tornate.** Elena è laureata in giurisprudenza e lavora in uno studio legale. Le valutazioni riferite all’agosto 2025 sono retrospettive: non presuppongono che allora conoscesse il bando di magistratura dell’ottobre 2025 o quello notarile del dicembre 2025. L’esercizio confronta i vincoli e costruisce quattro settimane di studio interne; non permette di inviare oggi una domanda per una finestra chiusa.')
t=t.replace('non ha ancora compiuto trentacinque anni. Per il notariato','non aveva ancora compiuto trentacinque anni. Si assume che avesse inviato tempestivamente la candidatura e che non avesse precedenti esiti di non idoneità da procuratore dello Stato. Per il notariato')
t=t.replace('Nel caso proposto, alla scadenza del 12 agosto 2025 Elena non ha ancora compiuto trentacinque anni.','Nel controllo retrospettivo, alla scadenza del 12 agosto 2025 Elena non aveva ancora compiuto trentacinque anni.')
t=t.replace('Se Elena decide di proteggere Avvocatura dello Stato,','Se Elena decide di proteggere la preparazione per l’Avvocatura sulla candidatura già tempestivamente presentata,')
t=t.replace('La quarta verifica requisito, calendario, materiali e tenuta del piano.','La quarta verifica gli avvisi applicabili, i materiali e la tenuta del piano; il controllo dei requisiti e l’invio non sono rinviati a questa settimana.')
t=t.replace('Avvocatura dello Stato è il binario che richiede la decisione più rapida per via della finestra anagrafica della tornata studiata.','l’Avvocatura è il binario da proteggere solo sulla premessa esplicita della domanda già presentata. Se Elena non l’avesse inviata, le quattro settimane resterebbero preparazione generale: il piano non riaprirebbe la scadenza e una futura candidatura richiederebbe una nuova verifica anagrafica.')
t=t.replace('Chi prepara magistratura deve tenere conto anche del limite delle precedenti non idoneità previsto per quel concorso.','Chi prepara magistratura deve tenere conto del limite delle precedenti non idoneità previsto per quel concorso; per procuratore dello Stato l’art. 4 del bando 2025 esclude dopo due precedenti esiti di non idoneità. La semplice iscrizione a una procedura non coincide con un esito computabile.')
t=t.replace('una sovrapposizione di questo tipo','una vicinanza di questo tipo')
marker='### Strumento compilabile: roadmap trimestrale'
new='''### Esempio su due anni, subordinato ai controlli

Il percorso seguente è una proposta didattica per una persona già laureata, con quindici ore settimanali sostenibili e un solo binario principale. Non è una stima della durata necessaria per vincere. Le quindici ore si distribuiscono inizialmente in sei di studio, sei di produzione e tre di correzione o richiamo; una simulazione lunga richiede di riallocare ore nello stesso monte, non di sommarle di nascosto. Per il notariato la pratica segue un calendario giuridico e professionale separato: non si considera adempiuta mediante queste ore di studio. Per l’Avvocatura un orizzonte biennale è utilizzabile soltanto se resta coerente con età, benefici documentabili ed esiti pregressi.

| Periodo interno | Prodotto atteso | Verifica e decisione |
| --- | --- | --- |
| Anno 1, mesi 1–3 | Mappa del programma e tre prove diagnostiche, una per area scritta | Correzione di ogni prova; scegliere due lacune prioritarie e verificare il fascicolo requisiti |
| Anno 1, mesi 4–6 | Sei elaborati progressivi e sei riscritture mirate | Confronto con le diagnosi; se permane un errore di base, ridurre l’ampiezza e assegnare studio mirato |
| Anno 1, mesi 7–9 | Tre simulazioni complete, almeno una per area, e nove esposizioni orali brevi | Controllo di completezza, tempo e fonti; introdurre una nuova simulazione soltanto dopo la correzione della precedente |
| Anno 1, mesi 10–12 | Un fascicolo finale per area: prima prova, correzione, versione migliorata e prova differita | Revisione annuale: confermare il binario, cambiare distribuzione o sospendere la doppia preparazione |
| Anno 2, mesi 13–15 | Tre prove complete sulle aree più fragili e aggiornamento dei requisiti | Confronto con i difetti del primo anno; nessuna nuova tornata è presunta aperta |
| Anno 2, mesi 16–18 | Due cicli sulle tre aree, con correzioni e richiami orali | Valutare continuità e affaticamento; il ciclo ravvicinato si introduce solo se il recupero è sostenibile |
| Anno 2, mesi 19–21 | Simulazione delle condizioni previste dal bando, se pubblicato, e fascicolo logistico | Se non esiste il bando, restare nel ciclo di mantenimento senza inventare data, sede o materiali ammessi |
| Anno 2, mesi 22–24 | Tre verifiche differite e decisione documentata sul ciclo successivo | Integrare esiti reali, requisiti, risorse e correzioni; nessun avanzamento automatico per il solo tempo trascorso |

Il prodotto cambia con il binario. In magistratura le tre aree sono civile, penale e amministrativo e si scrive nella forma richiesta dalla traccia; per l’Avvocatura si allenano le coppie sostanza/processo dei tre temi; nel notariato si producono atto testamentario, atto tra vivi civile e atto commerciale, ciascuno con principi. Una simulazione notarile non può essere registrata come sostituto del tema penale, anche quando condivide con altre prove una parte del metodo.

La revisione mensile usa quattro evidenze: elaborati completati sul numero pianificato, difetti ricorrenti dopo la riscrittura, capacità di concludere nei tempi e tenuta del richiamo differito. Sono indicatori didattici, non una scala ufficiale di idoneità. Se per due mesi consecutivi manca metà delle consegne, si riduce il piano e si verifica la causa; non si attribuisce al candidato un difetto personale né si aggiungono automaticamente notti di studio. Se un bando anticipa la prova, il programma residuo viene selezionato in rapporto al livello osservato: una scadenza vicina non produce conoscenze già acquisite.

**Variante con otto ore settimanali.** Non dimezzare la correzione per conservare il numero degli elaborati. Mantieni un ciclo breve di studio, produzione e revisione ogni settimana e distanzia le prove complete. L’obiettivo trimestrale può passare da sei a tre elaborati completi, ognuno corretto e riscritto. La scelta di consegnare a un concorso resta autonoma: prima della prova si controllano nuovamente il regime degli esiti e la preparazione effettiva, senza trattare l’iscrizione come un obbligo di consumare un tentativo.

'''
assert marker in t;t=t.replace(marker,new+marker)
t=t.replace('Decreto ministeriale 16 dicembre 2025','Decreto dirigenziale 16 dicembre 2025')
p.write_text(t,encoding='utf8');print('SP03/06 corrected')
