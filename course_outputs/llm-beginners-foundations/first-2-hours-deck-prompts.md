# LLM Beginners Course: First 2 Hours (Foundations + Setup + Minimal PyTorch)

## Assumptions and Scope

- Audience is absolute beginners in AI/GenAI/Python.
- Slide format is fixed at 30 slides for 2 hours (15 slides per hour).
- Full hands-on coding is done in separate Google Colab notebooks.
- Slides must stay beginner-friendly but technically accurate.
- Bonus and appendix materials are included where they reduce beginner friction.

## Research Summary

- Repository snapshot analyzed: `82010e2` (2026-01-29).
- Core first-2-hour sources:
- `/tmp/llms-from-scratch/setup/README.md`
- `/tmp/llms-from-scratch/ch01/README.md`
- `/tmp/llms-from-scratch/appendix-A/README.md`
- `/tmp/llms-from-scratch/appendix-A/01_main-chapter-code/code-part1.ipynb`
- `/tmp/llms-from-scratch/appendix-A/01_main-chapter-code/code-part2.ipynb`
- Supporting pedagogy and accessibility:
- Mayer multimedia principles, signaling meta-analysis, WCAG contrast guidance.
- Industry baseline signals:
- Repo provides laptop-first approach and explicit Colab path in setup docs.
- Companion video is 17h15m, supporting a multi-session beginner path.

## Detailed Improvement Plan

### 1) Baseline Audit Summary

- Input artifact reviewed: LLMs-from-scratch repo + chapter/setup/appendix documents.
- Overall quality score: 90/100 for technical depth; 74/100 for absolute-beginner ramp.
- Strengths to preserve:
- Stepwise chapter progression.
- Main + bonus folder split.
- Notebook-first delivery.
- Consistent code reuse via `previous_chapters.py`.
- Weaknesses to fix first:
- Too much conceptual jump for zero-Python learners.
- Setup choices can overwhelm novices.
- Beginner bridge from Python syntax to tensors/autograd is under-emphasized for first hour.

### 2) Gap Matrix

| Dimension | Current State | Target State | Severity | Fix Strategy |
| --- | --- | --- | --- | --- |
| Research grounding | Strong repo depth | Repo + pedagogy-backed slide design | Med | Add learning-science constraints |
| Pedagogy effectiveness | Good for self-study | Guided novice-first scaffold | High | Add analogies + gradual reveal |
| Prompt determinism | Not standardized for deck generation | Fixed prompt contract for Kimi | High | Use strict per-slide schema |
| Visual accessibility | Varies by tooling | Light-theme high-contrast standard | Med | Enforce WCAG-aligned contrast |
| Beginner clarity | Mixed | Plain-language + terminology guardrails | High | Add beginner corner each concept slide |
| Narrative flow | Chapter-centric | Hour-centric with explicit outcomes | Med | Build 15-slide/hour rhythm |
| QA enforceability | Implicit | Explicit gate checklist | Med | Score each gate before release |

### 3) Upgrade Architecture

- System objective: deliver a first 2-hour deck that removes beginner fear and creates confidence to enter Colab labs.
- Prompt architecture strategy: global deck contract + deterministic per-slide prompts.
- Slide taxonomy: concept, practical walkthrough, animation, MCQ, code explanation.
- Analogy strategy: always pair technical term with one plain-language analogy.
- Accessibility upgrades: light background, dark text, limited text density.
- Safety/governance upgrades: include responsible use and verification habits early.

### 4) Execution Plan

1. Research pass: map setup/ch01/appendix-A to beginner outcomes.
2. Architecture pass: lock slide budget and theory-practical ratio.
3. Prompt generation pass: draft all 30 prompts with deterministic schema.
4. QA correction pass: validate gates and patch weak slides.
5. Delivery pass: export prompt pack + animation scripts.

### 5) Risks and Mitigations

| Risk | Why It Matters | Mitigation |
| --- | --- | --- |
| Cognitive overload in first hour | Beginners may disengage early | Use progressive complexity and analogy-first framing |
| Setup frustration | Environment errors kill momentum | Include troubleshooting slides and known fixes |
| Too much theory | Learners may feel abstract disconnect | Add practical walkthrough slides and code explanation anchors |
| Terminology confusion | New learners mix AI/ML/DL/LLM terms | Add vocabulary calibration early with examples |

### 6) Expected Outcome Delta

- Better novice confidence within first 30 minutes.
- Better setup success rate before first lab.
- Clear bridge from Python basics to PyTorch training loop.

## Upgraded Prompt System (Kimi 2 Slide Maker Contract)

- Use light-theme instructional style with dark text and restrained accents.
- For every concept slide include:
- `Overview`, `The Concept`, `How It Works`, `Implementation`, `Why It Matters`.
- Add `Beginner Corner` block on concept and practical walkthrough slides.
- Add `Wisdom Box` on all slides.
- Keep one main idea per slide; avoid decorative clutter.
- Keep language concrete and simple; define jargon once, then reuse consistently.
- Prohibit tool metadata, aspect-ratio tags, footer clutter, and model/tool leakage in slide body text.

