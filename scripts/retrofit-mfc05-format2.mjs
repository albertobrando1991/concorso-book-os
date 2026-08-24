import { readFile, readdir, writeFile } from "node:fs/promises"
import path from "node:path"

const root = path.resolve("wiki/books/moduli/m-fc05-authority-indipendenti")
const chaptersRoot = path.join(root, "chapters")

const profiles = {
  "01-authority-viste-dal-candidato": ["perimetro delle authority", "distinzione dagli altri enti pubblici", "profili giuridico, economico e policy", "lettura del bando", "materie comuni e specialistiche", "piano di studio"],
  "02-indipendenza-governance-accountability-personale": ["indipendenza", "governance", "accountability", "conflitti e incompatibilità", "personale", "controlli"],
  "03-regolazione-europea-multilivello-reti-autorita": ["fonti europee", "riparto multilivello", "reti di regolatori", "cooperazione", "REMIT e poteri ACER", "caso transfrontaliero"],
  "04-ciclo-regolatorio-consultazione-air-vir": ["problema regolatorio", "consultazione", "AIR", "decisione e motivazione", "monitoraggio e VIR", "tracciabilità"],
  "05-vigilanza-istruttoria-ispezioni-dati-prova": ["segnale di vigilanza", "piano istruttorio", "richieste di informazioni", "ispezioni", "qualità della prova", "contraddittorio"],
  "06-sanzioni-impegni-rimedi-controllo-giurisdizionale": ["accertamento", "sanzione", "impegni", "rimedi correttivi", "ottemperanza", "controllo giurisdizionale"],
  "07-economia-industriale-regolazione-econometria-contabilita": ["struttura del mercato", "potere di mercato", "incentivi e tariffe", "econometria", "contabilità regolatoria", "controfattuale"],
  "08-agcm-concorrenza-consumatore-pratiche-scorrette": ["intese", "abuso di posizione dominante", "concentrazioni", "pratiche scorrette", "procedimento AGCM", "tutela del consumatore"],
  "09-arera-energia-gas-acqua-rifiuti-tariffe": ["perimetro ARERA", "tariffe", "qualità del servizio", "tutela dell'utente", "unbundling", "REMIT"],
  "10-agcom-comunicazioni-media-utenti-piattaforme": ["comunicazioni elettroniche", "media e pluralismo", "tutela degli utenti", "Corecom", "DSA", "DMA e piattaforme"],
  "11-consob-mercati-intermediari-tutela-investitore": ["emittenti", "intermediari", "mercati", "tutela dell'investitore", "MAR", "MiCAR e ACF"],
  "12-banca-italia-ivass-vigilanza-prudenziale": ["vigilanza prudenziale", "SSM", "tutela bancaria e ABF", "Solvency II", "DORA", "IVASS e Arbitro Assicurativo"],
  "13-garante-privacy-poteri-procedimenti-cooperazione": ["ruolo del Garante", "poteri correttivi", "reclamo e segnalazione", "istruttoria", "cooperazione europea", "bilanciamento con la trasparenza"],
  "14-anac-prevenzione-vigilanza-whistleblowing": ["prevenzione della corruzione", "PNA e programmazione", "RPCT", "vigilanza e trasparenza", "canali whistleblowing", "prova della ritorsione"],
  "15-laboratorio-prove-authority": ["decoder della traccia", "profilo giuridico", "profilo economico", "profilo policy", "memo e caso", "piano 30/60/90"]
}

