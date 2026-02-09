# LLM Beginners Course: Next 2 Hours Deck (Module 11 - Ch7 Core: Instruction Tuning + Evaluation Pipeline)

## Design System (Apply to all slides)

- Use 8K ultra-high-resolution visuals.
- Use premium light palette: Pearl White `#FAFAFA` to Soft Grey `#F0F4F8`, Charcoal text `#2D3748`, Navy accents `#1A365D`, Gold accents `#C9A227`.
- Use descriptive sections only; do not use panel numbers.
- Keep wording beginner-friendly while technically precise.
- Add one wisdom box to every slide.

## Slide 1: Title - Instruction Tuning End-to-End

Prompt:
Create an 8K premium title slide showing a pretrained GPT model tuned on instruction-response pairs and then evaluated via rubric scoring.

Central Text:
- Title: MODULE 11 - INSTRUCTION TUNING + EVALUATION
- Subtitle: From Base Model to Task-Following Assistant Behavior
- Tagline: Data format, supervised tuning, response quality checks.

Wisdom:
"Instruction quality comes from data quality plus evaluation rigor."

## Slide 2: Agenda - Two-Hour Flow

Prompt:
Create an 8K agenda slide with two-column layout.

Hour 1:
1. Instruction dataset structure and formatting
2. Collation/masking for supervised fine-tuning
3. Training loop and loss tracking
4. Model save and response generation

Hour 2:
1. Evaluation workflow with rubric scoring
2. Deterministic response/score settings
3. Error analysis and quality loops
4. Transition to preference tuning (DPO)

Wisdom:
"Good assistants are engineered, not wished into existence."

## Slide 3: Ch7 Core Scope and Assets

Prompt:
Create an 8K concept slide mapping core Ch7 assets and evaluation utilities.

Extended Annotations (12):
1. Core notebook: `ch07/01_main-chapter-code/ch07.ipynb`.
2. Standalone SFT script: `gpt_instruction_finetuning.py`.
3. Standalone evaluator: `ollama_evaluate.py`.
4. Dataset files: `instruction-data.json` and response-augmented output file.
5. Load finetuned model notebook available for inference checks.
6. Exercise notebooks and experiments reinforce core flow.
7. Evaluation bonus folder adds model-based judging utilities.
8. Objective: improve instruction-following behavior.
9. Task remains causal LM training with formatted supervision text.
10. Common mistake: treating this as classification pipeline.
11. Output quality is assessed with both loss and response scoring.
12. Related topic: DPO bridge in Slide 29.

Beginner's Corner:
- What this means: We train GPT to answer instructions in a structured way.
- Why it matters: This is the core of assistant-style behavior.
- Common mistake: skipping evaluation and trusting training loss only.

Wisdom:
"Behavior tuning needs explicit data and explicit checks."

## Slide 4: Instruction Data Format

Prompt:
Create an 8K concept slide showing each record fields: instruction, input, output.

Extended Annotations (12):
1. Instruction dataset entries are structured triples.
2. Input field may be empty depending on task.
3. Output field is target response text.
4. Formatting template wraps entries into consistent prompt style.
5. Consistent template reduces training ambiguity.
6. Data split: train/val/test partitions.
7. Code anchors: `format_input` and dataset split logic.
8. Common bug: inconsistent prompt sections across samples.
9. Practical check: print formatted sample entries.
10. Dataset size affects convergence and generalization.
11. Quality of outputs drives model behavior ceiling.
12. Related topic: collate masking in Slide 5.

Beginner's Corner:
- What this means: Every training example says “given this instruction/input, produce this response.”
- Why it matters: Model learns response style from this exact structure.
- Common mistake: changing prompt template mid-training.

Wisdom:
"Template consistency is a hidden superpower in SFT."

## Slide 5: Custom Collate and Target Masking

Prompt:
Create an 8K concept slide showing batch padding, shifted targets, and ignore-index masking on extra padding tokens.