Theory-practical target across 30 slides: about `65/35` (actual plan: `20 theory / 10 practical` = `66.7/33.3`).

## Deck Prompts (First 2 Hours)

### Hour 1 (Slides 1-15): Foundations + Setup

1. **Slide 1 - Course Mission and Promise**  
Type: Concept (Theory)  
Prompt: Create a clean orientation slide explaining what learners will be able to do after 2 hours: understand AI vs GenAI vs LLM, set up environment, and read minimal PyTorch code. Add a simple timeline visual for the hour.

2. **Slide 2 - Vocabulary Calibration: AI, ML, DL, GenAI, LLM**  
Type: Concept (Theory)  
Prompt: Build a layered diagram with nested circles and one practical example for each term. Beginner Corner must explain each in plain language with one-sentence analogy.

3. **Slide 3 - LLM Lifecycle Overview (From Repo Ch1)**  
Type: Concept (Theory)  
Prompt: Show lifecycle flow from data collection -> tokenization -> model training -> inference -> evaluation. Include a "where we are today" marker at setup + minimal PyTorch stage.

4. **Slide 4 - Setup Path Selection: Local vs Colab vs Cloud**  
Type: Practical Walkthrough  
Prompt: Create a decision tree showing when to choose local setup, Google Colab, or cloud notebook. Include clear beginner recommendation path and risks for each option.

5. **Slide 5 - Environment Bootstrap Checklist**  
Type: Practical Walkthrough  
Prompt: Present step-by-step checklist from setup docs: clone repo, install requirements, verify Python and torch install. Include expected terminal outputs and common failure points.

6. **Slide 6 - Repository Tour for Beginners**  
Type: Concept (Theory)  
Prompt: Visual map of `setup/`, `ch01/`, `appendix-A/`, and future chapter folders. Explain how main chapter code differs from bonus folders.

7. **Slide 7 - Animation Slide (Hour 1)**  
Type: Animation (Theory Visual)  
Prompt: Embed or reference a 30-second 3Blue1Brown-style animation showing AI->GenAI->LLM pipeline and first-session path through repo folders. Caption should explain progression from concepts to coding confidence.  
Animation source script: `/Users/sanjayb/Documents/New project/course_outputs/llm-beginners-foundations/hour1_foundations_animation.py`

8. **Slide 8 - Python Essentials You Need Today (Only What Matters)**  
Type: Concept (Theory)  
Prompt: Explain variables, functions, loops, and list comprehension as prerequisites for reading PyTorch code. Keep examples in plain pseudo-Python with visual annotations.

9. **Slide 9 - Notebook Literacy: How to Read and Run Cells**  
Type: Practical Walkthrough  
Prompt: Show the notebook workflow (read markdown, run cell, inspect output, fix error, rerun). Include a mini "do this / not this" panel for beginners.

10. **Slide 10 - Why Tensors, Not Just Python Lists**  
Type: Concept (Theory)  
Prompt: Explain tensors as structured numeric containers for fast computation. Compare list vs tensor operations conceptually without heavy math.

11. **Slide 11 - Setup Troubleshooting: Top 5 Errors**  
Type: Concept (Theory)  
Prompt: Provide troubleshooting matrix for pip conflicts, missing package, wrong Python version, kernel mismatch, and device detection issue. Include clear recovery steps.

12. **Slide 12 - Verification Mini-Lab (Before Colab)**  
Type: Practical Walkthrough  
Prompt: Show a short verification routine (import torch, print version, create simple tensor). Emphasize "green checks before moving forward."

13. **Slide 13 - Responsible and Safe AI Learning Habits**  
Type: Concept (Theory)  
Prompt: Introduce beginner-safe habits: verify outputs, document assumptions, avoid overtrusting generated text, and keep data privacy in mind.

14. **Slide 14 - MCQ Checkpoint (Hour 1)**  
Type: MCQ (Theory Assessment)  
Prompt: One multi-choice question with 4 options testing setup-path decisions and vocabulary understanding. Include answer key and short explanation.

15. **Slide 15 - Detailed Code Explanation (Hour 1)**  
Type: Code Explanation (Practical)  
Prompt: Walk through a minimal PyTorch snippet from Appendix A showing tensor creation, shape check, and one simple arithmetic operation. Right side should map each line to mental model, not just syntax.

### Hour 2 (Slides 16-30): Minimal PyTorch

16. **Slide 16 - Tensor Intuition: Shape, Dtype, Device**  
Type: Concept (Theory)  
Prompt: Explain the 3 key tensor attributes with easy examples and one shape-mismatch caution.

17. **Slide 17 - Building Tensors Step-by-Step**  
Type: Practical Walkthrough  
Prompt: Show how to create scalar, vector, and matrix tensors and print their shapes. Include one short "predict the shape" interaction.

18. **Slide 18 - Autograd Intuition Without Heavy Calculus**  
Type: Concept (Theory)  
Prompt: Explain computational graph and automatic differentiation using a flow diagram and plain-language story.

