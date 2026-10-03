# Report editoriale — Integrazioni nazionali M-SA01, capitoli 04 e 09

## 1. Sintesi editoriale

- Genere: manuale-workbook per concorsi sanitari amministrativi.
- Pubblico: candidati ai profili amministrativi del SSN.
- Perimetro: nuovo testo su principi e organizzazione SSN, organi, LEA e servizi, programmazione, integrazione sociosanitaria, autorizzazione/accreditamento/accordi; finanziamento, riparto, budget, cassa, remunerazione e mobilità. Controllati i dieci nuovi quiz del capitolo 04 e i cinque del capitolo 09.
- Esito: nessun errore oggettivo né blocker editoriale rilevato nel delta esaminato; quindici chiavi corrette e univoche.
- Revisione indipendente in sola lettura al 2 ottobre 2026, basata sui diff, sui passaggi collegati, sulle quattro source notes richieste e su verifiche web istituzionali puntuali.
- Entrambi i capitoli superano lint legacy e gate rinvii senza blocker o warning. Tutte le source_refs dichiarate sono presenti.

## 2. Punti applicati della checklist

Applicati i punti 1–26 e 28–30 nel perimetro testuale esaminato: progressione, autonomia didattica, definizioni e distinzioni, accuratezza dei claim normativi attivati, esempi e casi, coerenza con fonti e quiz, stile e superficie.

Il punto 27, impaginazione, non è verificato: questa revisione non comprende un PDF aggiornato né ispezione visiva delle figure. I punti sulla coerenza dell'intero libro sono limitati ai due capitoli, ai loro raccordi e all'architettura comune/specialistico. Non si estende l'esito al resto del volume.

## 3. Tabella errori

Nessun errore oggettivo individuato nel perimetro. Non vengono inventati rilievi per riempire la tabella.

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| — | Delta capitoli 04 e 09 | Controllo del perimetro | — | Nessun errore oggettivo rilevato; riga di esito, non rilievo inventato | Nessuna | Chiuso |

## 4. Osservazioni per capitolo

### Capitolo 04 — Atti, procedimenti e flussi informativi

La teoria precede l'applicazione: diritto alla salute e universalità; distinzione fra Stato, Regione e azienda; aziendalizzazione senza trasformazione in impresa privata; organi versus componenti della direzione; LEA e appropriatezza; servizi territoriali e ospedalieri; programmazione e integrazione; tre titoli dell'erogatore e loro diversi effetti.

La distinzione fra collegio sindacale e di direzione è leggibile e non si limita alle denominazioni. Il testo evita di attribuire al DG qualsiasi firma, alla COT una funzione di pronto soccorso o all'accreditamento un diritto illimitato al pagamento. Il caso della fattura richiede ricostruzione del rapporto senza ordinare né pagamento né rigetto automatici.

Le prestazioni sociosanitarie sono distinte senza imporre un riparto generalizzato 50/50. La valutazione multidimensionale e il progetto individuale hanno una funzione spiegata. L'autonomia della prosa è adeguata al perimetro nazionale; il richiamo a regole territoriali non sostituisce definizioni e differenze necessarie al candidato.

Chiavi verificate dei dieci nuovi quesiti: **B, A, B, B, B, C, C, B, B, B**. Nessun distrattore fornisce una seconda risposta corretta. In particolare Q3 distingue organi e direzione; Q7 non nega indiscriminatamente qualsiasi remunerazione ma esclude l'automatismo; Q8 preserva la differenza fra pubblicazione ed entrata in vigore; Q9 distingue idoneità, selezione e incarico.

### Capitolo 09 — Contabilità, budget e controllo di gestione

La nuova sezione rende comprensibili le risorse prima della contabilizzazione: fabbisogno e spesa complessiva hanno perimetri distinti; il riparto precede l'assegnazione; il budget attribuisce mezzi e obiettivi; la cassa riguarda tempi effettivi. Investimento e funzionamento sono collegati senza considerarli fondi fungibili.