Extended Annotations (12):
1. Sequences are variable-length and require padding.
2. Inputs use all tokens except final position.
3. Targets are right-shifted by one token.
4. Extra padding targets are masked to ignore index.
5. Prevents loss contamination from pad-only positions.
6. Optional max length truncates long samples.
7. Code anchor: `custom_collate_fn`.
8. Common bug: forgetting target mask beyond first pad token.
9. Practical check: inspect one collated batch and mask positions.
10. Device transfer is handled in collate path.
11. Correct masking materially affects stability.
12. Related topic: loss computation in Slide 6.

Beginner's Corner:
- What this means: We teach only meaningful next-token targets, not padding noise.
- Why it matters: Cleaner gradient signal and better learning.
- Common mistake: computing loss on padded tail tokens.

Wisdom:
"Masking is small code with large training impact."

## Slide 6: SFT Objective and Loss Tracking

Prompt:
Create an 8K concept slide linking token-level LM loss to instruction-following quality trends.

Extended Annotations (12):
1. SFT still optimizes autoregressive next-token loss.
2. Formatted instruction-response text defines supervision signal.
3. Train and validation losses are tracked periodically.
4. Loss trend informs optimization progress.
5. Loss alone does not guarantee response usefulness.
6. Need downstream response evaluation for quality.
7. Code anchor: `train_model_simple` usage in script.
8. Common bug: overfitting small instruction sets.
9. Practical check: evaluate on held-out instructions.
10. Eval cadence should be consistent across runs.
11. Response generation step validates practical behavior.
12. Related topic: evaluator pipeline in Slide 20.

Beginner's Corner:
- What this means: We train GPT to better continue in instruction-answer format.
- Why it matters: This is the foundation before preference tuning.
- Common mistake: assuming lower loss always means better helpfulness.

Wisdom:
"SFT loss is necessary evidence, not complete evidence."

## Slide 7: Animation - Instruction SFT Dataflow (Hour 1)

Prompt:
Create an 8K storyboard slide: JSON entry -> formatted prompt -> token batch -> masked targets -> model update.

Animation Asset:
- `/Users/sanjayb/Documents/New project/course_outputs/llm-beginners-foundations/hour21-ch7-instruction-sft-flow-animation.py`

Wisdom:
"Data formatting choices directly shape assistant behavior."

## Slide 8: Loading Pretrained Backbone for SFT

Prompt:
Create an 8K concept slide showing GPT-2 weight loading into configurable model sizes before instruction tuning.

Extended Annotations (12):
1. Start from pretrained GPT checkpoint.
2. Config selects model size (small/medium/large/xl variants).
3. Weights are loaded before SFT training starts.
4. Model moved to available device.
5. Reproducibility uses fixed seeds.
6. Baseline initial loss can be measured pre-SFT.
7. Code anchors: `download_and_load_gpt2` and `load_weights_into_gpt`.
8. Common bug: context length mismatch with collate max length.
9. Practical check: run one forward pass pre-training.
10. Medium model can balance quality vs runtime in chapter flow.
11. Keep tokenizer consistent with model family.
12. Related topic: training loop in Slide 10.

Beginner's Corner:
- What this means: We adapt a strong base model instead of starting from scratch.
- Why it matters: Faster learning with less data.
- Common mistake: mixing wrong config with loaded weights.

Wisdom:
"Strong initialization shrinks the path to useful behavior."

## Slide 9: Dataloader Setup for Instruction SFT

Prompt:
Create an 8K concept slide showing train/val dataloaders with custom collate and fixed batch settings.

Extended Annotations (12):
1. InstructionDataset pre-tokenizes formatted samples.
2. Train loader shuffles and may drop last batch.
3. Validation loader is deterministic and no shuffle.
4. Batch size must respect memory limits.
5. Collate handles padding/truncation/mask rules.
6. Device-aware collate reduces copy complexity.
7. Code anchors: InstructionDataset + DataLoader setup.
8. Common bug: inconsistent collate function between loaders.
9. Practical check: inspect train/val batch shapes and mask counts.
10. Input length truncation controls compute.
11. Data split ratios affect validation confidence.
12. Related topic: response generation loop in Slide 11.

