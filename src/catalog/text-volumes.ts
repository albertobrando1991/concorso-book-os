export type TextVolumeTier = "base" | "standard" | "vertical" | "premium"
export type TextLaunchWave = "foundation" | "first" | "second" | "third" | "continuous"

export interface TextVolumeDigitalIntroduction {
  summary: string
  topics: string[]
  whyDifferent: string
}

export interface TextVolume {
  code: string
  title: string
  shortTitle: string
  tier: TextVolumeTier
  launchWave: TextLaunchWave
  modules: string[]
  bookIds: string[]
  audience: string
  promise: string
  verticals: string[]
  digitalIntroduction?: TextVolumeDigitalIntroduction
  /**
   * Book id of a volume-level book holding chapters that open (low outline_section,
   * e.g. "how to use this volume") or close (outline_section >= 50, e.g. a final
   * simulation) the compiled volume, in addition to the specialist modules in bookIds.
   */
  orientationBookId?: string
}

export const TEXT_VOLUME_BOOK_ID_PREFIX = "volumi/"

export const TEXT_VOLUME_CATALOG: TextVolume[] = [
  {
    code: "VOL-01",
    title: "Manuale base PA",
    shortTitle: "Base PA",
    tier: "base",
    launchWave: "foundation",
    modules: [],
    bookIds: ["il-metodo-bando"],
    audience: "Tutti i candidati ai concorsi pubblici",
    promise: "Metodo, materie comuni essenziali, prove e strumenti riusabili.",
    verticals: ["B-PA01/B-PA11", "Ricettario digitale collegato", "Bando Decoder e planner"],
    digitalIntroduction: {
      summary:
        "Il Manuale base PA è il punto di partenza della collana per chi prepara concorsi pubblici in amministrazioni e profili diversi. Accompagna il candidato dalla lettura del bando alla costruzione del piano, dallo studio delle materie comuni all'allenamento delle prove, fino al ripasso e alla gestione di più selezioni. L'obiettivo non è aggiungere un altro insieme di nozioni, ma dare ordine alla preparazione: capire che cosa studiare, con quale profondità, in quale sequenza e come verificare i progressi. Al termine, il lettore dispone di un nucleo riutilizzabile di conoscenze e di un metodo per adattarlo ai contenuti specifici del concorso scelto.",
      topics: [
        "Come leggere il bando, riconoscere prove, materie e priorità e trasformare queste informazioni in un piano di studio da 30, 60 o 90 giorni.",
        "Il nucleo comune dei concorsi pubblici: Costituzione, diritto amministrativo, pubblico impiego, trasparenza, anticorruzione, privacy, contabilità e contratti pubblici essenziali.",
        "Le competenze trasversali richieste nelle prove: logica, comprensione del testo, informatica, inglese e quesiti situazionali.",
        "Come affrontare quiz, prova scritta, casi pratici e colloquio orale con tecniche, simulazioni e strategie di risposta.",
        "Come usare il diario degli errori, il ripasso, le checklist e il Ricettario operativo per adattare il metodo a profili e concorsi diversi."
      ],
      whyDifferent:
        "Questo non è un manuale da leggere in ordine e dimenticare dopo una prova. Integra teoria essenziale, metodo e strumenti operativi: parte dal bando, assegna priorità alle materie, trasforma ogni capitolo in attività verificabili e conserva ciò che impari come base per i concorsi successivi. Invece di accumulare materiali, costruisci un sistema personale che collega studio, quiz, errori, simulazioni e ripasso. Il risultato è una preparazione modulare: il nucleo comune resta, mentre cambiano soltanto gli approfondimenti richiesti dal profilo specifico."
    }
  },
  {
    code: "VOL-02",
    title: "Enti locali, Camere di commercio e Polizia locale",
    shortTitle: "Enti locali",
    tier: "standard",
    launchWave: "first",
    modules: ["M-FL01", "M-FL02", "M-FL03", "M-FL04"],
    bookIds: [
      "moduli/m-fl01-comuni-unioni",
      "moduli/m-fl02-regioni-province-citta-metropolitane",
      "moduli/m-fl03-camere-commercio",
      "moduli/m-fl04-polizia-locale"
    ],
    audience: "Comuni, Unioni, Regioni, Province, CCIAA e Polizia locale",
    promise: "Modulo standard per il bacino più ricorrente degli enti territoriali.",
    verticals: ["TUEL e servizi locali", "Registro Imprese CCIAA", "Codice della strada e sicurezza urbana"],
    orientationBookId: "vol-02-enti-locali-polizia-locale"
  },
  {
    code: "VOL-03",
    title: "Funzioni centrali, Fisco, Previdenza e Ispettivo",
    shortTitle: "Funzioni centrali e fisco",
    tier: "standard",
    launchWave: "first",
    modules: ["M-FC01", "M-FC02", "M-FC03"],
    bookIds: [
      "moduli/m-fc01-ministeri",
      "moduli/m-fc02-agenzie-fiscali",
      "moduli/m-fc03-enti-non-economici"
    ],
    audience:
      "Ministeri, PCM, Avvocatura dello Stato, Agenzie fiscali, riscossione, INPS, INAIL ed enti pubblici non economici",
    promise: "Percorso specialistico per funzioni centrali generaliste, fisco, dogane, previdenza e ispettivo.",
    verticals: [
      "Ministeri, PCM e Avvocatura dello Stato",
      "ADM dogane e accise",
      "Tecniche ispettive INPS/INAIL",
      "Previdenza e servizi EPNE"
    ]
  },
  {
    code: "VOL-04",
    title: "Giustizia e UPP",
    shortTitle: "Giustizia",
    tier: "standard",
    launchWave: "third",
    modules: ["M-FC04"],
    bookIds: ["moduli/m-fc04-giustizia"],
    audience: "Ufficio per il processo, cancelleria, giustizia minorile e penitenziaria",
    promise: "Modulo giudiziario collegato al base e distinto dalle carriere magistratuali premium.",
    verticals: ["Ordinamento giudiziario", "PCT e uffici giudiziari", "Raccordo M-SP03"]
  },
  {
    code: "VOL-05",
    title: "Authority e regolazione",
    shortTitle: "Authority",
    tier: "premium",
    launchWave: "third",
    modules: ["M-FC05"],
    bookIds: ["moduli/m-fc05-authority-indipendenti"],
    audience: "AGCM, ARERA e autorità indipendenti",
    promise: "Modulo premium per target ristretto, tecnico-regolatorio e ad alto valore.",
    verticals: ["Regolazione mercati", "Compliance", "Istruttorie e provvedimenti"]
  },
  {
    code: "VOL-06",
    title: "Scuola, Universita, Ricerca, Cultura",
    shortTitle: "Istruzione e cultura",
    tier: "standard",
    launchWave: "first",
    modules: ["M-IR01", "M-IR02", "M-IR03", "M-IR04"],
    bookIds: [
      "moduli/m-ir01-scuola",
      "moduli/m-ir02-universita-afam",
      "moduli/m-ir03-enti-ricerca",
      "moduli/m-ir04-cultura-beni-culturali"
    ],
    audience: "Scuola, università, AFAM, enti di ricerca e MiC",
    promise: "Famiglia ampia con sotto-percorsi editoriali distinti per amministrativi e specialisti.",
    verticals: ["DSGA", "Project/grant manager ricerca", "Archivisti, bibliotecari e beni culturali"]
  },
  {
    code: "VOL-07",
    title: "Sanità amministrativa e professioni sanitarie",
    shortTitle: "Sanità",
    tier: "vertical",
    launchWave: "first",
    modules: ["M-SA01", "M-SA02", "M-SA03", "M-SA04"],
    bookIds: [
      "moduli/m-sa01-sanita-amministrativa",
      "moduli/m-sa02-professioni-sanitarie",
      "moduli/m-sa03-dirigenza-medica-sanitaria",
      "moduli/m-sa04-tecnici-sanitari-prevenzione"
    ],
    audience: "ASL, aziende ospedaliere, professioni sanitarie, dirigenza e tecnici sanitari",
    promise: "Volume verticale per bandi sanitari con forte bisogno di review settoriale.",
    verticals: ["Infermieristica e professioni sanitarie", "Dirigenza medica/non medica", "TSLB, TSRM, prevenzione"]
  },
  {
    code: "VOL-08",
    title: "ICT, digitale, cybersecurity e dati",
    shortTitle: "ICT e cyber",
    tier: "vertical",
    launchWave: "second",
    modules: ["M-TR01"],
    bookIds: ["moduli/m-tr01-ict-trasformazione-digitale"],
    audience: "Profili ICT, data, cyber e trasformazione digitale nella PA",
    promise: "Modulo verticale tecnico per profili digitali non coperti dal base.",
    verticals: ["Cybersecurity", "Dati e interoperabilità", "Servizi digitali PA"]
  },
  {
    code: "VOL-09",
    title: "Appalti, PNRR e procurement",
    shortTitle: "Appalti e PNRR",
    tier: "vertical",
    launchWave: "first",
    modules: ["M-TR02"],
    bookIds: ["moduli/m-tr02-appalti-pnrr-fondi-ue"],
    audience: "RUP, procurement, fondi UE, PNRR e uffici gare",
    promise: "Verticale ad alta domanda per contratti pubblici avanzati e gestione fondi.",
    verticals: ["RUP e ciclo appalto", "PNRR e fondi UE", "Esecuzione e controlli"]
  },
  {
    code: "VOL-10",
    title: "Tecnico-ingegneristico, territorio, lavori pubblici",
    shortTitle: "Tecnico-ingegneristico",
    tier: "vertical",
    launchWave: "second",
    modules: ["M-TR03"],
    bookIds: ["moduli/m-tr03-tecnico-ingegneristico"],
    audience: "Ingegneri, architetti, tecnici PA, territorio e lavori pubblici",
    promise: "Verticale profondo per profili tecnici che non possono stare nel modulo generalista.",
    verticals: ["Ingegneria civile PA", "Urbanistica ed edilizia", "MIT e lavori pubblici"]
  },
  {
    code: "VOL-11",
    title: "Ambiente, protezione civile e sostenibilità",
    shortTitle: "Ambiente",
    tier: "vertical",
    launchWave: "third",
    modules: ["M-TR04"],
    bookIds: ["moduli/m-tr04-ambiente-protezione-civile"],
    audience: "MASE, ambiente, protezione civile, sostenibilità e controlli territoriali",
    promise: "Verticale tecnico-ambientale con fonti settoriali e casi operativi.",
    verticals: ["Valutazioni ambientali", "Protezione civile", "Sostenibilita e controlli"]
  },
  {
    code: "VOL-12",
    title: "Carriere speciali premium",
    shortTitle: "Carriere premium",
    tier: "premium",
    launchWave: "third",
    modules: ["M-SP01", "M-SP02", "M-SP03", "M-SP04"],
    bookIds: [
      "moduli/m-sp01-forze-ordine",
      "moduli/m-sp02-vigili-fuoco",
      "moduli/m-sp03-magistratura-avvocatura-notariato",
      "moduli/m-sp04-prefettizia-diplomatica"
    ],
    audience: "Forze di polizia, VVF, magistratura ordinaria, Avvocatura dello Stato, notariato, carriera prefettizia e carriera diplomatica",
    promise: "Metodo e strategia per selezioni ad alta barriera.",
    verticals: ["Magistratura", "Diplomazia e prefettizia", "VVF direttivo tecnico"]
  }
]