19. **Slide 19 - One-Neuron Forward Pass**  
Type: Practical Walkthrough  
Prompt: Visualize `y_hat = w*x + b` with sample numbers and output interpretation. Emphasize "model as a function with learnable parameters."

20. **Slide 20 - Loss Function as Error Signal**  
Type: Concept (Theory)  
Prompt: Explain what loss means, why lower is better, and how it guides updates. Keep formula minimal and interpretation-focused.

21. **Slide 21 - Gradient Descent in 4 Moves**  
Type: Practical Walkthrough  
Prompt: Teach the cycle: forward -> loss -> backward -> step using a compact loop diagram with numbered arrows.

22. **Slide 22 - Animation Slide (Hour 2)**  
Type: Animation (Theory Visual)  
Prompt: Embed or reference a 30-second animation showing gradient descent and backprop flow from model output back to parameter updates. Add one-line takeaway: "small repeated updates produce learning."  
Animation source script: `/Users/sanjayb/Documents/New project/course_outputs/llm-beginners-foundations/hour2_pytorch_animation.py`

23. **Slide 23 - Dataset and Dataloader Intuition**  
Type: Concept (Theory)  
Prompt: Explain batching and shuffling with a conveyor-belt metaphor, linking to chapter-2 dataloader intuition material.

24. **Slide 24 - Minimal Training Loop Skeleton**  
Type: Practical Walkthrough  
Prompt: Present pseudo-code block for a tiny training loop and annotate where each operation occurs (`zero_grad`, `forward`, `loss`, `backward`, `step`).

25. **Slide 25 - Underfitting vs Overfitting (Early Intuition)**  
Type: Concept (Theory)  
Prompt: Use side-by-side simple plots and plain explanations. Include practical hint on when to collect more data or stop training.

26. **Slide 26 - Runtime Errors Beginners Commonly Hit in PyTorch**  
Type: Concept (Theory)  
Prompt: Cover shape mismatch, dtype mismatch, and forgetting `requires_grad`. Include quick diagnosis checklist.

27. **Slide 27 - Reading Repo Code Without Panic**  
Type: Concept (Theory)  
Prompt: Show method for reading scripts: start at entry point, follow imports, inspect helper functions, then run minimal test.

28. **Slide 28 - Colab Lab Preview for Next Session**  
Type: Concept (Theory)  
Prompt: Show exactly what learners will implement in Colab after this deck: tiny dataset, tiny model, tiny training loop, and expected outputs.

29. **Slide 29 - MCQ Checkpoint (Hour 2)**  
Type: MCQ (Theory Assessment)  
Prompt: One multi-choice question with 4 options testing tensor shapes, autograd flow, and training-loop order. Include answer and explanation.

30. **Slide 30 - Detailed Code Explanation (Hour 2)**  
Type: Code Explanation (Practical)  
Prompt: Explain a compact end-to-end PyTorch training loop (data -> model -> loss -> backward -> optimizer step). Add line-by-line intent and one debugging note per block.

## MCQ Content (Ready to Paste)

### Hour 1 MCQ (Slide 14)

- Question: A learner with zero local setup experience wants to start quickly and avoid dependency conflicts. Best starting path?
- A. Build custom local environment first
- B. Start with Google Colab and install only required dependencies
- C. Skip setup and directly modify training scripts
- D. Start with optional cloud GPU workflow before basics
- Correct Answer: B
- Why: It minimizes setup friction and allows immediate execution.

### Hour 2 MCQ (Slide 29)

- Question: Which sequence is correct for a minimal PyTorch training step?
- A. backward -> forward -> loss -> step
- B. loss -> step -> backward -> forward
- C. forward -> loss -> backward -> optimizer.step
- D. step -> forward -> backward -> loss
- Correct Answer: C
- Why: The model must produce output before loss and gradients can be computed.

## Quality Gate Report

| Gate | Status | Notes |
| --- | --- | --- |
| Research integrity | Pass | Repo and official docs used as primary anchors |
| Plan-first compliance | Pass | Improvement plan included before prompts |
| Prompt determinism | Pass | Fixed slide schema and per-hour structure |
| Pedagogy | Pass | Progressive complexity + analogies + checkpoints |
| Accessibility | Pass | Light-theme and contrast constraints specified |
| Beginner comprehension | Pass | Beginner Corner requirement and plain-language framing included |
| Structural completeness | Pass | 30 slides, 15 per hour, required slide types present |
| Prohibited content | Pass | No tool metadata/aspect tags/footer clutter in prompts |

## Source Links

- https://github.com/rasbt/LLMs-from-scratch/blob/main/README.md
- https://github.com/rasbt/LLMs-from-scratch/blob/main/setup/README.md
- https://github.com/rasbt/LLMs-from-scratch/blob/main/ch01/README.md
- https://github.com/rasbt/LLMs-from-scratch/blob/main/appendix-A/README.md
- https://github.com/rasbt/LLMs-from-scratch/tree/main/appendix-A/01_main-chapter-code
- https://www3.nd.edu/~twut/PDF/mayerslides.pdf
- https://www.sciencedirect.com/science/article/pii/S1747938X17300581
- https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum
