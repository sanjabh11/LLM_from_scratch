from manim import *


class VariantFamilySwapAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Module 9: Variant Family Swap", color=WHITE).scale(0.72).to_edge(UP)
        subtitle = Text("Llama / Qwen / Gemma / Olmo under shared workflow", color=TEAL).scale(0.34).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        core = RoundedRectangle(width=3.0, height=1.0, corner_radius=0.12, color=BLUE).set_fill(BLUE, opacity=0.12).shift(UP * 0.2)
        ctext = Text("Shared Pipeline\n(tokenize -> forward -> generate)", color=WHITE).scale(0.26).move_to(core)
        self.play(FadeIn(core), FadeIn(ctext), run_time=1.8)

        fam_names = ["Llama", "Qwen", "Gemma", "Olmo"]
        colors = [GREEN, YELLOW, ORANGE, PURPLE]
        fam_boxes = VGroup(*[
            RoundedRectangle(width=1.6, height=0.6, corner_radius=0.1, color=colors[i]).set_fill(colors[i], opacity=0.12)
            for i in range(4)
        ]).arrange(RIGHT, buff=0.25).to_edge(DOWN).shift(UP * 0.7)
        fam_labels = VGroup(*[Text(fam_names[i], color=WHITE).scale(0.27).move_to(fam_boxes[i]) for i in range(4)])

        links = VGroup(*[Arrow(core.get_bottom(), fam_boxes[i].get_top(), buff=0.08, color=GREY_B) for i in range(4)])
        self.play(FadeIn(fam_boxes), FadeIn(fam_labels), run_time=1.8)
        self.play(LaggedStart(*[Create(l) for l in links], lag_ratio=0.12), run_time=1.6)

        meters = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            x_length=4.5,
            y_length=2.5,
            axis_config={"color": GREY_B},
        ).to_edge(RIGHT).shift(UP * 0.5)
        m_lbl = Text("quality / speed / memory", color=WHITE).scale(0.24).next_to(meters, UP, buff=0.08)
        self.play(Create(meters), FadeIn(m_lbl), run_time=1.4)

        dots = VGroup(
            Dot(meters.c2p(6.0, 6.5), color=GREEN),
            Dot(meters.c2p(7.2, 5.8), color=YELLOW),
            Dot(meters.c2p(5.6, 6.0), color=ORANGE),
            Dot(meters.c2p(6.8, 5.2), color=PURPLE),
        )
        self.play(LaggedStart(*[FadeIn(d, scale=0.7) for d in dots], lag_ratio=0.1), run_time=1.4)

        decision = RoundedRectangle(width=6.8, height=0.7, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.12).to_edge(DOWN)
        dtext = Text("Select family by constraints, then validate with shared smoke suite", color=WHITE).scale(0.27).move_to(decision)
        self.play(FadeIn(decision), FadeIn(dtext), run_time=1.5)

        self.play(Circumscribe(fam_boxes[1], color=YELLOW, run_time=1.0))
        self.play(Circumscribe(fam_boxes[0], color=GREEN, run_time=1.0))
        self.wait(14.1)
