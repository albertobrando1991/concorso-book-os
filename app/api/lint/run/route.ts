import { NextResponse } from "next/server"
import { getWikiRoot } from "@/src/server/config"
import { LintAgent } from "@/src/server/agents/lint-agent"
import { FileWikiStore } from "@/src/server/wiki/file-store"

export async function POST() {
  const agent = new LintAgent(new FileWikiStore(getWikiRoot()))
  const result = await agent.run()

  return NextResponse.json(result)
}

