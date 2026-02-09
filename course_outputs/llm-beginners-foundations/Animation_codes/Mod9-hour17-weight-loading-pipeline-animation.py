from manim import *


class WeightLoadingPipelineAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Module 9: Weight Loading Pipeline", color=WHITE).scale(0.72).to_edge(UP)
        subtitle = Text("source -> adapter -> validation -> model", color=TEAL).scale(0.36).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        src = RoundedRectangle(width=2.1, height=0.72, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12)
        src_t = Text("checkpoint\n(TF/HF/ST)", color=WHITE).scale(0.25).move_to(src)
        adp = RoundedRectangle(width=2.0, height=0.72, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12)
        adp_t = Text("adapter", color=WHITE).scale(0.3).move_to(adp)
        val = RoundedRectangle(width=2.3, height=0.72, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.12)
        val_t = Text("shape checks", color=WHITE).scale(0.29).move_to(val)
        mdl = RoundedRectangle(width=2.3, height=0.72, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.12)
        mdl_t = Text("model assign", color=WHITE).scale(0.29).move_to(mdl)

        row = VGroup(src, adp, val, mdl).arrange(RIGHT, buff=0.35).shift(UP * 0.5)
        labels = VGroup(src_t, adp_t, val_t, mdl_t)
        arr = VGroup(*[Arrow(row[i].get_right(), row[i+1].get_left(), buff=0.06, color=GREY_B) for i in range(3)])

        self.play(FadeIn(row), FadeIn(labels), run_time=2.0)
        self.play(LaggedStart(*[Create(a) for a in arr], lag_ratio=0.12), run_time=1.6)
        self.wait(1.2)

        toks = VGroup(*[
            RoundedRectangle(width=0.8, height=0.5, corner_radius=0.08, color=TEAL).set_fill(TEAL, opacity=0.12).add(Text(str(v), color=WHITE).scale(0.23))
            for v in [15496, 11, 314, 716]
        ]).arrange(RIGHT, buff=0.08).to_edge(LEFT).shift(DOWN * 1.8)
        gen = RoundedRectangle(width=4.0, height=0.9, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12).to_edge(RIGHT).shift(DOWN * 1.8)
        gtxt = Text("sanity generation output", color=WHITE).scale(0.28).move_to(gen)
        flow = Arrow(toks.get_right(), gen.get_left(), buff=0.1, color=TEAL)
        self.play(LaggedStart(*[FadeIn(t, shift=UP*0.05) for t in toks], lag_ratio=0.1), run_time=1.7)
        self.play(Create(flow), FadeIn(gen), FadeIn(gtxt), run_time=1.6)

        check = VGroup(
            Text("config match", color=YELLOW).scale(0.24),
            Text("tokenizer match", color=YELLOW).scale(0.24),
            Text("shape match", color=YELLOW).scale(0.24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.08).next_to(row, DOWN, buff=0.45)
        self.play(FadeIn(check, shift=UP * 0.05), run_time=1.4)

        self.play(Circumscribe(val, color=YELLOW, run_time=1.0))
        self.play(Circumscribe(gen, color=GREEN, run_time=1.0))
        self.wait(14.1)
