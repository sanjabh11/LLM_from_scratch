from manim import *


class MultiHeadCausalMaskAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Scene 1
        title = Text("Ch3 Multi-Head + Causal Mask", color=WHITE).scale(0.68).to_edge(UP)
        subtitle = Text("parallel heads with no future-token leakage", color=TEAL).scale(0.4).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.7)

        # Scene 2: split into heads
        vec = RoundedRectangle(width=4.2, height=0.62, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12)
        vec_lbl = Text("input embedding stream", color=WHITE).scale(0.33).move_to(vec)
        heads = VGroup(
            RoundedRectangle(width=1.25, height=0.55, corner_radius=0.08, color=GREEN).set_fill(GREEN, opacity=0.15),
            RoundedRectangle(width=1.25, height=0.55, corner_radius=0.08, color=GREEN).set_fill(GREEN, opacity=0.15),
            RoundedRectangle(width=1.25, height=0.55, corner_radius=0.08, color=GREEN).set_fill(GREEN, opacity=0.15),
        ).arrange(RIGHT, buff=0.2).next_to(vec, DOWN, buff=0.75)
        htxt = VGroup(*[Text(f"head {i+1}", color=WHITE).scale(0.28).move_to(heads[i]) for i in range(3)])
        arrows = VGroup(*[Arrow(vec.get_bottom() + LEFT * (1.4 - i * 1.4), heads[i].get_top(), buff=0.06, color=GREY_B) for i in range(3)])
        self.play(Create(vec), FadeIn(vec_lbl), run_time=1.8)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.15), FadeIn(heads), FadeIn(htxt), run_time=2.5)
        self.wait(1.5)

        # Scene 3: mask
        mask = VGroup(
            *[
                Square(side_length=0.38, color=GREY_B).set_fill(
                    GREEN if c <= r else RED,
                    opacity=0.28,
                )
                for r in range(4)
                for c in range(4)
            ]
        ).arrange_in_grid(rows=4, cols=4, buff=0.04).to_edge(LEFT).shift(DOWN * 0.55)
        mask_lbl = Text("causal mask", color=WHITE).scale(0.3).next_to(mask, UP, buff=0.1)
        no_future = Text("red cells blocked (future)", color=RED).scale(0.28).next_to(mask, DOWN, buff=0.1)
        self.play(Create(mask), FadeIn(mask_lbl), run_time=2.4)
        self.play(FadeIn(no_future, shift=UP * 0.12), run_time=1.0)
        self.wait(1.7)

        # Scene 4: parallel attention outputs
        outs = VGroup(
            RoundedRectangle(width=1.25, height=0.5, corner_radius=0.08, color=YELLOW).set_fill(YELLOW, opacity=0.16),
            RoundedRectangle(width=1.25, height=0.5, corner_radius=0.08, color=YELLOW).set_fill(YELLOW, opacity=0.16),
            RoundedRectangle(width=1.25, height=0.5, corner_radius=0.08, color=YELLOW).set_fill(YELLOW, opacity=0.16),
        ).arrange(RIGHT, buff=0.2).next_to(heads, DOWN, buff=0.6)
        olbl = VGroup(*[Text("attn out", color=WHITE).scale(0.26).move_to(outs[i]) for i in range(3)])
        arr2 = VGroup(*[Arrow(heads[i].get_bottom(), outs[i].get_top(), buff=0.05, color=YELLOW) for i in range(3)])
        self.play(LaggedStart(*[Create(a) for a in arr2], lag_ratio=0.15), FadeIn(outs), FadeIn(olbl), run_time=2.3)
        self.wait(1.5)

        # Scene 5: concat + projection
        concat = RoundedRectangle(width=4.3, height=0.58, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.14).to_edge(DOWN).shift(UP * 0.45)
        clbl = Text("concatenate heads -> output projection", color=WHITE).scale(0.32).move_to(concat)
        carr = Arrow(outs.get_bottom(), concat.get_top(), buff=0.08, color=PURPLE)
        self.play(Create(carr), Create(concat), FadeIn(clbl), run_time=2.1)
        self.play(Circumscribe(mask, color=RED, run_time=1.2))
        self.wait(7.5)
