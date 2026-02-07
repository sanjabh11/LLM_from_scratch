from manim import *
import numpy as np

class FourierSeriesAnimation(Scene):
    def construct(self):
        # Scene 1: Title + Setup
        self.camera.background_color = BLACK
        title = Text("Fourier Series: Sine/Cosine Basis", color=WHITE).scale(0.7)
        underline = Line(LEFT * 5, RIGHT * 5, color=GRAY_B).next_to(title, DOWN, buff=0.3)
        self.play(Write(title), run_time=2, rate_func=smooth)
        self.play(Create(underline), run_time=1.5, rate_func=smooth)
        self.wait(1)

        axes = Axes(
            x_range=[-PI, PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": GRAY_A},
        ).scale(0.9).to_edge(DOWN, buff=0.8)
        self.play(Create(axes), run_time=1.5, rate_func=smooth)
        self.wait(1)

        self.play(FadeOut(title), FadeOut(underline), run_time=1.0, rate_func=smooth)

        # Scene 2: Basis Sine Waves
        sine_colors = [BLUE, TEAL, GREEN]
        sine_labels = ["sin(x)", "sin(2x)", "sin(3x)"]
        sine_waves = VGroup()
        sine_texts = VGroup()

        for i, n in enumerate([1, 2, 3]):
            graph = axes.get_graph(lambda x, k=n: np.sin(k * x), color=sine_colors[i])
            graph.shift(UP * (1.2 - 1.0 * i))
            label = MathTex(sine_labels[i], color=sine_colors[i]).scale(0.6)
            label.next_to(graph, RIGHT, buff=0.4)
            sine_waves.add(graph)
            sine_texts.add(label)

        for graph, label in zip(sine_waves, sine_texts):
            self.play(Create(graph), FadeIn(label), run_time=1.5, rate_func=smooth)
        self.wait(1)

        # Scene 3: Cosine Partners
        cosine_labels = ["cos(x)", "cos(2x)"]
        cosine_waves = VGroup()
        cosine_texts = VGroup()

        for i, n in enumerate([1, 2]):
            graph = axes.get_graph(lambda x, k=n: np.cos(k * x), color=PURPLE)
            graph.shift(UP * (1.2 - 1.0 * i))
            label = MathTex(cosine_labels[i], color=PURPLE).scale(0.6)
            label.next_to(graph, RIGHT, buff=0.4)
            cosine_waves.add(graph)
            cosine_texts.add(label)

        self.play(
            ReplacementTransform(sine_waves[0], cosine_waves[0]),
            ReplacementTransform(sine_texts[0], cosine_texts[0]),
            run_time=2,
            rate_func=smooth,
        )
        self.play(
            ReplacementTransform(sine_waves[1], cosine_waves[1]),
            ReplacementTransform(sine_texts[1], cosine_texts[1]),
            run_time=2,
            rate_func=smooth,
        )
        self.wait(1)

        # Scene 4: Projection Intuition
        target = axes.get_graph(lambda x: 0.8 * np.exp(-2 * x**2), color=WHITE)
        basis = axes.get_graph(lambda x: np.sin(x), color=BLUE)
        overlap_label = Text("coefficient = overlap", color=GRAY_A).scale(0.5)
        overlap_label.next_to(axes, UP, buff=0.3)

        self.play(FadeIn(target), run_time=1.5, rate_func=smooth)
        self.play(Create(basis), run_time=1.5, rate_func=smooth)
        self.play(Write(overlap_label), run_time=1.2, rate_func=smooth)
        self.play(Circumscribe(overlap_label, color=TEAL), run_time=1.2)
        self.wait(1)

        # Scene 5: Build the Approximation
        approx1 = axes.get_graph(lambda x: 0.6 * np.sin(x), color=WHITE)
        approx3 = axes.get_graph(lambda x: 0.6 * np.sin(x) + 0.3 * np.sin(3 * x), color=WHITE)
        approx5 = axes.get_graph(
            lambda x: 0.6 * np.sin(x) + 0.3 * np.sin(3 * x) + 0.2 * np.sin(5 * x),
            color=WHITE,
        )
        terms_text = Text("1 term → 3 terms → 5 terms", color=GRAY_B).scale(0.45)
        terms_text.to_edge(UP, buff=0.5)

        target_faint = target.copy().set_color(GRAY_D)

        self.play(FadeOut(basis), FadeOut(overlap_label), run_time=1.0, rate_func=smooth)
        self.play(Transform(target, target_faint), run_time=1.0, rate_func=smooth)
        self.play(FadeIn(terms_text), run_time=1.0, rate_func=smooth)

        self.play(Create(approx1), run_time=1.5, rate_func=smooth)
        self.play(Transform(approx1, approx3), run_time=1.5, rate_func=smooth)
        self.play(Transform(approx1, approx5), run_time=1.5, rate_func=smooth)
        self.wait(1)

        # Scene 6: Wrap-up
        summary = Text("Fourier series = coordinates in wave space", color=WHITE).scale(0.55)
        summary.to_edge(DOWN, buff=0.3)

        self.play(FadeIn(summary), run_time=1.5, rate_func=smooth)
        self.play(Indicate(approx1, color=TEAL), run_time=1.2)
        self.wait(2)
