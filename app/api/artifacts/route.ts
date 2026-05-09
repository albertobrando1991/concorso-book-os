import { NextResponse } from "next/server"
import { listArtifacts } from "@/src/server/artifacts/service"

export async function GET() {
  const artifacts = await listArtifacts()
  return NextResponse.json({ artifacts })
}