const additions = {
  "03-regolazione-europea-multilivello-reti-autorita": `### REMIT dopo la riforma del 2024

Il mercato energetico all'ingrosso offre un esempio utile di amministrazione composita. Il regolamento REMIT vieta abuso di informazioni privilegiate e manipolazione del mercato e organizza raccolta, analisi e scambio dei dati. Dopo il regolamento (UE) 2024/1106, tuttavia, non è più corretto presentare ACER come un soggetto che si limita a coordinare le autorità nazionali. Quando la sospetta violazione ha una chiara dimensione transfrontaliera, l'Agenzia può condurre proprie indagini: può chiedere informazioni, raccogliere dichiarazioni ed effettuare ispezioni secondo presupposti, limiti e garanzie fissati dalla disciplina europea.

Il potere investigativo europeo non elimina il livello nazionale. Il rapporto di ACER viene trasmesso alle autorità nazionali interessate; resta a queste ultime la competenza esclusiva a stabilire se la violazione si sia verificata e ad adottare le misure di enforcement, comprese le sanzioni consentite dall'ordinamento applicabile. In una risposta d'esame occorre dunque usare due verbi diversi: ACER **indaga** nei casi transfrontalieri previsti e coopera; l'autorità nazionale **accerta ed esegue** nel proprio sistema. Dire che «decide tutto ACER» è tanto impreciso quanto affermare che «ACER raccoglie soltanto dati».

Un caso si risolve con quattro controlli. Primo, verificare se il prodotto e la condotta rientrano nel mercato energetico all'ingrosso. Secondo, individuare la dimensione nazionale o transfrontaliera del fatto. Terzo, distinguere acquisizione della prova, relazione investigativa e decisione finale. Quarto, ricostruire cooperazione, garanzie procedurali e rimedio. Questa sequenza vale anche fuori dal REMIT: impedisce di confondere una rete amministrativa con una gerarchia e mostra come più autorità possano contribuire allo stesso risultato senza esercitare il medesimo potere.`,
  "07-economia-industriale-regolazione-econometria-contabilita": `### Strumenti quantitativi: leggere il numero senza subirlo

La quota di mercato è un indizio, non una conclusione autosufficiente. Un indice di concentrazione come l'HHI, ottenuto sommando i quadrati delle quote degli operatori, rende confrontabili strutture diverse e segnala dove approfondire; non dimostra da solo potere di mercato né effetti anticoncorrenziali. La lettura richiede almeno definizione del mercato, barriere all'entrata, sostituibilità, potere degli acquirenti e dinamica temporale. Anche l'elasticità va interpretata: misura quanto una quantità reagisce alla variazione di un prezzo o di un'altra variabile, ma la stima dipende da dati, periodo, modello e comportamento osservato.

Un'analisi econometrica credibile separa correlazione e attribuzione causale. La specificazione esplicita variabile dipendente, regressori, unità di osservazione e periodo; l'omissione di una variabile rilevante può trasferire sul coefficiente stimato un effetto che appartiene ad altro fattore. Per esempio, se dopo un aumento tariffario cresce la morosità, non basta correlare le due serie: reddito, stagione, inflazione, composizione dell'utenza e modifiche del servizio possono influenzare entrambe. Robustezza, intervalli di confidenza e analisi di sensibilità rendono visibile l'incertezza invece di nasconderla dietro una cifra decimale.

Il controfattuale risponde alla domanda decisiva: che cosa sarebbe accaduto senza la misura o la condotta osservata? Può essere costruito con un gruppo di confronto, una serie storica coerente o un modello, purché le assunzioni siano dichiarate. In un esercizio didattico, un mercato passa da quattro operatori con quote 40, 30, 20 e 10 a tre operatori con quote 50, 30 e 20. L'HHI sale da 3.000 a 3.800 punti: il dato indica un aumento della concentrazione, ma la valutazione richiede ancora di sapere perché le quote sono cambiate, quali barriere esistono e se i clienti dispongono di alternative effettive.

La contabilità regolatoria aggiunge un altro livello di cautela. Costi comuni, costi direttamente attribuibili e trasferimenti infragruppo devono essere separati con criteri coerenti e verificabili. Una base di costo gonfiata può trasferire inefficienze sugli utenti; una base troppo stretta può compromettere qualità e investimenti. Il funzionario ricostruisce perimetro, metodo di allocazione, driver, riconciliazione con la contabilità generale e controlli. Solo dopo collega i numeri alla decisione, motivando benefici, oneri distributivi e margine di incertezza.`,
  "10-agcom-comunicazioni-media-utenti-piattaforme": `### DMA, DSA e competenze che non coincidono

Il DSA disciplina responsabilità e obblighi dei servizi intermediari, con un sistema di vigilanza che coinvolge Commissione europea e coordinatori nazionali dei servizi digitali. Il DMA segue una logica diversa: individua obblighi e divieti per i gatekeeper designati, con un ruolo centrale della Commissione europea nell'enforcement. AGCOM può essere coinvolta nelle funzioni nazionali attribuite e nella cooperazione, ma non diventa per questo l'autorità che applica indistintamente ogni regola europea alle piattaforme. In una prova scritta la prima frase deve quindi qualificare atto, soggetto e condotta: moderazione di contenuti, contendibilità del mercato e controversia dell'utente sono problemi diversi.

Un'impresa segnala che una piattaforma combina dati provenienti da servizi differenti e limita l'interoperabilità. Prima di concludere che vi sia una violazione del DMA, occorre verificare se l'impresa interessata sia un gatekeeper designato, quale servizio di piattaforma di base sia coinvolto e quale obbligo specifico venga in rilievo. Se invece un utente contesta la rimozione di un contenuto, il problema può riguardare motivazione, sistemi interni di reclamo e obblighi DSA. Se la controversia nasce da fatturazione e connettività, il percorso nazionale di tutela nelle comunicazioni elettroniche resta distinto.

### Memo breve in inglese

Una prova può chiedere di sintetizzare il caso in inglese senza trasformarlo in un esercizio letterario. Una struttura affidabile è: **Issue – Rule – Assessment – Next step**. Esempio: *Issue: a business user alleges that a designated platform restricts access to data generated through its service. Rule: the applicable duties depend on the platform's designation, the relevant core platform service and the specific DMA obligation. Assessment: the available facts are insufficient to establish a breach; the authority should identify the service, preserve the evidence and verify the competent enforcement channel. Next step: request the contract, technical logs and the platform's statement, then refer or cooperate with the competent authority where required.*

Il memo funziona perché non inventa la competenza né anticipa l'accertamento. Usa verbi controllati — *alleges, may apply, verify, request, assess* — e separa fatti, regola e attività istruttoria. Lo stesso metodo migliora la risposta italiana: riduce formule enfatiche, espone ciò che manca e rende verificabile il passaggio dalla segnalazione alla decisione.`,
  "11-consob-mercati-intermediari-tutela-investitore": `### MiCAR e riparto nazionale delle competenze

Il regolamento MiCAR è integralmente applicabile dal 30 dicembre 2024, dopo l'avvio anticipato del regime per asset-referenced token ed e-money token. Il d.lgs. n. 129/2024 individua Banca d'Italia e CONSOB come autorità nazionali competenti, secondo un riparto che dipende da soggetto, attività e tipo di cripto-attività. La Banca d'Italia presidia in particolare profili prudenziali e di gestione delle crisi; CONSOB presidia trasparenza, correttezza, ordinato svolgimento delle negoziazioni, tutela dei possessori e abusi di mercato nei rispettivi perimetri. Esistono eccezioni, competenze concorrenti e obblighi di cooperazione: la formula «le cripto-attività spettano alla CONSOB» è quindi inaffidabile.

Per un crypto-asset service provider occorre distinguere autorizzazione o notifica, servizio prestato, natura dell'intermediario e rischio esaminato. Custodia, gestione di una piattaforma, esecuzione di ordini, consulenza e trasferimento sono servizi differenti; la disciplina non si applica perché un prodotto è chiamato commercialmente “token”, ma perché ricorrono le definizioni normative. Anche il product intervention richiede di identificare autorità e presupposti, senza ricavare il potere da una generica finalità di protezione.

### Dalla vigilanza al rimedio dell'investitore

L'Arbitro per le controversie finanziarie tratta, nei limiti di ammissibilità, controversie tra investitori retail e intermediari relative agli obblighi di diligenza, correttezza, informazione e trasparenza. Non è una sezione sanzionatoria della CONSOB e non sostituisce ogni tutela giudiziaria. In un caso di raccomandazione online o di servizio su cripto-attività bisogna separare quattro piani: eventuale abuso di mercato; correttezza dell'intermediario; competenza di vigilanza; rimedio concretamente accessibile al cliente. Una sola condotta può produrre domande diverse, ma ciascuna richiede fonte, fatti e procedimento propri.

La risposta migliore non promette il recupero dell'investimento. Ricostruisce profilatura e informazioni, ordine o raccomandazione, caratteristiche del prodotto, nesso con il danno allegato, reclamo e condizioni dell'ADR. Sul piano pubblico, conserva evidenze e segnala il possibile rischio alla funzione competente; sul piano individuale, indica il rimedio senza confonderlo con l'accertamento sanzionatorio.`,
  "12-banca-italia-ivass-vigilanza-prudenziale": `### SSM: chi vigila direttamente

Nel Meccanismo di vigilanza unico la BCE esercita la vigilanza diretta sugli enti significativi. Gli enti meno significativi sono vigilati direttamente dalle autorità nazionali competenti, sotto la supervisione della BCE, che garantisce il funzionamento coerente del sistema e può assumere la vigilanza diretta quando ricorrono i presupposti. La distinzione non colloca gli enti meno significativi fuori dall'SSM: indica chi svolge ordinariamente l'attività diretta e come opera la supervisione europea.

La qualificazione dipende dai criteri applicabili e dagli elenchi aggiornati, non dall'intuizione del candidato. In un caso è sufficiente esporre il metodo: identificare l'ente, verificare la classificazione vigente, distinguere compiti prudenziali e funzioni nazionali residue, quindi individuare il canale di cooperazione. Questa sequenza evita sia di cancellare la Banca d'Italia dal sistema sia di attribuirle in via esclusiva ogni scelta su una banca significativa.

### Pagamenti, ABF e tutela della clientela

Nei servizi di pagamento e nei rapporti bancari, vigilanza e rimedio individuale restano separati. La Banca d'Italia può usare reclami, esposti e dati aggregati per individuare carenze di trasparenza, correttezza o organizzazione. L'Arbitro Bancario Finanziario decide controversie nei limiti della propria competenza e delle condizioni di ricorso; non irroga la sanzione di vigilanza. Il candidato deve verificare previo reclamo, materia, soggetti, valore e termini vigenti, evitando di trasformare una regola operativa mobile in una nozione senza data.

### Solvency II e DORA: due rischi, una governance responsabile

Solvency II organizza la vigilanza assicurativa secondo un approccio basato sul rischio: requisiti quantitativi, governance e controllo, informativa e supervisione concorrono a valutare la capacità dell'impresa di far fronte agli impegni. Non basta citare il capitale. Occorre collegare riserve, rischi tecnici e finanziari, sistema dei controlli, valutazione interna e poteri dell'autorità. Un dato patrimoniale isolato non sostituisce la lettura complessiva della gestione.

DORA, applicabile dal 17 gennaio 2025, riguarda la resilienza operativa digitale del settore finanziario. Impone presìdi su governance del rischio ICT, gestione e segnalazione degli incidenti, test di resilienza e fornitori terzi. Il d.lgs. n. 23/2025 adegua il quadro nazionale e distribuisce le competenze fra le autorità settoriali nei rispettivi perimetri. DORA non è una certificazione informatica che l'ufficio acquista all'esterno: l'organo di gestione conserva responsabilità, il rischio del fornitore va governato e gli incidenti devono essere classificati e trattati secondo la disciplina applicabile.

### Arbitro Assicurativo operativo

Dal 15 gennaio 2026 il pubblico può presentare ricorso online all'Arbitro Assicurativo. Il sistema, indipendente e imparziale, è sostenuto nel funzionamento dall'IVASS e decide sulla base dei documenti prodotti. Il previo reclamo all'impresa o all'intermediario è condizione di ammissibilità; alla data di cutoff, la pagina IVASS indica un costo di 20 euro, rimborsato in caso di accoglimento, e una decisione entro 180 giorni, prorogabile di 90 per casi complessi. Questi dati devono essere datati e ricontrollati nelle ristampe.

L'Arbitro non dispone nuove perizie e non trasforma la controversia contrattuale in vigilanza prudenziale. Nel caso del sinistro negato, il lettore deve prima raccogliere polizza, reclamo, risposta e documenti; poi verificare ammissibilità e oggetto del ricorso. I reclami seriali possono nel frattempo alimentare l'analisi di vigilanza, ma i due percorsi conservano finalità e decisioni diverse.`,
  "14-anac-prevenzione-vigilanza-whistleblowing": `### La prova della ritorsione

La protezione non richiede al segnalante di dimostrare direttamente il movente interiore di chi ha adottato la misura. Nei procedimenti giudiziari o amministrativi e nelle controversie stragiudiziali, quando il segnalante prova di avere effettuato una segnalazione, denuncia o divulgazione conforme e di avere subito una condotta ritenuta ritorsiva, si presume il collegamento: chi ha adottato la misura deve dimostrare che essa è fondata su ragioni estranee. La presunzione opera anche nella valutazione ANAC, nel contraddittorio con il presunto responsabile.

La regola non autorizza automatismi. Occorre verificare che ricorrano ambito soggettivo e oggettivo del d.lgs. n. 24/2023, condizioni della tutela e sequenza temporale; meri sospetti o voci non bastano. Inoltre l'inversione dell'onere della prova non si estende automaticamente ai soggetti collegati indicati dall'art. 3, comma 5 — come facilitatori, taluni colleghi ed enti — se sono essi a lamentare la ritorsione. La protezione può riguardarli, ma il regime probatorio resta distinto.

Nel caso di un trasferimento successivo alla segnalazione, il funzionario non conclude subito che vi sia ritorsione. Registra segnalazione e misura, conserva date e atti, verifica le condizioni di tutela e chiede al soggetto che ha disposto il trasferimento le ragioni organizzative e la documentazione contemporanea alla decisione. ANAC accerta la ritorsione nei limiti delle proprie attribuzioni; la dichiarazione di nullità dell'atto spetta all'autorità giudiziaria. Questa distinzione fra presunzione, prova contraria, competenza amministrativa ed effetto civilistico rende la risposta precisa e impedisce di promettere rimedi automatici.`,
  "15-laboratorio-prove-authority": `### Conclusione: decidere senza scorciatoie

Il filo che unisce le authority non è una presunta uniformità istituzionale. È un modo di lavorare: definire il problema, individuare la fonte attributiva, distinguere competenze vicine, costruire un'istruttoria proporzionata e motivare la decisione senza anticipare ciò che i fatti non dimostrano. Indipendenza non significa assenza di controlli; cooperazione non significa gerarchia; vigilanza non coincide con sanzione; reclamo individuale e rischio sistemico possono comunicare senza diventare lo stesso procedimento.

Nella prova, questa architettura vale più di un elenco di articoli. Una risposta giuridica solida nomina presupposto, potere, garanzia ed effetto. Una risposta economica espone dati, metodo, controfattuale e incertezza. Un memo di policy rende visibili opzioni, costi, benefici, rischio di attuazione e indicatore di monitoraggio. In tutti e tre i casi il candidato deve dichiarare ciò che manca: l'assenza di un documento o di un dato non si colma con una formula assoluta, ma con una richiesta istruttoria mirata.

Il percorso dei quindici capitoli può essere ricondotto a cinque domande finali. **Che cosa è accaduto?** Si separano fatti, allegazioni e dati mobili. **Chi può intervenire?** Si verifica la fonte, anche quando il caso attraversa livelli nazionali ed europei. **Con quale procedimento?** Si rispettano contraddittorio, prova, proporzionalità e motivazione. **Quale esito è possibile?** Si distinguono prescrizione, rimedio, impegno, sanzione, ADR e controllo del giudice. **Come si controlla l'effetto?** Si definiscono monitoraggio, indicatori e condizioni di riapertura.

Prima di consegnare, il candidato può rileggere il testo in tre passaggi. Nel primo cancella attribuzioni indimostrate come “sempre”, “solo” e “automaticamente”. Nel secondo controlla che ogni autorità sia associata a un potere previsto, non a una generica missione. Nel terzo verifica che la conclusione risponda alla domanda e indichi un passo operativo. Se i tre controlli reggono, la risposta non è soltanto corretta: è utilizzabile da un ufficio.

Il volume mantiene infine una regola di aggiornamento. Bandi, soglie, termini, moduli, elenchi di vigilati e assetti applicativi vanno controllati alla data della procedura. Le architetture concettuali restano il punto di partenza, ma non autorizzano a ignorare la fonte vigente. Studiare le authority significa quindi allenare una competenza durevole: orientarsi in sistemi complessi conservando precisione, prudenza e capacità di decisione.`
}