export const TEXT_CATALOG_MODULE_COUNT = new Set(TEXT_VOLUME_CATALOG.flatMap((volume) => volume.modules)).size

export function isSpecialistTextVolume(volume: TextVolume) {
  return volume.code !== "VOL-01" && volume.modules.length > 0
}

export const TEXT_CATALOG_PACKAGE_RULES = [
  {
    key: "standard",
    label: "Pacchetto Standard",
    formula: "Libro base + 1 modulo di famiglia",
    description: "Candidati amministrativi, contabili, ispettivi non tecnici, servizi al pubblico e front-office."
  },
  {
    key: "vertical",
    label: "Pacchetto Verticale",
    formula: "Libro base + modulo di famiglia + verticale",
    description: "Profili tecnici, ICT/cyber, sanitari clinici, appalti avanzati, ispettivi e territorio."
  },
  {
    key: "premium",
    label: "Pacchetto Premium",
    formula: "Libro base + modulo premium",
    description: "Carriere speciali, Authority, magistratura, diplomazia, prefettizia e VVF direttivo."
  }
]

export function textBookIdFromPath(bookPath: string) {
  return bookPath.replace(/^books\//, "").replace(/\/index\.md$/, "")
}

export function normalizeTextBookId(bookId: string) {
  const normalized = bookId.replace(/^books\//, "").replace(/\/index\.md$/, "")
  const lowercase = normalized.toLowerCase()
  const volumeCode = lowercase.replace(/^volumi\//, "")

  if (/^vol-\d{2}$/.test(volumeCode)) {
    const volume = TEXT_VOLUME_CATALOG.find((item) => item.code.toLowerCase() === volumeCode)

    if (volume && !isSpecialistTextVolume(volume)) return volume.bookIds[0] || normalized

    return `${TEXT_VOLUME_BOOK_ID_PREFIX}${volumeCode}`
  }

  if (/^m-[a-z0-9-]+$/.test(lowercase)) return `moduli/${lowercase}`

  return normalized
}

export function textVolumeBookId(volume: TextVolume) {
  if (!isSpecialistTextVolume(volume)) return volume.bookIds[0] || "il-metodo-bando"

  return `${TEXT_VOLUME_BOOK_ID_PREFIX}${volume.code.toLowerCase()}`
}

export function isTextVolumeBookId(bookId: string) {
  return normalizeTextBookId(bookId).startsWith(TEXT_VOLUME_BOOK_ID_PREFIX)
}

export function findTextVolumeForBookId(bookId: string) {
  const normalized = normalizeTextBookId(bookId)

  if (normalized.startsWith(TEXT_VOLUME_BOOK_ID_PREFIX)) {
    const code = normalized.replace(TEXT_VOLUME_BOOK_ID_PREFIX, "")

    return TEXT_VOLUME_CATALOG.find((volume) => volume.code.toLowerCase() === code)
  }

  return TEXT_VOLUME_CATALOG.find((volume) => volume.bookIds.includes(normalized))
}

export function bookIdsForTextVolumeBookId(bookId: string) {
  const volume = findTextVolumeForBookId(bookId)

  return volume && isTextVolumeBookId(bookId) ? volume.bookIds : []
}

export function textVolumeTierLabel(tier: TextVolumeTier) {
  if (tier === "base") return "Libro base"
  if (tier === "standard") return "Standard"
  if (tier === "vertical") return "Verticale"

  return "Premium"
}

export function textLaunchWaveLabel(wave: TextLaunchWave) {
  if (wave === "foundation") return "Fondazione"
  if (wave === "first") return "Prima ondata"
  if (wave === "second") return "Seconda ondata"
  if (wave === "third") return "Terza ondata"

  return "Ondata continua"
}

export function textCatalogSortRank(bookId: string) {
  const normalized = normalizeTextBookId(bookId)

  if (normalized.startsWith(TEXT_VOLUME_BOOK_ID_PREFIX)) {
    const volumeIndex = TEXT_VOLUME_CATALOG.findIndex((volume) => textVolumeBookId(volume) === normalized)

    return volumeIndex === -1 ? 10_000 : volumeIndex * 100
  }

  const volumeIndex = TEXT_VOLUME_CATALOG.findIndex((volume) => volume.bookIds.includes(normalized))

  if (volumeIndex === -1) return 10_000

  const bookIndex = TEXT_VOLUME_CATALOG[volumeIndex].bookIds.indexOf(normalized)

  return volumeIndex * 100 + Math.max(0, bookIndex)
}
