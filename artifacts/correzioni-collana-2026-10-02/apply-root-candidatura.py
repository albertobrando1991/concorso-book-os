from pathlib import Path
import importlib.util
spec=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)
ref='sources/vol-01-candidatura-casi-correzioni-2026-10-03.md';u.REF=ref
rules='''### Partecipazione alle prove: misure e dichiarazioni

Controlla prima della domanda le misure necessarie per **disabilità o DSA**, le esigenze legate a **gravidanza e allattamento**, e le eventuali **riserve e preferenze**. Per ciascuna voce annota presupposto, documento richiesto, termine, canale di invio e ricevuta. Non aspettare il giorno della prova e non presumere che un dato inserito nel curriculum valga anche come richiesta specifica.

Nel regime del DPR 487/1994, art. 7, le misure per disabilità e DSA accertati sono definite secondo la disciplina richiamata e le valutazioni della commissione; per i DSA il DM 9 novembre 2021 disciplina strumenti compensativi, tempi aggiuntivi e sostituzione della prova scritta con orale nei casi previsti. Per gravidanza e allattamento il comma 7 tutela la partecipazione con misure organizzative, anche prove asincrone e spazi per allattare, e prevede comunicazione preventiva secondo il bando. Nessuna di queste tutele autorizza a saltare una prova senza seguire il percorso previsto.

**Ambito:** il DPR 487 salva gli ordinamenti speciali richiamati dall’art. 1, comma 6, e non si applica al reclutamento del SSN e dei segretari comunali. Per questi e gli altri percorsi speciali verifica le norme proprie e il bando, senza dedurre che manchino tutele o che siano identiche a quelle del regime ordinario.
'''
s='anatomia-del-bando';t=u.read(s);t=u.replace(t,'## Checklist prima della domanda',rules+'\n## Checklist prima della domanda');u.save(s,t,['V01-43'],ref)
s='checklist-operative';t=u.read(s)
t=u.replace(t,'## Checklist 3 - Dopo l’invio della domanda','''### Controllo delle richieste specifiche

| Controllo prima dell’invio | Esito o dato da annotare |
|---|---|
| Ausili, tempi aggiuntivi o misure per disabilità/DSA: ho formulato la richiesta specifica? | |
| Ho verificato certificazione, formato, termine e canale previsti? | |
| Gravidanza/allattamento: ho comunicato preventivamente l’esigenza secondo il bando? | |
| Ho dichiarato separatamente le riserve e le preferenze applicabili? | |
| Ho verificato data di possesso dei titoli e documentazione richiesta? | |
| Ho conservato ricevuta, protocollo e risposta sulle misure richieste? | |

Per il regime e le esclusioni del DPR 487/1994 riprendi il Capitolo 2, **«Partecipazione alle prove: misure e dichiarazioni»**. Prima della prova verifica l’esito della richiesta e le istruzioni ricevute; se mancano, usa tempestivamente il canale ufficiale. Una misura richiesta non può essere considerata automaticamente concessa nella forma desiderata.

## Checklist 3 - Dopo l’invio della domanda''')
u.save(s,t,['V01-43'],ref)
s='appendice-c-template-bando-decoder';t=u.read(s)
t=u.replace(t,'### Rischi formali','''### Misure di partecipazione e titoli dichiarati

Compila una scheda per ciascuna richiesta o beneficio: disabilità/DSA, gravidanza/allattamento, riserva, preferenza. Se non applicabile, scrivi «non applicabile»; se il bando non è chiaro, annota la richiesta di chiarimento.

| Campo | Dato ricavato dal bando |
|---|---|
| Misura, riserva o preferenza richiesta | |
| Norma/voce del bando e presupposto | |
| Data entro cui il presupposto deve essere posseduto | |
| Documento o certificazione da produrre | |
| Termine e canale della richiesta/dichiarazione | |
| Ricevuta o protocollo | |
| Esito e istruzioni per la prova | |

Controlla l’ambito della disciplina: il DPR 487/1994 non si estende automaticamente al reclutamento SSN, dei segretari comunali e agli ordinamenti speciali salvaguardati. La guida è nel Capitolo 2, **«Partecipazione alle prove: misure e dichiarazioni»**.

### Rischi formali''')
u.save(s,t,['V01-43'],ref)
u.record()
