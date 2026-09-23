export const BOOK_COVERAGE_TAXONOMY_VERSION = "concorso-book/12-volumes-25-modules/2026-07-14" as const

export type BookCoverageDepth = "orientation" | "essential" | "advanced"
export type BookCoverageStatus = "verified" | "partial" | "planned" | "unverified"
export type BookCoverageReviewStatus = "approved" | "pending" | "rejected"

export interface BookCoverageNormativeRef {
  urn: string
  articles: string | null
  sourceRefs: string[]
}

export interface BookCoverageRegistryRow {
  id: string
  volumeCode: string
  moduleCodes: string[]
  subject: string
  subjectSlugs: string[]
  concepts: string[]
  profileScope: string[]
  examOutputs: string[]
  depth: BookCoverageDepth
  status: BookCoverageStatus
  chapterRefs: string[]
  exclusions: string[]
  sourceRefs: string[]
  normativeRefs: BookCoverageNormativeRef[]
  verifiedAt: string | null
  validAsOf: string | null
  reviewStatus: BookCoverageReviewStatus
}

/**
 * Registro fail-closed delle sole coperture verificate.
 *
 * Le note di architettura e il catalogo commerciale non dimostrano che un
 * volume copra un argomento. Ogni riga deve quindi indicare capitoli realmente
 * inclusi nel bundle, fonti editoriali, profondita, esclusioni e ambiti. La
 * coppia status=verified/reviewStatus=approved certifica la mappatura della
 * copertura, non sostituisce i gate che regolano la pubblicazione del volume.
 */
const COMMON_PROFILE_SCOPE = ["all"]
const COMMON_EXAM_OUTPUTS = ["all"]
const VERIFIED_AT = "2026-09-23T16:45:00.000Z"

const CONSTITUTION_URN = "urn:nir:stato:costituzione:1947-12-27;1"
const LAW_241_URN = "urn:nir:stato:legge:1990-08-07;241"
const PUBLIC_EMPLOYMENT_URN = "urn:nir:stato:decreto.legislativo:2001-03-30;165"
const TRANSPARENCY_URN = "urn:nir:stato:decreto.legislativo:2013-03-14;33"
const PUBLIC_COMPETITIONS_URN = "urn:nir:presidente.repubblica:decreto:1994-05-09;487"
const TUEL_URN = "urn:nir:stato:decreto.legislativo:2000-08-18;267"
const CAD_URN = "urn:nir:stato:decreto.legislativo:2005-03-07;82"

