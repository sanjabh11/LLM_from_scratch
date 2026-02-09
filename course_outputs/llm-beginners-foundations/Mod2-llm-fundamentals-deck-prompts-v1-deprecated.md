# LLM Beginners Course: Next 2 Hours Deck (Chapter 1 Fundamentals)

## 0. Internal Generation Rules (Do Not Render)

- Do not render prompt-engineering labels or internal instructions on learner slides.
- Do not render hidden keys or instructor-only notes in participant view.
- Keep all examples unclassified and operationally safe.
- Add one lower-right Wise Owl insight on every slide.

## 1. Ch1 Alignment Notes

- Ch1 has no direct notebook assets.
- Hands-on bridge assets:
- `appendix-A/01_main-chapter-code/code-part1.ipynb`
- `appendix-A/01_main-chapter-code/code-part2.ipynb`
- `appendix-A/01_main-chapter-code/exercise-solutions.ipynb`

## 2. 30-Slide Structure (No MCQ)

- Slides 1-2: title + agenda
- Slides 3-12: concept foundations
- Slide 13: practical bridge
- Slide 14: hands-on appendix A
- Slide 15: code explanation A
- Slides 16-24: concept + practical mixed
- Slides 25-26: practical + troubleshooting
- Slide 27: code explanation B
- Slides 28-29: hands-on appendix B/C
- Slide 30: session takeaway

## 3. Slide-by-Slide Map with Hands-on Anchors

| Slide | Type | Topic | Hands-on Anchor |
| --- | --- | --- | --- |
| 1 | Title | LLM fundamentals mission | - |
| 2 | Agenda | 2-hour capability map | - |
| 3 | Concept | What an LLM is (probabilistic next-token predictor) | - |
| 4 | Concept | AI vs ML vs DL vs LLM | - |
| 5 | Concept | Text to tokens intuition | - |
| 6 | Concept | Why subword tokenization exists | - |
| 7 | Animation | pipeline intuition | - |
| 8 | Concept | Context window | - |
| 9 | Concept | Embeddings intuition | - |
| 10 | Concept | Transformer high-level block map | - |
| 11 | Practical | Decoding intuition and outputs | `[Hands-on Anchor: CH1-LAB-01 | Asset: appendix-A/01_main-chapter-code/code-part1.ipynb | Objective: inspect tensor outputs as model-like numeric flow | Pre-req: None]` |
| 12 | Troubleshooting | Misconceptions: confidence vs correctness | `[Hands-on Anchor: CH1-LAB-02 | Asset: appendix-A/01_main-chapter-code/code-part1.ipynb | Objective: compare expected vs observed outputs mindset | Pre-req: CH1-LAB-01]` |
| 13 | Practical | Safe verification workflow | `[Hands-on Anchor: CH1-LAB-03 | Asset: appendix-A/01_main-chapter-code/code-part2.ipynb | Objective: apply simple verification routine | Pre-req: CH1-LAB-01]` |
| 14 | Appendix A | Hands-on checklist (Hour 1 bridge) | `[Hands-on Anchor: CH1-LAB-APP-A | Asset: appendix-A/01_main-chapter-code/code-part1.ipynb | Objective: run selected cells in order | Pre-req: CH1-LAB-01..03]` |
| 15 | Code A | minimal tensor->logit conceptual bridge | `[Hands-on Anchor: CH1-CODE-01 | Asset: appendix-A/01_main-chapter-code/code-part1.ipynb | Objective: explain line-by-line numerical flow | Pre-req: CH1-LAB-01]` |
| 16 | Concept | Self-attention intuition | - |
| 17 | Concept | Q/K/V mapping | - |
| 18 | Concept | Causal masking | - |
| 19 | Animation | attention flow | - |
| 20 | Concept | Pretraining objective intuition | - |
| 21 | Concept | Scaling intuition | - |
| 22 | Practical | Hallucination risk and mitigation | `[Hands-on Anchor: CH1-LAB-04 | Asset: appendix-A/01_main-chapter-code/code-part2.ipynb | Objective: connect outputs to validation checks | Pre-req: CH1-LAB-03]` |
| 23 | Practical | Prompt quality comparison | `[Hands-on Anchor: CH1-LAB-05 | Asset: appendix-A/01_main-chapter-code/exercise-solutions.ipynb | Objective: test structured vs vague instruction templates | Pre-req: CH1-LAB-04]` |
| 24 | Concept | Evaluation basics for beginners | - |
| 25 | Practical | Lifecycle map: pretrain->tune->evaluate | `[Hands-on Anchor: CH1-LAB-06 | Asset: appendix-A/01_main-chapter-code/code-part2.ipynb | Objective: map conceptual lifecycle to executable blocks | Pre-req: CH1-LAB-03]` |
| 26 | Troubleshooting | failure modes and corrective actions | `[Hands-on Anchor: CH1-LAB-07 | Asset: appendix-A/01_main-chapter-code/exercise-solutions.ipynb | Objective: diagnose and correct naive assumptions | Pre-req: CH1-LAB-05]` |
| 27 | Code B | simplified attention code bridge | `[Hands-on Anchor: CH1-CODE-02 | Asset: appendix-A/01_main-chapter-code/code-part2.ipynb | Objective: map QK^T->softmax->weighted sum to code lines | Pre-req: CH1-LAB-04]` |
| 28 | Appendix B | instructor run-order for lab bridge | `[Hands-on Anchor: CH1-LAB-APP-B | Asset: appendix-A/01_main-chapter-code/code-part2.ipynb | Objective: complete hour-2 bridge sequence | Pre-req: CH1-LAB-04..07]` |
| 29 | Appendix C | extension options before Ch2 | `[Hands-on Anchor: CH1-LAB-APP-C | Asset: appendix-A/01_main-chapter-code/exercise-solutions.ipynb | Objective: choose reinforcement exercises | Pre-req: CH1-LAB-05]` |
| 30 | Takeaway | session recap and Ch2 prep | - |

## 4. Tight Code Slide Guidance

### Slide 15 (Code A)

- Keep snippet strictly aligned to `code-part1.ipynb`.
- Explain only:
1. tensor creation
2. shape inspection
3. simple transform
- Must include one explicit shape check line and one common mismatch fix.

### Slide 27 (Code B)

- Keep snippet strictly aligned to `code-part2.ipynb`.
- Explain only:
1. score computation intuition
2. normalization/softmax intuition
3. weighted aggregation intuition
- Mark as conceptual bridge, not full model training.

## 5. Animation References

- Hour 1 animation: `/Users/sanjayb/Documents/New project/course_outputs/llm-beginners-foundations/hour3_llm-fundamentals-animation.py`
- Hour 2 animation: `/Users/sanjayb/Documents/New project/course_outputs/llm-beginners-foundations/hour4_self-attention-animation.py`

