# Alignment Manifest v1

Repository baseline: `rasbt/LLMs-from-scratch` @ commit `82010e2` (2026-01-29).

## 1. Decisions Applied

1. Remove MCQ slides from each 2-hour deck.
2. Replace MCQ slots with Hands-on Appendix slides.
3. Add one mandatory Session Takeaway slide at the end of every 2-hour deck.
4. Tighten code explanation slides to map directly to real notebook/script assets.
5. Add mandatory Hands-on Anchor tags to every practical and code slide.
6. Create a global Code Appendix Pack with 4 code slides per chapter (Ch1-Ch7, total 28 slides).

## 2. Standard 30-Slide Blueprint (No MCQs)

Use this exact structure for every 2-hour deck:

| Slide Range | Type | Count | Notes |
| --- | --- | --- | --- |
| 1-2 | Title + Agenda | 2 | no anchor required |
| 3-12 | Concept foundation | 10 | no anchor required unless practical |
| 13 | Practical walkthrough | 1 | `Hands-on Anchor` required |
| 14 | Hands-on Appendix A | 1 | maps to immediate lab asset(s) |
| 15 | Code explanation A | 1 | `Hands-on Anchor` required |
| 16-24 | Concept + practical mixed | 9 | anchor required on practical slides |
| 25-26 | Practical + troubleshooting | 2 | `Hands-on Anchor` required |
| 27 | Code explanation B | 1 | `Hands-on Anchor` required |
| 28-29 | Hands-on Appendix B/C | 2 | lab prep + extension |
| 30 | Session Takeaway | 1 | mandatory end slide |

## 3. Hands-on Anchor Tag Specification

Every practical and code slide must contain one tag in this exact format:

```text
[Hands-on Anchor: <ID> | Asset: <repo path> | Objective: <what learner does> | Pre-req: <IDs or None>]
```

Example:

```text
[Hands-on Anchor: CH2-LAB-06 | Asset: ch02/01_main-chapter-code/dataloader.ipynb | Objective: Create sliding-window input/target pairs | Pre-req: CH2-LAB-01, CH2-LAB-02]
```

## 4. Ch2 Module Manifest (Slide-by-Slide)

Module: Text/tokenization/data pipeline  
Primary assets: `ch02/01_main-chapter-code/ch02.ipynb`, `ch02/01_main-chapter-code/dataloader.ipynb`, Ch2 bonus notebooks.

