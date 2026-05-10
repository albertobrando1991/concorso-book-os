"use client"

import { useMemo, useState } from "react"
import { GitFork } from "lucide-react"
import type { KnowledgeGraph, GraphNode } from "@/src/server/wiki/graph"

interface KnowledgeGraphPanelProps {
  graph: KnowledgeGraph
}

const typeLabels: Record<GraphNode["type"], string> = {
  source: "Sources",
  topic: "Topics",
  entity: "Entities",
  book: "Books",
  chapter: "Chapters",
  review: "Reviews",
  wiki: "Wiki",
  other: "Other"
}

const colors: Record<GraphNode["type"], string> = {
  source: "#2368c4",
  topic: "#13795b",
  entity: "#7c3aed",
  book: "#ad6b00",
  chapter: "#b45309",
  review: "#b42318",
  wiki: "#314158",
  other: "#647184"
}

export function KnowledgeGraphPanel({ graph }: KnowledgeGraphPanelProps) {
  const [activeType, setActiveType] = useState<GraphNode["type"] | "all">("all")
  const [selectedId, setSelectedId] = useState(graph.nodes[0]?.id || "")
  const visible = useMemo(() => {
    const nodes = activeType === "all" ? graph.nodes : graph.nodes.filter((node) => node.type === activeType)
    const ids = new Set(nodes.map((node) => node.id))
    const links = graph.links.filter((link) => ids.has(link.source) && ids.has(link.target))

    return {
      nodes,
      links,
      positions: layoutNodes(nodes)
    }
  }, [activeType, graph])
  const selected = graph.nodes.find((node) => node.id === selectedId)
  const linkedCount = graph.links.filter((link) => link.source === selectedId || link.target === selectedId).length

  return (
    <section className="graphPanel" id="graph">
      <header>
        <div>
          <span className="panelKicker">Knowledge Graph</span>
          <h2>Grafo fonti, topic, entità e capitoli</h2>
        </div>
        <GitFork size={22} aria-hidden />
      </header>

      <div className="graphControls">
        <button className={activeType === "all" ? "active" : ""} onClick={() => setActiveType("all")}>
          Tutto
        </button>
        {(Object.keys(typeLabels) as GraphNode["type"][]).map((type) => (
          <button
            className={activeType === type ? "active" : ""}
            onClick={() => setActiveType(type)}
            key={type}
          >
            {typeLabels[type]}
          </button>
        ))}
      </div>

      <div className="graphLayout">
        <svg viewBox="0 0 900 520" role="img" aria-label="Knowledge graph interattivo">
          {visible.links.map((link) => {
            const source = visible.positions.get(link.source)
            const target = visible.positions.get(link.target)
            if (!source || !target) return null

            return (
              <line
                key={`${link.source}-${link.target}-${link.kind}`}
                x1={source.x}
                y1={source.y}
                x2={target.x}
                y2={target.y}
                className={link.kind}
              />
            )
          })}
          {visible.nodes.map((node) => {
            const position = visible.positions.get(node.id)
            if (!position) return null

            return (
              <g
                key={node.id}
                role="button"
                tabIndex={0}
                onClick={() => setSelectedId(node.id)}
                onKeyDown={(event) => {
                  if (event.key === "Enter") setSelectedId(node.id)
                }}
                className={selectedId === node.id ? "selected" : ""}
              >
                <circle cx={position.x} cy={position.y} r={node.type === "chapter" ? 13 : 10} fill={colors[node.type]} />
                <text x={position.x + 14} y={position.y + 4}>
                  {truncate(node.label)}
                </text>
              </g>
            )
          })}
        </svg>

        <aside className="graphDetails">
          {selected ? (
            <>
              <strong>{selected.label}</strong>
              <span>{typeLabels[selected.type]}</span>
              <code>{selected.path}</code>
              <small>{linkedCount} collegamenti</small>
            </>
          ) : (
            <span>Seleziona un nodo.</span>
          )}
        </aside>
      </div>
    </section>
  )
}

function layoutNodes(nodes: GraphNode[]) {
  const positions = new Map<string, { x: number; y: number }>()
  const groups = groupByType(nodes)
  const centerX = 450
  const centerY = 260
  const radii: Record<string, number> = {
    source: 215,
    topic: 175,
    entity: 135,
    chapter: 95,
    book: 60,
    review: 235,
    wiki: 250,
    other: 250
  }

  let groupIndex = 0

  for (const [type, group] of groups) {
    const radius = radii[type] || 220
    const offset = groupIndex * 0.55

    group.forEach((node, index) => {
      const angle = offset + (Math.PI * 2 * index) / Math.max(group.length, 1)
      positions.set(node.id, {
        x: centerX + Math.cos(angle) * radius,
        y: centerY + Math.sin(angle) * radius
      })
    })

    groupIndex += 1
  }

  return positions
}

function groupByType(nodes: GraphNode[]) {
  const groups = new Map<GraphNode["type"], GraphNode[]>()

  for (const node of nodes) {
    const group = groups.get(node.type) || []
    group.push(node)
    groups.set(node.type, group)
  }

  return groups
}

function truncate(value: string) {
  return value.length > 34 ? `${value.slice(0, 31)}...` : value
}

