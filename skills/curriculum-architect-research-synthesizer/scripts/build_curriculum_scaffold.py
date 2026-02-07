#!/usr/bin/env python3
"""
Build a deterministic Markdown scaffold for a learning program.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def positive_int(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("value must be > 0")
    return number


def render_markdown(
    topic: str,
    tool: str,
    days: int,
    weekly_hours: int,
    modules: int,
    track: str,
) -> str:
    lines = []
    lines.append(f"# Learning Program: {topic}")
    lines.append("")
    lines.append("## Program Snapshot")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("| --- | --- |")
    lines.append(f"| Tool/Technology | {tool} |")
    lines.append("| Learner Profile |  |")
    lines.append("| Target Outcomes |  |")
    lines.append(f"| Time Budget | {days} days |")
    lines.append(f"| Track Intensity | {track} |")
    lines.append(f"| Weekly Load | {weekly_hours} hours/week |")
    lines.append(f"| Total Modules | {modules} |")
    lines.append("| Capstone Theme |  |")
    lines.append("")
    lines.append("## Source Inventory")
    lines.append("")
    lines.append("| ID | Source Type | Title | URL | Provider | Published/Updated | Duration/Length | Difficulty | Topics | Weighted Score | Include Reason |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    lines.append("")
    lines.append("## Global Syllabus")
    lines.append("")
    lines.append("| Module | Phase | Time Allocation | Objective Summary | Core Deliverable |")
    lines.append("| --- | --- | --- | --- | --- |")
    lines.append("")

    for index in range(1, modules + 1):
        lines.append(f"### Module {index}: [Module Name]")
        lines.append("")
        lines.append("**Phase:** [Beginner/Intermediate/Advanced]")
        lines.append("**Estimated Time:** [X hours]")
        lines.append("**Prerequisites:** [List]")
        lines.append("")
        lines.append("**Observable Objectives**")
        lines.append("- [Action verb + measurable output]")
        lines.append("- [Action verb + measurable output]")
        lines.append("")
        lines.append("**Required Resources**")
        lines.append("| Type | Resource | Link | Exact Section/Timestamp | Why It Matters |")
        lines.append("| --- | --- | --- | --- | --- |")
        lines.append("")
        lines.append("**Hands-On Labs**")
        lines.append("| Lab | Brief | Inputs | Expected Output | Time | Difficulty |")
        lines.append("| --- | --- | --- | --- | --- | --- |")
        lines.append("")
        lines.append("**Assessment Rubric (0-4 each)**")
        lines.append("| Criterion | 0 | 2 | 4 |")
        lines.append("| --- | --- | --- | --- |")
        lines.append("| Technical correctness |  |  |  |")
        lines.append("| Workflow fluency |  |  |  |")
        lines.append("| Debugging quality |  |  |  |")
        lines.append("| Communication clarity |  |  |  |")
        lines.append("")

    lines.append("## Capstone Blueprint")
    lines.append("")
    lines.append("| Item | Details |")
    lines.append("| --- | --- |")
    lines.append("| Project Title |  |")
    lines.append("| Problem Statement |  |")
    lines.append("| Required Features |  |")
    lines.append("| Optional Stretch Features |  |")
    lines.append("| Data/Inputs |  |")
    lines.append("| Architecture/Workflow Expectations |  |")
    lines.append("| Milestones |  |")
    lines.append("| Final Evaluation Rubric |  |")
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a Markdown scaffold for a learning program.",
    )
    parser.add_argument("--topic", required=True, help="Program topic/title")
    parser.add_argument("--tool", default="", help="Primary tool/technology")
    parser.add_argument("--days", type=positive_int, default=30, help="Total plan duration in days")
    parser.add_argument(
        "--weekly-hours",
        type=positive_int,
        default=6,
        help="Weekly learner availability in hours",
    )
    parser.add_argument("--modules", type=positive_int, default=6, help="Module count")
    parser.add_argument(
        "--track",
        choices=["fast", "standard", "deep"],
        default="standard",
        help="Curriculum intensity track",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional output file path; print to stdout when omitted",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tool = args.tool.strip() or args.topic.strip()
    markdown = render_markdown(
        topic=args.topic.strip(),
        tool=tool,
        days=args.days,
        weekly_hours=args.weekly_hours,
        modules=args.modules,
        track=args.track,
    )

    if args.output:
        args.output.write_text(markdown + "\n")
        print(f"Wrote scaffold to {args.output}")
        return
    print(markdown)


if __name__ == "__main__":
    main()
