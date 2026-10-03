from pathlib import Path
import re,shutil
S=Path('wiki/sources/bandi-rappresentativi-m-sp01-forze-polizia-2026.md');s=S.read_text(encoding='utf-8');s+='''

Ulteriore controllo CC3.081: art.4 commi4–8, p.6: posta ordinaria per copia della domanda da esibire alla prima prova, PEC attiva per notifiche, fototessera digitale; annullamento e nuovo invio per variazioni entrotermine; regolarizzazione di vizi sanabili non equivale a proroga generale. Ricerca testuale integrale nelPDF51p di «pagamento», «versamento», «contributo»: nessuna tassa concorsuale rilevata; unica occorrenza contributo riguarda copie di dati personali nell’informativa privacy. Il decoder distingue «contributo non previsto negli articoli della domanda» da importi inventati.

CC898 decreto modifica locale letto per intero: numero0000222, **10marzo2026**, sostituisce allegatoE per tempi corsa; la precedente nota attribuiva imprecisamente date18marzo/10aprile senza riscontro nelPDF locale. L’esempio utilizzato deve nominare l’atto effettivamente acquisito, non presentare le due date come entrambe accertate.
''';S.write_text(s,encoding='utf-8')
p=Path('wiki/books/moduli/m-sp01-forze-ordine/chapters/07-bando-decoder.md');t=p.read_text(encoding='utf-8');a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-sp01-07.md');assert not a.exists();shutil.copyfile(p,a)
# Rimuovere griglie ripetute a sei percorsi: una scheda per un solo concorso, alla fine.
t=re.sub(r'(?m)^\| Elemento \| Dati essenziali \| Verifica o azione \|\n(?:\|[^\n]*\n)+','Usa la scheda finale per **un solo concorso**: aggiungi i dati di questa sezione, con fonte e azione successiva. Per confrontare un altro percorso compila una scheda separata.\n',t)
t=t.replace('Se un dato non è presente, non lo completi “a buon senso”. Lo marchi come “non pubblicato” o “non dichiarato”.','Se non trovi un dato, non lo completi per intuizione: distingui lo stato della tua ricerca da ciò che la procedura ha effettivamente pubblicato o previsto.')
t=t.replace('Se un dato manca, scrivi “non pubblicato” o “non dichiarato”.','Se un dato manca, usa lo stato preciso definito nel nucleo sugli ignoti.')
t=t.replace('Un dato mancante non si completa per intuizione: si marca come “non pubblicato” o “non dichiarato”.','Un dato non trovato richiede ricerca; «non previsto» richiede una regola che escluda quell’adempimento.')
t=t.replace('Se il calendario non è presente, scrivi “non pubblicato”.','Se non trovi il calendario nella pagina consultata, scrivi «non reperito in questa ricerca»; puoi dire «non ancora pubblicato» solo dopo il controllo completo dei canali previsti o un avviso che lo confermi.')
t=t.replace('Se l’allegato non è disponibile, devi scrivere “non pubblicato”. Se è disponibile ma non contiene il dato che cerchi, devi scrivere “non dichiarato”.','Se non riesci ad aprire l’allegato, scrivi «non acquisito: accesso da ripetere». Se il documento letto non contiene il dato, indica «non trovato in questo documento» e controlla gli atti richiamati. Non dedurre che l’adempimento non esista.')
t=t.replace('nel Decoder devi scrivere “non pubblicato” o “non dichiarato”, secondo il caso.','nel Decoder devi indicare «notizia non confermata; verificare bando e avvisi», senza concludere che la pubblicazione non esista.')
t=t.replace('Scrive: “banca dati: non pubblicato sulla fonte ufficiale alla data del controllo”.','Scrive: «Banca non reperita nella pagina consultata; controllare gli allegati e il canale indicato dal bando».')
start=t.index('Un ignoto dichiarato è un dato');end=t.index('La regola vale soprattutto',start)
t=t[:start]+'''Un ignoto dichiarato è una questione aperta descritta con precisione. Usa quattro stati, perché richiedono azioni diverse:

| Stato | Significato e azione |
| --- | --- |
| Non reperito | La ricerca non ha trovato il dato: controlla altri canali ufficiali e allegati |
| Non ancora pubblicato | Il controllo dei canali o un avviso ufficiale conferma l’attesa: registra prossimo controllo |
| Non previsto | Gli atti applicabili non prevedono quella prova o quell’adempimento: motiva con la disposizione |
| Da verificare | Hai un dato o un’interpretazione incerta: identifica documento e quesito da risolvere |

«Non dichiarato nel documento letto» descrive solo quel documento. Non dimostra né assenza di pubblicazione altrove né assenza dell’obbligo. Se il collegamento a un PDF non funziona, il problema è l’accesso alla fonte, non la certezza che l’amministrazione non abbia pubblicato nulla.

''' +t[end:]
t=t.replace('nel Decoder operativo devi usare “non pubblicato” o “non dichiarato”.','nel Decoder operativo devi registrare lo stato preciso, il documento mancante e l’azione per verificarlo.')
t=t.replace('“Non pubblicato” e “non dichiarato” sono formule operative, non segni di incompletezza.','Non reperito, non pubblicato, non previsto e da verificare indicano situazioni diverse.')
start=t.index('La seconda decisione possibile è attendere.');end=t.index('La terza decisione',start)
t=t[:start]+'''La seconda decisione è attendere un’informazione per una specifica scelta, per esempio acquistare un viaggio prima della sede definitiva. Questo **non sospende la scadenza della domanda**. Se possiedi i requisiti e vuoi partecipare, presenta la candidatura entro il termine anche se calendario o banca dati sono ancora attesi. Se un requisito essenziale è incerto, attiva subito la verifica, senza dichiarare ciò che non puoi attestare e senza presumere una proroga.

''' +t[end:]
t=t.replace('Il primo giorno identifichi corpo, binario e fonte ufficiale.','Il primo giorno identifichi corpo, binario, termine esatto e canale della domanda; se mancano meno di sette giorni, comprimi subito la sequenza e proteggi il termine.')
t=t.replace('Per il concorso base dei Carabinieri trova un dato non pubblicato sul calendario e decide: attendere, studiando solo le materie comuni già dichiarate.','Per il concorso base dei Carabinieri il calendario è ancora atteso: se intende partecipare e possiede i requisiti, invia comunque la domanda entro termine e rinvia soltanto la scelta logistica dipendente dal calendario.')
t=t.replace('Attendere è corretto quando mancano dati ufficiali decisivi.','Attendere un calendario non proroga la domanda: separa candidatura, studio e logistica.')
t=t.replace('Il quarto errore è non distinguere “non pubblicato” da “non dichiarato”. Se un calendario deve uscire in seguito, il dato è non pubblicato. Se il documento non contiene una soglia, il dato è non dichiarato. In entrambi i casi non devi inventare.','Il quarto errore è trasformare una ricerca incompleta in un fatto della procedura. «Non trovato» non equivale a «non previsto»: registra la ricerca, il documento da acquisire e l’azione successiva.')
t=t.replace('2. Un dato di calendario non presente sulla fonte ufficiale deve essere registrato come:','2. Dopo aver consultato una sola pagina non trovi il calendario. Quale annotazione è corretta?').replace('C. non pubblicato.','C. non reperito nella ricerca svolta; verificare gli altri canali prescritti.').replace('Se il calendario può uscire in seguito ma non è ancora disponibile, il dato va marcato come “non pubblicato”.','Non aver trovato il documento non dimostra che non sia stato pubblicato. A e D sostituiscono una prova con una congettura; B cambia impropriamente la fonte di riferimento.')
start=t.index('### Scheda compilabile finale:');end=t.index('## Riferimenti normativi',start)
t=t[:start]+'''### Esempio compilato: Carabinieri, 3.081 allievi, 2026

Questo è un esempio di lettura retrospettiva del bando, non una procedura ancora aperta. I dati del candidato sono immaginari; le regole provengono dagli articoli 2–6 e dalla scheda inPA della procedura.

| Campo | Dato ed effetto |
| --- | --- |
| Corpo e ruolo | Arma, allievo carabiniere in ferma quadriennale, 146° corso; binario base |
| Categoria del caso | Civile, ventidue anni alla scadenza, diploma già conseguito: questi due requisiti risultano compatibili; verificare anche gli altri dell’art. 2 |
| Posti | 3.081: 2.134 VFP, 915 civili, 32 bilinguisti; non 3.081 tutti disponibili per la categoria civile |
| Termine | 7 aprile 2026, ore 23:59, secondo la scheda ufficiale inPA |
| Canale | Area concorsi carabinieri.it con SPID o CIE; inPA pubblica e reindirizza, non sostituisce l’applicativo |
| Recapiti e allegato | Posta ordinaria, PEC attiva e fototessera digitale secondo art. 4 |
| Contributo | Non previsto negli articoli della domanda: non inserire un importo preso da altro concorso |
| Invio e prova | Completare inoltro; salvare domanda e ricevuta del sistema, non soltanto bozza |
| Modifica | Entro termine: annullare e compilare una nuova domanda; salvare la nuova ricevuta |
| Prove | Scritto, efficienza fisica, psicofisici, attitudinali, titoli; art. 6 |
| Calendario | Atto separato da monitorare; la sua attesa non sospende la candidatura |
| Decisione del caso | Partecipare dopo verifica completa dei requisiti; invio anticipato rispetto al termine e controllo della ricevuta |

La prova del lavoro non è una casella «fatto»: è la ricevuta riferita alla versione corretta della domanda. Se il candidato corregge una copia sul proprio computer ma non annulla e reinvia secondo l’applicativo, la domanda trasmessa resta quella precedente. Dopo la scadenza non deve presumere di poter aggiungere qualunque dato invocando la regolarizzazione dei vizi sanabili.

### Scheda personale: un concorso per foglio

Compila prima il blocco della candidatura e poi quello della preparazione. Usa un secondo foglio per un altro concorso; non comprimere sei percorsi nelle stesse celle.

**Identità e accesso**

Corpo, ruolo, anno e codice: ________________________________________

Categoria e riserva invocata: ________________________________________

Età, formula e data di riferimento: __________________________________

Titolo e data di conseguimento richiesta: ____________________________

Altri requisiti e verifica compiuta: _________________________________

**Candidatura**

Scadenza, ora e fonte: ______________________________________________

Canale, credenziali e recapiti richiesti: ____________________________

Contributo: previsto / non previsto / da verificare; fonte: __________

Allegati e documenti da procurare: ___________________________________

Regola per annullamento, modifica e nuovo invio: _____________________

Invio definitivo: data, ora, identificativo ricevuta: _________________

**Preparazione e controlli successivi**

Prima prova, formato, materie e soglia: ______________________________

Altre prove e certificazioni con scadenza: ___________________________

Dato non reperito o da verificare, canale e azione: ___________________

Calendario atteso, prossimo controllo: _______________________________

Decisione e prime due attività: _____________________________________

____________________________________________________________________

''' +t[end:]
assert '<br>' not in t
p.write_text(t,encoding='utf-8');print('SP01/07: decoder operativo, stati, scadenza e scheda stampabile')
