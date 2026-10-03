from pathlib import Path
import re,json,hashlib
base=Path('wiki/books/moduli')
files=[base/'m-fl02-regioni-province-citta-metropolitane/chapters/01-il-sistema-territoriale-multilivello.md',base/'m-fl03-camere-commercio/chapters/01-camere-commercio-sistema-camerale-unioncamere.md']
schemi=[[
'''### Schema 18.1 — Dal bando alla risposta

**Bando territoriale → livello competente → funzione → atto → controllo → output.**

| Passaggio BANDO | Prodotto da conservare |
|---|---|
| Bando | Ente, profilo, materie e tipo di prova. |
| Aree | Priorità fra ordinamento, fondi e territorio. |
| Nuclei | Distinzioni tra competenza, funzione e atto. |
| Diario | Errore da correggere: livelli confusi o Province considerate abolite. |
| Output | Mappa livello-funzione-atto, caso risolto o risposta orale. |

Prima domanda: quale livello istituzionale rende corretta la risposta?''',
'''### Schema 18.2 — Livelli autonomi, funzioni differenti

| Livello | Funzione da riconoscere |
|---|---|
| Stato | Unità dell'ordinamento, competenze riservate e livelli essenziali. |
| Regione | Legislazione nelle materie attribuite, programmazione, amministrazione e coordinamento. |
| Provincia e Città metropolitana | Funzioni di area vasta secondo le rispettive attribuzioni. |
| Comune | Servizi di prossimità, sportelli e attuazione locale. |

La lettura procede per competenze: l'ordine della tabella non rappresenta una catena di comando. Finanziamento, coordinamento e controllo richiedono ciascuno una base specifica.''',
'''### Schema 18.3 — Scegliere la scala della funzione

1. **Sussidiarietà:** partire dal livello vicino ai cittadini e verificare se può esercitare efficacemente la funzione.
2. **Differenziazione:** considerare caratteristiche diverse, come piccoli Comuni, aree metropolitane e zone interne.
3. **Adeguatezza:** verificare competenze, risorse, dimensione e capacità di coordinamento.

**Esito:** motivare l'allocazione della funzione in base a problema, territorio e capacità amministrativa. La sola vicinanza non basta; una scala più ampia va giustificata.''',
'''### Schema 18.4 — Percorso di un avviso regionale

| Fase | Soggetto, documento e verifica |
|---|---|
| 1. Programma | La Regione definisce obiettivi e risorse. |
| 2. Avviso | Sono pubblicati destinatari, requisiti e criteri. |
| 3. Domanda | Il Comune presenta progetto e dichiarazioni richieste. |
| 4. Istruttoria | L'ufficio competente verifica ammissibilità e applica i criteri; forma la graduatoria se prevista. |
| 5. Concessione | L'atto individua beneficiario, importo e obblighi. |
| 6. Attuazione | Il beneficiario organizza affidamenti, attività e spesa secondo le regole applicabili. |
| 7. Rendiconto e controllo | Documenti, pagamenti e tracciabilità provano gli adempimenti; irregolarità possono comportare revoca o recupero nei presupposti. |
| 8. Monitoraggio | Dati e indicatori seguono avanzamento e risultati. |

Lo schema è didattico: avviso e disciplina della misura precisano competenze e sequenza. Monitoraggio e controlli accompagnano anche le fasi precedenti; non iniziano necessariamente dopo il rendiconto.''',
'''### Schema 18.5 — Area vasta: dalla funzione all'atto

| Ente | Collegamento operativo |
|---|---|
| Provincia | Viabilità, edilizia scolastica, pianificazione e assistenza ai Comuni: individuare la specifica attribuzione e l'atto necessario. |
| Città metropolitana | Piano strategico, mobilità, infrastrutture e servizi di scala metropolitana: distinguere pianificazione e gestione. |
| Comune | Prossimità, sportelli, servizi locali e attuazione sul territorio: collocare il compito nella rete sovracomunale. |

**Controllo:** funzione sovracomunale → fonte attributiva → soggetto competente → atto coerente. La Città metropolitana non coincide con il solo Comune capoluogo; Provincia e Città metropolitana non sono uffici residuali.'''
],[
'''### Schema 30.1 — Dal bando camerale alla prova

**Bando → ente → funzione → servizio → output.**

| Passaggio BANDO | Prodotto da conservare |
|---|---|
| Bando | Ente del sistema, profilo, servizio e prove. |
| Aree | Ordinamento, Registro, servizi e mercato. |
| Nuclei | Autonomia funzionale, pubblicità legale e distinzione Registro/REA. |
| Diario | Errore da correggere: Camera assimilata a Comune o Registro ridotto ad archivio. |
| Output | Risposta orale, caso di sportello o checklist. |

Prima domanda: quale funzione camerale rende corretta la risposta?''',
'''### Schema 30.2 — Autonomia funzionale in quattro elementi

| Elemento | Significato nella pratica |
|---|---|
| Natura pubblica | Legalità, procedimento e trasparenza nell'esercizio delle attribuzioni. |
| Funzioni proprie | Interessi generali delle imprese, mercato e pubblicità legale. |
| Circoscrizione | Territorio economico, unità locali, filiere e servizi. |
| Sistema camerale | Reti, strumenti condivisi e supporto. |

La Camera non è un Comune, un ufficio periferico statale o una semplice associazione rappresentativa di imprese.''',
'''### Schema 30.3 — Rete camerale: nominare ogni relazione

| Soggetti collegati | Relazione |
|---|---|
| Camere e Unioncamere | Appartenenza al sistema, rappresentanza degli interessi generali, indirizzi e iniziative coordinate nelle attribuzioni previste. |
| Camere e unioni regionali | Raccordo nell'ambito regionale secondo l'assetto concretamente presente. |
| Camere e organismi strumentali | Servizi, dati e infrastrutture condivise, secondo i rispettivi compiti. |
| Camere e utenti | Servizi e procedimenti di competenza verso imprese, professionisti, PA e altri utenti. |

**Tre piani distinti:** Unioncamere rappresenta e raccorda; l'organismo tecnico mette a disposizione lo strumento; la Camera competente svolge la propria funzione. La rete non trasferisce automaticamente la decisione sulla singola pratica a Unioncamere o al gestore della piattaforma. Riferimento: Statuto Unioncamere, artt. 1–3.''',
'''### Schema 30.4 — Dalla funzione al servizio

| Funzione | Servizio o risultato riconoscibile |
|---|---|
| Registro e REA | Iscrizioni, variazioni, visure e certificati, con effetti distinti. |
| Semplificazione | ComUnica, pratiche digitali e raccordo con SUAP. |
| Regolazione del mercato | Tutela della fede pubblica, vigilanza e controlli nelle attribuzioni. |
| Servizi alle imprese | Informazione, promozione e supporto alla digitalizzazione. |
| Organizzazione e comunicazione | Uffici, sportello, procedimento, trasparenza e relazione con utenti. |

Le righe indicano aree funzionali, non fasi obbligatorie di una sola pratica. In prova collega ogni funzione a procedimento, utente e output.''',
'''### Schema 30.5 — Classificare la domanda dell'impresa

**Impresa o professionista → richiesta da qualificare → canale competente → risultato.**

| Oggetto della domanda | Percorso da distinguere |
|---|---|
| Dato camerale o documento | Registro imprese, REA, visura o certificato: individuare il servizio camerale competente. |
| Avvio o modifica di attività produttiva | Titolo, SCIA o comunicazione secondo la disciplina applicabile: individuare il percorso SUAP e gli uffici coinvolti. |
| Assistenza digitale | Spiegare accesso, flusso e stato della pratica senza sostituire le dichiarazioni dell'impresa. |

**Output corretto:** per ciascuna richiesta indicare soggetto, adempimento, canale ed effetto atteso. L'accesso telematico unitario non rende unica la competenza; una visura non sostituisce il titolo necessario per l'attività.'''
]]
manifest=[]
for p,blocks in zip(files,schemi):
 s=p.read_text(encoding='utf8');before=hashlib.sha256(p.read_bytes()).hexdigest();matches=list(re.finditer(r'!\[Figura[^\n]+\]\([^\n]+\)',s));assert len(matches)==5
 for m,b in reversed(list(zip(matches,blocks))):s=s[:m.start()]+b+s[m.end():]
 s=re.sub(r'asset_refs:\n(?:  - [^\n]+\n)+','asset_refs: []\n',s)
 s=s.replace('"illustrated"','"native-schemes"').replace(', "scripts/generate-mfl03-chapter01-assets.cjs"','')
 p.write_text(s,encoding='utf8');manifest.append({'path':p.as_posix(),'before':before,'after':hashlib.sha256(p.read_bytes()).hexdigest(),'schemes':5,'historicalRasterFilesPreserved':True})
Path('artifacts/correzioni-collana-2026-10-02/VOL-02-native-schemes.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
