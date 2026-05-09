import { NextResponse } from "next/server"
import { getDashboardData } from "@/src/server/dashboard/data"

export async function GET() {
  const data = await getDashboardData()
  return NextResponse.json(data)
}