Remunerazione di funzione e remunerazione a prestazione sono distinte; la tariffa non è confusa con il costo individuale. La mobilità è spiegata dai due punti di vista e il saldo non diventa un indicatore univoco di qualità. Nel caso didattico, 8 milioni assegnati meno 6 incassati producono 2 milioni da verificare sotto il profilo dei trasferimenti: non vengono qualificati automaticamente come perdita. Il milione vincolato non diventa liberamente utilizzabile per servizi ordinari.

Chiavi verificate dei cinque nuovi quesiti: **B, B, B, A, A**. Enunciati, soluzioni e alternative sono coerenti; i mini-esercizi richiedono documenti e dati pertinenti e non soltanto l'elenco delle sigle.

## 5. Coerenza globale

Letti i consolidamenti `ssn-organizzazione-aziende-standard-lea`, `contabilita-budget-aziende-sanitarie`, `integrazione-sociosanitaria-accreditamento-quadro-nazionale-2026` e `lea-aggiornamenti-pubblicati-settembre-2026`. I claim inseriti sono coerenti con questi perimetri. Il testo mantiene il confine nazionale e non incorpora disciplina campana o cultura generale. Non trasforma schemi nazionali in procedure regionali uniformi.

Controlli automatizzati eseguiti sui file interi:

| Capitolo | Lint legacy | Rinvii VOL-01 | Fonti mancanti |
|---|---|---|---:|
| 04 | Passato, 0 blocker, 0 warning | Passato, 0 blocker, 0 warning | 0 |
| 09 | Passato, 0 blocker, 0 warning | Passato, 0 blocker, 0 warning | 0 |

Usato `requireFormatVersion2:false`, senza promuovere i capitoli al formato 2. `git diff --check` sul modulo non segnala problemi. Gli esiti automatici non sostituiscono i controlli semantici descritti sopra.

## 6. Contenuto da verificare

### Claim sensibili verificati direttamente

