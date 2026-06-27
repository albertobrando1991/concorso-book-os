"use client"

import { useRouter } from "next/navigation"

interface BookSelectorProps {
  books: Array<{
    title: string
    path: string
  }>
  currentBookId: string
}

export function BookSelector({ books, currentBookId }: BookSelectorProps) {
  const router = useRouter()

  const handleSelect = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const bookId = e.target.value
    router.push(`/?bookId=${encodeURIComponent(bookId)}`)
  }

  return (
    <div className="bookSelectorWrapper">
      <select
        value={currentBookId}
        onChange={handleSelect}
        className="bookSelectDropdown"
        aria-label="Seleziona libro di testo"
      >
        {books.map((book) => {
          const bookId = book.path.replace("books/", "").replace("/index.md", "")
          return (
            <option key={book.path} value={bookId}>
              {book.title}
            </option>
          )
        })}
      </select>
    </div>
  )
}
