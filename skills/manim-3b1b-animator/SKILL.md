---
name: manim-3b1b-animator
description: Create 3Blue1Brown-style mathematical animations in Manim Community Edition (v0.19+) with scene planning, narration scripting, and runnable Python code. Use when users ask for Manim CE animations, 3Blue1Brown visual style, math explainer videos, or 30-second GIF outputs rendered on Google Colab and downloadable.
---

# Manim 3B1B Animator

## Overview

Produce clean, dark-background Manim CE animations with smooth pacing, clear narration, and 3Blue1Brown-style visuals. Output is a 30-second GIF rendered on Google Colab and made downloadable. Follow a strict workflow: clarify, plan scenes, script narration, then deliver code and Colab rendering steps.

## Workflow

1. Understand and clarify. Analyze the topic and ask 1-3 focused questions if the request is ambiguous (scope, focus, audience, or math depth). Duration is fixed to 30 seconds for GIF output; if the user requests a different duration or format, confirm the constraint and proceed with 30 seconds unless explicitly overridden.
2. Plan the animation. Provide a numbered scene breakdown (4-10 scenes, 30-120 seconds total). For each scene, include visuals, animations, and a 1-2 sentence narration cue.
3. Narration script. Provide a full voiceover script with approximate timing cues in [mm:ss-mm:ss] format aligned to the scene plan.
4. Generate code. Only after plan approval or if the user explicitly skips planning. Output one complete, runnable Python script with `from manim import *`, a single `class <Topic>Animation(Scene):`, scene comments like `# Scene 1: ...`, and `self.wait(1-2)` between scenes. Ensure total runtime sums to ~30 seconds.
5. Rendering advice (Colab-only). Always include a Colab-ready setup, render to GIF, and download steps. Do not include local render commands.

If revising, incorporate user feedback into the plan first before updating code.

## Style Rules

- Background: set `self.camera.background_color = BLACK` or `"#0f0f0f"` as the first line in `construct`.
- Colors: use Manim palette with primary white/gray text and accents in `BLUE`, `TEAL`, `PURPLE`, `GREEN`. Avoid garish colors.
- Text/Equations: use `MathTex` for formulas (default font, size 48-60) and `Text` for words. Reveal text with `Write`.
- Animations: default to `rate_func=smooth` or `linear`. Prefer `Create`, `GrowFromCenter`, `FadeIn`, and `Transform`/`ReplacementTransform`. Use `Circumscribe` or `Indicate` for emphasis.
- Structure: favor `VGroup` for grouping, `SurroundingRect` or `BackgroundRectangle` for highlights, and `Arrow`/`Brace` for annotations. Use `always_redraw` or updaters for dynamic elements. Keep each key idea on screen for 2-8 seconds.

## Code Requirements

- Use Manim Community Edition APIs only. Never use ManimGL or `manimlib` imports.
- Avoid deprecated methods like `ShowCreation`.
- Keep code under 300 lines unless clearly required by complexity.
- Target total animation duration of 30 seconds (sum of `run_time` and `wait`).
- Ensure `MathTex` is used for LaTeX equations and is runnable with a standard LaTeX install.

## Colab Rendering (GIF, 30s)

Use a Colab cell with these steps, and adjust the output path if the quality preset changes:

```bash
!apt-get update -qq
!apt-get install -y texlive-latex-extra texlive-fonts-extra texlive-latex-recommended texlive-science dvisvgm
!pip -q install manim
```

```bash
!manim -qm --format=gif animation.py <SceneName>
```

```python
from google.colab import files
files.download("media/videos/animation/720p30/<SceneName>.gif")
```

If the output path differs, locate it with `!ls media/videos/animation` and update the download path.

## References

- See `references/examples.md` for concise code patterns in the 3Blue1Brown style.