Beginner's Corner:
- What this means: Same model, new data pipeline tailored to instruction examples.
- Why it matters: Dataloader correctness is prerequisite for stable SFT.
- Common mistake: using generic collate without target masking.

Wisdom:
"SFT quality begins in the dataloader."

## Slide 10: Training Loop and Artifact Outputs

Prompt:
Create an 8K concept slide showing SFT epochs, periodic eval, loss plot save, and model checkpoint save.

Extended Annotations (12):
1. Optimizer updates all model parameters in this chapter script.
2. Eval frequency controls monitoring granularity.
3. Loss plot artifact supports retrospective analysis.
4. Save model checkpoint after training.
5. Log training runtime and key milestones.
6. Keep experiment metadata with outputs.
7. Code anchors: optimizer setup, train call, save lines.
8. Common bug: forgetting to save model and losing best run.
9. Practical check: confirm checkpoint file exists and reloads.
10. Reusable artifacts support downstream evaluation.
11. Script mode gives reproducible chapter summary path.
12. Related topic: load-finetuned-model in Slide 18.

Beginner's Corner:
- What this means: Training should produce auditable files, not just console logs.
- Why it matters: You need repeatability and handoff-ready artifacts.
- Common mistake: running long jobs without artifact plan.

Wisdom:
"No artifacts, no reproducible progress."

## Slide 11: Generating Responses on Held-Out Test Set

Prompt:
Create an 8K concept slide showing batched/iterative generation across test entries and saving `model_response` fields.

Extended Annotations (12):
1. Test set prompts are formatted with same template.
2. Model generates responses per test entry.
3. Post-processing removes response header marker.
4. Responses are stored in JSON for scoring.
5. Deterministic generation settings improve comparison.
6. Generation context size must match model config.
7. Code anchors: generation loop and JSON save section.
8. Common bug: slicing generated text incorrectly from prompt prefix.
9. Practical check: inspect random response samples manually.
10. Response file enables offline evaluation workflows.
11. This step bridges training and evaluation stages.
12. Related topic: scoring in Slide 20.

Beginner's Corner:
- What this means: After training, we ask model to answer unseen instructions.
- Why it matters: This is where usefulness is visible.
- Common mistake: evaluating on training samples only.

Wisdom:
"Generalization is measured on unseen prompts."

## Slide 12: Script vs Notebook for Ch7 Core

Prompt:
Create an 8K concept slide comparing exploratory notebook flow and reproducible script flow for SFT + evaluation.

Extended Annotations (12):
1. Notebook supports concept learning and inspection.
2. Script supports consistent reruns and automation.
3. Both should align on preprocessing template.
4. Script test mode accelerates smoke checks.
5. Keep versioned dependencies for consistency.
6. Use same random seed policy where possible.
7. Anchors: `ch07.ipynb`, `gpt_instruction_finetuning.py`, `tests.py`.
8. Common bug: drift between notebook and script behavior.
9. Practical strategy: validate logic in notebook, operationalize script.
10. Artifact naming should include model/run metadata.
11. Prepare for later DPO and LoRA modules.
12. Related topic: troubleshooting in Slide 26.

Beginner's Corner:
- What this means: Learn in notebook, productionize in script.
- Why it matters: Keeps experimentation and reliability balanced.
- Common mistake: relying only on notebook state.

Wisdom:
"Reproducibility is where education becomes engineering."

## Slide 13: Practical Walkthrough - Run Ch7 Notebook Core

Prompt:
Create an 8K practical slide with ordered checklist for core notebook cells and key expected outputs.

Hands-on Anchor:
`[Hands-on Anchor: M11-LAB-01 | Asset: ch07/01_main-chapter-code/ch07.ipynb | Objective: execute core instruction SFT workflow and verify loss/response artifacts | Pre-req: M10-LAB-APP-B]`

Wisdom:
"Run order discipline keeps training and evaluation coherent."

## Slide 14: Hands-on Appendix A - Hour 1 SFT Checklist

