# Reference Deck Patterns (Extracted from User-Provided Slides)

Use this file when users provide example decks/images and request style replication plus improvement.

## 1) Visual DNA Summary

Observed recurring characteristics:
- Dark technical blueprint canvas with cyan circuit motifs and metallic isometric objects.
- High information density with clear segmentation into named panels.
- Strong semantic color coding (status and data meaning).
- Numbered callout markers that map narration order.
- Bottom pedagogy strip that combines Beginner's Corner and a lower-right Wise Owl insight.

Design implication:
- Treat these decks as `Mission Blueprint Dark` mode, while preserving accessibility and clarity.

## 2) Semantic Color Mapping

Adopt fixed color semantics once chosen for a deck:
- `Green`: fused/optimal path, robust outcome, successful integration.
- `Yellow/Amber`: prediction/estimation/intermediate correction layer.
- `Red`: failure mode, drift, gaps, degradation, single-point weakness.
- `Cyan/Teal`: primary data flow, sensor inputs, technical wiring.
- `Orange`: preprocessing/transformation stage or emphasis transitions.
- `White/Light Gray`: neutral labels and body text.

Rule:
- Do not reuse red/green/yellow arbitrarily for decoration. Keep semantics stable across all slides.

## 3) Panel Archetypes

### Archetype A: Central Engine + Satellite Panels
- Large center system panel (fusion engine, computation core).
- Side/top/bottom supporting panels (sensors, output, timing).
- Numbered flow order around the center.

### Archetype B: Comparison Storyline Board
- One scenario map (for example roadway/tunnel) with multiple trajectories.
- Distinct color-coded paths for alternatives and fused path.
- Embedded mini-charts and short quantitative claims.

### Archetype C: Technical Dissection Grid
- 2x2 or 2x3 modular panel grid.
- Each panel is one stage of the end-to-end technical story.
- Connector lines indicate direction and dependencies.

### Archetype D: Pipeline Macro-Board
- Left-to-right stages: input -> feature extraction -> classification/output.
- Repeating block motif for layered architectures.
- Compact textual bullets per block to explain purpose.

### Archetype E: Code + Explanation Split
- Left 55-60%: code card with readable syntax and step comments.
- Right 40-45%: numbered explanation lane with one pointer per step.
- Bottom-right: Wise Owl reinforcement insight tied to practical takeaway.

## 4) Detail Density and Annotation Style

Observed pattern:
- Macro structure: 4-7 major panels per slide.
- Micro structure: 10-15 annotations/callouts.
- Every callout is directional, short, and tied to a visual anchor.

Rule:
- Keep lines concise but specific. Prefer one idea per callout.
- Mix conceptual, operational, and error-mode annotations.

## 5) Beginner's Corner Pattern

Placement:
- Bottom strip, left or center-left.

Required contents:
- What this means.
- Why it matters.
- Common mistake (with corrective action).

Language style:
- Plain language with one vivid analogy.
- Keep terms concrete and avoid jargon stacking.

## 6) Wise Owl Pattern (Mandatory)

Placement:
- Lower-right module on every slide.

Visual form:
- Small owl icon badge plus one compact high-impact insight.
- Rounded or boxed card with strong contrast from surrounding background.

Content style:
- One memorable sentence that links concept to intuition or real-world behavior.
- Avoid generic motivation text; keep it technically meaningful.

## 7) Coding Explanation Pattern

Required structure for code slides:
1. Code block with step comments and one highlighted key line per step.
2. Numbered explanation lane matching code step numbers.
3. Error or edge-case note for at least one step.
4. Result statement with practical performance or behavior outcome.
5. Wise Owl reinforcement sentence.

## 8) Common Failure Modes Seen in Similar Decks

- Visual over-density without hierarchy.
- Color reuse that breaks semantic meaning.
- Inconsistent panel logic between slides.
- Missing governance/safety framing in defense examples.
- Beginner text disconnected from main visual.
- MCQ answer keys accidentally visible to participants.

Mitigation:
- Enforce quality gates for hierarchy, semantic color consistency, and panel continuity.

## 9) Assessment Visibility Control

When MCQs are included:
- Keep options visible to participants.
- Keep correct answer in presenter-only collapsed dropdown control.
- If dropdown UI is unavailable, store answer only in presenter notes.
- Never place answer hints in visible subtitles, color cues, or icon states.
