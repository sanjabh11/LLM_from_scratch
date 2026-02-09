1) Repository Structure: Top 20 Points

Root is curriculum-first: ch01 to ch07 track the end-to-end LLM lifecycle.
ch01 is pure conceptual onboarding (no code artifacts).
ch02 introduces text data workflow with main code + 4 bonus tokenization/data folders.
ch03 centers on attention implementation with efficient MHA and buffer-focused bonuses.
ch04 is architecture-heavy: GPT build + KV cache + GQA/MLA/SWA/MoE/DeltaNet options.
ch05 is the densest chapter: pretraining core + 13 bonus subtracks.
ch06 focuses on classification finetuning and comparative experiments.
ch07 focuses on instruction finetuning, evaluation, dataset generation, and DPO.
Each core chapter (ch02-ch07) has 01_main-chapter-code plus optional bonus folders.
Main chapter folders consistently include notebooks, reusable scripts, and chapter tests.
Cross-chapter code reuse is explicit via previous_chapters.py.
Appendices are pedagogically separate: A (PyTorch), B (references), C (solutions), D (training loop upgrades), E (LoRA).
setup/ is extensive (local setup, Docker devcontainer, cloud usage, Colab workflow).
Repo is package-ized under pkg/llms_from_scratch.
Package exposes chapter APIs (ch02…ch07, appendices, KV-cache, Llama/Qwen helpers).
Package contains unit tests per chapter module.
CI is mature: Linux/macOS/Windows workflows, uv/pip/pixi variants, lint/link checks.
Dependency strategy supports both standard and bonus tracks (requirements, pyproject, pixi).
There is a companion relation to reasoning-from-scratch (sequel path).
Content is code-heavy overall (repo-level practical artifacts significantly exceed theory docs).
2) Theory vs Practical Ratio (for deck design)
From repository artifact analysis:

Core chapters (ch01-ch07): 27.5% theory / 72.5% practical
Core + setup + appendices A/D/E: 30.4% theory / 69.6% practical
Recommended for absolute beginners:

Slide-deck delivery ratio: 65% theory / 35% practical walkthrough
Full course ratio including separate Colab labs: 45% theory / 55% practical
This keeps slides understandable for beginners while preserving the repo’s hands-on intent.

3) 30-Slide / 2-Hour Deck Standard
Per hour (15 slides):

1 MCQ slide (mandatory)
1 detailed code-explanation slide (mandatory; full coding done in Colab)
13 concept + worked-example + troubleshooting slides
Per 2-hour deck (30 slides):

2 MCQ slides
2 detailed code-explanation slides
26 topic/deep-dive slides
4) Required Course Hours
Recommended beginner-complete track:

12 decks × 2 hours = 24 hours of slide content
360 slides total
Suggested deck mapping (24h):

Foundations + setup + minimal PyTorch
LLM fundamentals (Ch1)
Text/tokenization/data pipeline (Ch2)
Attention mechanics (Ch3)
GPT architecture from scratch (Ch4 core)
Inference/performance/attention alternatives (Ch4 bonus)
Pretraining pipeline (Ch5 core)
Training improvements (schedulers, speed, tuning)
Architecture variants + weight loading (Llama/Qwen/Gemma/Olmo)
Classification finetuning (Ch6)
Instruction tuning + evaluation pipeline (Ch7 core)
DPO + LoRA + capstone integration
Optional advanced extension:

+6 hours (3 additional decks) for deeper bonus internals and experiments.
Full comprehensive path: 30 hours.