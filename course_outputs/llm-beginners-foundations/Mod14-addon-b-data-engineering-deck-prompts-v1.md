# Add-On B (Patch Bundle B): Data Engineering Deck
# Title: Synthetic Data, Tokenizer Extension, and Dataset Quality Loops

## Design System (Apply to all slides)

- Use 8K ultra-high-resolution visuals.
- Use premium light palette: Pearl White `#FAFAFA` to Soft Grey `#F0F4F8`, Charcoal text `#2D3748`, Navy accents `#1A365D`, Gold accents `#C9A227`.
- Use descriptive sections only; do not use panel numbers.
- Keep wording beginner-friendly while technically precise.
- Add one wisdom box to every slide.

## Slide 1: Title - Data Engineering for Better LLM Outcomes

Prompt:
Create an 8K premium title slide showing a loop: raw data -> synthetic generation -> refinement -> tokenizer update -> improved training results.

Text:
- Title: ADD-ON B - DATA ENGINEERING
- Subtitle: Generate, Refine, and Encode Better Training Data
- Tagline: Better data pipelines, better model behavior.

Wisdom:
"Model quality is often a data engineering problem first."

## Slide 2: Agenda

Prompt:
Create an 8K agenda slide with two-hour flow:
1. synthetic instruction dataset generation
2. reflection-based data refinement
3. tokenizer extension with domain tokens
4. external dataset prep and baseline framing

Wisdom:
"Data preparation is a competitive advantage when done systematically."

## Slide 3: Source Map for Add-On B

Prompt:
Create an 8K concept slide mapping these assets:
- `ch07/05_dataset-generation/llama3-ollama.ipynb`
- `ch07/05_dataset-generation/reflection-gpt4.ipynb`
- `ch05/09_extending-tokenizers/extend-tiktoken.ipynb`
- `ch06/03_bonus_imdb-classification/download_prepare_dataset.py`

Extended Annotations (12):
1. Synthetic dataset creation starts with prompt templates.
2. Reflection loop improves generated instruction quality.
3. Tokenizer extension supports domain-specific vocabulary.
4. External dataset prep script standardizes large-corpus workflow.
5. These assets complement core SFT/DPO modules.
6. Data engineering decisions affect all later modules.
7. Quality checks are mandatory between each stage.
8. Keep reproducible scripts/notebooks for every transform.
9. Avoid mixing model changes while testing data changes.
10. Use same evaluation rubric for before/after comparison.
11. Dataset governance and traceability matter.
12. Related topic: runbook in Slide 28.

Beginner's Corner:
- What this means: We improve what the model learns from, not only how it trains.
- Why it matters: Clean, rich data can outperform complex training tricks.
- Common mistake: tuning models heavily on weak datasets.

Wisdom:
"Data-first iteration saves compute and improves outcomes."

## Slide 4: Synthetic Dataset Generation Workflow

Prompt:
Create an 8K concept slide showing instruction seed prompts expanded into synthetic instruction-output entries.

Extended Annotations (12):
1. Start from seed domains/tasks.
2. Generate candidate instruction examples.
3. Control output schema consistency.
4. Keep metadata for provenance.
5. Filter low-quality generations early.
6. Save outputs in structured JSON.
7. Anchor: `llama3-ollama.ipynb`.
8. Common bug: uncontrolled generation settings causing noisy data.
9. Practical check: random sample audit before training.
10. Synthetic expansion should preserve task diversity.
11. Deterministic settings improve reproducibility.
12. Related topic: reflection pass in Slide 5.

Beginner's Corner:
- What this means: Use a strong model to draft more training examples.
- Why it matters: Helps scale data quickly.
- Common mistake: assuming generated data is automatically high quality.

Wisdom:
"Synthetic volume without quality control can hurt more than help."

## Slide 5: Reflection-Tuning Data Refinement

Prompt:
Create an 8K concept slide showing generated examples being critiqued and revised in a second pass.