Prompt:
Create an 8K appendix slide listing checks for format template, collate masking, and first eval losses.

Hands-on Anchor:
`[Hands-on Anchor: M11-LAB-APP-A | Asset: ch07/01_main-chapter-code/ch07.ipynb; ch07/01_main-chapter-code/gpt_instruction_finetuning.py | Objective: validate hour-1 SFT data+training setup before full response generation | Pre-req: M11-LAB-01]`

Wisdom:
"Catch formatting and masking issues before long runs."

## Slide 15: Code Bridge A - `InstructionDataset` + `custom_collate_fn`

Prompt:
Create an 8K code demonstration slide.

LEFT (60%) - CODE (tight excerpt):
- `format_input` usage.
- response concatenation.
- collate padding + target masking.

RIGHT (40%) - FLOW:
- json entry -> formatted text -> token ids -> masked targets.

Hands-on Anchor:
`[Hands-on Anchor: M11-CODE-01 | Asset: ch07/01_main-chapter-code/gpt_instruction_finetuning.py | Objective: line-by-line explain SFT input-target construction and masking | Pre-req: M11-LAB-APP-A]`

Wisdom:
"If target construction is wrong, SFT learns the wrong task."

## Slide 16: Transition - From Training to Evaluating Responses

Prompt:
Create an 8K concept slide showing handoff from model checkpoint + response JSON into evaluator script.

Extended Annotations (12):
1. Training output includes checkpoint and response file.
2. Evaluator consumes response JSON with references.
3. Deterministic evaluator settings improve consistency.
4. Scoring is a proxy, not absolute truth.
5. Pair numeric scores with manual inspections.
6. Keep evaluation prompt template stable.
7. Anchors: `ollama_evaluate.py` and evaluation notebooks.
8. Common bug: missing `model_response` key in JSON.
9. Practical strategy: run small subset first.
10. Track average and distribution of scores.
11. Evaluation loop enables iterative improvement.
12. Related topic: model-based scoring in Slide 20.

Beginner's Corner:
- What this means: We systematically score generated answers after training.
- Why it matters: Helps compare runs objectively.
- Common mistake: relying only on a few manually chosen examples.

Wisdom:
"Evaluation is part of training, not an optional afterthought."

## Slide 17: Practical - Run `gpt_instruction_finetuning.py`

Prompt:
Create an 8K practical slide with expected outputs: loss plot, response JSON, and checkpoint file.

Hands-on Anchor:
`[Hands-on Anchor: M11-LAB-02 | Asset: ch07/01_main-chapter-code/gpt_instruction_finetuning.py | Objective: execute standalone instruction SFT and produce evaluation-ready artifacts | Pre-req: M11-LAB-01]`

Wisdom:
"Standalone script runs are the baseline for trustworthy iteration."

## Slide 18: Practical - Load Finetuned Instruction Model

Prompt:
Create an 8K practical slide for loading saved SFT model and validating example responses.

Hands-on Anchor:
`[Hands-on Anchor: M11-LAB-03 | Asset: ch07/01_main-chapter-code/load-finetuned-model.ipynb | Objective: reload SFT checkpoint and run post-training inference sanity checks | Pre-req: M11-LAB-02]`

Wisdom:
"A finetuned model is only valuable when reloadable."

## Slide 19: Animation - Evaluation Pipeline Loop (Hour 2)

Prompt:
Create an 8K storyboard slide: response file -> scoring model -> numeric scores -> aggregate stats -> revision loop.

Animation Asset:
- `/Users/sanjayb/Documents/New project/course_outputs/llm-beginners-foundations/hour22-ch7-evaluation-pipeline-animation.py`

Wisdom:
"Quality improves when feedback loops are explicit."

## Slide 20: Model-Based Scoring with Ollama/GPT-4 Style Rubrics

Prompt:
Create an 8K concept slide showing rubric prompt construction and integer score extraction.

