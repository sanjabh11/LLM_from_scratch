# Final Student Capstone Checklist v2

## Goal
Ship a beginner-friendly but engineering-rigorous LLM capstone that is reproducible, test-backed, and presentation-ready.

## A. Foundation Readiness
- [ ] Environment preflight completed with zero critical failures.
- [ ] Core module prerequisites completed (Modules 1-7 minimum).
- [ ] Required dependencies and runtime notes documented.

## B. Data and Tokenization Quality
- [ ] Dataset source and preprocessing steps documented.
- [ ] Synthetic/refined data changes are versioned and justified.
- [ ] Tokenization path and any tokenizer extensions are documented.
- [ ] Data leakage, duplicates, and schema issues checked.

## C. Model Build and Training Evidence
- [ ] Training configuration captured (seed, LR, batch size, context length).
- [ ] Baseline and improved runs compared with same evaluation protocol.
- [ ] Checkpoint artifacts versioned and recoverable.
- [ ] At least one ablation or comparison included.

## D. Reliability and Tests
- [ ] Setup tests pass.
- [ ] Tokenizer/attention/variant test suite pass status recorded.
- [ ] If distributed run used, DDP launch logs included.
- [ ] Failure triage notes included for at least one issue and fix.

## E. Productization Readiness
- [ ] One runnable UI path provided (generation/classification/instruction).
- [ ] Inference behavior is demonstrated with stable prompts.
- [ ] Error handling and fallback behavior shown.
- [ ] User-facing demo script prepared (2-5 minutes).

## F. Evaluation and Governance
- [ ] Evaluation rubric defined (quality, safety, consistency, latency).
- [ ] At least 10 representative prompts/tasks evaluated.
- [ ] Hallucination or failure examples documented with mitigation.
- [ ] Release gate decision included: PASS / CONDITIONAL PASS / BLOCK.

## G. Submission Pack
- [ ] Slide deck(s): theory + practical + appendix references.
- [ ] Hands-on anchor mapping included.
- [ ] Reproducibility packet: environment output, tests, configs, hashes.
- [ ] Short retrospective: what worked, what failed, what next.

## Scoring Rubric (Instructor Use)
- Technical correctness: 30%
- Reproducibility and reliability: 25%
- Practical implementation quality: 20%
- Communication clarity (beginner-friendly): 15%
- Governance/safety awareness: 10%