Extended Annotations (12):
1. Reflection pass critiques generated outputs.
2. Revision step improves clarity and correctness.
3. Creates iterative data-improvement loop.
4. Can remove ambiguity and instruction drift.
5. Keep diff between original and revised entries.
6. Track acceptance/rejection reasons.
7. Anchor: `reflection-gpt4.ipynb`.
8. Common bug: overwriting originals without traceability.
9. Practical check: compare score deltas pre/post reflection.
10. Reflection prompts should be stable and documented.
11. Helps create “teaching signal” quality data.
12. Related topic: evaluation gates in Slide 23.

Beginner's Corner:
- What this means: A second pass can clean up weak generated examples.
- Why it matters: Better supervision leads to better model outputs.
- Common mistake: skipping revision because first draft “looks okay.”

Wisdom:
"Data refinement is where quality compounds."

## Slide 6: Data Quality Dimensions for Instruction Corpora

Prompt:
Create an 8K concept slide with quality axes: correctness, diversity, clarity, safety, formatting consistency.

Extended Annotations (12):
1. Correctness is non-negotiable.
2. Diversity prevents narrow overfitting.
3. Clarity improves learnability of responses.
4. Safety constraints should be explicit.
5. Template consistency stabilizes training.
6. Length distribution should be monitored.
7. Detect duplicates and near-duplicates.
8. Balance domains/task types intentionally.
9. Include hard/edge cases deliberately.
10. Common bug: quality drift during fast expansion.
11. Use scorecards per data batch.
12. Related topic: tokenizer effects in Slide 9.

Beginner's Corner:
- What this means: “Good data” has multiple quality dimensions.
- Why it matters: One weak dimension can degrade model behavior.
- Common mistake: optimizing only for dataset size.

Wisdom:
"Quality is multidimensional; optimize it deliberately."

## Slide 7: Animation - Dataset Generation Loop (Hour 1)

Prompt:
Create an 8K storyboard slide: seed set -> synthetic expansion -> reflection cleanup -> quality gate -> training-ready dataset.

Animation Asset:
- `/Users/sanjayb/Documents/New project/course_outputs/llm-beginners-foundations/hour27-dataset-generation-loop-animation.py`

Wisdom:
"High-quality datasets are engineered artifacts."

## Slide 8: Tokenizer Extension Motivation

Prompt:
Create an 8K concept slide showing domain terms splitting poorly before extension and compactly after extension.

Extended Annotations (12):
1. Default tokenizer may fragment domain terms heavily.
2. Extra tokens can improve compact representation.
3. Impacts sequence length and potentially learning dynamics.
4. Requires model/tokenizer compatibility updates.
5. Useful for code, medical, legal, or org-specific vocab.
6. Should be validated with downstream metrics.
7. Anchor: `extend-tiktoken.ipynb`.
8. Common bug: adding tokens without adapting model embeddings.
9. Practical check: compare token counts before/after extension.
10. Keep tokenizer versioning explicit.
11. Evaluate trade-offs before committing.
12. Related topic: training impact in Slide 10.

Beginner's Corner:
- What this means: Teach tokenizer to treat important domain terms as better units.
- Why it matters: More efficient and potentially clearer model conditioning.
- Common mistake: changing tokenizer without regenerating datasets/checkpoints.

Wisdom:
"Tokenizer changes are model interface changes."

## Slide 9: Extending Tiktoken Safely

Prompt:
Create an 8K concept slide with safe extension checklist: token list curation, collision checks, version pinning.

Extended Annotations (12):
1. Curate candidate tokens from real corpus stats.
2. Avoid unstable or noisy token additions.
3. Document tokenizer version and changes.
4. Regenerate tokenized datasets after extension.
5. Confirm embedding matrix sizing.
6. Keep fallback path to base tokenizer.
7. Anchor: `extend-tiktoken.ipynb`.
8. Common bug: mixed tokenizer versions in training/eval.
9. Practical check: serialize tokenizer config with run artifacts.
10. Use A/B experiments to justify extension.
11. Avoid over-extending with low-value tokens.
12. Related topic: benchmarking in Slide 20.