export const BOOK_COVERAGE_REGISTRY: readonly BookCoverageRegistryRow[] = [
  {
    id: "vol-01-diritto-amministrativo",
    volumeCode: "VOL-01",
    moduleCodes: [],
    subject: "Diritto amministrativo",
    subjectSlugs: ["diritto-amministrativo"],
    concepts: ["fonti", "organizzazione-amministrativa", "atti-e-provvedimenti", "accesso-e-trasparenza"],
    profileScope: COMMON_PROFILE_SCOPE,
    examOutputs: COMMON_EXAM_OUTPUTS,
    depth: "advanced",
    status: "verified",
    chapterRefs: ["chapter-diritto-amministrativo-per-candidati"],
    exclusions: [],
    sourceRefs: [
      "sources/legge-7-agosto-1990-n-241-procedimento-amministrativo-e-accesso-ai-documenti-amministrativi-testo-vigente-normattiva.md",
      "sources/d-lgs-14-marzo-2013-n-33-trasparenza.md"
    ],
    normativeRefs: [
      {
        urn: LAW_241_URN,
        articles: null,
        sourceRefs: ["sources/legge-7-agosto-1990-n-241-procedimento-amministrativo-e-accesso-ai-documenti-amministrativi-testo-vigente-normattiva.md"]
      },
      {
        urn: TRANSPARENCY_URN,
        articles: null,
        sourceRefs: ["sources/d-lgs-14-marzo-2013-n-33-trasparenza.md"]
      }
    ],
    verifiedAt: VERIFIED_AT,
    validAsOf: "2026-07-23T00:00:00.000+02:00",
    reviewStatus: "approved"
  },
  {
    id: "vol-01-procedimento-amministrativo",
    volumeCode: "VOL-01",
    moduleCodes: [],
    subject: "Procedimento amministrativo",
    subjectSlugs: ["procedimento-amministrativo"],
    concepts: ["fasi-del-procedimento", "responsabile", "termini", "partecipazione", "accesso", "autotutela"],
    profileScope: COMMON_PROFILE_SCOPE,
    examOutputs: COMMON_EXAM_OUTPUTS,
    depth: "advanced",
    status: "verified",
    chapterRefs: ["chapter-diritto-amministrativo-per-candidati"],
    exclusions: [],
    sourceRefs: ["sources/legge-7-agosto-1990-n-241-procedimento-amministrativo-e-accesso-ai-documenti-amministrativi-testo-vigente-normattiva.md"],
    normativeRefs: [{
      urn: LAW_241_URN,
      articles: null,
      sourceRefs: ["sources/legge-7-agosto-1990-n-241-procedimento-amministrativo-e-accesso-ai-documenti-amministrativi-testo-vigente-normattiva.md"]
    }],
    verifiedAt: VERIFIED_AT,
    validAsOf: "2026-07-23T00:00:00.000+02:00",
    reviewStatus: "approved"
  },
  {
    id: "vol-01-pubblico-impiego",
    volumeCode: "VOL-01",
    moduleCodes: [],
    subject: "Pubblico impiego",
    subjectSlugs: ["pubblico-impiego"],
    concepts: ["rapporto-di-lavoro", "organizzazione", "dirigenza", "responsabilita", "accesso-agli-impieghi"],
    profileScope: COMMON_PROFILE_SCOPE,
    examOutputs: COMMON_EXAM_OUTPUTS,
    depth: "advanced",
    status: "verified",
    chapterRefs: ["chapter-pubblico-impiego-e-organizzazione-pa"],
    exclusions: [],
    sourceRefs: [
      "sources/d-lgs-30-marzo-2001-n-165-pubblico-impiego.md",
      "sources/d-p-r-9-maggio-1994-n-487-accesso-agli-impieghi-pubblici-e-concorsi.md"
    ],
    normativeRefs: [
      {
        urn: PUBLIC_EMPLOYMENT_URN,
        articles: null,
        sourceRefs: ["sources/d-lgs-30-marzo-2001-n-165-pubblico-impiego.md"]
      },
      {
        urn: PUBLIC_COMPETITIONS_URN,
        articles: null,
        sourceRefs: ["sources/d-p-r-9-maggio-1994-n-487-accesso-agli-impieghi-pubblici-e-concorsi.md"]
      }
    ],
    verifiedAt: VERIFIED_AT,
    validAsOf: "2026-08-21T00:00:00.000+02:00",
    reviewStatus: "approved"
  },
  {
    id: "vol-01-contabilita-pubblica",
    volumeCode: "VOL-01",
    moduleCodes: [],
    subject: "Contabilita pubblica",
    subjectSlugs: ["contabilita-pubblica"],
    concepts: ["principi-costituzionali", "bilancio", "gestione-finanziaria", "controlli", "armonizzazione"],
    profileScope: COMMON_PROFILE_SCOPE,
    examOutputs: COMMON_EXAM_OUTPUTS,
    depth: "essential",
    status: "verified",
    chapterRefs: ["chapter-contabilita-pubblica-essenziale"],
    exclusions: ["Contabilita di Stato specialistica", "Contabilita economico-patrimoniale avanzata", "Casistica contabile settoriale"],
    sourceRefs: [
      "sources/principi-costituzionali-finanza-pubblica-art-81-97-119.md",
      "sources/ordinamento-finanziario-enti-locali-tuel-dup-peg-rendiconto-revisione.md",
      "sources/armonizzazione-contabile-enti-territoriali-d-lgs-118-2011.md"
    ],
    normativeRefs: [
      {
        urn: CONSTITUTION_URN,
        articles: "81, 97, 119",
        sourceRefs: ["sources/principi-costituzionali-finanza-pubblica-art-81-97-119.md"]
      },
      {
        urn: TUEL_URN,
        articles: "149-241",
        sourceRefs: ["sources/ordinamento-finanziario-enti-locali-tuel-dup-peg-rendiconto-revisione.md"]
      }
    ],
    verifiedAt: VERIFIED_AT,
    validAsOf: "2026-07-23T00:00:00.000+02:00",
    reviewStatus: "approved"
  },
  {
    id: "vol-01-informatica-pa-digitale",
    volumeCode: "VOL-01",
    moduleCodes: [],
    subject: "Informatica e PA digitale",
    subjectSlugs: ["informatica-pa-digitale"],
    concepts: ["competenze-digitali", "cad", "identita-digitale", "documenti-informatici", "sicurezza"],
    profileScope: COMMON_PROFILE_SCOPE,
    examOutputs: COMMON_EXAM_OUTPUTS,
    depth: "essential",
    status: "verified",
    chapterRefs: ["chapter-informatica-pa-digitale-competenze-digitali"],
    exclusions: ["Programmazione avanzata", "Architetture cloud", "Cybersecurity per profili ICT specialistici"],
    sourceRefs: [
      "sources/d-lgs-7-marzo-2005-n-82-amministrazione-digitale.md",
      "sources/pa-digitale-cad-identita-documenti-servizi-dati.md"
    ],
    normativeRefs: [{
      urn: CAD_URN,
      articles: null,
      sourceRefs: ["sources/d-lgs-7-marzo-2005-n-82-amministrazione-digitale.md"]
    }],
    verifiedAt: VERIFIED_AT,
    validAsOf: "2026-07-23T00:00:00.000+02:00",
    reviewStatus: "approved"
  },
  {
    id: "vol-01-inglese",
    volumeCode: "VOL-01",
    moduleCodes: [],
    subject: "Lingua inglese",
    subjectSlugs: ["inglese"],
    concepts: ["grammatica", "lessico", "comprensione", "cloze-test"],
    profileScope: COMMON_PROFILE_SCOPE,
    examOutputs: COMMON_EXAM_OUTPUTS,
    depth: "essential",
    status: "verified",
    chapterRefs: ["chapter-inglese-concorsuale-essenziale"],
    exclusions: ["Certificazioni linguistiche", "Produzione scritta avanzata", "Inglese tecnico specialistico"],
    sourceRefs: ["sources/inglese-concorsi-corpus-fonti-ufficiali-2026-05-28.md"],
    normativeRefs: [],
    verifiedAt: VERIFIED_AT,
    validAsOf: "2026-07-23T00:00:00.000+02:00",
    reviewStatus: "approved"
  },
  {
    id: "vol-01-logica-attitudinali",
    volumeCode: "VOL-01",
    moduleCodes: [],
    subject: "Logica e test attitudinali",
    subjectSlugs: ["logica-attitudinali"],
    concepts: ["logica-verbale", "ragionamento", "comprensione-del-testo", "problem-solving"],
    profileScope: COMMON_PROFILE_SCOPE,
    examOutputs: COMMON_EXAM_OUTPUTS,
    depth: "essential",
    status: "verified",
    chapterRefs: ["chapter-logica-comprensione-ragionamento"],
    exclusions: ["Banche dati ufficiali specifiche del singolo bando"],
    sourceRefs: ["sources/ripam-quesiti-attitudinali-logica-ragionamento-comprensione.md"],
    normativeRefs: [],
    verifiedAt: VERIFIED_AT,
    validAsOf: "2026-07-24T00:00:00.000+02:00",
    reviewStatus: "approved"
  },
  {
    id: "vol-01-quesiti-situazionali",
    volumeCode: "VOL-01",
    moduleCodes: [],
    subject: "Quesiti situazionali",
    subjectSlugs: ["quesiti-situazionali"],
    concepts: ["competenze-trasversali", "comportamenti-organizzativi", "giudizio-situazionale", "soft-skills"],
    profileScope: COMMON_PROFILE_SCOPE,
    examOutputs: COMMON_EXAM_OUTPUTS,
    depth: "essential",
    status: "verified",
    chapterRefs: ["chapter-quesiti-situazionali-soft-skills"],
    exclusions: ["Framework proprietari o griglie di valutazione non pubblicate dall'ente banditore"],
    sourceRefs: [
      "sources/framework-competenze-trasversali-pa-dm-28-giugno-2023.md",
      "sources/prove-situazionali-concorsi-ripam-maeci-sna.md"
    ],
    normativeRefs: [],
    verifiedAt: VERIFIED_AT,
    validAsOf: "2026-07-24T00:00:00.000+02:00",
    reviewStatus: "approved"
  },
  {
    id: "vol-02-enti-locali-istruttore-amministrativo",
    volumeCode: "VOL-02",
    moduleCodes: ["M-FL01"],
    subject: "Enti locali",
    subjectSlugs: ["enti-locali"],
    concepts: ["tuel", "organi", "atti", "servizi-locali", "programmazione", "finanza-locale", "casi-pratici"],
    profileScope: ["P0094", "Istruttore amministrativo", "Funzioni locali"],
    examOutputs: COMMON_EXAM_OUTPUTS,
    depth: "advanced",
    status: "verified",
    chapterRefs: [
      "chapter-m-fl01-01-tuel-operativo-autonomia-organi-funzioni-comune",
      "chapter-m-fl01-02-statuto-regolamenti-autonomia-normativa-locale",
      "chapter-m-fl01-03-organizzazione-comunale-uffici-servizi-gestioni-associate",
      "chapter-m-fl01-04-deliberazioni-determinazioni-decreti-ordinanze-pareri",
      "chapter-m-fl01-05-procedimento-locale-protocollo-albo-urp-accesso",
      "chapter-m-fl01-06-servizi-digitali-comunali-cad-anpr-gestione-documentale",
      "chapter-m-fl01-07-servizi-demografici-elettorali",
      "chapter-m-fl01-08-welfare-locale-servizi-sociali-isee-minori-servizi-educativi",
      "chapter-m-fl01-09-programmazione-integrata-comunale-dup-bilancio-peg-piao-performance",
      "chapter-m-fl01-10-gestione-finanziaria-rendiconto-tesoreria-controlli",
      "chapter-m-fl01-11-entrate-tributi-locali-patrimonio-economato-riscossione",
      "chapter-m-fl01-12-procurement-operativo-ufficio-comunale",
      "chapter-m-fl01-13-territorio-patrimonio-edilizia-lavori-interfaccia-amministrativa",
      "chapter-m-fl01-14-laboratorio-teorico-pratico-profili-comunali"
    ],
    exclusions: [],
    sourceRefs: [
      "sources/d-lgs-18-agosto-2000-n-267-enti-locali.md",
      "sources/bandi-inpa-vol-02-campione-2026.md",
      "sources/vol-02-dossier-redazionale-enti-locali-polizia-locale.md"
    ],
    normativeRefs: [
      {
        urn: TUEL_URN,
        articles: null,
        sourceRefs: ["sources/d-lgs-18-agosto-2000-n-267-enti-locali.md"]
      },
      {
        urn: LAW_241_URN,
        articles: null,
        sourceRefs: ["sources/legge-7-agosto-1990-n-241-procedimento-amministrativo-e-accesso-ai-documenti-amministrativi-testo-vigente-normattiva.md"]
      },
      {
        urn: CAD_URN,
        articles: null,
        sourceRefs: ["sources/d-lgs-7-marzo-2005-n-82-amministrazione-digitale.md"]
      }
    ],
    verifiedAt: VERIFIED_AT,
    validAsOf: "2026-08-05T00:00:00.000+02:00",
    reviewStatus: "approved"
  }
]