1. **Aggiornamenti LEA e decorrenza:** consultato il testo primario del [fascicolo GU 227 del 30 settembre 2026](https://www.gazzettaufficiale.it/eli/gu/2026/09/30/227/sg/pdf), non il solo risultato del motore di ricerca. L'articolo 8 del DPCM 7 agosto 2026, pagina PDF 27 (indice 26), e l'articolo 12 del DM 3 agosto 2026, pagina PDF 51 (indice 50), dispongono la decorrenza al trentesimo giorno successivo alla pubblicazione. Ne segue il 30 ottobre 2026: il box del capitolo qualifica correttamente questi atti come pubblicati ma non ancora efficaci al 2 ottobre. Non vengono attivati codici o prestazioni degli allegati non esaminati.

2. **Accreditamento:** letto il testo coordinato dell'articolo 36 L. 193/2024 nel [fascicolo GU 101 del 4 maggio 2026](https://www.gazzettaufficiale.it/eli/gu/2026/05/04/101/sg/pdf), pagina PDF 137 (indice 136). L'oggetto circoscritto e il termine ultimo riportati nel capitolo corrispondono al testo: artt. 8-quater comma 7, 8-quinquies comma 1-bis e DM 19 dicembre 2022; esiti del Tavolo da sottoporre a intesa e limite del 31 dicembre 2026. La prosa non sostiene che l'intero sistema sia sospeso e non certifica l'assenza di successive intese: invita a coordinare gli atti per una data concreta. Nessun claim operativo regionale non verificato viene dedotto dalla scadenza massima.

3. **Collegio sindacale:** la [Corte costituzionale, sentenza 98/2018, paragrafo 4.1](https://www.gazzettaufficiale.it/atto/corte_costituzionale/caricaArticoloDefault/originario?atto.codiceRedazionale=T-180098&atto.dataPubblicazioneGazzetta=2018-05-23&atto.tipoProvvedimento=SENTENZA) riproduce espressamente art. 3-ter comma 3: durata triennale e tre designazioni Regione/MEF/Salute. È una conferma primaria del modello nazionale già consolidato, non una certificazione di tutti gli ordinamenti speciali, correttamente esclusi dalla generalizzazione nel capitolo.

4. **Organi aziendali:** il [testo coordinato pubblicato nella GU del 10 novembre 2012, supplemento 201](https://www.gazzettaufficiale.it/eli/gu/2012/11/10/263/so/201/sg/pdf) riporta la modifica di art. 3 comma 1-quater che include DG, collegio di direzione e collegio sindacale. Non si è usata la formulazione anteriore che elencava soltanto DG e collegio sindacale.

5. **Finanziamento:** consultata la [Camera dei deputati, Organizzazione SSN](https://temi.camera.it/leg19/temi/19_tl18_organizzazione_ssn.html), sezioni su livello, componenti e fonti. Confermati distinzione fra fabbisogno e aggregato della spesa, riparto CIPESS, ticket, IRAP/addizionale IRPEF, compartecipazione IVA, quote e garanzia. Non importati valori annuali o regimi particolari.

6. **Remunerazione:** il contenuto istituzionale [Ministero della Salute, Nomenclatori e tariffe](https://www.salute.gov.it/new/it/tema/programmazione-e-finanziamento-del-ssn/tariffari-nazionali-delle-prestazioni-del-ssn/), disponibile nel risultato testuale esteso del motore, e l'estratto di [art. 8-sexies](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A1992-12-30%3B502~art8sexies=) confermano la distinzione fra funzioni assistenziali e tariffe. L'apertura diretta ministeriale ha restituito challenge Gcore; non si attribuisce a quel tentativo una verifica di tariffe numeriche correnti. La prosa nuova non ne riporta.

### Limiti pertinenti

Normattiva ha mostrato la pagina del D.Lgs. 502/1992 con riferimento al 2 ottobre 2026 e aggiornamento dell'atto al 9 maggio 2026, ma alcuni permalink di articolo e l'esportazione integrale hanno restituito errore. Non si dichiara pertanto ricontrollato ogni comma del decreto. Le verifiche primarie puntuali sopra sostengono i claim effettivamente attivati; l'inaccessibilità degli articoli non citati nel delta non viene convertita in un falso errore del manoscritto.

## 7. Suggerimenti facoltativi (non errori)

In una futura rifinitura si può rendere meno concentrata sulla lettera B la distribuzione delle risposte: non è un problema di correttezza e richiederebbe un nuovo controllo delle chiavi dopo ogni riordino.

Il cap. 04 mantiene, dopo le nuove sezioni, una breve ricapitolazione storica nel precedente «Inquadramento teorico». Può essere presentata come raccordo riassuntivo per rendere più fluido il passaggio agli atti; la ripetizione è contenuta e non crea contraddizioni.

## 8. Priorità degli interventi

1. Nessuna correzione obbligatoria individuata nel delta revisionato.
2. Registrare l'esito nei report 14/15 e riallineare matrice/frontmatter secondo lo stato effettivo dei controlli, a cura dell'agente principale.
3. Rigenerare e ispezionare l'impaginato nelle fasi successive; non estendere il vecchio esito grafico alle pagine aumentate.

## 9. Giudizio di pubblicabilità

**Pubblicabile con correzioni minori**, per i due delta testuali esaminati. Non restano rilievi oggettivi aperti; le eventuali rifiniture proposte sono facoltative. Il giudizio non conclude la pipeline del volume, non copre il PDF e non sostituisce la conferma umana dello step 24.

## 10. Limiti di questa revisione

Revisione focalizzata sulle integrazioni e sui raccordi, non riedizione integrale dei capitoli preesistenti. Non sono stati controllati tutti gli allegati LEA, tariffe numeriche, norme regionali, procedure aziendali reali o ogni comma esterno alla prosa attivata. Nessuna modifica a manoscritti, source notes, matrice o run-state; unico artefatto creato: questo memo. Fonti correnti consultate il 2 ottobre 2026, con accessi falliti distinti da quelli riusciti.
