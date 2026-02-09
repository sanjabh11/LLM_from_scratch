from manim import *
import numpy as np


class SelfAttentionIntuition(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Scene 1: Title
        title = Text("Self-Attention Intuition", color=WHITE).scale(0.82).to_edge(UP)
        subtitle = Text("Which earlier words matter most?", color=TEAL).scale(0.45).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.1)
        self.wait(1.5)

        # Scene 2: Token row
        words = ["The", "robot", "sees", "it"]
        token_row = VGroup(
            *[
                RoundedRectangle(width=1.0, height=0.58, corner_radius=0.1, color=BLUE).add(
                    Text(w, color=WHITE).scale(0.32)
                )
                for w in words
            ]
        ).arrange(RIGHT, buff=0.2).shift(UP * 0.8)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.2) for t in token_row], lag_ratio=0.16), run_time=2.4)
        self.wait(2)

        # Scene 3: Query/Key/Value view
        q = Text("Q", color=YELLOW).scale(0.58).next_to(token_row[3], DOWN, buff=0.35)
        k = Text("K", color=GREEN).scale(0.58).next_to(token_row[1], DOWN, buff=0.35)
        v = Text("V", color=TEAL).scale(0.58).next_to(token_row[1], DOWN, buff=0.9)
        q_arrow = Arrow(q.get_top(), token_row[3].get_bottom(), buff=0.05, color=YELLOW)
        k_arrow = Arrow(k.get_top(), token_row[1].get_bottom(), buff=0.05, color=GREEN)
        v_arrow = Arrow(v.get_top(), token_row[1].get_bottom(), buff=0.05, color=TEAL)
        self.play(FadeIn(q), FadeIn(k), FadeIn(v), Create(q_arrow), Create(k_arrow), Create(v_arrow), run_time=2.6)
        self.wait(2)

        # Scene 4: Attention scores heatmap
        heatmap = VGroup(
            *[
                Square(side_length=0.42, color=GREY_B).set_fill(
                    color=BLUE if r == c else TEAL,
                    opacity=0.25 + 0.15 * ((r + c) % 2),
                )
                for r in range(4)
                for c in range(4)
            ]
        ).arrange_in_grid(rows=4, cols=4, buff=0.05).to_edge(LEFT).shift(DOWN * 0.6)
        hm_label = Text("Attention score matrix", color=WHITE).scale(0.32).next_to(heatmap, UP, buff=0.12)
        mask_line = DashedLine(
            heatmap.get_corner(UL) + RIGHT * 0.88 + DOWN * 0.05,
            heatmap.get_corner(DR) + LEFT * 0.05 + UP * 0.88,
            color=PURPLE,
        )
        mask_text = Text("Causal mask: no future tokens", color=PURPLE).scale(0.28).next_to(heatmap, DOWN, buff=0.12)
        self.play(Create(heatmap), FadeIn(hm_label), run_time=2.8)
        self.play(Create(mask_line), FadeIn(mask_text), run_time=1.6)
        self.wait(2)

        # Scene 5: Weighted sum and output
        formula = Text("output = Σᵢ αᵢ·Vᵢ", color=WHITE, font="Menlo").scale(0.7).to_edge(RIGHT).shift(DOWN * 0.35)
        alpha_note = Text("Higher score -> stronger influence", color=GREEN).scale(0.32).next_to(formula, DOWN, buff=0.2)
        out_text = Text("Context-aware representation", color=YELLOW).scale(0.4).next_to(formula, UP, buff=0.2)
        self.play(Write(formula), FadeIn(out_text, shift=UP * 0.2), run_time=2.7)
        self.play(FadeIn(alpha_note, shift=UP * 0.2), run_time=1.2)
        self.play(Circumscribe(token_row[3], color=YELLOW, run_time=1.6))
        self.wait(5)
