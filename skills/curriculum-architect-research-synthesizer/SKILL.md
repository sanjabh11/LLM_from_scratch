---
name: curriculum-architect-research-synthesizer
description: Design evidence-grounded beginner-to-expert learning programs for a specific tool or technology, including source harvesting (YouTube, official docs, forums), syllabus architecture, labs, diagnostics, and capstones. Use when users request a curriculum, study roadmap, bootcamp plan, competency matrix, exercise library, assessment system, or NotebookLM-ready learning pack.
---

# Curriculum Architect Research Synthesizer

## Overview

Design a complete learning program optimized for practical mastery within a fixed time budget.
Synthesize credible sources, score quality, map competency progression, and deliver structured outputs that can be imported into NotebookLM.

## Required Inputs

Collect these fields before designing the program. Ask only for missing fields.

| Field | Requirement | Default if user does not provide |
| --- | --- | --- |
| Tool or technology | Required | Ask again; do not assume |
| Learner starting level | Required | Beginner |
| Target role or outcomes | Required | Build practical project fluency |
| Total timeline | Required | 30 days |
| Weekly availability | Required | 6 hours/week |
| Preferred track intensity | Optional | Standard |
| Industry context | Optional | General software/product context |
| Constraints (cost, device, policy) | Optional | Free/open resources first |

If tool/technology or time budget is missing, stop and ask first.

## Workflow

1. Define success criteria.
Set measurable outcomes tied to user goals (for example: "build and deploy X", "debug Y", "pass interview-style task Z").
2. Harvest sources.
Collect:
- 15-30 YouTube resources with title, URL, duration, chapter timestamps, and inferred difficulty.
- Official documentation structure with quickstart, tutorials, API/reference sections, patterns, and release/version context.
- 10-20 high-signal forum threads (Reddit or equivalent) for practical pitfalls and workflows.
3. Score and filter sources.
Apply the weighted rubric in `references/source-quality-rubric.md`.
Discard low-credibility or stale resources unless required for historical context.
4. Build the learning architecture.
Produce:
- Concept dependency map (foundations -> intermediate -> advanced).
- Competency matrix (tasks x proficiency levels).
- Prerequisite bridge plan for missing fundamentals.
5. Build the program.
Adapt scope to time budget and intensity track.
Include beginner, intermediate, and advanced progression with explicit exit criteria.
6. Design assessment and practice system.
Create diagnostic pre-check, module checks, scenario labs, and one cumulative capstone.
7. Run quality gates.
Verify citation completeness, coverage balance, realism of workload, and direct alignment to target outcomes.
8. Deliver final pack.
Use the exact output templates in `references/output-templates.md`.

## Source Selection Rules

- Prioritize official docs and primary technical references for correctness.
- Prefer sources updated within the last 18 months when possible; flag older but canonical content as "legacy-still-relevant" or "legacy-risky".
- Enforce diversity: avoid over-reliance on one creator/channel.
- Prefer resources with concrete demos, code walkthroughs, or troubleshooting evidence.
- Extract contradictory guidance and resolve it explicitly.
- Mark every uncertain claim with `Verification Needed`.

## Curriculum Design Rules

- Keep objectives observable and testable using action verbs.
- Map every module to at least one real-world job task.
- Control cognitive load by track: `Fast` (essential path), `Standard` (balanced theory + hands-on), `Deep` (expanded architecture, edge cases, internals).
- Use spiral progression: reintroduce core concepts with increasing complexity.
- Include anti-patterns and common failure modes in each phase.
- Require at least one portfolio-grade artifact before completion.

## Output Contract

Always return sections in this order:

1. Program Snapshot
2. Source Inventory
3. Concept Dependency Map
4. Competency Matrix
5. Global Syllabus
6. Module Specs
7. Exercise Library
8. Diagnostic and Rubric Pack
9. Capstone Blueprint
10. NotebookLM Ingestion Pack
11. Assumptions and Verification Notes

Use the table/spec formats from `references/output-templates.md`.
Include direct links for all resources.
Do not output uncited recommendations.

## Fallback Handling

- If the requested source counts are not achievable, return the maximum high-quality set found and explain the gap.
- If forum sources are noisy, include fewer threads and raise confidence only for corroborated advice.
- If the time budget is unrealistic for target outcomes, provide three items: minimum viable plan, recommended extended plan, and tradeoff summary.

## Quality Checklist

Before finalizing, confirm all checks:

- Source inventory includes links, difficulty, and quality score.
- Every module has objectives, resources, labs, and rubric.
- Exercises map to real-world tasks.
- Capstone aligns with learner goals and constraints.
- Workload fits declared time budget.
- All assumptions are explicit and auditable.

## Resources

- Use `references/source-quality-rubric.md` for source scoring and threshold decisions.
- Use `references/output-templates.md` for final artifact formatting.
- Use `scripts/build_curriculum_scaffold.py` when a deterministic Markdown scaffold is needed quickly.
