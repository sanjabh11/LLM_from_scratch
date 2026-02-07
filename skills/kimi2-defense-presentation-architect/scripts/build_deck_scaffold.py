#!/usr/bin/env python3
"""Generate a deterministic 30-slide defense AI training scaffold in Markdown."""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_ANNOTATIONS = [
    "Core definition in plain English",
    "Why this concept exists",
    "When to use this approach",
    "When not to use it",
    "Common practitioner mistake",
    "Memory or performance implications",
    "sklearn implementation mapping",
    "PyTorch equivalent mapping",
    "Everyday real-world application",
    "Defense application",
    "Comparison with alternative approach",
    "Practitioner pro tip",
    "Historical context",
    "Debugging guidance",
    "Related concept cross-reference",
]


def parse_csv(value: str) -> list[str]:
    items = [item.strip() for item in value.split(",") if item.strip()]
    return items


def parse_int_csv(value: str) -> list[int]:
    if not value.strip():
        return []
    out: list[int] = []
    for raw in value.split(","):
        raw = raw.strip()
        if not raw:
            continue
        out.append(int(raw))
    return out


def cycle_topics(topics: list[str], count: int, fallback_prefix: str) -> list[str]:
    if not topics:
        return [f"{fallback_prefix} {i + 1}" for i in range(count)]
    out: list[str] = []
    index = 0
    for _ in range(count):
        out.append(topics[index])
        index = (index + 1) % len(topics)
    return out


def concept_block(slide_number: int, topic: str) -> str:
    lines = [
        f"## Slide {slide_number}: {topic}",
        "- Type: Concept Diagram",
        "- Panel Archetype: Choose one (Central Engine + Satellites | Comparison Storyline | Technical Dissection Grid | Pipeline Macro-Board)",
        "- Sections: Overview | The Concept | How It Works | Implementation | Why It Matters | Complete View",
        "- Semantic Color Rules: Keep red=failure, yellow=intermediate, green=fused-success, cyan=data-flow unless overridden by deck-level mapping",
        "- Beginner's Corner: Required",
        "- Wise Owl (Lower-Right): Required",
        "- Extended Annotations:",
    ]
    for idx, annotation in enumerate(DEFAULT_ANNOTATIONS, start=1):
        lines.append(f"  {idx}. {annotation}")
    return "\n".join(lines)


def recap_block(slide_number: int, label: str) -> str:
    return "\n".join(
        [
            f"## Slide {slide_number}: {label}",
            "- Type: Recap",
            "- Required: Journey visual, 6 key takeaways, capability checklist, next-step preview, Wise Owl (Lower-Right)",
        ]
    )


def mcq_block(slide_number: int, label: str) -> str:
    return "\n".join(
        [
            f"## Slide {slide_number}: {label}",
            "- Type: MCQ Assessment (Optional)",
            "- Participant Visible: Question stem + options A/B/C/D only",
            "- Answer Visibility Rule: Correct answer must NOT appear on participant slide",
            "- Instructor Control: Use collapsed dropdown labeled `Instructor Answer (Hidden During Presentation)`",
            "",
            "### MCQ Template",
            "Question: [Insert question]",
            "A. [Option A]",
            "B. [Option B]",
            "C. [Option C]",
            "D. [Option D]",
            "",
            "<details>",
            "<summary>Instructor Answer (Hidden During Presentation)</summary>",
            "Correct Option: [A/B/C/D]",
            "Rationale: [Why this is correct]",
            "Trap Explanation: [Why tempting wrong option fails]",
            "</details>",
            "",
            "- Wise Owl (Lower-Right): Required",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a 30-slide defense AI deck scaffold")
    parser.add_argument("--title", required=True, help="Deck title")
    parser.add_argument(
        "--session-a",
        default="",
        help="Comma-separated topics for Session A concept slides",
    )
    parser.add_argument(
        "--session-b",
        default="",
        help="Comma-separated topics for Session B concept slides",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output Markdown file path",
    )
    parser.add_argument(
        "--mcq-slides",
        default="",
        help="Comma-separated slide numbers to reserve as MCQ slides (for example: 13,14,28,29)",
    )

    args = parser.parse_args()

    session_a_topics = cycle_topics(parse_csv(args.session_a), 12, "Session A Concept")
    session_b_topics = cycle_topics(parse_csv(args.session_b), 14, "Session B Concept")
    mcq_slides = set(parse_int_csv(args.mcq_slides))

    parts: list[str] = []
    parts.append(f"# {args.title}")
    parts.append(
        "\n## Slide 1: Title\n- Type: Title\n- Required: cinematic hero visual + title/subtitle/tagline + Wise Owl (Lower-Right)"
    )
    parts.append(
        "\n## Slide 2: Agenda\n- Type: Agenda\n- Required: two-column session map + outcomes + Wise Owl (Lower-Right)"
    )

    slide = 3
    for topic in session_a_topics:
        if slide in mcq_slides:
            parts.append("\n" + mcq_block(slide, f"Session A Knowledge Check {slide}"))
        else:
            parts.append("\n" + concept_block(slide, topic))
        slide += 1

    parts.append("\n" + recap_block(15, "Session A Recap"))

    slide = 16
    for topic in session_b_topics:
        if slide in mcq_slides:
            parts.append("\n" + mcq_block(slide, f"Session B Knowledge Check {slide}"))
        else:
            parts.append("\n" + concept_block(slide, topic))
        slide += 1

    parts.append("\n" + recap_block(30, "Final Recap and Key Takeaways"))

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(parts) + "\n", encoding="utf-8")

    print(f"Wrote scaffold: {output_path}")


if __name__ == "__main__":
    main()
