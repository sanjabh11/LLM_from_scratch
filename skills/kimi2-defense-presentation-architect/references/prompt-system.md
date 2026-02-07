# Prompt System (Upgraded)

Use this file to generate deck prompts after the improvement plan is complete.

## Visual Mode Contract

Select one mode per deck and keep it consistent unless user explicitly requests mixed mode.

### Mode 1: Executive Light
- Background: pearl white to soft gray gradient (`#FAFAFA` to `#F0F4F8`).
- Text primary: deep charcoal (`#2D3748`), secondary (`#4A5568`).
- Technical accent: navy (`#1A365D`), key emphasis: brass/copper (`#C9A227`, `#B7791F`).
- Grid/line: whisper gray (`#E2E8F0`).

### Mode 2: Mission Blueprint Dark
- Background: deep blueprint navy range for technical training context.
- Text: high-contrast light text for readability.
- Semantic accents fixed: green=fused success, yellow=intermediate prediction, red=failure/degradation, cyan=primary data flow, orange=preprocessing emphasis.
- Preserve color semantics across all slides once assigned.

## Global Prompt Contract

Apply to every slide prompt:
- Enforce selected visual mode with high contrast and semantic consistency.
- Use descriptive section names, not "Panel 1/2/3" labels.
- Keep the visual narrative instructional, not decorative.
- Include defense application mapping for core technical concepts.
- Include beginner explanation and practitioner-depth notes.
- Ban meta artifacts (tool/version/footer/control comments).
- Include a lower-right Wise Owl insight module on every slide.

## Panel Architecture Contract

Use one of these structures per concept slide:
- Central engine + satellite panels
- Comparison storyline board
- Technical dissection grid (2x2 or 2x3)
- Pipeline macro-board
- Code split board (left code, right explanation)

Minimum panel rules:
- 4-7 major panels per concept slide.
- 10-15 micro annotations/callouts with anchored pointers.
- Clear directional flow markers.

## Global Negative Constraints

Never include:
- Tool names or model names in final slide prompts.
- Aspect ratio boilerplate.
- Dark neon themes.
- Placeholder debugging markers.
- Panel numbering as structural crutch.
- Exposed MCQ answers in participant-visible content.
- Missing Wise Owl module.

## Slide Types

### Type A: Title

Required blocks:
- Visual scene (premium, light, cinematic but uncluttered).
- Title, subtitle, one-line mission statement.
- Wise Owl lower-right insight box.

### Type B: Agenda

Required blocks:
- Two-column progression map.
- Session outcomes phrased as capabilities.
- Visual hierarchy with restrained accent bars.
- Wise Owl lower-right insight box.

### Type C: Concept Diagram (Primary)

Required blocks:
- Overview.
- The Concept.
- How It Works.
- Implementation.
- Why It Matters.
- Complete View.
- Extended Annotations (12-15).
- Beginner's Corner.
- Wise Owl lower-right insight box.

Mandatory annotation taxonomy:
1. Core definition
2. Problem solved
3. Use conditions
4. Non-use conditions
5. Common mistake
6. Performance implications
7. sklearn mapping
8. PyTorch mapping
9. Civilian application
10. Defense application
11. Alternative comparison
12. Practitioner tip
13. Historical context
14. Debugging guide
15. Related concept link

### Type D: Code Demonstration

Required blocks:
- Left (55-60%): code with numbered step comments and one highlighted critical line per step.
- Right (40-45%): numbered explanation lane matched to code step numbers.
- Add one error-path or edge-case note with corrective action.
- Add one result statement (runtime/behavior/performance outcome).
- Beginner's Corner.
- Wise Owl lower-right insight box.

### Type E: Recap

Required blocks:
- Journey visualization.
- Six key takeaways.
- Capability checklist (what learner can now do).
- Next-stage transition.
- Wise Owl lower-right insight box.

### Type F: MCQ Assessment (Optional, only when requested)

Required blocks:
- Question stem.
- 4 options (A-D) visible to participants.
- No correct answer in visible slide body.
- Presenter-only answer control in collapsed dropdown.

Presenter dropdown contract:
- Use a collapsed control labeled `Instructor Answer (Hidden During Presentation)`.
- Store `Correct Option`, `Rationale`, and `Trap Explanation` inside this dropdown.
- If the rendering stack does not support dropdown UI, place answer key in presenter notes only (never in participant-visible canvas).

Reference implementation block:

```markdown
### MCQ
Question: [prompt text]
A. [option]
B. [option]
C. [option]
D. [option]

<details>
<summary>Instructor Answer (Hidden During Presentation)</summary>
Correct Option: B
Rationale: ...
Trap Explanation: ...
</details>
```

## Beginner's Corner Contract

Always include:
- What this means (simple analogy, plain words).
- Why it matters (one defense + one daily-life example).
- Common mistake (clear corrective action).

## Wise Owl Contract

Always include:
- Placement: lower-right region.
- Form: owl icon badge plus one concise insight sentence.
- Content: technically meaningful heuristic, not motivational filler.

## Defense Mapping Contract

For each major concept slide:
- Add one operationally safe defense use case.
- Add one governance or safety checkpoint.
- Add one reliability or validation note.

## Visual Description Contract

Write visual descriptions in 3-4 sentences with:
- Scene composition
- Material and lighting
- Information flow cues
- Emphasis points tied to pedagogy

Avoid decorative excess that does not improve comprehension.

## Deterministic Generation Pattern

Generate in this order:
1. Slide list with intent.
2. Per-slide prompt draft.
3. Per-slide QA fix.
4. Final consolidated prompts.

If drift appears between slides, regenerate only failed slides and re-run QA.