| Slide | Type | Topic | Hands-on Anchor |
| --- | --- | --- | --- |
| 1 | Title | Ch2 mission and outcomes | - |
| 2 | Agenda | Hour split and lab goals | - |
| 3 | Concept | Why models need tokenized numeric inputs | - |
| 4 | Concept | Character vs word vs subword units | - |
| 5 | Practical | Sentence splitting into subwords | `[Hands-on Anchor: CH2-LAB-01 | Asset: ch02/01_main-chapter-code/ch02.ipynb | Objective: Run tokenizer on sample text | Pre-req: None]` |
| 6 | Practical | Token IDs and vocab lookup | `[Hands-on Anchor: CH2-LAB-02 | Asset: ch02/01_main-chapter-code/ch02.ipynb | Objective: Map tokens to integer IDs | Pre-req: CH2-LAB-01]` |
| 7 | Animation | Text -> tokens -> IDs -> embeddings | - |
| 8 | Concept | Special tokens and context markers | - |
| 9 | Practical | BPE merge intuition | `[Hands-on Anchor: CH2-LAB-03 | Asset: ch02/05_bpe-from-scratch/bpe-from-scratch-simple.ipynb | Objective: Observe BPE merge steps | Pre-req: CH2-LAB-01]` |
| 10 | Practical | Tokenizer behavior differences | `[Hands-on Anchor: CH2-LAB-04 | Asset: ch02/02_bonus_bytepair-encoder/compare-bpe-tiktoken.ipynb | Objective: Compare tokenizer outputs | Pre-req: CH2-LAB-03]` |
| 11 | Concept | Embedding lookup overview | - |
| 12 | Concept | Embedding vs one-hot+linear intuition | - |
| 13 | Practical | Position encoding intuition | `[Hands-on Anchor: CH2-LAB-05 | Asset: ch02/01_main-chapter-code/ch02.ipynb | Objective: Inspect token + positional embedding flow | Pre-req: CH2-LAB-02]` |
| 14 | Appendix A | Immediate lab checklist (Hour 1) | `[Hands-on Anchor: CH2-LAB-APP-A | Asset: ch02/01_main-chapter-code/ch02.ipynb | Objective: Execute Hour-1 core cells in order | Pre-req: CH2-LAB-01..05]` |
| 15 | Code A | Tight code bridge: tokenize -> IDs -> embedding tensor shapes | `[Hands-on Anchor: CH2-CODE-01 | Asset: ch02/01_main-chapter-code/ch02.ipynb | Objective: Validate `(batch, seq, dim)` shapes | Pre-req: CH2-LAB-02]` |
| 16 | Concept | Why next-token training uses shifted targets | - |
| 17 | Practical | Sliding window mechanics | `[Hands-on Anchor: CH2-LAB-06 | Asset: ch02/01_main-chapter-code/ch02.ipynb | Objective: Generate windows with context length | Pre-req: CH2-LAB-02]` |
| 18 | Practical | Stride and overlap tradeoffs | `[Hands-on Anchor: CH2-LAB-07 | Asset: ch02/04_bonus_dataloader-intuition/dataloader-intuition.ipynb | Objective: Compare stride effects with simple numbers | Pre-req: CH2-LAB-06]` |
| 19 | Animation | Window -> pair -> batch flow | - |
| 20 | Practical | Build (input,target) training pairs | `[Hands-on Anchor: CH2-LAB-08 | Asset: ch02/01_main-chapter-code/dataloader.ipynb | Objective: Create shifted target pairs | Pre-req: CH2-LAB-06]` |
| 21 | Practical | DataLoader batching and shuffling | `[Hands-on Anchor: CH2-LAB-09 | Asset: ch02/01_main-chapter-code/dataloader.ipynb | Objective: Build and iterate DataLoader | Pre-req: CH2-LAB-08]` |
| 22 | Practical | Numeric toy example for clarity | `[Hands-on Anchor: CH2-LAB-10 | Asset: ch02/04_bonus_dataloader-intuition/dataloader-intuition.ipynb | Objective: Verify pair math on toy sequence | Pre-req: CH2-LAB-06]` |
| 23 | Concept | Sequence boundaries and truncation | - |
| 24 | Practical | Batch tensor shape verification | `[Hands-on Anchor: CH2-LAB-11 | Asset: ch02/01_main-chapter-code/dataloader.ipynb | Objective: Check X/Y shapes and dtypes | Pre-req: CH2-LAB-09]` |
| 25 | Practical | Off-by-one and label leakage bugs | `[Hands-on Anchor: CH2-LAB-12 | Asset: ch02/01_main-chapter-code/exercise-solutions.ipynb | Objective: Diagnose shift mistakes | Pre-req: CH2-LAB-08]` |
| 26 | Practical | DataLoader troubleshooting patterns | `[Hands-on Anchor: CH2-LAB-13 | Asset: ch02/01_main-chapter-code/dataloader.ipynb | Objective: Fix common loader errors | Pre-req: CH2-LAB-09]` |
| 27 | Code B | Tight code bridge: dataset class + loader loop | `[Hands-on Anchor: CH2-CODE-02 | Asset: ch02/01_main-chapter-code/dataloader.ipynb | Objective: Explain each step in loader pipeline | Pre-req: CH2-LAB-09]` |
| 28 | Appendix B | Colab run-order and checkpoints | `[Hands-on Anchor: CH2-LAB-APP-B | Asset: ch02/01_main-chapter-code/dataloader.ipynb | Objective: Execute Hour-2 core cells in order | Pre-req: CH2-LAB-06..13]` |
| 29 | Appendix C | Bonus path selection map | `[Hands-on Anchor: CH2-LAB-APP-C | Asset: ch02/02_bonus_bytepair-encoder/compare-bpe-tiktoken.ipynb; ch02/05_bpe-from-scratch/bpe-from-scratch.ipynb | Objective: choose advanced tokenizer extension | Pre-req: CH2-LAB-03]` |
| 30 | Takeaway | Session recap + next-module prep | - |

