from manim import *


class SlidingWindowDataloaderAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Scene 1: Title
        title = Text("Ch2: Sliding Window + DataLoader", color=WHITE).scale(0.68).to_edge(UP)
        subtitle = Text("Build training examples from token streams", color=TEAL).scale(0.42).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.8)

        # Scene 2: Token stream
        stream_vals = ["12", "19", "4", "88", "41", "77", "3", "65"]
        stream = VGroup(
            *[
                RoundedRectangle(width=0.72, height=0.54, corner_radius=0.08, color=BLUE).set_fill(BLUE, opacity=0.12).add(
                    Text(v, color=WHITE).scale(0.28)
                )
                for v in stream_vals
            ]
        ).arrange(RIGHT, buff=0.12).shift(UP * 0.7)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.15) for b in stream], lag_ratio=0.1), run_time=2.2)
        self.wait(1.3)

        # Scene 3: Sliding context window
        frame = SurroundingRectangle(VGroup(*stream[0:4]), color=YELLOW, buff=0.05)
        lbl = Text("context length = 4", color=YELLOW).scale(0.3).next_to(frame, UP, buff=0.08)
        target = SurroundingRectangle(VGroup(*stream[1:5]), color=YELLOW, buff=0.05)
        self.play(Create(frame), FadeIn(lbl), run_time=1.4)
        self.play(Transform(frame, target), run_time=1.4)
        target2 = SurroundingRectangle(VGroup(*stream[2:6]), color=YELLOW, buff=0.05)
        self.play(Transform(frame, target2), run_time=1.4)
        self.wait(1.2)

        # Scene 4: Input-target pairs
        pair_title = Text("Create (input, target) pairs", color=GREEN).scale(0.34).to_edge(LEFT).shift(DOWN * 0.25)
        in_box = RoundedRectangle(width=3.3, height=0.62, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.1)
        out_box = RoundedRectangle(width=3.3, height=0.62, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.1)
        in_box.to_edge(RIGHT).shift(UP * 0.0)
        out_box.next_to(in_box, DOWN, buff=0.22)
        in_text = Text("input:  [12, 19, 4, 88]", color=WHITE).scale(0.32).move_to(in_box)
        out_text = Text("target: [19, 4, 88, 41]", color=WHITE).scale(0.32).move_to(out_box)
        self.play(Write(pair_title), Create(in_box), Create(out_box), FadeIn(in_text), FadeIn(out_text), run_time=2.3)
        self.wait(1.6)

        # Scene 5: Batch assembly
        batch_title = Text("DataLoader batches multiple pairs", color=WHITE).scale(0.34).to_edge(DOWN).shift(UP * 0.95)
        stack = VGroup(
            RoundedRectangle(width=3.35, height=0.55, corner_radius=0.08, color=GREEN).set_fill(GREEN, opacity=0.12),
            RoundedRectangle(width=3.35, height=0.55, corner_radius=0.08, color=GREEN).set_fill(GREEN, opacity=0.12),
            RoundedRectangle(width=3.35, height=0.55, corner_radius=0.08, color=GREEN).set_fill(GREEN, opacity=0.12),
        ).arrange(DOWN, buff=0.12).to_edge(DOWN).shift(UP * 0.18)
        batch_shape = Text("X, Y ∈ ℤ^(batch, seq)", color=YELLOW, font="Menlo").scale(0.45).next_to(stack, RIGHT, buff=0.35).shift(UP * 0.2)
        self.play(Write(batch_title), LaggedStart(*[FadeIn(s, shift=RIGHT * 0.2) for s in stack], lag_ratio=0.15), run_time=2.4)
        self.play(Write(batch_shape), run_time=1.3)
        self.play(Circumscribe(stack, color=GREEN, run_time=1.2))
        self.wait(7.7)
