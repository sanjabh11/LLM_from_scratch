# Ch2 Additional Hands-on Appendix Slides

Use these to replace non-aligned checkpoint slides and tighten Colab linkage.

## Appendix Slide A (Use at Slide 14)

Title: `Hands-on Appendix A - Hour 1 Lab Execution`

Content:
- Execute in order:
1. `ch02/01_main-chapter-code/ch02.ipynb` (tokenization + IDs)
2. `ch02/05_bpe-from-scratch/bpe-from-scratch-simple.ipynb` (BPE intuition)
3. `ch02/03_bonus_embedding-vs-matmul/embeddings-and-linear-layers.ipynb` (embedding equivalence intuition)

Mandatory tag:
`[Hands-on Anchor: CH2-LAB-APP-A | Asset: ch02/01_main-chapter-code/ch02.ipynb | Objective: complete Hour-1 core run-path | Pre-req: CH2-LAB-01..05]`

## Appendix Slide B (Use at Slide 28)

Title: `Hands-on Appendix B - Hour 2 Lab Execution`

Content:
- Execute in order:
1. `ch02/01_main-chapter-code/dataloader.ipynb`
2. `ch02/04_bonus_dataloader-intuition/dataloader-intuition.ipynb`
3. `ch02/01_main-chapter-code/exercise-solutions.ipynb` (selected checks)

Mandatory tag:
`[Hands-on Anchor: CH2-LAB-APP-B | Asset: ch02/01_main-chapter-code/dataloader.ipynb | Objective: complete sliding-window and DataLoader flow | Pre-req: CH2-LAB-06..13]`

## Appendix Slide C (Use at Slide 29)

Title: `Hands-on Appendix C - Advanced Extensions`

Content:
- Extension path 1: tokenizer comparison benchmark
`ch02/02_bonus_bytepair-encoder/compare-bpe-tiktoken.ipynb`
- Extension path 2: full BPE from scratch
`ch02/05_bpe-from-scratch/bpe-from-scratch.ipynb`

Mandatory tag:
`[Hands-on Anchor: CH2-LAB-APP-C | Asset: ch02/02_bonus_bytepair-encoder/compare-bpe-tiktoken.ipynb; ch02/05_bpe-from-scratch/bpe-from-scratch.ipynb | Objective: choose one advanced tokenizer path | Pre-req: CH2-LAB-03]`

## Optional Takeaway Slide (Use at Slide 30 if needed)

Title: `Session Takeaway - Ch2`

Summary bullets:
- You can convert raw text to model-ready numeric representations.
- You can form correct shifted input/target pairs for next-token learning.
- You can build and debug a basic DataLoader pipeline.
- You are ready for attention mechanics in Ch3.