## 5. Module-Level Lab Manifest (All 12 Deck Blocks)

Each row maps one 2-hour deck block to required lab assets.

| Module # | Deck Block | Deck Slide Range | Core Lab Assets | Objective | Pre-req |
| --- | --- | --- | --- | --- | --- |
| 1 | Foundations + setup + minimal PyTorch | 1-30 | `setup/02_installing-python-libraries/python_environment_check.ipynb`; `appendix-A/01_main-chapter-code/code-part1.ipynb`; `appendix-A/01_main-chapter-code/code-part2.ipynb` | Environment readiness and tensor/training basics | None |
| 2 | LLM fundamentals (Ch1) | 1-30 | No Ch1 notebook. Bridge with `appendix-A/01_main-chapter-code/code-part1.ipynb`, `appendix-A/01_main-chapter-code/code-part2.ipynb` | Conceptual mental model anchored to minimal code | Module 1 |
| 3 | Text/tokenization/data pipeline (Ch2) | 1-30 | `ch02/01_main-chapter-code/ch02.ipynb`; `ch02/01_main-chapter-code/dataloader.ipynb`; Ch2 bonus notebooks | Text to model-ready batches | Module 2 |
| 4 | Attention mechanics (Ch3) | 1-30 | `ch03/01_main-chapter-code/ch03.ipynb`; `ch03/01_main-chapter-code/multihead-attention.ipynb`; bonus MHA/buffers notebooks | Build and reason about attention internals | Module 3 |
| 5 | GPT architecture from scratch (Ch4 core) | 1-30 | `ch04/01_main-chapter-code/ch04.ipynb`; `ch04/01_main-chapter-code/gpt.py`; `ch04/01_main-chapter-code/tests.py` | Assemble GPT block/model from components | Module 4 |
| 6 | Inference/performance/attention alternatives (Ch4 bonus) | 1-30 | `ch04/02_performance-analysis/flops-analysis.ipynb`; `ch04/03_kv-cache/*`; `ch04/04_gqa/*`; `ch04/05_mla/*`; `ch04/06_swa/*`; `ch04/07_moe/*`; `ch04/08_deltanet/*` | Compare inference/perf tradeoffs and alt attention | Module 5 |
| 7 | Pretraining pipeline (Ch5 core) | 1-30 | `ch05/01_main-chapter-code/ch05.ipynb`; `ch05/01_main-chapter-code/gpt_train.py`; `ch05/01_main-chapter-code/gpt_generate.py` | Run base pretraining/generation loop | Module 5 |
| 8 | Training improvements (schedulers/speed/tuning) | 1-30 | `ch05/04_learning_rate_schedulers/*`; `ch05/10_llm-training-speed/*`; `ch05/05_bonus_hparam_tuning/hparam_search.py`; `ch05/03_bonus_pretraining_on_gutenberg/*` | Improve throughput and training quality | Module 7 |
| 9 | Architecture variants + weight loading | 1-30 | `ch05/02_alternative_weight_loading/*.ipynb`; `ch05/07_gpt_to_llama/*.ipynb`; `ch05/08_memory_efficient_weight_loading/memory-efficient-state-dict.ipynb`; `ch05/11_qwen3/*.ipynb`; `ch05/12_gemma3/*.ipynb`; `ch05/13_olmo3/*.ipynb`; `ch05/14_ch05_with_other_llms/*.ipynb` | Load and compare LLM families and variants | Module 7 |
| 10 | Classification finetuning (Ch6) | 1-30 | `ch06/01_main-chapter-code/ch06.ipynb`; `ch06/01_main-chapter-code/load-finetuned-model.ipynb`; `ch06/03_bonus_imdb-classification/sklearn-baseline.ipynb`; `ch06/01_main-chapter-code/gpt_class_finetune.py` | Fine-tune and evaluate classifier behavior | Module 7 |
| 11 | Instruction tuning + evaluation pipeline (Ch7 core) | 1-30 | `ch07/01_main-chapter-code/ch07.ipynb`; `ch07/01_main-chapter-code/load-finetuned-model.ipynb`; `ch07/03_model-evaluation/*.ipynb`; `ch07/01_main-chapter-code/gpt_instruction_finetuning.py` | Build instruction-tuned workflow and evaluation | Module 10 |
| 12 | DPO + LoRA + capstone integration | 1-30 | `ch07/04_preference-tuning-with-dpo/dpo-from-scratch.ipynb`; `ch07/04_preference-tuning-with-dpo/create-preference-data-ollama.ipynb`; `appendix-E/01_main-chapter-code/appendix-E.ipynb`; `appendix-D/01_main-chapter-code/appendix-D.ipynb` | Preference tuning + parameter-efficient finetuning + capstone | Module 11 |

