# Repo Coverage v2 Patch Plan

## Objective

Close the remaining uncovered teaching assets from `/tmp/llms-from-scratch` with the smallest practical set of add-on modules, without bloating the core 24h path.

## Current Coverage Snapshot

- Relevant repo code assets (notebooks + python, teaching roots only): `142`
- Explicitly mapped in current program artifacts: `108`
- Remaining uncovered: `34`

## Design Principle

Patch uncovered assets via **3 targeted add-on tracks** instead of rewriting core modules:
1. Productization track (UI + inference packaging)
2. Data-engineering track (dataset generation + tokenizer extension)
3. Reliability/engineering track (tests, helper scripts, package bridge)

---

## Patch Bundle A: Productization Add-On (2 hours)

### Purpose
Convert model outputs into student-demoable mini products.

### Assets to cover
- `ch05/06_user_interface/app_orig.py`
- `ch05/06_user_interface/app_own.py`
- `ch06/04_user_interface/app.py`
- `ch07/06_user_interface/app.py`

### New artifacts to produce
- `next-2-hours-addon-a-productization-ui-deck-prompts-v1.md`
- `hour25-ui-productization-animation.py`
- `hour26-inference-ui-feedback-loop-animation.py`

### Required Hands-on Anchors
- `ADDON-A-LAB-01` (Ch5 UI baseline)
- `ADDON-A-LAB-02` (Ch6 classification UI)
- `ADDON-A-LAB-03` (Ch7 instruction UI)
- `ADDON-A-LAB-APP-B` (cross-UI runbook)

### Acceptance criteria
- At least one runnable UI flow per task family (gen/classification/instruction).
- Same model artifact can be exercised in UI and script paths.
- 30-slide deck in standard format, no leakage/meta text.

---

## Patch Bundle B: Data Engineering Add-On (2 hours)

### Purpose
Teach learners how to expand/improve training data quality beyond base chapter datasets.

### Assets to cover
- `ch07/05_dataset-generation/llama3-ollama.ipynb`
- `ch07/05_dataset-generation/reflection-gpt4.ipynb`
- `ch05/09_extending-tokenizers/extend-tiktoken.ipynb`
- `ch06/03_bonus_imdb-classification/download_prepare_dataset.py`

### New artifacts to produce
- `next-2-hours-addon-b-data-engineering-deck-prompts-v1.md`
- `hour27-dataset-generation-loop-animation.py`
- `hour28-tokenizer-extension-impact-animation.py`

### Required Hands-on Anchors
- `ADDON-B-LAB-01` (synthetic dataset generation)
- `ADDON-B-LAB-02` (reflection/improvement loop)
- `ADDON-B-LAB-03` (tokenizer extension)
- `ADDON-B-LAB-04` (external dataset bootstrap)

### Acceptance criteria
- Students can produce augmented dataset variant and justify quality delta.
- Tokenizer extension effects are measured on at least one concrete task.
- Deck follows 30-slide no-MCQ core pattern with appendix/runbook slides.

---

## Patch Bundle C: Reliability + Engineering Add-On (2 hours)

### Purpose
Close testing, reproducibility, helper-script, and package-bridge gaps so students can ship robustly.

### Assets to cover
- `setup/02_installing-python-libraries/python_environment_check.py`
- `setup/02_installing-python-libraries/tests.py`
- `ch02/05_bpe-from-scratch/tests.py`
- `ch03/02_bonus_efficient-multihead-attention/tests/test_mha_implementations.py`
- `ch05/07_gpt_to_llama/tests/test_llama32_nb.py`
- `ch05/07_gpt_to_llama/tests/tests_rope_and_parts.py`
- `ch05/11_qwen3/tests/test_qwen3_nb.py`
- `ch05/11_qwen3/tests/test_qwen3_kvcache_nb.py`
- `ch05/12_gemma3/tests/test_gemma3_nb.py`
- `ch05/12_gemma3/tests/test_gemma3_kv_nb.py`
- `ch05/13_olmo3/tests/test_olmo3_nb.py`
- `ch05/13_olmo3/tests/test_olmo3_kvcache_nb.py`
- `ch05/13_olmo3/tests/olmo3_layer_debugger.py`
- `appendix-A/01_main-chapter-code/DDP-script.py`
- `appendix-A/01_main-chapter-code/DDP-script-torchrun.py`
- package bridge references in `pkg/` (read-only mapping, not full deep-dive)

### New artifacts to produce
- `next-2-hours-addon-c-reliability-engineering-deck-prompts-v1.md`
- `hour29-reproducibility-gates-animation.py`
- `hour30-test-to-release-pipeline-animation.py`

### Required Hands-on Anchors
- `ADDON-C-LAB-01` (environment/test readiness)
- `ADDON-C-LAB-02` (unit/smoke tests across variant families)
- `ADDON-C-LAB-03` (DDP script launch and validation)
- `ADDON-C-LAB-APP-B` (release gate checklist)

### Acceptance criteria
- Students can execute a minimal reproducibility gate before claiming model improvements.
- Tests and runbooks are integrated into training/evaluation lifecycle.
- Deck includes explicit failure triage and release checklist.

---

## Consolidation Deliverables (after A/B/C)

1. `repo-coverage-v2-alignment-matrix.md`
- Every uncovered asset mapped to one add-on slide/lab anchor.

2. `repo-coverage-v2-status.md`
- Before/after coverage counts and residual risk notes.

3. `final-student-capstone-checklist-v2.md`
- One-page operational checklist for students.

---

## Execution Order

1. Run Add-On A (Productization) first.
2. Run Add-On B (Data Engineering) second.
3. Run Add-On C (Reliability) third.
4. Produce consolidation deliverables.

Reasoning:
- Students get motivation and visible outcomes early (A).
- Then improve data and model quality inputs (B).
- Then harden delivery and reproducibility (C).

---

## Time/Slide Budget Impact

- Add-On A: 2h, 30 slides
- Add-On B: 2h, 30 slides
- Add-On C: 2h, 30 slides
- Total patch extension: `+6 hours`, `+90 slides`

No change to core 24h path or previously produced module decks.

---

## Definition of Done (Repo Coverage v2)

- All currently missing `34` assets are explicitly mapped.
- Each add-on has:
  - 30-slide deck
  - 2 validated ~30s animations
  - mandatory Hands-on Anchors on practical/code slides
- Leakage-safe scan passes on all new deck files.
- Coverage matrix confirms zero unmapped teaching assets within selected roots.
