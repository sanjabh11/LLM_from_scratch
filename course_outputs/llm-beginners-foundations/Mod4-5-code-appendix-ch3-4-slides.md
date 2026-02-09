# Code Appendix Pack - Chapter 3 (4 Slides)

Use this as part of the centralized 28-slide code appendix deck (7 chapters x 4 slides).

## C3-S1: Single-Head Attention Forward Pass

- Asset: `ch03/01_main-chapter-code/ch03.ipynb`
- Focus:
1. Q/K/V projection
2. score matrix (`QK^T`)
3. scaling
4. softmax
5. weighted sum
- Hands-on Anchor:
`[Hands-on Anchor: CH3-CAPP-01 | Asset: ch03/01_main-chapter-code/ch03.ipynb | Objective: line-by-line explain single-head attention | Pre-req: CH3-LAB-03]`

## C3-S2: Causal Mask + Dropout Path

- Asset: `ch03/01_main-chapter-code/ch03.ipynb`
- Focus:
1. triangular mask construction
2. masking scores before softmax
3. dropout on attention weights
4. output stability checks
- Hands-on Anchor:
`[Hands-on Anchor: CH3-CAPP-02 | Asset: ch03/01_main-chapter-code/ch03.ipynb | Objective: explain masked attention and regularization | Pre-req: CH3-LAB-05]`

## C3-S3: Multi-Head Split/Concat Mechanics

- Asset: `ch03/01_main-chapter-code/multihead-attention.ipynb`
- Focus:
1. head splitting into parallel attention lanes
2. batched matrix operations
3. concatenation and projection
4. output shape verification
- Hands-on Anchor:
`[Hands-on Anchor: CH3-CAPP-03 | Asset: ch03/01_main-chapter-code/multihead-attention.ipynb | Objective: map tensor shape changes across multi-head steps | Pre-req: CH3-LAB-08]`

## C3-S4: Efficient Implementations + Buffers

- Assets:
- `ch03/02_bonus_efficient-multihead-attention/mha-implementations.ipynb`
- `ch03/03_understanding-buffers/understanding-buffers.ipynb`
- Focus:
1. implementation benchmark comparison
2. buffer registration purpose
3. state_dict behavior with buffers
4. safe optimization decision checklist
- Hands-on Anchor:
`[Hands-on Anchor: CH3-CAPP-04 | Asset: ch03/02_bonus_efficient-multihead-attention/mha-implementations.ipynb; ch03/03_understanding-buffers/understanding-buffers.ipynb | Objective: compare speed and correctness while preserving reproducibility | Pre-req: CH3-LAB-09, CH3-LAB-10]`

