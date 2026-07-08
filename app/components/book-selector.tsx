"use client"

import {
  TEXT_VOLUME_CATALOG,
  findTextVolumeForBookId,
  normalizeTextBookId,
  textBookIdFromPath
} from "@/src/catalog/text-volumes"

interface BookSelectorProps {
  books: Array<{
    title: string
    path: string
  }>
  currentBookId: string
}

export function BookSelector({ books, currentBookId }: BookSelectorProps) {
  const handleSelect = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const bookId = e.target.value
    if (bookId === currentBookId) return

    window.location.assign(`/?bookId=${encodeURIComponent(bookId)}`)
  }

  return (
    <div className="bookSelectorWrapper">
      <select
        value={currentBookId}
        onChange={handleSelect}
        className="bookSelectDropdown"
        aria-label="Seleziona libro di testo"
      >
        {TEXT_VOLUME_CATALOG.map((volume) => {
          const volumeBooks = books.filter((book) => volume.bookIds.includes(normalizeTextBookId(textBookIdFromPath(book.path))))

          if (volumeBooks.length === 0) return null

          return (
            <optgroup key={volume.code} label={`${volume.code} - ${volume.shortTitle}`}>
              {volumeBooks.map((book) => {
                const bookId = textBookIdFromPath(book.path)

                return (
                  <option key={book.path} value={bookId}>
                    {book.title}
                  </option>
                )
              })}
            </optgroup>
          )
        })}
        {books.some((book) => !findTextVolumeForBookId(textBookIdFromPath(book.path))) ? (
          <optgroup label="Altri testi">
            {books
              .filter((book) => !findTextVolumeForBookId(textBookIdFromPath(book.path)))
              .map((book) => {
                const bookId = textBookIdFromPath(book.path)

                return (
                  <option key={book.path} value={bookId}>
                    {book.title}
                  </option>
                )
              })}
          </optgroup>
        ) : null}
      </select>
    </div>
  )
}