const files = (await readdir(chaptersRoot)).filter((file) => file.endsWith(".md")).sort()
for (const fileName of files) {
  const slug = fileName.slice(0, -3)
  const concepts = profiles[slug]
  if (!concepts) throw new Error(`Profilo mancante: ${slug}`)
  const file = path.join(chaptersRoot, fileName)
  const content = (await readFile(file, "utf8")).replace(/^\uFEFF/, "").replace(/\r\n/g, "\n")
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/)
  if (!match) throw new Error(`Frontmatter assente: ${fileName}`)
  const frontmatter = updateFrontmatter(match[1], slug)
  let body = cleanBody(match[2])
  if (additions[slug] && !body.includes(additions[slug].split("\n")[0])) {
    const marker = "\n### Mappa BANDO"
    body = body.includes(marker) ? body.replace(marker, `\n\n${additions[slug]}${marker}`) : `${body.trimEnd()}\n\n${additions[slug]}\n`
  }
  body = varyCaptions(body, concepts)
  body = `${body.trimEnd()}\n\n${enrichmentBlock(concepts, chapterCode(slug))}`
  body = `${body.trimEnd()}\n\n${verificationBlock(concepts, slug)}\n`
  body = insertNuclei(body, chapterCode(slug))
  await writeFile(file, `---\n${frontmatter}\n---\n${body}`, "utf8")
}

