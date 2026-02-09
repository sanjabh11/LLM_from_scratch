from manim import *
import numpy as np


class LLMFundamentalsPipeline(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Scene 1: What an LLM does
        title = Text("LLM Fundamentals", color=WHITE).scale(0.9).to_edge(UP)
        subtitle = Text("Predict the next token, repeatedly", color=TEAL).scale(0.48).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.5)

        # Scene 2: Text to tokens
        sentence = Text("The sky is", color=WHITE).scale(0.62).shift(UP * 1.0)
        token_text = ["The", "sky", "is"]
        token_boxes = VGroup(
            *[
                RoundedRectangle(width=1.2, height=0.65, corner_radius=0.12, color=BLUE).add(
                    Text(t, color=WHITE).scale(0.35)
                )
                for t in token_text
            ]
        ).arrange(RIGHT, buff=0.22).shift(DOWN * 0.2)
        self.play(Write(sentence), run_time=1.2)
        self.play(TransformFromCopy(sentence, token_boxes), run_time=2.2)
        self.wait(2)

        # Scene 3: Transformer block stack
        blocks = VGroup(
            *[
                RoundedRectangle(width=3.0, height=0.5, corner_radius=0.08, color=c).set_fill(c, opacity=0.12)
                for c in [PURPLE, GREEN, TEAL]
            ]
        ).arrange(DOWN, buff=0.14).to_edge(RIGHT).shift(UP * 0.2)
        labels = VGroup(
            Text("Self-Attention", color=WHITE).scale(0.3).move_to(blocks[0]),
            Text("FeedForward", color=WHITE).scale(0.3).move_to(blocks[1]),
            Text("LayerNorm + Residual", color=WHITE).scale(0.3).move_to(blocks[2]),
        )
        arrow_in = Arrow(token_boxes.get_right(), blocks[0].get_left(), buff=0.12, color=WHITE)
        self.play(Create(arrow_in), FadeIn(blocks), FadeIn(labels), run_time=2.6)
        self.wait(2)

        # Scene 4: Next-token probabilities
        prob_title = Text("Next-token probabilities", color=YELLOW).scale(0.4).to_edge(LEFT).shift(DOWN * 0.5)
        
        # Custom bar chart to avoid LaTeX dependency
        bar_data = [("blue", 0.55, TEAL), ("rainy", 0.26, BLUE), ("cloudy", 0.12, GREEN), ("clear", 0.07, PURPLE)]
        bar_group = VGroup()
        bar_labels = VGroup()
        max_height = 2.0
        bar_width = 0.8
        
        for i, (name, value, color) in enumerate(bar_data):
            bar = Rectangle(width=bar_width, height=value * max_height / 0.6, color=color)
            bar.set_fill(color, opacity=0.7)
            bar.move_to(LEFT * 1.5 + RIGHT * i * 1.1 + DOWN * 1.2)
            bar.align_to(ORIGIN + DOWN * 2.2, DOWN)
            
            label = Text(name, color=WHITE).scale(0.28).next_to(bar, DOWN, buff=0.1)
            bar_group.add(bar)
            bar_labels.add(label)
        
        bars_with_labels = VGroup(bar_group, bar_labels).scale(0.52).next_to(prob_title, DOWN, buff=0.15)
        sample_note = Text("Sample or pick highest -> blue", color=WHITE).scale(0.34).next_to(bars_with_labels, DOWN, buff=0.2)
        self.play(Write(prob_title), Create(bars_with_labels), run_time=3.2)
        self.play(FadeIn(sample_note, shift=UP * 0.2), run_time=1.1)
        self.wait(2)

        # Scene 5: Autoregressive loop
        generated = Text("The sky is blue", color=WHITE).scale(0.58).to_edge(DOWN)
        loop_arrow = CurvedArrow(
            generated.get_right() + RIGHT * 0.25,
            token_boxes.get_left() + LEFT * 0.1,
            angle=1.4,
            color=GREEN,
        )
        loop_text = Text("Repeat until stop token", color=GREEN).scale(0.34).next_to(loop_arrow, UP, buff=0.05)
        self.play(Write(generated), run_time=1.3)
        self.play(Create(loop_arrow), FadeIn(loop_text), run_time=1.7)
        self.play(Circumscribe(token_boxes, color=TEAL, run_time=1.6))
        self.wait(4.5)
