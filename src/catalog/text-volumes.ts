export type TextVolumeTier = "base" | "standard" | "vertical" | "premium"
export type TextLaunchWave = "foundation" | "first" | "second" | "third" | "continuous"

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
    verticals: ["B-PA01/B-PA11", "Ricettario digitale collegato", "Bando Decoder e planner"]
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
    promise: "Modulo standard per il bacino piu ricorrente degli enti territoriali.",
    verticals: ["TUEL e servizi locali", "Registro Imprese CCIAA", "Codice della strada e sicurezza urbana"]
  },
  {
    code: "VOL-03",
    title: "Fisco, Dogane, Previdenza e Ispettivo",
    shortTitle: "Fisco e previdenza",
    tier: "standard",
    launchWave: "first",
    modules: ["M-FC02", "M-FC03"],
    bookIds: [
      "moduli/m-fc02-agenzie-fiscali",
      "moduli/m-fc03-enti-non-economici"
    ],
    audience: "Agenzie fiscali, riscossione, INPS, INAIL ed enti pubblici non economici",
    promise: "Percorso specialistico fiscale, doganale, previdenziale e ispettivo.",
    verticals: ["ADM dogane e accise", "Tecniche ispettive INPS/INAIL", "Previdenza e servizi EPNE"]
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
    audience: "AGCM, ARERA e autorita indipendenti",
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
    audience: "Scuola, universita, AFAM, enti di ricerca e MiC",
    promise: "Famiglia ampia con sotto-percorsi editoriali distinti per amministrativi e specialisti.",
    verticals: ["DSGA", "Project/grant manager ricerca", "Archivisti, bibliotecari e beni culturali"]
  },
  {
    code: "VOL-07",
    title: "Sanita amministrativa e professioni sanitarie",
    shortTitle: "Sanita",
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
    verticals: ["Cybersecurity", "Dati e interoperabilita", "Servizi digitali PA"]
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
    title: "Ambiente, protezione civile e sostenibilita",
    shortTitle: "Ambiente",
    tier: "vertical",
    launchWave: "third",
    modules: ["M-TR04"],
    bookIds: ["moduli/m-tr04-ambiente-protezione-civile"],
    audience: "MASE, ambiente, protezione civile, sostenibilita e controlli territoriali",
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
    audience: "Forze dell'ordine, VVF, magistratura, diplomazia, prefettizia, alta dirigenza",
    promise: "Pacchetto premium per carriere ad alta barriera e pricing alto.",
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
    description: "Carriere speciali, Authority, magistratura, diplomazia, prefettizia, VVF direttivo e alta dirigenza."
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