Extended Annotations (12):
1. Evaluator prompts compare model response vs reference output.
2. Score scale example: 0 to 100 integer.
3. Deterministic settings reduce score noise.
4. Local evaluator requires runtime availability checks.
5. Parse and validate returned numeric scores.
6. Handle malformed responses gracefully.
7. Code anchor: `query_model` and `generate_model_scores`.
8. Common bug: non-integer score parse failures.
9. Practical check: inspect failed parse examples.
10. Average score gives coarse summary signal.
11. Pair with sample-level qualitative audit.
12. Related topic: bonus eval notebooks in Slide 22.

Beginner's Corner:
- What this means: Another model can grade your model with a consistent rubric.
- Why it matters: Fast feedback at scale.
- Common mistake: treating auto-score as perfect ground truth.

Wisdom:
"Automatic judges are useful, but never infallible."

## Slide 21: Practical - Run `ollama_evaluate.py`

Prompt:
Create an 8K practical slide with command checklist, expected summary stats, and preflight checks for local model runtime.

Hands-on Anchor:
`[Hands-on Anchor: M11-LAB-04 | Asset: ch07/01_main-chapter-code/ollama_evaluate.py | Objective: score generated responses and compute aggregate quality metrics | Pre-req: M11-LAB-02]`

Wisdom:
"Preflight checks prevent wasted evaluation runs."

## Slide 22: Practical - Extended Evaluation Notebooks

Prompt:
Create an 8K practical slide connecting core evaluator to Ch7 model-evaluation notebooks and correlation analysis.

Hands-on Anchor:
`[Hands-on Anchor: M11-LAB-05 | Asset: ch07/03_model-evaluation/llm-instruction-eval-ollama.ipynb; ch07/03_model-evaluation/llm-instruction-eval-openai.ipynb; ch07/03_model-evaluation/scores/correlation-analysis.ipynb | Objective: compare evaluator backends and analyze scoring consistency | Pre-req: M11-LAB-04]`

Wisdom:
"Consistency checks increase trust in scoring pipelines."

## Slide 23: Practical - Dataset Utility Enhancements

Prompt:
Create an 8K practical slide for near-duplicate detection and small dataset cleanup utilities.

Hands-on Anchor:
`[Hands-on Anchor: M11-LAB-06 | Asset: ch07/02_dataset-utilities/find-near-duplicates.py; ch07/02_dataset-utilities/create-passive-voice-entries.ipynb | Objective: improve instruction dataset quality before retraining | Pre-req: M11-LAB-01]`

Wisdom:
"Cleaner datasets often beat more epochs."

## Slide 24: Decision Matrix - When to Stop SFT and Move On

Prompt:
Create an 8K concept slide with matrix: loss trend, response quality, score plateau, and next action (more data, better eval, DPO).

Extended Annotations (12):
1. Stop when gains plateau across multiple signals.
2. If loss improves but responses lag, inspect data quality.
3. If scores are noisy, strengthen evaluator robustness.
4. If behavior is misaligned, preference tuning may help.
5. Keep compute budget and ROI explicit.
6. Compare against baseline checkpoints.
7. Preserve best checkpoints before next stage.
8. Common bug: overtraining without quality gains.
9. Practical strategy: scheduled evaluation gates.
10. Use targeted error slices for data improvement.
11. Prepare artifacts for DPO/LoRA stage.
12. Related topic: transition in Slide 29.

Beginner's Corner:
- What this means: Use evidence to decide next step, not guesswork.
- Why it matters: Saves time and compute.
- Common mistake: continuing SFT when preference tuning is needed.

Wisdom:
"Progress decisions should be metric-backed and goal-backed."

## Slide 25: Practical - Common Ch7 Failure Modes

Prompt:
Create an 8K practical troubleshooting slide for malformed formatting, mask bugs, repetitive outputs, and evaluation parser errors.

Hands-on Anchor:
`[Hands-on Anchor: M11-LAB-07 | Asset: ch07/01_main-chapter-code/gpt_instruction_finetuning.py; ch07/01_main-chapter-code/ollama_evaluate.py | Objective: diagnose and fix common instruction-tuning and scoring failures | Pre-req: M11-LAB-05]`

