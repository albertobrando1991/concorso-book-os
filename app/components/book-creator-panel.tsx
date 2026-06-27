"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { Loader2, Plus, BookOpen } from "lucide-react"

export function BookCreatorPanel() {
  const router = useRouter()
  const [isOpen, setIsOpen] = useState(false)
  const [bookId, setBookId] = useState("")
  const [title, setTitle] = useState("")
  const [structureSource, setStructureSource] = useState(
    "FM1. Servizi digitali\nFM2. Premessa\n1. Introduzione generale\n2. Diritto amministrativo e procedimento\n3. Trasparenza e anticorruzione"
  )
  const [isLoading, setIsLoading] = useState(false)
  const [message, setMessage] = useState("")
  const [error, setError] = useState("")

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    setError("")
    setMessage("")

    try {
      const response = await fetch("/api/books", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          bookId: bookId.trim(),
          title: title.trim(),
          structureSource: structureSource.trim()
        })
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.error || "Impossibile creare il libro")
      }

      setMessage(`Libro "${data.title}" creato con successo! Inizializzati ${data.chaptersCreated} capitoli.`)
      setBookId("")
      setTitle("")
      setIsOpen(false)

      router.push(`/?bookId=${encodeURIComponent(data.bookId)}`)
      router.refresh()
    } catch (currentError) {
      setError(currentError instanceof Error ? currentError.message : "Errore durante la creazione")
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <section className="panel bookCreatorPanel" id="book-creator" style={{ marginBottom: "16px" }}>
      <header onClick={() => setIsOpen(!isOpen)} style={{ cursor: "pointer", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
          <Plus size={19} aria-hidden />
          <h2>Aggiungi Nuovo Libro di Testo</h2>
        </div>
        <button
          type="button"
          className="studioIconButton"
          style={{ width: "30px", height: "30px", border: "none", background: "transparent", fontSize: "20px" }}
          aria-label={isOpen ? "Chiudi pannello" : "Apri pannello"}
        >
          {isOpen ? "−" : "+"}
        </button>
      </header>

      {isOpen && (
        <form onSubmit={handleSubmit} className="bookCreatorForm" style={{ marginTop: "16px", display: "grid", gap: "14px" }}>
          <p className="formInstructions" style={{ color: "var(--muted)", fontSize: "13px", margin: "0 0 10px" }}>
            Inserisci i dettagli per iniziare un nuovo libro. Verrà creata la cartella in <code>books/[ID]</code> contenente il file <code>index.md</code> e tutti i file capitolo relativi.
          </p>

          <div className="formGroup" style={{ display: "grid", gap: "6px" }}>
            <label htmlFor="creator-book-id" style={{ fontWeight: 600, fontSize: "14px" }}>
              ID del Libro (slug ASCII minuscolo, es: <code>manuale-istruttore-enti-locali</code>)
            </label>
            <input
              id="creator-book-id"
              type="text"
              required
              placeholder="es: manuale-enti-locali"
              value={bookId}
              onChange={(e) => setBookId(e.target.value.toLowerCase().replace(/[^a-z0-9-]/g, "-"))}
              style={{ padding: "8px 12px", border: "1px solid var(--line)", borderRadius: "6px", fontSize: "14px" }}
            />
          </div>

          <div className="formGroup" style={{ display: "grid", gap: "6px" }}>
            <label htmlFor="creator-title" style={{ fontWeight: 600, fontSize: "14px" }}>Titolo Completo del Libro</label>
            <input
              id="creator-title"
              type="text"
              required
              placeholder="es: Manuale Completo Istruttore Amministrativo negli Enti Locali"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              style={{ padding: "8px 12px", border: "1px solid var(--line)", borderRadius: "6px", fontSize: "14px" }}
            />
          </div>

          <div className="formGroup" style={{ display: "grid", gap: "6px" }}>
            <label htmlFor="creator-structure" style={{ fontWeight: 600, fontSize: "14px" }}>
              Outline di Partenza (una sezione o capitolo per riga)
            </label>
            <textarea
              id="creator-structure"
              required
              rows={8}
              placeholder={`FM1. Servizi digitali\nFM2. Premessa\n1. Introduzione generale\n2. Diritto amministrativo\n3. Pubblico impiego e contratti`}
              value={structureSource}
              onChange={(e) => setStructureSource(e.target.value)}
              style={{ padding: "10px 12px", border: "1px solid var(--line)", borderRadius: "6px", fontSize: "14px", fontFamily: "inherit" }}
            />
            <small className="fieldHint" style={{ color: "var(--muted)", fontSize: "12px" }}>
              Usa il prefisso <code>FM</code> per le prime pagine e la numerazione standard per i capitoli effettivi.
            </small>
          </div>

          <button
            type="submit"
            className="writerButton"
            disabled={isLoading}
            style={{
              display: "inline-flex",
              alignItems: "center",
              justifyContent: "center",
              gap: "8px",
              padding: "10px 16px",
              background: "var(--nav)",
              color: "#fff",
              border: "none",
              borderRadius: "6px",
              fontWeight: 600,
              cursor: "pointer",
              fontSize: "14px"
            }}
          >
            {isLoading ? <Loader2 size={17} className="spin" aria-hidden /> : <BookOpen size={17} aria-hidden />}
            {isLoading ? "Creazione in corso..." : "Inizializza Libro ed Outline"}
          </button>
        </form>
      )}

      {message && <div className="studioMessage" style={{ marginTop: "12px", padding: "10px 12px", background: "#f1fbf5", border: "1px solid #b8e2ca", borderRadius: "6px", color: "var(--green)", fontSize: "13px" }}>{message}</div>}
      {error && <div className="writerError" style={{ marginTop: "12px", padding: "10px 12px", background: "#fef3f2", border: "1px solid #fee4e2", borderRadius: "6px", color: "var(--red)", fontSize: "13px" }}>{error}</div>}
    </section>
  )
}
