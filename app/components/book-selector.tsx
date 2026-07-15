"use client"

import {
  TEXT_VOLUME_CATALOG,
  findTextVolumeForBookId,
  isSpecialistTextVolume,
  isTextVolumeBookId,
  normalizeTextBookId,
  textBookIdFromPath,
  textVolumeBookId
} from "@/src/catalog/text-volumes"

interface BookSelectorProps {
  books: Array<{
    title: string
    path: string
  }>
  currentBookId: string
}

export function BookSelector({ books, currentBookId }: BookSelectorProps) {
  const currentVolume = findTextVolumeForBookId(currentBookId)
  const currentValue = isTextVolumeBookId(currentBookId)
    ? normalizeTextBookId(currentBookId)
    : currentVolume && isSpecialistTextVolume(currentVolume)
      ? textVolumeBookId(currentVolume)
      : currentBookId

  const handleSelect = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const bookId = e.target.value
    if (bookId === currentValue) return

    window.location.assign(`/?bookId=${encodeURIComponent(bookId)}`)
  }

  return (
    <div className="bookSelectorWrapper">
      <select
        value={currentValue}
        onChange={handleSelect}
        className="bookSelectDropdown"
        aria-label="Seleziona libro di testo"
      >
        {TEXT_VOLUME_CATALOG.map((volume) => {
          const volumeBooks = books.filter((book) => volume.bookIds.includes(normalizeTextBookId(textBookIdFromPath(book.path))))

          if (volumeBooks.length === 0) return null

          if (!isSpecialistTextVolume(volume)) {
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
          }

          return (
            <option key={volume.code} value={textVolumeBookId(volume)}>
              {volume.code} - {volume.title}
            </option>
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