Beginner's Corner:
- What this means: Tokenizer upgrades need engineering hygiene.
- Why it matters: Prevents incompatible pipelines.
- Common mistake: ad-hoc tokenizer edits without traceability.

Wisdom:
"Tokenizer governance is part of reproducible ML."

## Slide 10: Measuring Impact of Data + Tokenizer Changes

Prompt:
Create an 8K concept slide with A/B matrix: baseline vs synthetic+refined vs tokenizer-extended.

Extended Annotations (12):
1. Keep one-change-at-a-time comparisons.
2. Track quality and efficiency metrics jointly.
3. Use same evaluation prompts and rubric.
4. Measure training stability differences.
5. Track token-length distribution changes.
6. Include latency/memory effects when relevant.
7. Preserve baseline checkpoint for rollback.
8. Report confidence intervals when possible.
9. Common bug: multiple simultaneous changes obscure causality.
10. Practical strategy: staged experimental ladder.
11. Use final decision table for adoption.
12. Related topic: capstone readiness in Slide 24.

Beginner's Corner:
- What this means: Data changes need evidence, not assumptions.
- Why it matters: Avoids expensive but unhelpful modifications.
- Common mistake: accepting improvements from noisy one-off runs.

Wisdom:
"Evidence-based iteration beats optimistic iteration."

## Slide 11: External Dataset Prep Pipeline (IMDb Example)

Prompt:
Create an 8K concept slide showing external dataset download, parse, split, and CSV export workflow.

Extended Annotations (12):
1. External datasets need reproducible bootstrap scripts.
2. Standardized train/val/test splits enable fair comparisons.
3. Track source and license information.
4. Persist processed files as stable inputs.
5. Large datasets improve benchmark reliability.
6. Prepare baseline models for context.
7. Anchor: `download_prepare_dataset.py`.
8. Common bug: non-deterministic split behavior.
9. Practical check: save split stats and class balance.
10. Reuse this pattern for new domains.
11. Helps bridge classroom to real-world datasets.
12. Related topic: baseline comparisons in Slide 12.

Beginner's Corner:
- What this means: Scripted dataset prep is reusable engineering work.
- Why it matters: Enables repeatable benchmarking.
- Common mistake: manual one-time dataset prep steps.

Wisdom:
"Automated data prep is foundational MLOps behavior."

## Slide 12: Baseline Spectrum and Benchmark Framing

Prompt:
Create an 8K concept slide showing why logistic regression/BERT/GPT baselines should be compared under the same dataset protocol.

Extended Annotations (12):
1. Baselines set realistic performance context.
2. Simpler models can be competitive in some settings.
3. Compare compute, speed, and quality jointly.
4. Keep preprocessing and splits consistent.
5. Report model size alongside accuracy.
6. Avoid cherry-picking tasks for one model family.
7. Anchors: IMDb bonus scripts/notebooks.
8. Common bug: unfair comparisons via mismatched conditions.
9. Practical strategy: baseline table template in reports.
10. Encourage critical interpretation of metrics.
11. Strong baselines improve teaching rigor.
12. Related topic: final decision matrix in Slide 24.

Beginner's Corner:
- What this means: Good benchmarking compares alternatives fairly.
- Why it matters: Prevents overclaiming model gains.
- Common mistake: comparing models under different setups.

Wisdom:
"A strong baseline is a scientific sanity check."

## Slide 13: Practical - Generate Synthetic Instruction Data

Prompt:
Create an 8K practical slide with run checklist for `llama3-ollama.ipynb` and output validation.

Hands-on Anchor:
`[Hands-on Anchor: ADDON-B-LAB-01 | Asset: ch07/05_dataset-generation/llama3-ollama.ipynb | Objective: generate synthetic instruction examples and validate schema/quality samples | Pre-req: ADDON-A-LAB-APP-B]`

Wisdom:
"Generation is step one; validation is step two."

## Slide 14: Hands-on Appendix A - Hour 1 Quality Gates

