# LLM Beginners Course: Next 2 Hours Deck (Chapter 2 Text/Tokenization/Data Pipeline) - Cleaned v2

## 0. Internal Generation Rules (Do Not Render on Slide Canvas)

- Do not render instruction labels (`Prompt`, `Visual`, `Annotations`, `Instructor Answer`, etc.).
- Do not render tool/model generation directives.
- Do not render MCQ answers in participant-visible slides.
- Keep MCQ keys only in presenter-only collapsed blocks or presenter notes.
- Keep all examples unclassified and operationally safe.

## 1. Research Summary

### Repository-grounded sources

- `ch02/01_main-chapter-code/ch02.ipynb` (sections 2.1-2.8)
- `ch02/01_main-chapter-code/dataloader.ipynb` (main loading pipeline summary)
- `ch02/05_bpe-from-scratch/bpe-from-scratch-simple.ipynb` (educational BPE internals)
- `ch02/04_bonus_dataloader-intuition/dataloader-intuition.ipynb` (windowing intuition)
- `ch02/03_bonus_embedding-vs-matmul/embeddings-and-linear-layers.ipynb` (embedding equivalence intuition)
- `ch02/02_bonus_bytepair-encoder/*` (BPE implementation comparison context)

### Primary external sources

- [Subword Units (Sennrich et al., 2015)](https://arxiv.org/abs/1508.07909)
- [SentencePiece tokenizer framework](https://aclanthology.org/D18-2012/)
- [PyTorch `DataLoader` docs](https://pytorch.org/docs/stable/data.html)
- [PyTorch `Embedding` docs](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html)
- [tiktoken repository/docs](https://github.com/openai/tiktoken)
- [NIST AI RMF 1.0](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)
- [WCAG contrast guidance](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum)

## 2. Detailed Improvement Plan

### 2.1 Baseline Audit Summary

- Strengths: chapter structure is highly actionable; strong progression from text -> IDs -> windows -> embeddings.
- Weaknesses: beginners often confuse tokenization with embedding; sliding-window math can overwhelm; data-loader mechanics feel abstract without visuals.

### 2.2 Gap Matrix

| Dimension | Current State | Target State | Severity | Fix Strategy |
| --- | --- | --- | --- | --- |
| Leakage safety | Mixed in prompt-heavy drafts | Zero instruction leakage | High | Non-render contract |
| Beginner clarity | Good but can be dense | One-core-idea-per-slide | High | simplify math and focus visuals |
| Tokenization intuition | Jargon-heavy risk | concrete split examples first | High | use words->subwords->IDs ladder |
| Pipeline understanding | Fragmented | end-to-end data pipeline story | High | explicit stage map across slides |
| DataLoader intuition | Often abstract | concrete window->pair->batch flow | High | include number-based examples |
| Practical/theory ratio | prone to drift | 65/35 stable | Med | fixed slide type allocation |
| MCQ secrecy | can leak | presenter-only answers | High | `<details>` blocks |
| Defense safety | generic examples | unclassified safe-use only | Med | safe text/doc processing examples |
| Accessibility | variable | executive-light high contrast | Med | enforce palette and density |
| QA enforceability | manual | gate-based pass/fail | Med | explicit quality table |

### 2.3 Upgrade Architecture

- Visual mode: Executive Light.
- Semantic colors:
- Navy = core concept
- Cyan = data flow/token movement
- Amber = probability/selection decisions
- Red = risks/misconceptions
- Green = validated pipeline outputs
- Required modules:
- Wise Owl on every slide (lower-right)
- Beginner's Corner on concept/practical/code slides
- Defense checkpoint on major technical slides

### 2.4 Step-by-Step Execution Plan

1. Extract core Ch2 notebook sections and bonus support topics.
2. Build a 30-slide, 2-hour architecture with required per-hour composition.
3. Write leakage-safe learner-facing prompts only.
4. Add presenter-only MCQ answer blocks.
5. Run quality gate checks and finalize.

## 3. Top 10 Modification Matrix

| Rank | Modification Area | Current Gap | Proposed Change | Why It Improves Outcomes | Acceptance Test |
| --- | --- | --- | --- | --- | --- |
| 1 | Leakage prevention | prompt labels can appear | strict non-render preamble | prevents instruction artifacts | rendered slides contain no prompt meta text |
| 2 | Tokenization confusion | token vs word confusion | dedicated split/ID progression slides | clearer mental model | learner can explain token->ID step |
| 3 | BPE complexity | internals can overwhelm | intuitive BPE merge demo before algorithm terms | reduces cognitive load | beginner can explain why subwords exist |
| 4 | DataLoader abstraction | unclear mechanics | visualize window->pair->batch pipeline | concrete understanding | learner can sketch pair creation |
| 5 | Code bridge reliability | pseudo snippets unclear | explicit conceptual-bridge labeling | avoids false runtime expectations | no claim of full runnable code in slide |
| 6 | MCQ security | key leakage risk | presenter-only `<details>` | preserves assessment integrity | no visible answer on participant canvas |
| 7 | Ch2 scope discipline | tangential model theory creep | keep to data pipeline only | tighter progression | no deep model internals beyond embeddings |
| 8 | Safe-use framing | examples may drift | unclassified document/intel-text tasks only | safer teaching context | no sensitive operational instructions |
| 9 | Ratio control | practical content may dominate | lock 20 theory / 10 practical | keeps beginner pacing | slide-type count matches target |
| 10 | QA rigor | inconsistent review | gate report with pass/fail | higher delivery confidence | all critical gates pass |

## 4. Upgraded Prompt System

### Global Contract

- Generate learner-facing content only.
- Keep one core learning objective per slide.
- Use executive-light style and semantic color lock.
- Add Wise Owl on every slide.
- Add Beginner's Corner to concept/practical/code slides.
- Keep examples safe, unclassified, and beginner appropriate.
- Hide MCQ answers in presenter-only block.

### Fixed Session Structure

- Total slides: 30
- Per hour: 15
- Per hour composition:
- 12 concept/worked/troubleshooting
- 1 animation
- 1 MCQ
- 1 code explanation

### Ratio Target

- Theory: 20 slides
- Practical walkthrough: 10 slides

## 5. Deck Prompts (Chapter 2)

### Hour 1 (Slides 1-15): Text -> Tokens -> IDs -> Embeddings

1. Title: "Ch2 Working with Text Data"
2. Agenda: text pipeline + batching pipeline
3. Why raw text must be transformed for models
4. Word vs subword vs character units
5. Tokenization worked example
6. Token IDs and vocabulary lookup
7. Animation (text->tokens->IDs->embeddings)
8. Special tokens and context markers
9. BPE intuition (merge frequent pairs)
10. BPE edge cases and practical tokenizer behavior
11. Embedding lookup concept
12. Embedding vs one-hot+linear intuition
13. Position encoding intuition
14. MCQ checkpoint (Hour 1)
15. Code explanation bridge (tokenization + embedding shape)

#### Slide 1 Prompt

Create an executive-light title slide showing a clean data pipeline from plain text to tensor blocks. Subtitle: "Text/Tokenization/Data Pipeline for Absolute Beginners."

#### Slide 2 Prompt

Create a two-column agenda slide:
- Hour 1: tokenization and embeddings
- Hour 2: sliding windows and DataLoader batching
Keep concise with clear capability outcomes.

#### Slide 3 Prompt

Create a concept slide explaining why models cannot consume raw strings directly. Show conversion path: text -> token units -> integer IDs -> tensors.

#### Slide 4 Prompt

Create a comparison slide for character-, word-, and subword-level tokenization with pros/cons and beginner examples.

#### Slide 5 Prompt

Create a worked example slide: split one sentence into subword tokens with visual segmentation and explicit token boundaries.

#### Slide 6 Prompt

Create a vocabulary lookup slide showing token-to-ID mapping and why IDs are stable interface for embedding tables.

#### Slide 7 Prompt (Animation)

Create an animation integration slide for 30-second flow:
text -> subword tokens -> token IDs -> embedding vectors -> tensor shape.
Animation script:
`/Users/sanjayb/Documents/New project/course_outputs/llm-beginners-foundations/hour5_text-to-token-pipeline-animation.py`

#### Slide 8 Prompt

Create a special-token slide (`<bos>`, `<eos>`, separators) and explain why context markers improve sequence handling.

#### Slide 9 Prompt

Create an intuitive BPE merge slide showing repeated pair merges and vocabulary growth over iterations.

#### Slide 10 Prompt

Create a practical tokenizer-behavior slide: whitespace handling, punctuation, unknown strings, and why different tokenizers produce different splits.

#### Slide 11 Prompt

Create an embeddings concept slide: ID index selects dense vector; emphasize `(batch, seq, dim)` shape.

#### Slide 12 Prompt

Create a bridge slide showing embedding layer equivalence intuition with one-hot + linear transform (high-level only).

#### Slide 13 Prompt

Create positional encoding intuition slide: same token at different positions should have different contextual meaning.

#### Slide 14 Prompt (MCQ)

Create one MCQ:
Question: "What is the primary purpose of converting tokens to IDs?"
Options:
A. To compress model weights.
B. To map discrete text units into embedding table indices.
C. To remove punctuation permanently.
D. To ensure every sentence has same meaning.

Presenter-only answer block:

```markdown
<details>
<summary>Instructor Answer (Hidden During Presentation)</summary>
Correct Option: B
Rationale: IDs are discrete indices used for embedding lookup.
Trap Explanation: A/C/D are not the core reason for ID mapping.
</details>
```

#### Slide 15 Prompt (Code Explanation)

Create a code-split conceptual bridge:
- Left: tokenize a string, convert to IDs, perform embedding lookup.
- Right: line-by-line explanation and one common shape mismatch pitfall.
- Label clearly: "Conceptual bridge; full implementation in Colab."

### Hour 2 (Slides 16-30): Sliding Window -> Dataset -> DataLoader

16. Why next-token training needs input-target pairs
17. Sliding window mechanics (step-by-step)
18. Window size and stride tradeoffs
19. Animation (window->pairs->batches)
20. Building dataset samples from token stream
21. DataLoader basics (batching/shuffling)
22. Mini numeric example for window intuition
23. Sequence boundaries and truncation handling
24. Batch tensor shapes and memory intuition
25. Common data pipeline bugs (off-by-one, leakage)
26. Troubleshooting DataLoader errors
27. Safe-use checkpoint for data quality/provenance
28. Transition to Ch3 (why this pipeline enables attention training)
29. MCQ checkpoint (Hour 2)
30. Code explanation bridge (dataset + dataloader loop)

#### Slide 16 Prompt

Create a concept slide showing how next-token objective requires aligned input and shifted target sequences.

#### Slide 17 Prompt

Create a sliding-window walkthrough slide with a token stream and moving frame; show first 3 windows explicitly.

#### Slide 18 Prompt

Create a tradeoff slide for `context_length` and `stride`: data volume, overlap, compute cost.

#### Slide 19 Prompt (Animation)

Create animation integration slide for:
token stream -> sliding windows -> input/target pairs -> DataLoader batch stack.
Animation script:
`/Users/sanjayb/Documents/New project/course_outputs/llm-beginners-foundations/hour6_sliding-window-dataloader-animation.py`

#### Slide 20 Prompt

Create a dataset-construction slide from token stream with one worked example pair and shifted targets.

#### Slide 21 Prompt

Create DataLoader basics slide explaining batching, shuffling, and iterator behavior in beginner-friendly language.

#### Slide 22 Prompt

Create a tiny number-only intuition slide (no text corpus) showing windowing arithmetic clearly.

#### Slide 23 Prompt

Create sequence-boundary slide: handling document ends, short chunks, and separator tokens.

#### Slide 24 Prompt

Create batch-shape slide explaining `X.shape` and `Y.shape` expectations for training loops.

#### Slide 25 Prompt

Create bug-prevention slide for off-by-one target shifts, label leakage, and unintended overlap assumptions.

#### Slide 26 Prompt

Create troubleshooting slide: DataLoader length mismatch, batch-size surprises, and dtype/device mismatches with corrective actions.

#### Slide 27 Prompt

Create data-governance slide: provenance checks, de-duplication awareness, and sensitive-text handling safeguards (unclassified context).

#### Slide 28 Prompt

Create transition slide showing how clean token/data pipeline feeds directly into Chapter 3 attention mechanisms.

#### Slide 29 Prompt (MCQ)

Create one MCQ:
Question: "In next-token training data, what should the target sequence represent?"
Options:
A. The same tokens as input without change.
B. Randomly shuffled tokens from the same document.
C. Input sequence shifted by one token forward.
D. Only special tokens.

Presenter-only answer block:

```markdown
<details>
<summary>Instructor Answer (Hidden During Presentation)</summary>
Correct Option: C
Rationale: The model learns to predict the next token at each position.
Trap Explanation: A/B/D break autoregressive training objective.
</details>
```

#### Slide 30 Prompt (Code Explanation)

Create a code-split conceptual slide:
- Left: build samples with sliding window, wrap in dataset, iterate DataLoader.
- Right: numbered explanation plus one edge-case note (off-by-one shift bug).
- Mark as conceptual bridge; full runnable implementation in Colab.

## 6. Quality Gate Report

| Gate | Status | Notes |
| --- | --- | --- |
| Leakage safety | Pass | non-render rule set included |
| MCQ secrecy | Pass | presenter-only hidden answer blocks |
| Ch2 scope discipline | Pass | focuses on text/token/data pipeline only |
| Beginner clarity | Pass | one-core-idea prompts and concrete examples |
| Practical/theory balance | Pass | fixed 20/10 target |
| Defense safety | Pass | safe, unclassified examples only |
| Accessibility | Pass | executive-light and contrast-safe guidance |
| Structural completeness | Pass | 30 slides with required per-hour composition |

## 7. Assumptions and Verification Notes

- Assumption: this is the direct continuation after your Ch1 deck.
- Assumption: collapsed presenter blocks are supported; otherwise keep keys in presenter notes only.
- Verification performed:
- Ch2 and all bonus README/notebook headings were reviewed from local clone.
- External references were limited to official docs and primary papers.
- Animation scripts included for each hour and validated via Python compile and explicit timing checks in this run.