## 6. Global Code Appendix Pack Plan (7 Chapters x 4 Slides = 28)

Purpose: keep core decks within 30-slide limit while centralizing deep code walkthroughs.

| Chapter | Code Appendix Slides | Assets |
| --- | --- | --- |
| Ch1 | C1-S1..C1-S4 | `appendix-A/01_main-chapter-code/code-part1.ipynb`, `appendix-A/01_main-chapter-code/code-part2.ipynb` |
| Ch2 | C2-S1..C2-S4 | `ch02/01_main-chapter-code/ch02.ipynb`, `ch02/01_main-chapter-code/dataloader.ipynb`, `ch02/05_bpe-from-scratch/bpe-from-scratch-simple.ipynb` |
| Ch3 | C3-S1..C3-S4 | `ch03/01_main-chapter-code/ch03.ipynb`, `ch03/01_main-chapter-code/multihead-attention.ipynb` |
| Ch4 | C4-S1..C4-S4 | `ch04/01_main-chapter-code/ch04.ipynb`, `ch04/01_main-chapter-code/gpt.py`, `ch04/03_kv-cache/*` |
| Ch5 | C5-S1..C5-S4 | `ch05/01_main-chapter-code/ch05.ipynb`, `ch05/01_main-chapter-code/gpt_train.py`, `ch05/02_alternative_weight_loading/*.ipynb` |
| Ch6 | C6-S1..C6-S4 | `ch06/01_main-chapter-code/ch06.ipynb`, `ch06/01_main-chapter-code/gpt_class_finetune.py` |
| Ch7 | C7-S1..C7-S4 | `ch07/01_main-chapter-code/ch07.ipynb`, `ch07/01_main-chapter-code/gpt_instruction_finetuning.py`, `ch07/04_preference-tuning-with-dpo/dpo-from-scratch.ipynb` |

## 7. Best Plan Recommendation

Use a two-track structure for reliability and slide-limit compliance:

1. Core 30-slide decks (12 modules): concepts + practical anchors + 2 tight code slides + 2 hands-on appendix slides + final takeaway.
2. Centralized 28-slide Code Appendix Pack: deep code walkthroughs chapter-by-chapter.

Why this is best:
- Keeps each live deck within the 30-slide hard limit.
- Maintains strong slide-to-Colab traceability through Hands-on Anchors.
- Avoids repeating heavy code in every module while preserving full hands-on coverage.

## 8. Next Implementation Actions

1. Patch existing Ch1 and Ch2 decks to this blueprint (remove MCQ slots, add Appendix A/B/C slots, add Slide 30 takeaway).
2. Generate module manifests with slide-level anchors for Modules 3-12.
3. Generate Code Appendix Pack (28 slides) with per-slide asset mapping and prerequisites.
4. Add a path-check script to validate all manifest asset links before release.

