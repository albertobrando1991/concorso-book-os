import type { Metadata } from "next"
import "./globals.css"

export const metadata: Metadata = {
  title: "ConcorsoBook OS",
  description: "Agentic Obsidian LLM Wiki for public competition books"
}

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="it">
      <body>{children}</body>
    </html>
  )
}

