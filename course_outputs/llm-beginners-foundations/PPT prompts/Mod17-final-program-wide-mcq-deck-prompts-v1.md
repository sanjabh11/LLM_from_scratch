# LLM Beginners Course: Final Program-Wide MCQ Deck (Leakage-Safe, 30 Slides)

## Rules (Apply to all MCQ slides)

- No answer keys on learner-facing slides.
- No hidden instructor notes inside prompt text.
- Keep language beginner-friendly and unambiguous.
- Use 4 options per question (A-D).
- Mix conceptual, practical, debugging, and design-decision questions.

## Slide 1: Title

Prompt:
Create an 8K premium title slide.

Text:
- Title: FINAL MASTERY CHECK
- Subtitle: LLM Beginners Program (Foundations to Alignment)
- Tagline: Evaluate understanding across the full stack.

## Slide 2: Agenda

Prompt:
Create an 8K agenda slide with three sections:
1. Fundamentals and architecture
2. Training and finetuning pipelines
3. Alignment and integration decisions

## Slide 3: MCQ (Foundations)

Prompt:
Question: Which statement best describes tensors in PyTorch?
A. They are only for image data.
B. They are multidimensional arrays supporting autograd operations.
C. They are fixed-size strings for model prompts.
D. They are GPU-only data structures.

## Slide 4: MCQ (Foundations)

Prompt:
Question: In a training loop, what is the correct order for one standard update step?
A. `optimizer.step()` -> `loss.backward()` -> `zero_grad()`
B. `zero_grad()` -> `loss.backward()` -> `optimizer.step()`
C. `loss.backward()` -> `zero_grad()` -> `optimizer.step()`
D. `optimizer.step()` -> `zero_grad()` -> `loss.backward()`

## Slide 5: MCQ (Ch1)

Prompt:
Question: A GPT-style LLM generates text primarily by:
A. Retrieving fixed answers from a hidden database.
B. Predicting one token at a time from prior context.
C. Planning complete paragraphs before tokenizing.
D. Running symbolic logic rules only.

## Slide 6: MCQ (Ch1)

Prompt:
Question: Why are embeddings used?
A. To compress model checkpoints for storage.
B. To map token IDs into dense vectors that encode useful patterns.
C. To replace attention layers entirely.
D. To avoid using tokenization.

## Slide 7: MCQ (Ch2)

Prompt:
Question: In next-token training data, targets are typically:
A. Identical to inputs.
B. Inputs shifted one position to the right.
C. Randomly shuffled tokens.
D. One-hot vectors of sequence length.

## Slide 8: MCQ (Ch2)

Prompt:
Question: What is a common purpose of stride in sliding-window dataset creation?
A. Set learning rate schedule.
B. Control overlap between adjacent training windows.
C. Enable mixed precision.
D. Freeze model layers.

## Slide 9: MCQ (Ch3)

Prompt:
Question: In scaled dot-product attention, scaling by `sqrt(d_k)` helps:
A. Increase vocabulary size.
B. Stabilize softmax behavior for large dot products.
C. Remove need for masking.
D. Eliminate residual connections.

## Slide 10: MCQ (Ch3)

Prompt:
Question: Why is causal masking used in decoder-only transformers?
A. To speed up tokenization.
B. To prevent tokens from attending to future positions.
C. To reduce embedding dimension.
D. To enforce bidirectional context.

## Slide 11: MCQ (Ch4 Core)

Prompt:
Question: In a pre-norm transformer block, LayerNorm is applied:
A. Only once at model output.
B. Before each sublayer (attention/FFN) in the block.
C. After softmax only.
D. Before tokenization.

## Slide 12: MCQ (Ch4 Core)

Prompt:
Question: In greedy decoding, next token is selected by:
A. Sampling from uniform distribution.
B. Taking argmax over final-step logits.
C. Choosing the lowest-probability token.
D. Averaging all token IDs.

## Slide 13: MCQ (Ch4 Bonus)

Prompt:
Question: KV cache primarily improves inference by:
A. Reducing vocabulary size.
B. Reusing previously computed keys/values across decode steps.
C. Training with larger batch sizes.
D. Removing positional embeddings.

## Slide 14: MCQ (Ch4 Bonus)

