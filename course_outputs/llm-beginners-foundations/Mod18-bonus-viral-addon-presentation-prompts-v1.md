# Bonus Add-On Presentation (Viral Student Edition)
# Title: Build, Evaluate, and Ship a Tiny Useful LLM App in One Session

## Purpose

Use this as a high-engagement add-on after Module 12 to convert theory into a shareable student artifact.

## Why this add-on

This add-on explicitly uses repo areas that are not fully emphasized in the core 24h path:
- UI apps (`ch05/06_user_interface`, `ch06/04_user_interface`, `ch07/06_user_interface`)
- dataset generation/utilities (`ch07/05_dataset-generation`, `ch07/02_dataset-utilities`)
- tokenizer extension (`ch05/09_extending-tokenizers`)
- extra setup/test reliability assets (`setup/*`, Appendix D/E helpers)

## 15-slide Add-On Deck Prompt Map

### Slide 1: Title
Prompt: Create an 8K premium title slide: "From Model to Product: Your First Mini LLM App".

### Slide 2: What students build
Prompt: Show the full loop: dataset -> finetune -> eval -> simple UI demo.

### Slide 3: Quick architecture
Prompt: Visual flow of SFT/DPO output model connected to a local app endpoint.

### Slide 4: Data cleanup accelerator
Prompt: Show near-duplicate detection from `ch07/02_dataset-utilities/find-near-duplicates.py`.

### Slide 5: Synthetic data booster
Prompt: Show controlled dataset generation path from `ch07/05_dataset-generation/llama3-ollama.ipynb`.

### Slide 6: Quality loop
Prompt: Show evaluator pass with `ch07/01_main-chapter-code/ollama_evaluate.py`.

### Slide 7: Mini UI layer
Prompt: Show app path options from `ch07/06_user_interface/app.py`.

### Slide 8: Student challenge
Prompt: Add “improve score by 10 points” challenge with fixed eval rubric.

### Slide 9: Tokenizer wow-factor
Prompt: Show domain token extension idea from `ch05/09_extending-tokenizers/extend-tiktoken.ipynb`.

### Slide 10: Stability guardrails
Prompt: Show training controls from `appendix-D/01_main-chapter-code/appendix-D.ipynb`.

### Slide 11: Efficient adapter option
Prompt: Show LoRA path from `appendix-E/01_main-chapter-code/appendix-E.ipynb`.

### Slide 12: Demo script
Prompt: Show before/after response comparison panel (baseline vs aligned model).

### Slide 13: Shareability rubric
Prompt: Define what makes the project “viral”: clarity, utility, reproducibility, short demo video.

### Slide 14: Submission pack
Prompt: Required deliverables: model artifact, eval report, 2-minute demo, README-lite.

### Slide 15: Takeaway
Prompt: "You now can ship a tiny but real LLM product loop."

## Mandatory Hands-on Anchors

`[Hands-on Anchor: ADDON-LAB-01 | Asset: ch07/02_dataset-utilities/find-near-duplicates.py | Objective: clean instruction data before retraining | Pre-req: M11-LAB-APP-B]`

`[Hands-on Anchor: ADDON-LAB-02 | Asset: ch07/05_dataset-generation/llama3-ollama.ipynb | Objective: generate synthetic instruction data extension | Pre-req: ADDON-LAB-01]`

`[Hands-on Anchor: ADDON-LAB-03 | Asset: ch07/01_main-chapter-code/ollama_evaluate.py | Objective: score baseline and improved runs with same rubric | Pre-req: ADDON-LAB-02]`

`[Hands-on Anchor: ADDON-LAB-04 | Asset: ch07/06_user_interface/app.py | Objective: wire a minimal interactive front-end for model outputs | Pre-req: ADDON-LAB-03]`

`[Hands-on Anchor: ADDON-LAB-05 | Asset: appendix-E/01_main-chapter-code/appendix-E.ipynb | Objective: run efficient adapter fine-tune variant for rapid iteration | Pre-req: ADDON-LAB-03]`
