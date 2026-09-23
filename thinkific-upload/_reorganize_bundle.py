#!/usr/bin/env python3
"""
One-shot migration: move the bundle from the legacy product layout to the collection-organized,
numbered-leaf layout (1 - Tracks/<product> · 2 - Modules · 3 - Functions), driven by
`_generate_placeholders.py:target_folder`.

Safe by design:
  - DRY-RUN by default. Pass --apply to actually move.
  - shutil.move on the same filesystem (instant, reversible — it relinks, no copy).
  - No clobber: skips a move whose destination already has content.
  - Idempotent: skips a move whose source is already gone.
  - Count gates: 34 leaf folders / 16 videos / 120 placeholder PDFs must be unchanged. Aborts
    (without removing legacy dirs) on any mismatch.
  - Removes the 5 emptied legacy top dirs only after a clean, verified run.

Usage:  python3 thinkific-upload/_reorganize_bundle.py [--apply]
"""
from __future__ import annotations
import importlib.util, pathlib, shutil, sys

HERE = pathlib.Path(__file__).resolve().parent
APPLY = "--apply" in sys.argv

# import target_folder/NUM/DATA from the generator (single source of truth for new paths)
_spec = importlib.util.spec_from_file_location("gen", HERE / "_generate_placeholders.py")
gen = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(gen)
COURSE = {c["slug"]: c for c in gen.DATA["courses"]}

# Legacy current leaf folder per course (authoritative — verified on disk pre-migration).
CURRENT = {
    "track-adk-foundations":             "Lyzr ADK - Developers/1 - Foundations",
    "track-adk-multimodal":              "Lyzr ADK - Developers/2 - Multimodal",
    "track-adk-knowledge-memory":        "Lyzr ADK - Developers/3 - Knowledge and Memory",
    "track-adk-tools-workflows":         "Lyzr ADK - Developers/4 - Tools and Workflows (Coming Soon)",
    "track-adk-gitagent-oss":            "Lyzr ADK - Developers/GitAgent and OSS (Coming Soon)",
    "track-studio-101":                  "Lyzr Agent Studio (Coming Soon)/Studio 101 - Build, Deploy and Monitor (Coming Soon)",
    "track-studio-201":                  "Lyzr Agent Studio (Coming Soon)/Studio 201 - Tools, Auth, KG and Simulation (Coming Soon)",
    "track-studio-401":                  "Lyzr Agent Studio (Coming Soon)/Studio 401 - Enterprise (Coming Soon)",
    "track-studio-knowledge-memory":     "Lyzr Agent Studio (Coming Soon)/Knowledge Base and Memory (Coming Soon)",
    "track-studio-traces":               "Lyzr Agent Studio (Coming Soon)/Traces (Coming Soon)",
    "track-studio-models-tools-mcp":     "Lyzr Agent Studio (Coming Soon)/Models, Tools and MCP (Coming Soon)",
    "track-studio-superflow":            "Lyzr Agent Studio (Coming Soon)/SuperFlow (Coming Soon)",
    "track-studio-responsible-ai":       "Lyzr Agent Studio (Coming Soon)/Responsible AI (Coming Soon)",
    "track-studio-manager-agent":        "Lyzr Agent Studio (Coming Soon)/Manager Agent (Coming Soon)",
    "track-studio-voice-agents":         "Lyzr Agent Studio (Coming Soon)/Voice Agents (Coming Soon)",
    "track-studio-control-sim-langship": "Lyzr Agent Studio (Coming Soon)/Control, Simulation and LangShip (Coming Soon)",
    "track-architect-fundamentals":      "Lyzr Architect (Coming Soon)/Architect Fundamentals (Coming Soon)",
    "module-agents":                     "Lyzr Modules (Coming Soon)/Agents (Coming Soon)",
    "module-models":                     "Lyzr Modules (Coming Soon)/Models (Coming Soon)",
    "module-memory":                     "Lyzr Modules (Coming Soon)/Memory (Coming Soon)",
    "module-knowledge-rag":              "Lyzr Modules (Coming Soon)/Knowledge and RAG (Coming Soon)",
    "module-tools-integrations":         "Lyzr Modules (Coming Soon)/Tools and Integrations (Coming Soon)",
    "module-orchestration":              "Lyzr Modules (Coming Soon)/Orchestration (Coming Soon)",
    "module-voice":                      "Lyzr Modules (Coming Soon)/Voice (Coming Soon)",
    "module-responsible-ai":             "Lyzr Modules (Coming Soon)/Responsible AI (Coming Soon)",
    "module-evaluation":                 "Lyzr Modules (Coming Soon)/Evaluation (Coming Soon)",
    "module-multimodal":                 "Lyzr Modules (Coming Soon)/Multimodal (Coming Soon)",
    "module-deployment":                 "Lyzr Modules (Coming Soon)/Deployment (Coming Soon)",
    "function-hr":                       "AI for Business - Verticals (Coming Soon)/AI in HR (Coming Soon)",
    "function-marketing":                "AI for Business - Verticals (Coming Soon)/AI in Marketing (Coming Soon)",
    "function-sales":                    "AI for Business - Verticals (Coming Soon)/AI in Sales (Coming Soon)",
    "function-procurement":              "AI for Business - Verticals (Coming Soon)/AI in Procurement (Coming Soon)",
    "function-venture-capital":          "AI for Business - Verticals (Coming Soon)/AI in Venture Capital (Coming Soon)",
    "function-ai-strategy":              "AI for Business - Verticals (Coming Soon)/AI and Agentic Strategy (Coming Soon)",
}
LEGACY_TOPS = ["Lyzr ADK - Developers", "Lyzr Agent Studio (Coming Soon)",
               "Lyzr Architect (Coming Soon)", "Lyzr Modules (Coming Soon)",
               "AI for Business - Verticals (Coming Soon)"]


