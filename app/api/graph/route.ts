import { NextResponse } from "next/server"
import { getWikiRoot } from "@/src/server/config"
import { FileWikiStore } from "@/src/server/wiki/file-store"
import { buildKnowledgeGraph } from "@/src/server/wiki/graph"

export async function GET() {
  const graph = await buildKnowledgeGraph(new FileWikiStore(getWikiRoot()))
  return NextResponse.json(graph)
}

