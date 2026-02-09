# Code Appendix Pack - Chapter 4 (4 Slides)

Use this as part of the centralized 28-slide code appendix deck.

## C4-S1: LayerNorm + GELU + FeedForward

- Asset: `ch04/01_main-chapter-code/gpt.py`
- Focus:
1. `LayerNorm` custom implementation
2. `GELU` nonlinearity
3. `FeedForward` block structure
4. output shape preservation
- Hands-on Anchor:
`[Hands-on Anchor: CH4-CAPP-01 | Asset: ch04/01_main-chapter-code/gpt.py | Objective: explain core mathematical blocks in GPT layer stack | Pre-req: CH4-LAB-01]`

## C4-S2: TransformerBlock with Residual Paths

- Assets:
- `ch04/01_main-chapter-code/gpt.py`
- `ch04/01_main-chapter-code/previous_chapters.py`
- Focus:
1. attention branch residual
2. FFN branch residual
3. dropout placement
4. norm-before-block pattern
- Hands-on Anchor:
`[Hands-on Anchor: CH4-CAPP-02 | Asset: ch04/01_main-chapter-code/gpt.py; ch04/01_main-chapter-code/previous_chapters.py | Objective: map residual dataflow through a full block | Pre-req: CH4-LAB-02]`

## C4-S3: GPTModel Forward Pass

- Asset: `ch04/01_main-chapter-code/gpt.py`
- Focus:
1. token embeddings + positional embeddings
2. transformer stack execution
3. final norm + output head logits
4. batch/sequence shape tracing
- Hands-on Anchor:
`[Hands-on Anchor: CH4-CAPP-03 | Asset: ch04/01_main-chapter-code/gpt.py | Objective: trace complete forward pass end-to-end | Pre-req: CH4-LAB-02]`

## C4-S4: Generation Loop + Determinism Checks

- Assets:
- `ch04/01_main-chapter-code/gpt.py`
- `ch04/01_main-chapter-code/tests.py`
- Focus:
1. context cropping logic
2. last-token logits extraction
3. greedy append loop
4. seed-based deterministic test expectations
- Hands-on Anchor:
`[Hands-on Anchor: CH4-CAPP-04 | Asset: ch04/01_main-chapter-code/gpt.py; ch04/01_main-chapter-code/tests.py | Objective: explain and verify autoregressive generation loop | Pre-req: CH4-LAB-06]`

