from manim import *


class Ch7InstructionSFTFlowAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Module 11: Instruction SFT Flow", color=WHITE).scale(0.7).to_edge(UP)
        subtitle = Text("json -> format -> collate -> train -> responses", color=TEAL).scale(0.34).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        boxes = VGroup(
            RoundedRectangle(width=1.65, height=0.62, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12),
            RoundedRectangle(width=1.65, height=0.62, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12),
            RoundedRectangle(width=1.65, height=0.62, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.12),
            RoundedRectangle(width=1.65, height=0.62, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.12),
            RoundedRectangle(width=1.65, height=0.62, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.12),
        ).arrange(RIGHT, buff=0.22).shift(UP * 0.45)
        labels = VGroup(
            Text("JSON", color=WHITE).scale(0.3).move_to(boxes[0]),
            Text("Format", color=WHITE).scale(0.3).move_to(boxes[1]),
            Text("Collate", color=WHITE).scale(0.3).move_to(boxes[2]),
            Text("Train", color=WHITE).scale(0.3).move_to(boxes[3]),
            Text("Generate", color=WHITE).scale(0.28).move_to(boxes[4]),
        )
        arrows = VGroup(*[Arrow(boxes[i].get_right(), boxes[i + 1].get_left(), buff=0.05, color=GREY_B) for i in range(4)])
        self.play(FadeIn(boxes), FadeIn(labels), run_time=1.9)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.1), run_time=1.5)

        prompt = RoundedRectangle(width=4.7, height=0.74, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.10).to_edge(LEFT).shift(DOWN * 1.5)
        ptxt = Text("### Instruction ... ### Input ... ### Response ...", color=WHITE).scale(0.24).move_to(prompt)
        self.play(FadeIn(prompt), FadeIn(ptxt), run_time=1.3)

        mask_panel = RoundedRectangle(width=3.7, height=0.9, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.10).next_to(prompt, RIGHT, buff=0.3)
        mtxt = Text("targets: pad -> -100\n(ignore extra pad tokens)", color=WHITE).scale(0.25).move_to(mask_panel)
        self.play(FadeIn(mask_panel), FadeIn(mtxt), run_time=1.4)

        loss_axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0.5, 4.0, 0.5],
            x_length=4.2,
            y_length=2.1,
            axis_config={"color": GREY_B},
        ).to_edge(RIGHT).shift(DOWN * 1.0)
        tr = loss_axes.plot(lambda x: 3.5 / (x + 1) + 0.5, x_range=[0, 10], color=GREEN)
        vl = loss_axes.plot(lambda x: 3.2 / (x + 1) + 0.7, x_range=[0, 10], color=YELLOW)
        ltxt = Text("train/val loss", color=WHITE).scale(0.24).next_to(loss_axes, UP, buff=0.07)
        self.play(Create(loss_axes), Create(tr), Create(vl), FadeIn(ltxt), run_time=2.0)

        out = RoundedRectangle(width=3.9, height=0.68, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.12).to_edge(DOWN)
        otxt = Text("instruction-data-with-response.json", color=WHITE).scale(0.25).move_to(out)
        self.play(FadeIn(out), FadeIn(otxt), run_time=1.2)

        self.play(Circumscribe(boxes[2], color=YELLOW, run_time=1.0))
        self.play(Circumscribe(out, color=TEAL, run_time=1.0))
        self.wait(14.3)
