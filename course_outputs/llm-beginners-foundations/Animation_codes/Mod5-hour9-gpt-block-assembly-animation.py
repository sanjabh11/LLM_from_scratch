from manim import *


class GPTBlockAssemblyAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Scene 1
        title = Text("Ch4: GPT Block Assembly", color=WHITE).scale(0.75).to_edge(UP)
        subtitle = Text("LayerNorm + Attention + FFN + Residual", color=TEAL).scale(0.4).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        # Scene 2: input embeddings
        inp = RoundedRectangle(width=4.6, height=0.58, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12)
        inp_lbl = Text("token + positional embeddings", color=WHITE).scale(0.33).move_to(inp)
        inp.shift(UP * 1.0)
        inp_lbl.move_to(inp)
        self.play(Create(inp), FadeIn(inp_lbl), run_time=1.8)
        self.wait(1.4)

        # Scene 3: first residual branch
        norm1 = RoundedRectangle(width=1.5, height=0.52, corner_radius=0.08, color=GREEN).set_fill(GREEN, opacity=0.14)
        attn = RoundedRectangle(width=1.5, height=0.52, corner_radius=0.08, color=YELLOW).set_fill(YELLOW, opacity=0.14)
        add1 = RoundedRectangle(width=1.0, height=0.52, corner_radius=0.08, color=TEAL).set_fill(TEAL, opacity=0.14)
        row1 = VGroup(norm1, attn, add1).arrange(RIGHT, buff=0.25).shift(UP * 0.1)
        r1_lbl = VGroup(
            Text("Norm", color=WHITE).scale(0.28).move_to(norm1),
            Text("Attention", color=WHITE).scale(0.28).move_to(attn),
            Text("+ Residual", color=WHITE).scale(0.24).move_to(add1),
        )
        arr1 = Arrow(inp.get_bottom(), row1[0].get_top(), buff=0.06, color=GREY_B)
        arr2 = Arrow(row1[0].get_right(), row1[1].get_left(), buff=0.05, color=GREY_B)
        arr3 = Arrow(row1[1].get_right(), row1[2].get_left(), buff=0.05, color=GREY_B)
        self.play(Create(arr1), FadeIn(row1), FadeIn(r1_lbl), run_time=2.3)
        self.play(Create(arr2), Create(arr3), run_time=1.3)
        self.wait(1.5)

        # Scene 4: second residual branch
        norm2 = RoundedRectangle(width=1.5, height=0.52, corner_radius=0.08, color=GREEN).set_fill(GREEN, opacity=0.14)
        ffn = RoundedRectangle(width=1.5, height=0.52, corner_radius=0.08, color=PURPLE).set_fill(PURPLE, opacity=0.14)
        add2 = RoundedRectangle(width=1.0, height=0.52, corner_radius=0.08, color=TEAL).set_fill(TEAL, opacity=0.14)
        row2 = VGroup(norm2, ffn, add2).arrange(RIGHT, buff=0.25).next_to(row1, DOWN, buff=0.8)
        r2_lbl = VGroup(
            Text("Norm", color=WHITE).scale(0.28).move_to(norm2),
            Text("FFN", color=WHITE).scale(0.31).move_to(ffn),
            Text("+ Residual", color=WHITE).scale(0.24).move_to(add2),
        )
        arr4 = Arrow(row1[2].get_bottom(), row2[0].get_top(), buff=0.06, color=GREY_B)
        arr5 = Arrow(row2[0].get_right(), row2[1].get_left(), buff=0.05, color=GREY_B)
        arr6 = Arrow(row2[1].get_right(), row2[2].get_left(), buff=0.05, color=GREY_B)
        self.play(Create(arr4), FadeIn(row2), FadeIn(r2_lbl), run_time=2.2)
        self.play(Create(arr5), Create(arr6), run_time=1.2)
        self.wait(1.5)

        # Scene 5: stacked blocks output
        stack = VGroup(
            RoundedRectangle(width=4.4, height=0.42, corner_radius=0.08, color=BLUE).set_fill(BLUE, opacity=0.10),
            RoundedRectangle(width=4.4, height=0.42, corner_radius=0.08, color=BLUE).set_fill(BLUE, opacity=0.10),
            RoundedRectangle(width=4.4, height=0.42, corner_radius=0.08, color=BLUE).set_fill(BLUE, opacity=0.10),
        ).arrange(DOWN, buff=0.1).to_edge(DOWN).shift(UP * 0.2)
        stack_lbl = Text("repeat block N times -> GPT backbone", color=YELLOW).scale(0.33).next_to(stack, UP, buff=0.12)
        arr7 = Arrow(row2[2].get_bottom(), stack.get_top(), buff=0.06, color=YELLOW)
        self.play(Create(arr7), FadeIn(stack), FadeIn(stack_lbl), run_time=2.5)
        self.play(Circumscribe(row1, color=TEAL, run_time=1.2))
        self.play(Circumscribe(row2, color=TEAL, run_time=1.2))
        self.wait(7.5)
