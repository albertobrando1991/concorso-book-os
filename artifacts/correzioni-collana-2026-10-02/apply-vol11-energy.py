from pathlib import Path
exec(Path('artifacts/correzioni-collana-2026-10-02/apply-vol11-pc.py').read_text(encoding='utf8').split("p=next(B.glob('10-")[0])
S='sources/vol-11-energia-sostenibilita-verifica-2026-10-03'
p=next(B.glob('12-*.md'));t=p.read_text(encoding='utf8')
t=t.replace('è stato modificato da un correttivo nel 2025','è stato modificato dal D.Lgs. 26 novembre 2025, n. 178, e da successivi interventi. Il D.Lgs. 9 gennaio 2026, n. 5, efficace dal 4 febbraio 2026, attua RED III')
t=add(t,12,3,'''### Tre casi e i termini del testo vigente

L'art. 6 collega **allegato A ad attività libera, B a PAS, C ad autorizzazione unica**. Il progetto unitario comprende gli interventi della stessa fonte in aree vicine riconducibili allo stesso centro di interessi: frazionarli artificiosamente non abbassa la potenza rilevante.

**Caso A:** fotovoltaico da 80 kW integrato sul tetto esistente della palestra, stessa inclinazione e orientamento, nessun cambio di sagoma, superficie entro la copertura. La traccia esclude vincoli, interferenze e ulteriori condizioni ostative e attesta disponibilità e compatibilità. Rientra nell'allegato A, sezione I, lettera a), che contempla potenza inferiore a 12 MW. Restano norme tecniche, modello unico ove prescritto e adempimenti settoriali. Se emerge un bene culturale o un'area protetta, non si conserva automaticamente la conclusione: si applica l'art. 7 con i relativi raccordi.

**Caso B:** fotovoltaico a terra da 6 MW in area industriale, disponibilità dell'area e compatibilità accertate, esclusa la ricorrenza di altre fattispecie. L'allegato B, sezione I, lettera d), comprende la fascia da 5 a 15 MW: PAS. **Caso C:** impianto fotovoltaico da 20 MW che non rientra in A o B: allegato C, sezione I, lettera a), autorizzazione unica regionale o dell'ente delegato, con valutazioni ambientali pertinenti. L'allegato C, sezione II, attribuisce allo Stato le fattispecie ivi individuate, fra cui impianti elettrici rinnovabili oltre 300 MW. La scala A/B/C precede la lettura della sola potenza.

Per la **PAS**, il Comune procedente è quello individuato dall'art. 8, anche in caso di più territori. I termini ordinari sono 30 giorni; diventano 45 se occorrono assensi comunali e 60 nel percorso con altre amministrazioni, secondo le condizioni della conferenza. Integrazioni, sospensioni e dissensi qualificati impediscono la scorciatoia «il giorno 31 si costruisce sempre». Nei casi dei commi 12 e 12-bis, VIncA e titolo edilizio sono preventivi; la PAS va poi presentata entro 90 giorni dall'acquisizione pertinente. Il titolo perfezionato acquista efficacia con la pubblicazione prevista nel Bollettino regionale. I lavori devono iniziare entro due anni e concludersi entro tre dall'avvio, salvi gli impedimenti di forza maggiore previsti.

Per l'**autorizzazione unica**, l'art. 9 distingue Regione/delegato e MASE secondo le sezioni dell'allegato C. La conferenza si conclude entro 120 giorni dalla prima riunione, con sospensione massima di 90 giorni per VIA, 60 per VIncA e 120 quando ricorrono entrambe. Lo screening, quando necessario, precede il procedimento; per la VIA regionale opera il raccordo con il PAUR nei casi stabiliti. Questi sono termini di fasi definite, non una promessa che ogni domanda incompleta riceva titolo dopo 120 giorni dal deposito.''')
t=add(t,12,4,'''### Obblighi, APE e diagnosi: soggetti diversi

Nel testo del D.Lgs. 102/2014 verificato il 3 ottobre 2026, l'art. 8 prevede diagnosi energetiche quadriennali per le grandi imprese, con la disciplina dei sistemi ISO 50001 che includano diagnosi conforme e l'esclusione per grandi imprese sotto 50 tep annui. Gli energivori seguono la specifica disciplina anche indipendentemente dalla dimensione. Non è un obbligo indistinto di ogni PMI o Comune.

L'art. 5 regola il programma di riqualificazione pari almeno al 3% annuo della superficie utile climatizzata degli immobili della **PA centrale**, con perimetro ed esclusioni: non attribuisce automaticamente la stessa percentuale a ciascun Comune. Gli enti locali concorrono attraverso programmazione e misure proprie. Una diagnosi individua usi e interventi; l'**APE** certifica la prestazione secondo il D.Lgs. 192/2005. L'art. 6 richiede l'APE e la sua affissione per edifici utilizzati dalla PA e aperti al pubblico sopra 250 m², nei presupposti della norma. La validità massima è dieci anni, subordinata ai controlli, con aggiornamento quando l'intervento modifica la classe.

La direttiva EED 2023/1791 e la EPBD 2024/1275 orientano un quadro più ambizioso. Al 1° ottobre 2026 la Commissione ha però contestato all'Italia il recepimento EED incompleto e il mancato invio del progetto di piano nazionale di ristrutturazione degli edifici. Scadenza europea, norma nazionale e attuazione non sono sinonimi. Per la decisione concreta si applica il testo nazionale pertinente senza attribuire a un Comune obblighi numerici desunti automaticamente da una direttiva.

### Calcolo completo di risparmio e ritorno

**Dati didattici:** baseline elettrica normalizzata della palestra 120.000 kWh/anno; consumo atteso dopo intervento 90.000, stesso servizio; prezzo assunto 0,22 €/kWh; investimento 36.000 euro; maggior manutenzione 600 euro/anno; fattore emissivo illustrativo 0,25 kg CO₂e/kWh.

Risparmio: 120.000 − 90.000 = **30.000 kWh**, ossia **25%**. Beneficio energetico lordo: 30.000 × 0,22 = **6.600 euro/anno**; beneficio netto: 6.600 − 600 = **6.000**. Ritorno semplice: 36.000/6.000 = **6 anni**. Emissioni evitate nel modello: 30.000 × 0,25 = **7.500 kg, cioè 7,5 t CO₂e/anno**. Il fattore è un'ipotesi della prova, non il fattore nazionale da usare in ogni inventario.

Si misurano kWh, orari, comfort e condizioni climatiche; il risparmio reale va normalizzato. Il ritorno semplice non sconta i flussi e non esaurisce la convenienza. Il PNIEC organizza il quadro energia-clima; il PNACC orienta l'adattamento. Per la palestra si affiancano riduzione dei consumi e gestione delle ondate di calore, con un indicatore separato delle ore fuori comfort: emissioni inferiori non provano da sole maggiore resilienza.''')
t=add(t,12,5,'''### Partecipazione, controllo e perimetro

L'art. 31 del D.Lgs. 199/2021 ammette, fra gli altri, persone fisiche, PMI, enti territoriali, enti di ricerca/formazione, enti religiosi e Terzo settore nelle categorie previste. Per le imprese la partecipazione non può costituire attività commerciale e industriale principale; il controllo deve fare capo ai soggetti ammessi situati nel territorio degli impianti di condivisione. Una grande impresa non può essere trattata automaticamente come una PMI socia avente controllo.

Il testo distingue la **zona di mercato**, entro cui può operare la condivisione, dalla **medesima cabina primaria**, requisito per incentivi e restituzioni nei presupposti specifici. Una CER può articolarsi in più configurazioni: non si sommano liberamente punti di cabine differenti per calcolare il beneficio di una sola configurazione. Il cliente conserva scelta del venditore e diritto di recesso, salvi corrispettivi equi e proporzionati per investimenti concordati; contratto e statuto devono disciplinare riparto e responsabilità.

### Esercizio TIAD: il minimo va calcolato ora per ora

Tutti i punti del caso sono nella medesima cabina primaria; le misure sono già quelle rilevanti per il TIAD e la configurazione soddisfa i requisiti del servizio. Nella prima ora l'energia immessa è 80 kWh e quella prelevata 50: condivisa **50**. Nella seconda sono 20 e 70: condivisa **20**. Totale condiviso: **70 kWh**.

Fare il minimo fra i totali, min(100,120)=100, è errato: compensa ore diverse. Se nella prima ora l'impianto aveva prodotto 100 kWh e autoconsumato fisicamente 20, l'immissione rilevante resta 80; non si usa la produzione lorda di 100. Nel TIAD l'energia autoconsumata è la condivisione riferita alla medesima cabina primaria; l'energia incentivabile richiede anche i requisiti del sostegno. I 70 kWh non consentono di promettere un importo senza tariffa, ammissibilità degli impianti e regole GSE applicabili.''')
save(p,t)
p=next(B.glob('13-*.md'));t=p.read_text(encoding='utf8')
t=add(t,13,3,'''### Come scegliere e applicare il regime

Nel **Regime 1** la misura deve fornire il contributo sostanziale previsto all'obiettivo climatico o ambientale e rispettare il DNSH rispetto agli altri obiettivi. Nel **Regime 2** deve evitare il danno significativo senza che le sia attribuito quel contributo sostanziale. Regime 2 non significa nessun controllo. La guida 2024 considera anche contributi sostanziali a risorsa idrica ed economia circolare: Regime 1 non equivale sempre alla sola mitigazione.

Il soggetto attuatore ricava regime e requisiti dagli impegni della misura, dalla mappatura, dalla scheda pertinente e dalle istruzioni dell'amministrazione titolare. Non sceglie la colonna meno onerosa. **Esempio didattico tratto dalla logica della guida, nuova costruzione:** il riferimento NZEB della traccia è 50 kWh/m² anno di energia primaria non rinnovabile. Nel regime climatico 1 la riduzione del 20% porta al riferimento di 40; nel regime 2 il riferimento resta 50. Il progetto da 45 non dimostra il requisito energetico del primo regime pur rientrando nel secondo riferimento. Restano comunque gli altri requisiti, come adattamento e rifiuti; il solo numero energetico non conclude l'intero DNSH. Questo esempio non si trasferisce automaticamente a una ristrutturazione, che richiede la propria scheda.''')
t=add(t,13,4,'''### Palestra: applicare un criterio CAM reale

Per il caso assumiamo progettazione interna avviata e validata dopo il 2 febbraio 2026, conforme al **D.M. 24 novembre 2025**, e gara avviata nell'ottobre 2026. Si applicano i nuovi CAM edilizia. Il decreto conserva casi transitori per PFTE di appalti integrati e progetti esecutivi di lavori conformi ai CAM 2022, con pubblicazione del bando o invio dell'invito entro tre mesi dalla validazione. La circolare MASE firmata il 10 aprile 2026 chiarisce che conta la conformità al regime precedente, non soltanto una validazione materialmente anteriore al 2 febbraio; per progettazione interna non ancora validata a quella data occorre l'adeguamento. La data della gara, da sola, non risolve ogni caso transitorio.

Nel caso la riqualificazione comprende movimenti di terra sul giardino. Il **criterio 2.5.2, Conservazione dello strato superficiale del terreno**, richiede rimozione e accantonamento separato degli orizzonti organico e attivo per riutilizzarli a verde. Se il profilo non è noto, il progetto comprende l'analisi pedologica che determina lo spessore. Non si prescrive uno spessore universale copiato da un altro cantiere.

**Dati fittizi:** l'indagine individua 0,25 m da salvaguardare su 300 m²: volume in posto **75 m³**. Il capitolato prevede area separata, protezione e riuso; eventuale variazione volumetrica del materiale sciolto va gestita nella logistica, senza confonderla con il volume in posto.

| Fase | Evidenza richiesta | Responsabilità e controllo |
|---|---|---|
| Progetto | Relazione CAM, profilo pedologico e relazione specialistica | Progettista; verifica coerenza fra 300 m², 0,25 m e 75 m³ |
| Gara | Prescrizione di separazione, conservazione e riuso nei documenti contrattuali | Stazione appaltante; controllo presenza del requisito |
| Cantiere | Area identificata, registrazioni e riscontro del materiale separato | Esecutore; controllo della direzione lavori |
| Chiusura | Riscontro del riuso a verde previsto e gestione motivata degli scostamenti | Direzione lavori e verifica finale competente |

Una variante amplia lo scavo a 360 m² con lo stesso profilo accertato: il volume diventa **90 m³**. Prima dell'esecuzione si aggiornano progetto, logistica e prove; una dichiarazione generica «materiali ecologici» non documenta il criterio. L'evidenza può concorrere a una verifica DNSH pertinente, ma non certifica automaticamente tutti i sei obiettivi.''')
t=add(t,13,5,'''### Le quattro fasi della LCA

La **definizione di obiettivo e campo** stabilisce funzione, unità funzionale, confini e uso del risultato. L'**inventario** raccoglie e quantifica flussi di energia, materiali, emissioni e rifiuti. La **valutazione degli impatti** collega quei flussi alle categorie ambientali con il metodo scelto. L'**interpretazione** valuta risultati, completezza, sensibilità e limiti e può richiedere di tornare alle fasi precedenti. Sono fasi metodologiche iterative, diverse dalla sequenza fisica produzione–uso–fine vita.

### LCC numerico su cinque anni

Due alternative garantiscono la stessa funzione e durata. A costa 10.000 euro iniziali, 3.000 annui per uso/manutenzione e 1.000 al termine del quinto anno. B costa 14.000 iniziali, 2.000 annui e 500 a fine vita. Assumiamo tasso reale **3%**, costi annuali a fine anno, prezzi reali costanti, nessuna imposta o valore residuo.

Il valore attuale è costo iniziale + somma dei costi dell'anno t divisi per (1,03)^t. Il fattore per cinque annualità è 4,579707. Per A: 10.000 + 3.000 × 4,579707 + 1.000/(1,03)^5 = **24.601,73 euro**. Per B: 14.000 + 2.000 × 4,579707 + 500/(1,03)^5 = **23.590,72 euro**. B costa inizialmente di più ma ha LCC inferiore di **1.011,01 euro** nelle ipotesi date.

Il confronto va riesaminato se cambiano durata, tasso o costi. Chilogrammi di CO₂e, consumo idrico e rifiuti restano grandezze fisiche: non si sommano agli euro. Eventuali esternalità ambientali monetizzate richiedono metodo, dati e condizioni giuridiche dichiarati; qui non sono incluse. Il LCC più basso non prova da solo l'impatto ambientale minore.''')
save(p,t)
print('Capitoli 12–13 integrati con fonti, casi FER/CER, diagnosi, DNSH, CAM e LCC.')