Prompt:
Create an 8K appendix slide with immediate quality gate checklist for synthetic data outputs.

Hands-on Anchor:
`[Hands-on Anchor: ADDON-B-LAB-APP-A | Asset: ch07/05_dataset-generation/instruction-data-llama3-7b.json; ch07/05_dataset-generation/llama3-ollama.ipynb | Objective: enforce synthetic data quality gates before refinement and training usage | Pre-req: ADDON-B-LAB-01]`

Wisdom:
"Gates convert raw output into trustworthy data assets."

## Slide 15: Code Bridge A - Generation + Reflection Pipeline

Prompt:
Create an 8K code demonstration slide.

LEFT (60%) - CODE:
- generate synthetic entries.
- reflection pass and revised output write.

RIGHT (40%) - FLOW:
- draft data -> critique -> improved data artifact.

Hands-on Anchor:
`[Hands-on Anchor: ADDON-B-CODE-01 | Asset: ch07/05_dataset-generation/llama3-ollama.ipynb; ch07/05_dataset-generation/reflection-gpt4.ipynb | Objective: explain end-to-end data generation/refinement code path | Pre-req: ADDON-B-LAB-APP-A]`

Wisdom:
"Refinement loops separate high-quality datasets from raw synthetic dumps."

## Slide 16: Transition - Data Quality to Tokenizer Strategy

Prompt:
Create an 8K concept slide connecting cleaned data to tokenizer extension decisions.

Extended Annotations (12):
1. Clean data reveals recurring domain terms.
2. Candidate token list can be derived from corpus stats.
3. Tokenizer updates should be justified by measurable gains.
4. Keep tokenizer/data versions linked.
5. Re-tokenize datasets after tokenizer changes.
6. Preserve baseline for rollback.
7. Anchor bridge: Ch7 generation + Ch5 tokenizer extension.
8. Common bug: applying tokenizer changes without reprocessing data.
9. Practical strategy: decision gate before extension.
10. Encourages disciplined interface evolution.
11. Supports capstone reliability.
12. Related topic: practical tokenizer lab in Slide 18.

Beginner's Corner:
- What this means: Better data can tell you when tokenizer updates are worthwhile.
- Why it matters: Prevents unnecessary tokenizer churn.
- Common mistake: extending tokenizer too early.

Wisdom:
"Update tokenizers based on corpus evidence, not intuition alone."

## Slide 17: Practical - Reflection-Based Dataset Improvement

Prompt:
Create an 8K practical slide for running `reflection-gpt4.ipynb` and comparing pre/post samples.

Hands-on Anchor:
`[Hands-on Anchor: ADDON-B-LAB-02 | Asset: ch07/05_dataset-generation/reflection-gpt4.ipynb | Objective: apply reflection refinement and document quality improvements on sample slices | Pre-req: ADDON-B-LAB-01]`

Wisdom:
"Show concrete before/after evidence, not just aggregate claims."

## Slide 18: Practical - Extend Tiktoken for Domain Terms

Prompt:
Create an 8K practical slide with safe extension checklist and token-count comparison outputs.

Hands-on Anchor:
`[Hands-on Anchor: ADDON-B-LAB-03 | Asset: ch05/09_extending-tokenizers/extend-tiktoken.ipynb | Objective: add domain tokens safely and measure tokenization efficiency changes | Pre-req: ADDON-B-LAB-02]`

Wisdom:
"Tokenizer changes should earn their complexity through measured impact."

## Slide 19: Animation - Tokenizer Extension Impact (Hour 2)

Prompt:
Create an 8K storyboard slide: phrase tokenization before/after extension -> sequence length shift -> training efficiency implication.

Animation Asset:
- `/Users/sanjayb/Documents/New project/course_outputs/llm-beginners-foundations/hour28-tokenizer-extension-impact-animation.py`

Wisdom:
"Encoding choices influence all downstream compute and quality."

## Slide 20: Practical - A/B Data and Tokenizer Experiments