def counts():
    """(placeholder PDFs, videos, leaf folders) across the bundle."""
    pdfs = len(list(HERE.rglob("0[0-9] *.pdf")))
    mp4 = len(list(HERE.rglob("*.mp4")))
    leaves = {f.parent for f in HERE.rglob("*") if f.is_file() and f.parent != HERE}
    return pdfs, mp4, len(leaves)


def main():
    assert set(CURRENT) == set(COURSE), "CURRENT map is not exactly the 34 catalog courses"
    before = counts()
    print(f"Before: {before[0]} placeholder PDFs · {before[1]} videos · {before[2]} leaf folders\n")

    moves = []
    for slug, legacy in CURRENT.items():
        moves.append((slug, HERE / legacy, gen.target_folder(COURSE[slug])))

    for slug, src, dst in moves:
        print(f"{slug:34} {src.relative_to(HERE)}\n{'':34} → {dst.relative_to(HERE)}")
    print()

    if not APPLY:
        print("DRY-RUN. Re-run with --apply to perform these 34 moves.")
        return 0

    moved = skipped = 0
    for slug, src, dst in moves:
        if dst.exists() and any(dst.iterdir()):
            print(f"• skip (dest populated): {dst.relative_to(HERE)}"); skipped += 1; continue
        if not src.exists():
            print(f"• skip (src gone): {src.relative_to(HERE)}"); skipped += 1; continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        moved += 1

    after = counts()
    print(f"\nMoved {moved}, skipped {skipped}.")
    print(f"After:  {after[0]} placeholder PDFs · {after[1]} videos · {after[2]} leaf folders")
    if after != before:
        print("‼ COUNT MISMATCH — leaving legacy dirs in place for inspection. Do not delete manually "
              "until reconciled.", file=sys.stderr)
        return 1

    for top in LEGACY_TOPS:
        d = HERE / top
        if d.exists():
            stray = [f for f in d.rglob("*") if f.is_file()]
            if stray:
                print(f"‼ {top} still has files {stray} — not removing.", file=sys.stderr); return 1
            shutil.rmtree(d)
            print(f"removed empty legacy dir: {top}")
    print("\n✓ Reorganization complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
