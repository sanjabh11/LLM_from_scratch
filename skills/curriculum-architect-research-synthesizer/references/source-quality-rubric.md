# Source Quality Rubric

Use this rubric to score every source before including it in the final learning program.
Score each dimension from 1 to 5, then compute the weighted score.

## Scoring Dimensions

| Dimension | Weight | 1 (Low) | 3 (Medium) | 5 (High) |
| --- | --- | --- | --- | --- |
| Credibility | 0.35 | Anonymous/unclear authority | Mixed authority | Official docs, recognized experts, or verifiable maintainers |
| Recency | 0.20 | Stale and likely outdated | Partly current | Current with latest major versions/practices |
| Pedagogical Clarity | 0.20 | Hard to follow, missing structure | Understandable but uneven | Clear explanations, progressive sequencing, concrete examples |
| Practical Transfer | 0.15 | Mostly theory, little application | Some practical use | Strong real-world workflows, debugging, deployment, tradeoffs |
| Signal Density | 0.10 | Filler-heavy, low insight | Moderate signal | High insight per minute/page with minimal fluff |

## Weighted Score Formula

```
weighted_score =
  (credibility * 0.35) +
  (recency * 0.20) +
  (pedagogical_clarity * 0.20) +
  (practical_transfer * 0.15) +
  (signal_density * 0.10)
```

## Selection Thresholds

- Include by default: `weighted_score >= 4.0`
- Include conditionally: `3.4 - 3.9` only if filling a clear gap
- Exclude by default: `< 3.4`

## Red-Flag Overrides

Exclude regardless of score when any of these apply:

- Source promotes unsafe or non-compliant practices for the domain.
- Source conflicts with official documentation and cannot be reconciled.
- Source is heavily version-obsolete without explicit legacy framing.

## Coverage Constraints

Apply these constraints after scoring:

- Keep at least 40% of core learning path resources from official documentation or official channels.
- Keep at most 35% from any single creator/channel/source community.
- Ensure each major competency area has at least 2 independent sources.