Prompt:
Create an 8K practical slide with experiment matrix template and logging rules.

Hands-on Anchor:
`[Hands-on Anchor: ADDON-B-LAB-04 | Asset: ch07/05_dataset-generation/llama3-ollama.ipynb; ch07/05_dataset-generation/reflection-gpt4.ipynb; ch05/09_extending-tokenizers/extend-tiktoken.ipynb | Objective: run controlled A/B experiments for data refinement and tokenizer extension effects | Pre-req: ADDON-B-LAB-03]`

Wisdom:
"Controlled experiments are how data engineering becomes science."

## Slide 21: Practical - Bootstrap IMDb-Scale Dataset

Prompt:
Create an 8K practical slide with run checklist and split validation for external dataset prep script.

Hands-on Anchor:
`[Hands-on Anchor: ADDON-B-LAB-05 | Asset: ch06/03_bonus_imdb-classification/download_prepare_dataset.py | Objective: bootstrap a large benchmark dataset with reproducible splits and artifacts | Pre-req: ADDON-B-LAB-04]`

Wisdom:
"Benchmark pipelines should be scripted, reproducible, and auditable."

## Slide 22: Practical - Baseline Benchmark Context

Prompt:
Create an 8K practical slide connecting dataset prep to baseline scripts/notebooks for fair model comparisons.

Hands-on Anchor:
`[Hands-on Anchor: ADDON-B-LAB-06 | Asset: ch06/03_bonus_imdb-classification/sklearn-baseline.ipynb; ch06/03_bonus_imdb-classification/train_gpt.py; ch06/03_bonus_imdb-classification/train_bert_hf.py; ch06/03_bonus_imdb-classification/train_sklearn_logreg.py | Objective: run or map baseline spectrum against prepared dataset protocol | Pre-req: ADDON-B-LAB-05]`

Wisdom:
"Baseline breadth improves confidence in conclusions."

## Slide 23: Data Governance and Versioning

Prompt:
Create an 8K concept slide with dataset artifact versioning, changelog, and provenance tracking.

Extended Annotations (12):
1. Version datasets after every transform.
2. Keep provenance for generated/refined rows.
3. Store generation config with data artifacts.
4. Track tokenizer version used per dataset.
5. Maintain schema contract docs.
6. Add lightweight data changelog.
7. Support rollback to previous dataset versions.
8. Common bug: losing lineage between data and model run.
9. Practical strategy: immutable snapshot folders.
10. Align data governance with evaluation governance.
11. Helps team collaboration and audits.
12. Related topic: release gates in Slide 24.

Beginner's Corner:
- What this means: Treat datasets like versioned code artifacts.
- Why it matters: Enables reliable comparisons and debugging.
- Common mistake: overwriting datasets in place.

Wisdom:
"Unversioned data leads to unverifiable results."

## Slide 24: Release Readiness for Data Assets

Prompt:
Create an 8K concept slide with release gate checklist for data + tokenizer changes.

Extended Annotations (12):
1. Schema validation passed.
2. Quality sample audit completed.
3. Duplicate/near-duplicate checks completed.
4. Tokenizer compatibility validated.
5. A/B impact report generated.
6. Reproducible script/notebook path documented.
7. Baseline comparison included.
8. Artifact hashes/version tags recorded.
9. Safety/compliance checks done.
10. Rollback plan documented.
11. Teaching-ready examples curated.
12. Related topic: final runbook in Slide 28.

Beginner's Corner:
- What this means: Don’t train on a dataset release that hasn’t passed gates.
- Why it matters: Protects model quality and trust.
- Common mistake: pushing “almost cleaned” datasets into training.

Wisdom:
"Data release discipline is model release discipline."

## Slide 25: Practical - Common Data Engineering Failure Drills

Prompt:
Create an 8K practical troubleshooting slide for schema drift, duplicate leakage, and tokenizer mismatch failures.

