# Centralized Code Appendix Deck (28 Slides, 7 Chapters x 4 Slides)

## Structure

- C1-S1..C1-S4: Foundations/Ch1 bridge code
- C2-S1..C2-S4: Ch2 data pipeline
- C3-S1..C3-S4: Ch3 attention mechanics
- C4-S1..C4-S4: Ch4 GPT architecture
- C5-S1..C5-S4: Ch5 pretraining pipeline
- C6-S1..C6-S4: Ch6 classification finetuning
- C7-S1..C7-S4: Ch7 instruction tuning and DPO bridge

Every slide must include one Hands-on Anchor tag.

## C1-S1

Prompt:
Code bridge for tensor basics and autograd from Appendix-A.
`[Hands-on Anchor: C1-S1 | Asset: appendix-A/01_main-chapter-code/code-part1.ipynb | Objective: map tensor operations to training intuition | Pre-req: None]`

## C1-S2

Prompt:
Code bridge for minimal training loop skeleton.
`[Hands-on Anchor: C1-S2 | Asset: appendix-A/01_main-chapter-code/code-part2.ipynb | Objective: explain zero_grad/backward/step sequence | Pre-req: C1-S1]`

## C1-S3

Prompt:
Code bridge for model forward and loss flow in beginner context.
`[Hands-on Anchor: C1-S3 | Asset: appendix-A/01_main-chapter-code/code-part2.ipynb | Objective: trace logits-to-loss path | Pre-req: C1-S2]`

## C1-S4

Prompt:
Code bridge from foundations to Ch1/Ch2 setup readiness.
`[Hands-on Anchor: C1-S4 | Asset: appendix-A/01_main-chapter-code/code-part1.ipynb; appendix-A/01_main-chapter-code/code-part2.ipynb | Objective: consolidate prerequisite coding patterns | Pre-req: C1-S1..S3]`

## C2-S1

Prompt:
Tokenization to IDs code walkthrough.
`[Hands-on Anchor: C2-S1 | Asset: ch02/01_main-chapter-code/ch02.ipynb | Objective: explain text->token IDs pipeline | Pre-req: C1-S4]`

## C2-S2

Prompt:
Embedding lookup shape walkthrough.
`[Hands-on Anchor: C2-S2 | Asset: ch02/01_main-chapter-code/ch02.ipynb | Objective: trace (batch,seq,dim) shapes | Pre-req: C2-S1]`

## C2-S3

Prompt:
Sliding-window dataset creation walkthrough.
`[Hands-on Anchor: C2-S3 | Asset: ch02/01_main-chapter-code/dataloader.ipynb | Objective: explain shifted input/target pair construction | Pre-req: C2-S1]`

## C2-S4

Prompt:
DataLoader iteration and batch debug walkthrough.
`[Hands-on Anchor: C2-S4 | Asset: ch02/01_main-chapter-code/dataloader.ipynb | Objective: verify loader outputs and common bug fixes | Pre-req: C2-S3]`

## C3-S1

Prompt:
Single-head attention score computation walkthrough.
`[Hands-on Anchor: C3-S1 | Asset: ch03/01_main-chapter-code/ch03.ipynb | Objective: map QK^T->softmax->weighted sum | Pre-req: C2-S4]`

## C3-S2

Prompt:
Causal masking code walkthrough.
`[Hands-on Anchor: C3-S2 | Asset: ch03/01_main-chapter-code/ch03.ipynb | Objective: explain no-future-token enforcement | Pre-req: C3-S1]`

## C3-S3

Prompt:
Multi-head reshape/transpose/recombine walkthrough.
`[Hands-on Anchor: C3-S3 | Asset: ch03/01_main-chapter-code/multihead-attention.ipynb | Objective: trace head splitting and recomposition | Pre-req: C3-S2]`

## C3-S4

Prompt:
Attention module debug checklist walkthrough.
`[Hands-on Anchor: C3-S4 | Asset: ch03/01_main-chapter-code/multihead-attention.ipynb | Objective: diagnose dimension/mask bugs | Pre-req: C3-S3]`

## C4-S1

Prompt:
LayerNorm + GELU + FFN code walkthrough.
`[Hands-on Anchor: C4-S1 | Asset: ch04/01_main-chapter-code/gpt.py | Objective: explain core block primitives | Pre-req: C3-S4]`

## C4-S2

