# alignment_manifest_v1

## Scope
Single consolidated lab manifest for all 12 core modules plus Add-On A/B/C.
Format: module -> slide range -> notebook/script -> objective -> pre-req.

| Module | Slide Range | Notebook/Script | Objective | Pre-req |
| --- | --- | --- | --- | --- |
| Module 1: Foundations + setup + minimal PyTorch | 1-10 | `appendix-A/01_main-chapter-code/code-part1.ipynb` | establish tensor/autograd intuition for absolute beginners | none |
| Module 1: Foundations + setup + minimal PyTorch | 11-20 | `appendix-A/01_main-chapter-code/code-part2.ipynb` | understand minimal train loop (`zero_grad/backward/step`) | Module 1 (1-10) |
| Module 1: Foundations + setup + minimal PyTorch | 21-30 | `appendix-A/01_main-chapter-code/DDP-script.py` | introduce scale-readiness bridge from single-process training | Module 1 (11-20) |
| Module 2: LLM fundamentals (Ch1) | 1-10 | `ch01/README.md` | form correct mental model: next-token prediction, limits, misconceptions | Module 1 |
| Module 2: LLM fundamentals (Ch1) | 11-20 | `appendix-A/01_main-chapter-code/code-part2.ipynb` | bridge concept-to-code without full Ch1 notebook dependency | Module 2 (1-10) |
| Module 2: LLM fundamentals (Ch1) | 21-30 | `appendix-A/01_main-chapter-code/code-part1.ipynb` | finalize beginner-safe intuition for vectors/probabilities | Module 2 (11-20) |
| Module 3: Text/tokenization/data pipeline (Ch2) | 1-10 | `ch02/01_main-chapter-code/ch02.ipynb` | text -> tokens -> IDs -> embeddings pipeline clarity | Module 2 |
| Module 3: Text/tokenization/data pipeline (Ch2) | 11-20 | `ch02/01_main-chapter-code/dataloader.ipynb` | sliding-window input/target pair generation | Module 3 (1-10) |
| Module 3: Text/tokenization/data pipeline (Ch2) | 21-30 | `ch02/05_bpe-from-scratch/bpe-from-scratch-simple.ipynb` | explain BPE internals and edge cases | Module 3 (11-20) |
| Module 4: Attention mechanics (Ch3) | 1-10 | `ch03/01_main-chapter-code/ch03.ipynb` | implement attention score flow and causal masking | Module 3 |
| Module 4: Attention mechanics (Ch3) | 11-20 | `ch03/01_main-chapter-code/multihead-attention.ipynb` | understand multi-head split/merge behavior | Module 4 (1-10) |
| Module 4: Attention mechanics (Ch3) | 21-30 | `ch03/02_bonus_efficient-multihead-attention/mha-implementations.ipynb` | compare implementation tradeoffs and efficiency | Module 4 (11-20) |
| Module 5: GPT architecture from scratch (Ch4 core) | 1-10 | `ch04/01_main-chapter-code/gpt.py` | block anatomy: embeddings, attention, FFN, residuals | Module 4 |
| Module 5: GPT architecture from scratch (Ch4 core) | 11-20 | `ch04/01_main-chapter-code/gpt.py` | full forward-path tracing for decoder-only GPT | Module 5 (1-10) |
| Module 5: GPT architecture from scratch (Ch4 core) | 21-30 | `ch04/01_main-chapter-code/tests.py` | validate correctness through smoke tests | Module 5 (11-20) |
| Module 6: Inference/performance/attention alternatives (Ch4 bonus) | 1-10 | `ch04/02_performance-analysis/*.py` | profile baseline inference bottlenecks | Module 5 |
| Module 6: Inference/performance/attention alternatives (Ch4 bonus) | 11-20 | `ch04/03_kv-cache/*` | understand KV-cache speedups and tradeoffs | Module 6 (1-10) |
| Module 6: Inference/performance/attention alternatives (Ch4 bonus) | 21-30 | `ch04/04_gqa/*`, `ch04/05_mla/*`, `ch04/06_swa/*`, `ch04/07_moe/*`, `ch04/08_deltanet/*` | compare attention alternatives at a systems level | Module 6 (11-20) |
| Module 7: Pretraining pipeline (Ch5 core) | 1-10 | `ch05/01_main-chapter-code/gpt_train.py` | pretraining loss flow and optimizer loop | Module 5 |
| Module 7: Pretraining pipeline (Ch5 core) | 11-20 | `ch05/01_main-chapter-code/gpt_generate.py` | evaluate checkpoints via controlled generation | Module 7 (1-10) |
| Module 7: Pretraining pipeline (Ch5 core) | 21-30 | `ch05/01_main-chapter-code/gpt_download.py` | robust weight bootstrap and artifact handling | Module 7 (11-20) |
| Module 8: Training improvements (schedulers, speed, tuning) | 1-10 | `ch05/04_learning_rate_schedulers/*` | explain LR schedule effects on stability | Module 7 |
| Module 8: Training improvements (schedulers, speed, tuning) | 11-20 | `ch05/10_llm-training-speed/*` | improve throughput and runtime efficiency | Module 8 (1-10) |
| Module 8: Training improvements (schedulers, speed, tuning) | 21-30 | `ch05/05_bonus_hparam_tuning/*` | run disciplined tuning loops and compare outcomes | Module 8 (11-20) |
| Module 9: Architecture variants + weight loading | 1-10 | `ch05/07_gpt_to_llama/*` | bridge GPT baseline to Llama-compatible structure | Module 7 |
| Module 9: Architecture variants + weight loading | 11-20 | `ch05/11_qwen3/*`, `ch05/12_gemma3/*`, `ch05/13_olmo3/*` | evaluate architecture family differences | Module 9 (1-10) |
| Module 9: Architecture variants + weight loading | 21-30 | `ch05/08_memory_efficient_weight_loading/*`, `ch05/14_ch05_with_other_llms/*` | teach safe and efficient weight loading patterns | Module 9 (11-20) |
| Module 10: Classification finetuning (Ch6) | 1-10 | `ch06/01_main-chapter-code/gpt_class_finetune.py` | supervised dataset prep and classifier adaptation | Module 7 |
| Module 10: Classification finetuning (Ch6) | 11-20 | `ch06/01_main-chapter-code/tests.py` | validate fine-tuning behavior with reproducible checks | Module 10 (1-10) |
| Module 10: Classification finetuning (Ch6) | 21-30 | `ch06/03_bonus_imdb-classification/sklearn-baseline.ipynb` | baseline framing across model families | Module 10 (11-20) |
| Module 11: Instruction tuning + evaluation pipeline (Ch7 core) | 1-10 | `ch07/01_main-chapter-code/gpt_instruction_finetuning.py` | instruction-format data path and SFT loop | Module 10 |
| Module 11: Instruction tuning + evaluation pipeline (Ch7 core) | 11-20 | `ch07/03_model-evaluation/*` | evaluate response quality with consistent protocol | Module 11 (1-10) |
| Module 11: Instruction tuning + evaluation pipeline (Ch7 core) | 21-30 | `ch07/01_main-chapter-code/ollama_evaluate.py` | close loop from training to practical evaluation | Module 11 (11-20) |
| Module 12: DPO + LoRA + capstone integration (Ch7 bonus) | 1-10 | `ch07/04_preference-tuning-with-dpo/dpo-from-scratch.ipynb` | preference optimization fundamentals | Module 11 |
| Module 12: DPO + LoRA + capstone integration (Ch7 bonus) | 11-20 | `appendix-E/01_main-chapter-code/appendix-E.ipynb` | parameter-efficient adaptation bridge (LoRA) | Module 12 (1-10) |
| Module 12: DPO + LoRA + capstone integration (Ch7 bonus) | 21-30 | `ch07/04_preference-tuning-with-dpo/*.py` | integrate preference and capstone release workflow | Module 12 (11-20) |
| Add-On A: Productization UI | 1-10 | `ch05/06_user_interface/app_orig.py`, `ch05/06_user_interface/app_own.py` | deploy generation paths in interactive UI | Module 7 |
| Add-On A: Productization UI | 11-20 | `ch06/04_user_interface/app.py` | deploy classification flow for learner demos | Module 10 |
| Add-On A: Productization UI | 21-30 | `ch07/06_user_interface/app.py` | deploy instruction assistant UI and feedback loop | Module 11 |
| Add-On B: Data Engineering | 1-10 | `ch07/05_dataset-generation/llama3-ollama.ipynb`, `ch07/05_dataset-generation/reflection-gpt4.ipynb` | generate/refine synthetic data with quality gates | Module 11 |
| Add-On B: Data Engineering | 11-20 | `ch05/09_extending-tokenizers/extend-tiktoken.ipynb` | tokenizer extension with compatibility controls | Module 3 |
| Add-On B: Data Engineering | 21-30 | `ch06/03_bonus_imdb-classification/download_prepare_dataset.py`, `ch06/03_bonus_imdb-classification/train_gpt.py`, `ch06/03_bonus_imdb-classification/train_bert_hf.py`, `ch06/03_bonus_imdb-classification/train_sklearn_logreg.py` | bootstrap external datasets and fair baseline comparisons | Add-On B (1-20) |
| Add-On C: Reliability + Engineering | 1-10 | `setup/02_installing-python-libraries/python_environment_check.py`, `setup/02_installing-python-libraries/tests.py`, `ch02/05_bpe-from-scratch/tests.py`, `ch03/02_bonus_efficient-multihead-attention/tests/test_mha_implementations.py` | run reproducibility preflight and math-level regression checks | Add-On B |
| Add-On C: Reliability + Engineering | 11-20 | `appendix-A/01_main-chapter-code/DDP-script.py`, `appendix-A/01_main-chapter-code/DDP-script-torchrun.py` | execute and validate distributed launch workflows | Add-On C (1-10) |
| Add-On C: Reliability + Engineering | 21-30 | `ch05/07_gpt_to_llama/tests/test_llama32_nb.py`, `ch05/07_gpt_to_llama/tests/tests_rope_and_parts.py`, `ch05/11_qwen3/tests/test_qwen3_nb.py`, `ch05/11_qwen3/tests/test_qwen3_kvcache_nb.py`, `ch05/12_gemma3/tests/test_gemma3_nb.py`, `ch05/12_gemma3/tests/test_gemma3_kv_nb.py`, `ch05/13_olmo3/tests/test_olmo3_nb.py`, `ch05/13_olmo3/tests/test_olmo3_kvcache_nb.py`, `ch05/13_olmo3/tests/olmo3_layer_debugger.py`, `ch07/02_dataset-utilities/find-near-duplicates.py`, `ch07/02_dataset-utilities/create-passive-voice-entries.ipynb`, `pkg/llms_from_scratch/utils.py` | apply release gates, triage failures, and produce reliability evidence | Add-On C (11-20) |

## Mandatory Anchor Policy
- Every practical/code/appendix slide in active 30-slide decks must include a `Hands-on Anchor` tag.
- Anchor IDs should be stable and chapter-scoped (`CHx-*`, `ADDON-*`, `C*-S*`).
