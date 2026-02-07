# Manim 3B1B Style Examples

Use these examples as quick patterns for clean, smooth, dark-background scenes.

## Example 1: Simple Transform

```python
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        square = Square(color=BLUE, fill_opacity=0.5)
        circle = Circle(color=TEAL, fill_opacity=0.7)
        self.play(Create(square))
        self.wait(1)
        self.play(Transform(square, circle))
        self.wait(1)
        self.play(FadeOut(circle))
        self.wait(1)
```

## Example 2: Equation Reveal

```python
from manim import *

class Pythagoras(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        eq = MathTex("a^2 + b^2 = c^2", color=WHITE).scale(2)
        self.play(Write(eq))
        self.wait(1)
        box = SurroundingRect(eq, color=TEAL)
        self.play(Create(box))
        self.wait(1)
```

## Example 3: Dynamic Graph

```python
from manim import *
import numpy as np

class SineWave(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        axes = Axes(x_range=[-2 * PI, 2 * PI], y_range=[-1.5, 1.5])
        labels = axes.get_axis_labels(x_label="t", y_label="sin(t)")
        curve = always_redraw(lambda: axes.get_graph(lambda x: np.sin(x), color=BLUE))
        dot = Dot().move_to(axes.c2p(0, 0))
        self.add(axes, labels, curve, dot)
        self.play(dot.animate.move_to(axes.c2p(2 * PI, 0)), run_time=8, rate_func=linear)
        self.wait(1)
```