Prompt:
Question: Grouped-Query Attention (GQA) is mainly intended to:
A. Increase tokenization speed.
B. Reduce KV-cache memory by sharing K/V across query-head groups.
C. Replace feed-forward layers.
D. Force deterministic outputs.

## Slide 15: Midpoint Recap

Prompt:
Create an 8K recap slide listing covered areas: Foundations, Ch1-Ch4 core/bonus.

## Slide 16: MCQ (Ch5 Core)

Prompt:
Question: Cross-entropy in language-model pretraining is commonly computed between:
A. Input IDs and positional IDs.
B. Flattened logits and shifted target token IDs.
C. Attention scores and dropout masks.
D. Embeddings and optimizer states.

## Slide 17: MCQ (Ch5 Core)

Prompt:
Question: Why track tokens seen during pretraining?
A. It replaces validation loss.
B. It provides a scale-aware progress metric across runs.
C. It sets model context length.
D. It disables overfitting.

## Slide 18: MCQ (Module 8)

Prompt:
Question: A linear warmup schedule is mainly used to:
A. Freeze gradients permanently.
B. Reduce early-step optimization instability.
C. Increase sequence length.
D. Remove need for validation.

## Slide 19: MCQ (Module 8)

Prompt:
Question: For fair speed benchmarking, which is most important?
A. Different datasets per run.
B. Controlled conditions (same data, seeds, settings, metrics).
C. Changing multiple optimizations at once.
D. Measuring only peak throughput once.

## Slide 20: MCQ (Module 9)

Prompt:
Question: A safe weight-loading pipeline should include:
A. Skipping shape checks for speed.
B. Strict shape/config/tokenizer compatibility validation.
C. Converting all models to one tokenizer without checks.
D. Only checking file extension.

## Slide 21: MCQ (Module 9)

Prompt:
Question: Memory-efficient weight loading is valuable because it:
A. Guarantees better model quality.
B. Reduces peak memory during checkpoint load.
C. Removes need for device transfer.
D. Automatically tunes hyperparameters.

## Slide 22: MCQ (Ch6)

Prompt:
Question: In the Ch6 classifier setup, logits are typically taken from:
A. The first token only.
B. The last token position for each sequence.
C. The average of all vocabulary logits.
D. The embedding table directly.

## Slide 23: MCQ (Ch6)

Prompt:
Question: A common efficient finetuning strategy for small classification data is:
A. Train every parameter from scratch.
B. Freeze most layers, train head and selected upper layers.
C. Remove pretrained weights.
D. Use only synthetic labels.

## Slide 24: MCQ (Ch7 Core)

Prompt:
Question: In instruction SFT collation, using ignore index on padded targets is done to:
A. Increase pad token probability.
B. Prevent pad-only positions from contributing to loss.
C. Replace tokenizer.
D. Enable beam search.

## Slide 25: MCQ (Ch7 Core)

Prompt:
Question: A key reason to evaluate generated responses after SFT is:
A. Loss is always sufficient.
B. Response usefulness may not be captured fully by loss trends alone.
C. Evaluation is optional for instruction models.
D. Scores replace dataset quality checks.

## Slide 26: MCQ (Module 12)

Prompt:
Question: DPO training signal is based primarily on:
A. Single target responses only.
B. Preference comparisons between chosen and rejected responses.
C. Randomly sampled logits.
D. Label-smoothed classification loss only.

## Slide 27: MCQ (Module 12)

Prompt:
Question: LoRA is attractive because it:
A. Requires retraining all weights.
B. Adds trainable low-rank adapters while keeping most base weights frozen.
C. Eliminates evaluation needs.
D. Works only for CNNs.

## Slide 28: MCQ (Integration)

Prompt:
Question: For capstone readiness, which is best practice?
A. Promote model after one good sample.
B. Use objective gates (data quality, stability, eval scores, reproducibility).
C. Skip artifact logging for speed.
D. Change evaluator every run.

## Slide 29: MCQ (Integration)

Prompt:
Question: When comparing two alignment strategies, you should:
A. Use different prompts and metrics for each.
B. Keep evaluation protocol constant and compare results under matched conditions.
C. Disable seed controls.
D. Ignore runtime/memory differences.

## Slide 30: Final Recap

Prompt:
Create an 8K recap slide with:
- 6 core competencies validated
- readiness statement for real-world project execution
- note: answer key is maintained separately for instructors.
