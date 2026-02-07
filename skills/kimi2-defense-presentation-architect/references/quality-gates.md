# Quality Gates

Run all gates before delivering final prompts.

## Gate 1: Research Integrity

Pass criteria:
- Claims are backed by primary or authoritative sources.
- Model-specific guidance is current.
- Defense governance principles are represented.

## Gate 2: Plan-First Compliance

Pass criteria:
- Detailed improvement plan is delivered before final prompts.
- Gap matrix and risk mitigations are explicit.

## Gate 3: Prompt Determinism

Pass criteria:
- Slide templates are consistent.
- Output schema is explicit.
- No hidden dependencies on unstated assumptions.

## Gate 4: Pedagogy

Pass criteria:
- Coherence: no irrelevant decorative noise.
- Signaling: key paths/relationships clearly cued.
- Contiguity: labels placed near relevant visuals.
- Segmenting: complex flows split into manageable chunks.

## Gate 5: Accessibility

Pass criteria:
- Contrast is valid for chosen visual mode (light or dark) and readable.
- Intended text contrast aligns to WCAG targets (4.5:1 normal text, 3:1 large text).
- Dense text blocks avoided.

## Gate 6: Color Semantics

Pass criteria:
- Semantic colors are explicitly declared once.
- Meaning is consistent slide-to-slide (for example: red is always failure/risk, green is always fused success).
- Colors are not reused decoratively in ways that conflict with semantics.

## Gate 7: Defense Relevance

Pass criteria:
- Major concept slides contain defense application mapping.
- Responsible AI concepts included: traceability, reliability, governance, bias awareness.
- Examples remain unclassified and training-safe.

## Gate 8: Annotation Quality

Pass criteria:
- Concept slides include 12-15 annotations.
- Annotations include practical implementation and debugging guidance.
- Civilian + defense examples included.

## Gate 9: Beginner Comprehension

Pass criteria:
- Beginner's Corner included on concept slides.
- Explanations are concrete and analogy-backed.
- Common mistake + fix is actionable.

## Gate 10: Wise Owl Presence

Pass criteria:
- Every slide includes Wise Owl module in lower-right placement.
- Insight text is concise and technically meaningful.

## Gate 11: Structural Completeness

Pass criteria:
- Title and agenda present.
- Session A and Session B concept coverage complete.
- Recaps included at section and deck end.

## Gate 12: MCQ Answer Secrecy (When MCQ Used)

Pass criteria:
- Correct answer is not visible in participant slide body.
- Correct answer exists in collapsed presenter-only dropdown or presenter notes.
- Dropdown label clearly indicates hidden instructor content.

## Gate 13: Prohibited Content

Pass criteria:
- No tool-name leakage in slide prompts.
- No aspect-ratio/meta tags.
- No dark-theme or neon instructions.
- No footer/version/control clutter.
- No visible answer keys on MCQ participant view.

## Scoring Rubric (Optional)

Score each gate from 0-2:
- `0` fail
- `1` partial
- `2` pass

Interpretation:
- `22-26`: release-ready
- `17-21`: revise and re-check
- `<17`: major rewrite required
