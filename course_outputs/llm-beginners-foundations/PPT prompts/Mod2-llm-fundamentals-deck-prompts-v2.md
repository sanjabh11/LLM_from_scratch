# LLM Beginners Course: Next 2 Hours Deck (Chapter 1 Fundamentals) -  

## 0. Internal Generation Rules (Do Not Render on Slide Canvas)

These rules are for generation only. They must never appear in learner-visible slides.

- Do not render labels like `Prompt`, `Visual`, `Annotations`, `Beginner's Corner`, `Wise Owl`, `Defense Checkpoint`, `Instructor Answer`.
- Do not render tool/model/process directives.
- Do not render hidden MCQ answers in participant view.
- Keep answer keys only in presenter-only collapsed blocks or presenter notes.
- Keep all examples unclassified and operationally safe.

## 1. Research Summary

### Repository-grounded sources

- `ch01/README.md` (conceptual overview, no code in chapter)
- `ch01/reading-recommendations.md` (learning sequence)
- `README.md` (book/repo progression)
- `appendix-A/01_main-chapter-code` (minimal code bridge for mandatory code slides)

### Primary external sources

- [Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762)
- [Subword Units / BPE basis (2015)](https://arxiv.org/abs/1508.07909)
- [Scaling Laws for Neural LMs (2020)](https://arxiv.org/abs/2001.08361)
- [GPT-3 / few-shot behavior (2020)](https://arxiv.org/abs/2005.14165)
- [InstructGPT / alignment (2022)](https://arxiv.org/abs/2203.02155)
- [NIST AI RMF 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)
- [WCAG contrast guidance](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum)

## 2. Detailed Improvement Plan

### 2.1 Baseline Audit Summary

- Strengths: strong conceptual arc, good analogies, practical bridges.
- Weaknesses: leakage risk from instruction labels, hidden-answer handling inconsistency, some scope creep beyond Ch1, a few risky defense examples.

### 2.2 Gap Matrix

| Dimension | Current State | Target State | Severity | Fix Strategy |
| --- | --- | --- | --- | --- |
| Leakage safety | Mixed | Zero instruction leakage | High | Add strict non-render rules |
| MCQ secrecy | Partially hidden | Fully presenter-only | High | Use `<details>` answer blocks |
| Ch1 scope control | Slightly broad | Ch1-focused mental model | High | Defer deep lifecycle details |
| Beginner clarity | Good but dense | One-core-idea-per-slide | Med | Reduce annotation load |
| Defense safety | Mixed examples | Unclassified-safe examples only | High | Replace risky examples |
| Prompt determinism | Good | Fully standardized | Med | Uniform slide schema |
| Practical/theory balance | Slight drift | 65/35 target | Med | Lock slide-type distribution |
| Accessibility | Good | Explicitly constrained | Med | Executive Light + contrast rules |
| Annotation quality | High but heavy | Focused, teachable | Med | 8-12 key annotations |
| QA enforceability | Manual | Gate-based pass/fail | Med | Add final quality check table |

### 2.3 Upgrade Architecture

- Visual mode: Executive Light.
- Semantic color lock:
- Navy = core architecture
- Cyan = data flow
- Amber = probability/prediction
- Red = risk/failure/misconception
- Green = validated/safe best practice
- Mandatory modules:
- Wise Owl (every slide, lower-right)
- Beginner's Corner (all concept/practical/code slides)
- Defense Checkpoint (major technical slides, safe-only)

### 2.4 Step-by-Step Execution Plan

1. Extract Ch1-only core concepts.
2. Allocate 30 slides (15/hour) with fixed required composition.
3. Write leakage-safe prompts (no renderable instruction labels).
4. Insert presenter-only MCQ answers.
5. Run quality gates and patch failures.

## 3. Top 10 Modification Matrix

| Rank | Modification Area | Current Gap | Proposed Change | Why It Improves Outcomes | Acceptance Test |
| --- | --- | --- | --- | --- | --- |
| 1 | Leakage prevention | Instruction labels may appear | Add strict non-render preamble | Prevents prompt artifacts on slides | No instruction labels in rendered output |
| 2 | MCQ secrecy | Answer can leak | Presenter-only `<details>` blocks | Preserves assessment integrity | Answer invisible in participant view |
| 3 | Ch1 scope | Slight content spillover | Restrict to mental model + attention intuition | Better beginner pacing | No advanced implementation overload |
| 4 | Defense safety | Some risky examples | Use safe tasks only | Keeps content compliant/safe | No operationally sensitive tasks |
| 5 | Beginner load | Dense panels | One core idea per slide | Better retention | Clear slide objective per slide |
| 6 | Code bridge reliability | Ambiguous snippets | Mark pseudo vs runnable clearly | Less confusion | Every code slide has intent + caveat |
| 7 | Color semantics | Potential drift | Locked color meaning globally | Faster comprehension | Same meaning across all slides |
| 8 | Annotation discipline | Too many callouts | 8-12 focused annotations | Better readability | No cluttered slide text |
| 9 | Ratio drift | Practical count can creep | Lock 20 theory / 10 practical | Meets teaching strategy | Deck matches 65/35 target |
| 10 | QA rigor | Inconsistent reviews | Explicit gate report | More reliable final outputs | All critical gates pass |

## 4. Upgraded Prompt System

### Global Contract

- Generate learner-facing slide content only.
- Enforce Executive Light theme and semantic color lock.
- Keep language beginner-first, plain and concrete.
- Keep one core learning objective per slide.
- Add Wise Owl insight on every slide.
- Add Beginner's Corner to concept/practical/code slides.
- For MCQs: show question + options only; hide answers in presenter-only block.

### Fixed Structure

- 30 slides total.
- 15 slides per hour.
- Per hour:
- 12 concept/worked/troubleshooting
- 1 animation
- 1 MCQ
- 1 detailed code explanation

### Ratio Target

- Theory: 20 slides
- Practical: 10 slides

## 5. Deck Prompts (Chapter 1 Fundamentals, Clean v2)

### Hour 1 (Slides 1-15): Mental Model Foundations

1. Title: "LLM Fundamentals: From Text to Probabilities"
2. Agenda: 2-hour capability map
3. What an LLM is (probabilistic next-token model)
4. AI vs ML vs DL vs LLM taxonomy
5. Tokenization basics (words vs subwords)
6. Why subword tokenization (BPE intuition)
7. Animation slide (Hour 1 pipeline)
8. Context window intuition
9. Embeddings as coordinates
10. Transformer at 10,000 feet
11. Decoding intuition (greedy/temp/top-k/top-p)
12. Misconceptions part 1 (no "internet brain", no guaranteed truth)
13. Responsible use baseline (verify outputs, traceability)
14. MCQ checkpoint (Hour 1)
15. Code explanation bridge: token IDs -> embeddings -> probabilities

#### Slide 1 Prompt

Create a clean executive-light title slide showing text flowing through a simple model pipeline to probability outputs. Include subtitle "Chapter 1 Mental Models for Absolute Beginners." Add lower-right Wise Owl insight: "Understand the mechanism before trusting the output."

#### Slide 2 Prompt

Create a two-column agenda slide with Hour 1 (mental model) and Hour 2 (attention/training limits). Keep concise, high contrast, and beginner-friendly.

#### Slide 3 Prompt

Create a concept slide that explains LLM output as a probability distribution over next tokens. Visual: input phrase and ranked candidate token probabilities. Beginner's Corner: "It predicts likely continuations, not guaranteed facts." Defense Checkpoint: "Use as draft assistant, not final authority."

#### Slide 4 Prompt

Create a nested taxonomy diagram: AI -> ML -> DL -> LLM. Include one practical example each. Misconception callout: "Not all AI is LLM."

#### Slide 5 Prompt

Create a worked-example slide showing sentence-to-token conversion with token IDs. Include subword split example and why IDs matter.

#### Slide 6 Prompt

Create a comparison slide for character-, word-, and subword-tokenization. Emphasize sequence length vs vocabulary size tradeoff.

#### Slide 7 Prompt (Animation)

Create an animation integration slide for a 30-second explainer: text -> tokens -> embeddings -> transformer -> next-token distribution -> repeat loop. Reference script path:
`/Users/sanjayb/Documents/New project/course_outputs/llm-beginners-foundations/hour3_llm-fundamentals-animation.py`

#### Slide 8 Prompt

Create a context-window slide with a scrolling text strip and highlighted active window. Show that information outside the window is unavailable.

#### Slide 9 Prompt

Create an embeddings slide with clustered semantic vectors and simple "related words are nearby" intuition.

#### Slide 10 Prompt

Create a high-level transformer architecture slide showing embeddings, stacked blocks, and output head. Avoid deep math.

#### Slide 11 Prompt

Create a practical decoding slide comparing greedy and sampling settings with one probability bar chart.

#### Slide 12 Prompt

Create troubleshooting slide: top 3 beginner misconceptions and corrections.

#### Slide 13 Prompt

Create a safety and governance basics slide with verification checklist, provenance awareness, and human review requirement.

#### Slide 14 Prompt (MCQ)

Create a single MCQ slide:
Question: "Which statement best describes GPT-style text generation?"
Options:
A. It writes whole paragraphs in one step.
B. It predicts one token at a time using prior context.
C. It always checks live databases before answering.
D. It stores exact full documents and retrieves them verbatim.

Presenter-only answer block:

```markdown
<details>
<summary>Instructor Answer (Hidden During Presentation)</summary>
Correct Option: B
Rationale: Autoregressive generation predicts one token at a time.
Trap Explanation: A/C/D describe behaviors a base GPT does not guarantee.
</details>
```

#### Slide 15 Prompt (Code Explanation)

Create a code-split slide with a tiny pseudocode bridge:
- Left: tokenize text -> map to embeddings -> compute softmax logits.
- Right: line-by-line conceptual explanation and one common shape-mismatch error fix.
- Mark explicitly as "conceptual bridge, full implementation in Colab."

### Hour 2 (Slides 16-30): Attention, Limits, and Safe Use

16. Self-attention intuition
17. Query-Key-Value mapping
18. Causal masking
19. Animation slide (Hour 2 attention flow)
20. Pretraining objective intuition
21. Scaling intuition (compute/data/params tradeoff)
22. Hallucinations and confidence mismatch
23. Prompting basics (clear task framing)
24. Evaluation basics (correctness/relevance/safety)
25. Lifecycle overview (pretrain -> tune -> evaluate)
26. Misconceptions part 2 (debugging prompt vs model)
27. Safe use-case map (unclassified tasks only)
28. Lab transition (what learner will build next)
29. MCQ checkpoint (Hour 2)
30. Code explanation bridge: simplified attention forward pass

#### Slide 16 Prompt

Create a self-attention intuition slide using "which prior words matter most" arrows and weighted links.

#### Slide 17 Prompt

Create a Q/K/V analogy slide (query asks, keys index relevance, values provide content). Keep beginner language.

#### Slide 18 Prompt

Create a causal-mask slide with lower-triangular visibility and "no future peeking" explanation.

#### Slide 19 Prompt (Animation)

Create an animation integration slide for attention flow: QK^T scores -> mask -> softmax -> weighted sum output. Reference script path:
`/Users/sanjayb/Documents/New project/course_outputs/llm-beginners-foundations/hour4_self-attention-animation.py`

#### Slide 20 Prompt

Create a pretraining loop slide: predict next token -> compute loss -> update weights -> repeat at scale.

#### Slide 21 Prompt

Create scaling-laws intuition slide with safe interpretation: more compute/data/params can improve performance but cost rises sharply.

#### Slide 22 Prompt

Create hallucination slide: plausible-sounding but incorrect output, plus verification checklist and mitigation habits.

#### Slide 23 Prompt

Create a prompt-quality comparison slide: vague prompt vs structured prompt with constraints and expected format.

#### Slide 24 Prompt

Create a beginner evaluation slide with simple rubric: correctness, relevance, consistency, safety.

#### Slide 25 Prompt

Create lifecycle slide mapping pretrain -> supervised tuning -> alignment -> evaluation (conceptual only).

#### Slide 26 Prompt

Create troubleshooting slide for repetition, cutoffs, refusals; include "fix prompt first" guidance.

#### Slide 27 Prompt

Create safe-use map slide with green-zone tasks:
- document summarization
- report drafting
- translation
- formatting/normalization
- non-critical triage assistance
Red-zone note: no autonomous high-stakes decision authority.

#### Slide 28 Prompt

Create transition slide previewing next lab tasks: tokenization inspection and miniature attention intuition notebook.

#### Slide 29 Prompt (MCQ)

Create a single MCQ slide:
Question: "Why is causal masking used in GPT-style decoders?"
Options:
A. To prevent access to future tokens during prediction.
B. To reduce model size.
C. To hide private data from users.
D. To convert text generation into image generation.

Presenter-only answer block:

```markdown
<details>
<summary>Instructor Answer (Hidden During Presentation)</summary>
Correct Option: A
Rationale: Causal masking enforces autoregressive time direction.
Trap Explanation: B/C/D are unrelated to the core decoder mask objective.
</details>
```

#### Slide 30 Prompt (Code Explanation)

Create a code-split conceptual attention slide:
- Left: `scores = Q @ K^T`, apply mask, softmax, `output = probs @ V`.
- Right: numbered explanations and one edge-case note (bad mask -> unstable probabilities).
- Label as conceptual bridge; full runnable code in Colab.

## 6. Quality Gate Report

| Gate | Status | Notes |
| --- | --- | --- |
| Leakage safety | Pass | Non-render rules defined |
| MCQ secrecy | Pass | Presenter-only blocks enforced |
| Beginner clarity | Pass | One-core-idea layout and plain language |
| Ch1 scope discipline | Pass | Mental-model focus maintained |
| Defense safety | Pass | Unclassified-safe examples only |
| Color semantics | Pass | Global semantic lock defined |
| Accessibility | Pass | Executive-light high-contrast guidance included |
| Structural completeness | Pass | 30 slides, required per-hour composition |

## 7. Assumptions and Verification Notes

- Assumption: You want this as direct replacement of prior Ch1 prompt pack.
- Assumption: Slide generator supports presenter-only collapsed blocks; if not, move answer keys to presenter notes.
- Verification:
- Prompt pack includes explicit anti-leakage safeguards.
- MCQ answers are hidden-format compliant.
- Animation scripts referenced are already compile-validated and timing-checked (~30s each).

