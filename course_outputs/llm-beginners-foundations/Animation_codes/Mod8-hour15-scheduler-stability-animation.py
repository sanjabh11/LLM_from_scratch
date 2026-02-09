from manim import *
import numpy as np


class SchedulerStabilityAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Module 8: Scheduler + Stability", color=WHITE).scale(0.74).to_edge(UP)
        subtitle = Text("warmup -> cosine decay -> gradient clipping", color=TEAL).scale(0.36).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        axes = Axes(
            x_range=[0, 100, 20],
            y_range=[0, 1.1, 0.2],
            x_length=5.6,
            y_length=2.7,
            axis_config={"color": GREY_B},
        ).shift(UP * 0.5)
        xlab = Text("training steps", color=WHITE).scale(0.24).next_to(axes.x_axis, DOWN)
        ylab = Text("learning rate", color=WHITE).scale(0.24).rotate(PI / 2).next_to(axes.y_axis, LEFT)
        self.play(Create(axes), FadeIn(xlab), FadeIn(ylab), run_time=2.0)

        warm = axes.plot(lambda x: 0.8 * (x / 20), x_range=[0, 20], color=YELLOW)
        decay = axes.plot(lambda x: 0.05 + 0.75 * 0.5 * (1 + np.cos(np.pi * (x - 20) / 80)), x_range=[20, 100], color=GREEN)
        self.play(Create(warm), run_time=1.2)
        self.play(Create(decay), run_time=1.6)

        wtxt = Text("linear warmup", color=YELLOW).scale(0.25).next_to(warm, UP, buff=0.1)
        ctxt = Text("cosine decay", color=GREEN).scale(0.25).next_to(decay, UP, buff=0.1).shift(RIGHT * 0.2)
        self.play(FadeIn(wtxt), FadeIn(ctxt), run_time=1.0)
        self.wait(1.2)

        g_axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 2.2, 0.5],
            x_length=4.8,
            y_length=2.2,
            axis_config={"color": GREY_B},
        ).to_edge(DOWN).shift(UP * 0.2)
        g_curve = g_axes.plot(lambda x: 0.5 + 0.12 * x if x < 8 else 2.0, x_range=[0, 10], color=BLUE)
        clip_line = DashedLine(g_axes.c2p(0, 1.0), g_axes.c2p(10, 1.0), color=RED)
        clip_lbl = Text("clip max_norm=1.0", color=RED).scale(0.24).next_to(clip_line, UP, buff=0.08)
        self.play(Create(g_axes), Create(g_curve), run_time=1.8)
        self.play(Create(clip_line), FadeIn(clip_lbl), run_time=1.2)

        spike = Dot(g_axes.c2p(9.1, 2.0), color=ORANGE)
        arrow = Arrow(spike.get_top() + UP * 0.1, g_axes.c2p(9.1, 1.0), buff=0.05, color=RED)
        self.play(FadeIn(spike), Create(arrow), run_time=1.1)

        stable = Text("Result: smoother loss trajectory", color=TEAL).scale(0.3).to_edge(RIGHT).shift(DOWN * 0.5)
        self.play(FadeIn(stable, shift=LEFT * 0.1), run_time=1.0)

        self.play(Circumscribe(warm, color=YELLOW, run_time=1.0))
        self.play(Circumscribe(clip_line, color=RED, run_time=1.0))
        self.wait(11.5)
