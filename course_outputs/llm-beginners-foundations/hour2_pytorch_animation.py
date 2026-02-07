from manim import *
import numpy as np


class GradientDescentIntuitionAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Scene 1: Title and objective
        title = Text("Minimal PyTorch Intuition", color=WHITE).scale(0.8).to_edge(UP)
        subtitle = Text("Forward Pass -> Loss -> Backward -> Update", color=TEAL).scale(0.45).next_to(title, DOWN)
        self.play(Write(title), run_time=1.8)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.2)
        self.wait(1)

        # Scene 2: One neuron as a formula
        eq = MathTex(r"\hat{y} = w x + b", color=WHITE).scale(1.1).next_to(subtitle, DOWN, buff=0.6)
        note = Text("A model is a parameterized function", color=GREEN).scale(0.36).next_to(eq, DOWN)
        self.play(Write(eq), run_time=1.8)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=1)
        self.wait(1)

        # Scene 3: Loss landscape with descent
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[0, 4, 1],
            x_length=5,
            y_length=2.7,
            axis_config={"color": GREY_B},
        ).to_edge(LEFT).shift(DOWN * 0.6)
        curve = axes.plot(lambda x: 0.7 * (x + 0.8) ** 2 + 0.2, color=BLUE)
        dot = Dot(color=YELLOW).move_to(axes.c2p(1.5, 0.7 * (1.5 + 0.8) ** 2 + 0.2))
        loss_label = Text("Loss", color=WHITE).scale(0.35).next_to(axes, UP, buff=0.1)
        self.play(Create(axes), Create(curve), FadeIn(dot), FadeIn(loss_label), run_time=2.2)
        target = axes.c2p(-0.8, 0.2)
        self.play(dot.animate.move_to(target), run_time=2.0, rate_func=smooth)
        self.wait(1)

        # Scene 4: Computational flow and backprop
        x_box = RoundedRectangle(width=1.1, height=0.55, corner_radius=0.12, color=BLUE).set_fill(BLUE, opacity=0.15)
        f_box = RoundedRectangle(width=1.6, height=0.55, corner_radius=0.12, color=TEAL).set_fill(TEAL, opacity=0.15)
        l_box = RoundedRectangle(width=1.2, height=0.55, corner_radius=0.12, color=GREEN).set_fill(GREEN, opacity=0.15)
        flow = VGroup(x_box, f_box, l_box).arrange(RIGHT, buff=0.35).to_edge(RIGHT).shift(DOWN * 0.25)
        labels = VGroup(
            Text("x", color=WHITE).scale(0.42).move_to(x_box),
            Text("model(w,b)", color=WHITE).scale(0.32).move_to(f_box),
            Text("loss", color=WHITE).scale(0.38).move_to(l_box),
        )
        fwd1 = Arrow(x_box.get_right(), f_box.get_left(), buff=0.08, color=WHITE)
        fwd2 = Arrow(f_box.get_right(), l_box.get_left(), buff=0.08, color=WHITE)
        bwd = Arrow(l_box.get_bottom(), x_box.get_bottom(), buff=0.2, color=PURPLE).shift(DOWN * 0.22)
        bwd_label = Text("backward gradients", color=PURPLE).scale(0.28).next_to(bwd, DOWN, buff=0.08)
        self.play(FadeIn(flow), FadeIn(labels), Create(fwd1), Create(fwd2), run_time=2)
        self.play(Create(bwd), FadeIn(bwd_label), run_time=1.5)
        self.wait(1)

        # Scene 5: Training loop mnemonic
        loop = VGroup(
            Text("1. forward()", color=WHITE).scale(0.4),
            Text("2. loss()", color=WHITE).scale(0.4),
            Text("3. backward()", color=WHITE).scale(0.4),
            Text("4. optimizer.step()", color=WHITE).scale(0.4),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_edge(DOWN)
        brace = Brace(loop, LEFT, color=TEAL)
        mantra = Text("Repeat many small updates", color=YELLOW).scale(0.42).next_to(loop, RIGHT, buff=0.35)
        self.play(FadeIn(loop, shift=UP * 0.2), GrowFromCenter(brace), run_time=2)
        self.play(Write(mantra), run_time=1.2)
        self.wait(2)