Hands-on Anchor:
`[Hands-on Anchor: ADDON-B-LAB-07 | Asset: ch07/05_dataset-generation/llama3-ollama.ipynb; ch07/05_dataset-generation/reflection-gpt4.ipynb; ch05/09_extending-tokenizers/extend-tiktoken.ipynb | Objective: diagnose and recover from top data-engineering pipeline failures | Pre-req: ADDON-B-LAB-06]`

Wisdom:
"Failure drills build resilient data pipelines."

## Slide 26: Troubleshooting - Reproducibility for Data Experiments

Prompt:
Create an 8K troubleshooting slide with fixed-seed, fixed-split, fixed-eval policy for data experiments.

Hands-on Anchor:
`[Hands-on Anchor: ADDON-B-LAB-08 | Asset: ch06/03_bonus_imdb-classification/download_prepare_dataset.py; ch06/03_bonus_imdb-classification/train_gpt.py | Objective: enforce reproducible setup for data-change impact measurement | Pre-req: ADDON-B-LAB-05]`

Wisdom:
"Without reproducibility, data improvements are unprovable."

## Slide 27: Code Bridge B - Dataset Lifecycle Skeleton

Prompt:
Create an 8K code demonstration slide.

LEFT (60%) - CODE:
- data generation entrypoint.
- refinement pass call.
- tokenizer extension step.
- split/export and benchmark bootstrap.

RIGHT (40%) - FLOW:
- raw -> curated -> encoded -> benchmark-ready dataset.

Hands-on Anchor:
`[Hands-on Anchor: ADDON-B-CODE-02 | Asset: ch07/05_dataset-generation/llama3-ollama.ipynb; ch07/05_dataset-generation/reflection-gpt4.ipynb; ch05/09_extending-tokenizers/extend-tiktoken.ipynb; ch06/03_bonus_imdb-classification/download_prepare_dataset.py | Objective: explain end-to-end data-engineering orchestration pattern | Pre-req: ADDON-B-LAB-08]`

Wisdom:
"Lifecycle thinking turns notebooks into systems."

## Slide 28: Hands-on Appendix B - Add-On B Runbook

Prompt:
Create an 8K appendix slide with exact run order and verification points across all Add-On B assets.

Hands-on Anchor:
`[Hands-on Anchor: ADDON-B-LAB-APP-B | Asset: ch07/05_dataset-generation/llama3-ollama.ipynb; ch07/05_dataset-generation/reflection-gpt4.ipynb; ch05/09_extending-tokenizers/extend-tiktoken.ipynb; ch06/03_bonus_imdb-classification/download_prepare_dataset.py; ch06/03_bonus_imdb-classification/sklearn-baseline.ipynb | Objective: execute complete data-engineering add-on workflow with objective gates | Pre-req: ADDON-B-LAB-01..08]`

Wisdom:
"A runbook is how advanced data workflows become teachable."

## Slide 29: Hands-on Appendix C - Student Data Engineering Portfolio Pack

Prompt:
Create an 8K appendix slide listing student deliverables: dataset versions, quality report, tokenizer change log, A/B outcomes.

Hands-on Anchor:
`[Hands-on Anchor: ADDON-B-LAB-APP-C | Asset: ch07/05_dataset-generation/instruction-data-llama3-7b.json; ch05/09_extending-tokenizers/extend-tiktoken.ipynb; ch06/03_bonus_imdb-classification/download_prepare_dataset.py | Objective: package student-facing evidence of robust data engineering workflow | Pre-req: ADDON-B-LAB-APP-B]`

Wisdom:
"Portfolio artifacts should prove process quality, not just final metrics."

## Slide 30: Session Takeaway

Prompt:
Create an 8K recap slide with six outcomes:
1. Generate synthetic instruction data safely.
2. Apply reflection-based quality refinement.
3. Extend tokenizer with governance and validation.
4. Bootstrap reproducible external datasets.
5. Run fair baseline comparisons.
6. Ship versioned, auditable data artifacts.

Next:
Proceed to Add-On C (Reliability + Engineering).

Wisdom:
"Data engineering rigor multiplies the value of every training hour."