Wisdom:
"Most instruction-tuning issues are detectable with focused diagnostics."

## Slide 26: Troubleshooting - Reproducibility and Smoke Tests

Prompt:
Create an 8K troubleshooting slide mapping script test mode and smoke execution expectations.

Hands-on Anchor:
`[Hands-on Anchor: M11-LAB-08 | Asset: ch07/01_main-chapter-code/tests.py; ch07/01_main-chapter-code/gpt_instruction_finetuning.py | Objective: enforce reproducible SFT smoke runs and baseline checks | Pre-req: M11-LAB-02]`

Wisdom:
"Smoke tests preserve trust while you iterate quickly."

## Slide 27: Code Bridge B - SFT + Evaluation Integration

Prompt:
Create an 8K code demonstration slide.

LEFT (60%) - CODE (tight excerpt):
- training call and artifact save.
- response generation loop.
- evaluation score loop.

RIGHT (40%) - FLOW:
- model checkpoint -> response file -> score report.

Hands-on Anchor:
`[Hands-on Anchor: M11-CODE-02 | Asset: ch07/01_main-chapter-code/gpt_instruction_finetuning.py; ch07/01_main-chapter-code/ollama_evaluate.py | Objective: explain end-to-end SFT-to-evaluation integration pattern | Pre-req: M11-LAB-08]`

Wisdom:
"Integrated pipelines shorten the feedback cycle dramatically."

## Slide 28: Hands-on Appendix B - End-to-End Ch7 Core Runbook

Prompt:
Create an 8K appendix slide with exact run order: dataset prep -> SFT script -> reload check -> evaluator -> extended eval.

Hands-on Anchor:
`[Hands-on Anchor: M11-LAB-APP-B | Asset: ch07/01_main-chapter-code/ch07.ipynb; ch07/01_main-chapter-code/gpt_instruction_finetuning.py; ch07/01_main-chapter-code/load-finetuned-model.ipynb; ch07/01_main-chapter-code/ollama_evaluate.py; ch07/03_model-evaluation/llm-instruction-eval-ollama.ipynb | Objective: execute full Ch7 core instruction-tuning and evaluation workflow | Pre-req: M11-LAB-01..08]`

Wisdom:
"Runbooks convert complex workflows into repeatable operations."

## Slide 29: Hands-on Appendix C - Transition to Module 12 (DPO + LoRA + Capstone)

Prompt:
Create an 8K appendix slide listing artifacts required for preference tuning and PEFT next stage.

Hands-on Anchor:
`[Hands-on Anchor: M11-LAB-APP-C | Asset: ch07/04_preference-tuning-with-dpo/dpo-from-scratch.ipynb; ch07/04_preference-tuning-with-dpo/create-preference-data-ollama.ipynb; appendix-E/01_main-chapter-code/appendix-E.ipynb | Objective: prepare SFT outputs and evaluation traces for DPO/LoRA capstone module | Pre-req: M11-LAB-APP-B]`

Wisdom:
"Strong SFT artifacts are the launchpad for preference tuning."

## Slide 30: Session Takeaway - What Learners Can Do Now

Prompt:
Create an 8K recap slide with six outcomes and next-step bridge.

Key Takeaways:
1. Build instruction-formatted datasets for supervised tuning.
2. Implement masked collation correctly for SFT objective.
3. Run instruction finetuning with reproducible artifacts.
4. Generate and store held-out responses systematically.
5. Evaluate responses with model-based scoring pipelines.
6. Decide when to continue SFT vs move to preference tuning.

What You Can Now Do:
- Execute a complete Ch7 core instruction-tuning cycle.
- Validate behavior quality with structured evaluation.
- Improve dataset/evaluation loops based on evidence.
- Transition to Module 12 (DPO + LoRA + capstone) with prepared artifacts.

Next:
Module 12 - DPO + LoRA + capstone integration.

Wisdom:
"Instruction tuning becomes powerful when paired with disciplined evaluation."