Prompt:
TransformerBlock residual path walkthrough.
`[Hands-on Anchor: C4-S2 | Asset: ch04/01_main-chapter-code/gpt.py | Objective: trace pre-norm attention and FFN residual branches | Pre-req: C4-S1]`

## C4-S3

Prompt:
GPTModel forward pass walkthrough.
`[Hands-on Anchor: C4-S3 | Asset: ch04/01_main-chapter-code/gpt.py | Objective: map embeddings->blocks->norm->head | Pre-req: C4-S2]`

## C4-S4

Prompt:
Autoregressive generation loop walkthrough.
`[Hands-on Anchor: C4-S4 | Asset: ch04/01_main-chapter-code/gpt.py; ch04/01_main-chapter-code/tests.py | Objective: explain decode loop and deterministic checks | Pre-req: C4-S3]`

## C5-S1

Prompt:
Pretraining batch loss walkthrough.
`[Hands-on Anchor: C5-S1 | Asset: ch05/01_main-chapter-code/gpt_train.py | Objective: map logits flattening to cross-entropy | Pre-req: C4-S4]`

## C5-S2

Prompt:
Training loop + evaluation cadence walkthrough.
`[Hands-on Anchor: C5-S2 | Asset: ch05/01_main-chapter-code/gpt_train.py | Objective: explain eval_freq/eval_iter and tokens_seen tracking | Pre-req: C5-S1]`

## C5-S3

Prompt:
Checkpoint save/load and plot workflow walkthrough.
`[Hands-on Anchor: C5-S3 | Asset: ch05/01_main-chapter-code/gpt_train.py | Objective: verify artifact lifecycle | Pre-req: C5-S2]`

## C5-S4

Prompt:
Pretrained weight loading and generation walkthrough.
`[Hands-on Anchor: C5-S4 | Asset: ch05/01_main-chapter-code/gpt_generate.py; ch05/01_main-chapter-code/gpt_download.py | Objective: explain safe model-weight loading path | Pre-req: C5-S3]`

## C6-S1

Prompt:
Dataset balancing/splitting code walkthrough.
`[Hands-on Anchor: C6-S1 | Asset: ch06/01_main-chapter-code/gpt_class_finetune.py | Objective: explain supervised dataset prep for classification | Pre-req: C5-S4]`

## C6-S2

Prompt:
SpamDataset tokenization/padding walkthrough.
`[Hands-on Anchor: C6-S2 | Asset: ch06/01_main-chapter-code/gpt_class_finetune.py | Objective: trace encode/truncate/pad path | Pre-req: C6-S1]`

## C6-S3

Prompt:
Head replacement + selective unfreezing walkthrough.
`[Hands-on Anchor: C6-S3 | Asset: ch06/01_main-chapter-code/gpt_class_finetune.py | Objective: explain classifier adaptation strategy | Pre-req: C6-S2]`

## C6-S4

Prompt:
Classification training/eval metric loop walkthrough.
`[Hands-on Anchor: C6-S4 | Asset: ch06/01_main-chapter-code/gpt_class_finetune.py; ch06/01_main-chapter-code/tests.py | Objective: map loss/accuracy and smoke-test path | Pre-req: C6-S3]`

## C7-S1

Prompt:
Instruction dataset formatting walkthrough.
`[Hands-on Anchor: C7-S1 | Asset: ch07/01_main-chapter-code/gpt_instruction_finetuning.py | Objective: explain instruction/input/response formatting logic | Pre-req: C6-S4]`

## C7-S2

Prompt:
Custom collate and ignore-index masking walkthrough.
`[Hands-on Anchor: C7-S2 | Asset: ch07/01_main-chapter-code/gpt_instruction_finetuning.py | Objective: trace masked target construction for SFT | Pre-req: C7-S1]`

## C7-S3

Prompt:
Instruction SFT train/generate artifact path walkthrough.
`[Hands-on Anchor: C7-S3 | Asset: ch07/01_main-chapter-code/gpt_instruction_finetuning.py; ch07/01_main-chapter-code/ollama_evaluate.py | Objective: explain SFT outputs and evaluation handoff | Pre-req: C7-S2]`

## C7-S4

Prompt:
DPO + LoRA bridge walkthrough.
`[Hands-on Anchor: C7-S4 | Asset: ch07/04_preference-tuning-with-dpo/dpo-from-scratch.ipynb; appendix-E/01_main-chapter-code/appendix-E.ipynb | Objective: map from SFT to preference tuning and PEFT integration | Pre-req: C7-S3]`