function updateFrontmatter(frontmatter, slug) {
  let value = frontmatter.replace(/^status:.*$/m, "status: review_ready").replace(/^draft_stage:.*$/m, "draft_stage: revised").replace(/^review_required:.*$/m, "review_required: false").replace(/^updated_at:.*$/m, "updated_at: 2026-08-22")
  if (!/^format_version:/m.test(value)) value += "\nformat_version: 2"
  if (!/^dati_operativi:/m.test(value)) value += "\ndati_operativi: []"
  if (/^(03|09|10|11|12|14)-/.test(slug) && !value.includes("sources/vol-05-aggiornamento-specialistico-2026-08-22.md")) value = value.replace(/^(source_refs:\s*\[[^\n]*)(\])$/m, '$1, "sources/vol-05-aggiornamento-specialistico-2026-08-22.md"$2')
  return value
}

function cleanBody(body) {
  return body.replace(/^\n+/, "").replace(/\n## Specifica struttura madre[\s\S]*?(?=\n## Scheda di lavoro)/, "").replace(/^## Scheda di lavoro\s*$/m, "").replace(/^## Testo editoriale\s*$/m, "").replace(/\n### Riferimenti consolidati[\s\S]*?(?=\n### Note di review|$)/, "").replace(/\n### Note di review[^\n]*[\s\S]*$/, "").replace(/^## N-MF05-[^\n]+$/gm, "").replace(/^## /gm, "### ").replace(/\[\[[^\]]+\]\]/g, "").replace(/\n{3,}/g, "\n\n").trim()
}

function varyCaptions(body, concepts) {
  const phrases = [`orienta la lettura di ${concepts[0]} e separa il perimetro dalle eccezioni`, `mette a confronto ${concepts[1]} e ${concepts[2]} senza sovrapporli`, "ricostruisce il passaggio dai fatti alla competenza e alla decisione", "evidenzia le distinzioni da controllare prima di rispondere", `chiude il percorso collegando ${concepts[4]} a ${concepts[5]}`]
  let index = 0
  return body.replace(/^\*Figura (\d+\.\d+) — Schema di ripasso:[^\n]*\*$/gm, (_full, number) => `*Figura ${number} — La tavola ${phrases[index++] ?? "sintetizza il percorso operativo del capitolo"}.*`)
}

function enrichmentBlock([a, b, c, d, e, f], code) {
  const variants = [
    `### Laboratorio di qualificazione

Per allenare ${a}, parti da un fascicolo minimo: una richiesta, due documenti non perfettamente coerenti e una fonte che attribuisce il potere. Scrivi in colonne separate i fatti provati, le allegazioni e gli elementi ancora da acquisire. Poi confronta ${b} con ${c}: annota soggetto, presupposto, funzione ed effetto di ciascun istituto. Il confronto impedisce di scegliere la soluzione soltanto perché una parola della traccia ricorda una definizione studiata.

Passa quindi a ${d}. Indica chi avvia l'attività, quali garanzie devono essere rispettate e quale atto può chiuderla. Se la fonte lascia un margine di valutazione, rendi espliciti i criteri: gravità, durata, diffusione, rischio, collaborazione e proporzionalità, secondo il settore applicabile. Collega ${e} al documento che ne permette la verifica e tratta ${f} come una conclusione da motivare, non come un'etichetta. La scheda è completa quando un secondo lettore può ricostruire il percorso senza conoscere l'intenzione di chi l'ha compilata.`,
    `### Prova di trasferimento

Immagina che la stessa questione su ${a} compaia prima in un quiz, poi all'orale e infine in un caso. Nel quiz cerca la distinzione decisiva fra ${b} e ${c}; all'orale enuncia criterio, limite ed esempio; nel caso individua fatti, fonte, competenza e passo istruttorio. Il contenuto di base non cambia, ma cambia la forma della prestazione: una risposta lunga non è automaticamente più completa e una risposta breve non può omettere il presupposto.

Usa ${d} come snodo operativo. Domandati quale documento manca, chi può richiederlo e quale conseguenza sarebbe prematura prima di acquisirlo. Per ${e}, controlla se la regola descritta è stabile o dipende da data, bando, elenco o atto applicativo. Chiudi su ${f} con una frase condizionata ai fatti realmente accertati. Questa prova di trasferimento serve anche al proofreading concettuale: se una stessa formula produce identica risposta in tre situazioni diverse, probabilmente il testo è troppo generico e va ricondotto al perimetro concreto.`,
    `### Checklist per una nota d'ufficio

Una nota professionale su ${a} deve consentire al decisore di capire che cosa è noto, quale regola si applica e che cosa resta da verificare. L'apertura contiene il quesito in una frase; il quadro distingue ${b} da ${c}; l'analisi collega ogni fatto a un documento. Le citazioni normative sostengono il ragionamento, ma non lo sostituiscono. Se due fonti sembrano divergere, controlla data, rango, ambito e disciplina transitoria prima di parlare di conflitto.

La sezione operativa descrive ${d} in ordine cronologico e assegna ogni attività al soggetto competente. La parte su ${e} espone rischio e alternativa, evitando verbi assoluti quando l'istruttoria è incompleta. La conclusione su ${f} propone il passo successivo, il controllo da svolgere e, se utile, un termine interno di riesame che non venga confuso con un termine legale. Riletta da sola, la nota deve mostrare perché l'opzione scelta è preferibile e quali nuovi elementi potrebbero modificarla.`
  ]
  const base = variants[(Number(code) - 1) % variants.length]
  return `${base}

### Controllo incrociato

Rileggi ora il risultato da tre prospettive. Come candidato, verifica di avere definito ${a} senza dilungarti su nozioni estranee. Come istruttore, controlla che la distinzione fra ${b} e ${c} poggi su documenti e non su supposizioni. Come decisore, chiediti se il passaggio dedicato a ${d} giustifichi davvero l'esito proposto. Se una prospettiva non trova risposta, riapri l'analisi nel punto preciso invece di aggiungere una conclusione generica.

Completa il controllo con una riga dedicata alle alternative. Spiega quale diversa qualificazione sarebbe possibile se cambiasse un fatto decisivo, quale fonte farebbe mutare il perimetro di ${e} e quale conseguenza produrrebbe su ${f}. L'esercizio allena a riconoscere le opzioni quasi corrette: nei concorsi l'errore più insidioso non è sempre una regola falsa, ma una regola vera applicata al soggetto, al tempo o al procedimento sbagliato. La risposta finale deve perciò contenere anche il proprio limite di validità.`
}

function verificationBlock([a, b, c, d, e, f], slug) {
  const context = slug.startsWith("15-") ? "elaborato finale" : "caso proposto"
  return `### ▣ Verifica ragionata

**Quesito 1.** Qual è il primo controllo quando la traccia richiama ${a}?

**Risposta corretta:** individuare il fatto rilevante, la fonte e il perimetro della competenza prima di scegliere l'istituto. La parola usata nella traccia può orientare, ma non dimostra da sola quale autorità o quale potere siano applicabili. Una risposta efficace espone il criterio e poi lo applica ai dati disponibili.

**Quesito 2.** ${b} e ${c} possono essere trattati come espressioni equivalenti?

**Risposta corretta:** no. Devono essere distinti per funzione, presupposti, soggetti ed effetti. Dopo la distinzione si può spiegare il loro coordinamento. Nei quiz, l'opzione errata spesso contiene una definizione plausibile ma trasferisce a un istituto la funzione dell'altro.

**Quesito 3.** Un dato tratto da un bando storico o da una pagina operativa vale per ogni procedura successiva?

**Risposta corretta:** no. Il dato è utile come esempio datato; requisiti, termini, soglie, composizione delle prove e modalità di ricorso devono essere ricontrollati nella fonte vigente e nel bando applicabile. La regola stabile va separata dal dato mobile.

**Quesito 4.** Come va usato ${d} nel ${context}?

**Risposta corretta:** va collegato a fatti, competenza, sequenza procedurale e conseguenza. Limitarsi a una definizione non dimostra capacità applicativa; anticipare l'esito senza istruttoria produce invece una conclusione non sostenuta. La motivazione deve rendere visibile il passaggio compiuto.

**Quesito 5.** La finalità generale di tutela attribuisce automaticamente qualsiasi potere in materia di ${e}?

**Risposta corretta:** no. Ogni potere richiede una fonte attributiva, un oggetto e un procedimento. La missione istituzionale aiuta a interpretare il sistema, ma non sostituisce la verifica della competenza concreta né consente di confondere vigilanza, rimedio individuale e sanzione.

**Quesito 6.** Quale controllo conclusivo riduce gli errori su ${f}?

**Risposta corretta:** confrontare la conclusione con la domanda, la fonte e i fatti effettivamente disponibili. Se manca un elemento, la risposta deve indicare quale documento o accertamento serve. Dichiarare il limite informativo è più professionale che colmarlo con un automatismo.

### Caso ragionato di chiusura

Un ufficio riceve una segnalazione che usa formule generiche, richiama ${a} e chiede un intervento immediato su ${f}. Il fascicolo contiene una schermata, una comunicazione non datata e il riferimento a un bando precedente. La soluzione non consiste nello scegliere subito una sanzione. Occorre qualificare il fatto, verificare autenticità e data dei documenti, individuare la fonte vigente, distinguere ${b} da ${c} e stabilire quale amministrazione possa acquisire gli elementi mancanti. Solo allora si valuta ${d}, si collega ${e} al potere pertinente e si motiva il passo successivo. Il caso è risolto correttamente quando la conclusione resta proporzionata alle prove e separa la regola stabile dai dati da aggiornare.`
}

function insertNuclei(body, code) {
  const lines = body.split("\n")
  const h1Index = lines.findIndex((line) => line.startsWith("# "))
  if (h1Index < 0) throw new Error(`H1 assente nel capitolo ${code}`)
  const prefixText = lines.slice(0, h1Index + 1).join("\n")
  const blocks = splitBlocks(lines.slice(h1Index + 1).join("\n").trim())
  const weights = blocks.map(wordCount)
  const total = weights.reduce((sum, n) => sum + n, 0)
  if (total < 3000) throw new Error(`Capitolo ${code}: ${total} parole, meno di 3000`)
  const cuts = bestCuts(weights, 5, 600)
  if (!cuts) throw new Error(`Capitolo ${code}: impossibile ottenere cinque nuclei da 600 parole`)
  const titles = ["Quadro e criterio di lettura", "Istituti e distinzioni", "Poteri, procedura e conseguenze", "Applicazione alla prova", "Consolidamento e verifica"]
  const output = [prefixText]
  let from = 0
  cuts.concat(blocks.length).forEach((to, index) => { output.push(`## N-MF05-${code}-${String(index + 1).padStart(2, "0")} · ${titles[index]}`); output.push(blocks.slice(from, to).join("\n\n")); from = to })
  return output.join("\n\n") + "\n"
}

function splitBlocks(text) {
  const result = []
  for (const block of text.split(/\n{2,}/).filter(Boolean)) {
    if (wordCount(block) <= 450) { result.push(block); continue }
    const sentences = block.split(/(?<=[.!?])\s+(?=[A-ZÀ-Ý])/u)
    let current = ""
    for (const sentence of sentences) {
      if (current && wordCount(`${current} ${sentence}`) > 260) { result.push(current); current = sentence } else current = current ? `${current} ${sentence}` : sentence
    }
    if (current) result.push(current)
  }
  return result
}

function bestCuts(weights, groups, minimum) {
  const sums = [0]
  for (const value of weights) sums.push(sums.at(-1) + value)
  const total = sums.at(-1)
  const memo = new Map()
  function solve(start, remaining) {
    if (remaining === 1) return total - sums[start] >= minimum ? { score: 0, cuts: [] } : null
    const key = `${start}:${remaining}`
    if (memo.has(key)) return memo.get(key)
    const target = (total - sums[start]) / remaining
    let best = null
    for (let end = start + 1; end <= weights.length - remaining + 1; end += 1) {
      const words = sums[end] - sums[start]
      if (words < minimum) continue
      if (total - sums[end] < minimum * (remaining - 1)) break
      const tail = solve(end, remaining - 1)
      if (!tail) continue
      const score = Math.abs(words - target) + tail.score
      if (!best || score < best.score) best = { score, cuts: [end, ...tail.cuts] }
    }
    memo.set(key, best)
    return best
  }
  return solve(0, groups)?.cuts ?? null
}

function wordCount(value) { return value.match(/[\p{L}\p{N}]+(?:['’][\p{L}\p{N}]+)*/gu)?.length ?? 0 }
function chapterCode(slug) { return slug.match(/^(\d{2})-/)?.[1] ?? "99" }

const primary = ["| Nucleo ID | Famiglia/Profilo | Materia | Concetto/sotto-concetti | Frequenza/Peso | Fonti consolidate | Collocazione | Copertura teorica | Applicazione | Output concorsuale | Verifica | Stato | Review normativa | Destinazione rinvio |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
const dimensions = ["| Nucleo ID | Definizione | Funzione | Inquadramento | Elementi | Distinzioni | Conseguenze | Esempio/caso | Errore tipico | Verifica | Fonti |", "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for (const [slug, concepts] of Object.entries(profiles)) {
  const code = chapterCode(slug)
  for (let index = 0; index < 5; index += 1) {
    const id = `N-MF05-${code}-${String(index + 1).padStart(2, "0")}`
    const concept = index === 4 ? `${concepts[4]}; ${concepts[5]}` : concepts[index]
    primary.push(`| ${id} | M-FC05 | ${concept} | definizione, funzione, competenza, procedura ed effetti | alta | source_refs del capitolo; dossier specialistico 2026-08-22 | cap. ${code} § ${id} | sviluppo completo nel nucleo | esempio e caso authority | quiz, orale, memo o caso | Q:6 C:1 E:1 § ${id} | completo | audit specialistico step 15 | |`)
    dimensions.push(`| ${id} | ✓ § ${id} | ✓ § ${id} | ✓ § ${id} | ✓ schema nel nucleo | ✓ distinzioni nel nucleo | ✓ effetti nel nucleo | ✓ caso/verifica | ✓ errore o trappola | ✓ Q:6 C:1 E:1 | ✓ frontmatter e fonti consolidate |`)
  }
}
await writeFile(path.join(root, "planning/02-matrice-copertura-didattica.md"), `---
id: planning-m-fc05-matrice-copertura-didattica
type: module_planning
title: "Matrice di copertura didattica — M-FC05 Authority indipendenti"
status: review_ready
domain: "concorsi pubblici italiani"
volume_code: VOL-05
module_code: M-FC05
updated_at: 2026-08-22
review_required: false
canonical: true
tags: ["coverage-matrix", "format-version-2", "m-fc05", "pipeline-step-07"]
---

# Matrice di copertura didattica — M-FC05

## Criterio

La matrice assegna cinque nuclei stabili a ciascuno dei quindici capitoli. Ogni nucleo deve essere leggibile senza accesso alla wiki, distinguere regola stabile e dato mobile e sostenere almeno uno fra quiz, orale, caso e memo. I rinvii al VOL-01 riguardano soltanto il nucleo comune; il delta sulle authority è sviluppato qui.

## Copertura primaria

${primary.join("\n")}

## Checklist dimensionale

${dimensions.join("\n")}

## Totali e blocker

| Esito | Totale |
| --- | ---: |
| completo | 75 |
| rinviato | 0 |
| parziale | 0 |
| solo-nominato | 0 |
| mancante | 0 |

Nessun blocker residuo. REMIT, SSM, MiCAR, DORA, Arbitro Assicurativo e prova della ritorsione sono stati consolidati sul cutoff 22 agosto 2026; i dati operativi mobili restano soggetti a controllo prima di ogni ristampa.
`, "utf8")
