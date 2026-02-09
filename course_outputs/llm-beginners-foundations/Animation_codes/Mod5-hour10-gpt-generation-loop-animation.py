from manim import *


class GPTGenerationLoopAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Scene 1
        title = Text("Ch4: GPT Generation Loop", color=WHITE).scale(0.74).to_edge(UP)
        subtitle = Text("forward -> logits -> next token -> append", color=TEAL).scale(0.4).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        # Scene 2: context window crop
        seq = VGroup(
            *[
                RoundedRectangle(width=0.74, height=0.52, corner_radius=0.08, color=BLUE).set_fill(BLUE, opacity=0.12).add(
                    Text(str(v), color=WHITE).scale(0.24)
                )
                for v in [15496, 11, 314, 716, 27018, 24086]
            ]
        ).arrange(RIGHT, buff=0.1).shift(UP * 0.9)
        window = SurroundingRectangle(VGroup(*seq[-4:]), color=YELLOW, buff=0.05)
        note = Text("idx_cond = idx[:, -context_size:]", color=YELLOW).scale(0.32).next_to(window, UP, buff=0.1)
        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.1) for s in seq], lag_ratio=0.08), run_time=2.0)
        self.play(Create(window), FadeIn(note), run_time=1.6)
        self.wait(1.4)

        # Scene 3: model forward and logits (custom bars to avoid LaTeX)
        model_box = RoundedRectangle(width=2.4, height=1.0, corner_radius=0.12, color=GREEN).set_fill(GREEN, opacity=0.12).shift(DOWN * 0.1)
        model_lbl = Text("GPTModel", color=WHITE).scale(0.35).move_to(model_box)
        
        # Custom bar chart
        bar_data = [("tokA", 0.15, TEAL), ("tokB", 0.52, YELLOW), ("tokC", 0.2, BLUE), ("tokD", 0.13, PURPLE)]
        logits = VGroup()
        bar_labels = VGroup()
        for i, (name, val, col) in enumerate(bar_data):
            bar = Rectangle(width=0.5, height=val * 2.8, color=col).set_fill(col, opacity=0.7)
            bar.move_to(RIGHT * (i * 0.65 - 0.9) + DOWN * 0.15)
            bar.align_to(DOWN * 1.0, DOWN)
            label = Text(name, color=WHITE).scale(0.2).next_to(bar, DOWN, buff=0.05)
            logits.add(bar)
            bar_labels.add(label)
        logits_group = VGroup(logits, bar_labels).to_edge(RIGHT).shift(DOWN * 0.15)
        logits_lbl = Text("last-step logits -> probabilities", color=WHITE).scale(0.30).next_to(logits_group, UP, buff=0.1)
        arr1 = Arrow(window.get_bottom(), model_box.get_top(), buff=0.08, color=GREY_B)
        arr2 = Arrow(model_box.get_right(), logits_group.get_left(), buff=0.1, color=GREY_B)
        self.play(Create(arr1), Create(model_box), FadeIn(model_lbl), run_time=2.0)
        self.play(Create(arr2), Create(logits_group), FadeIn(logits_lbl), run_time=2.2)
        self.wait(1.4)

        # Scene 4: argmax and append
        pick = Text("argmax -> tokB", color=YELLOW).scale(0.33).next_to(logits, DOWN, buff=0.12)
        new_tok = RoundedRectangle(width=0.74, height=0.52, corner_radius=0.08, color=YELLOW).set_fill(YELLOW, opacity=0.2).add(
            Text("tokB", color=WHITE).scale(0.24)
        ).next_to(seq, RIGHT, buff=0.1)
        self.play(FadeIn(pick, shift=UP * 0.12), run_time=1.0)
        self.play(FadeIn(new_tok, shift=RIGHT * 0.15), run_time=1.4)
        self.wait(1.3)

        # Scene 5: loop repeat
        loop = CurvedArrow(new_tok.get_bottom() + DOWN * 0.1, window.get_bottom() + DOWN * 0.1, angle=-1.4, color=PURPLE)
        loop_lbl = Text("repeat for max_new_tokens", color=PURPLE).scale(0.31).next_to(loop, DOWN, buff=0.08)
        self.play(Create(loop), FadeIn(loop_lbl), run_time=2.0)
        self.play(Circumscribe(model_box, color=GREEN, run_time=1.2))
        self.wait(8.1)
