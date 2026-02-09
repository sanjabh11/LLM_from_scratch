from manim import *


class DatasetGenerationLoopAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Add-On B: Dataset Generation Loop", color=WHITE).scale(0.7).to_edge(UP)
        subtitle = Text("seed prompts -> synthetic samples -> reflection -> quality gate", color=TEAL).scale(0.33).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        seed = RoundedRectangle(width=2.3, height=0.72, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12).shift(LEFT * 4.0 + UP * 0.5)
        synth = RoundedRectangle(width=2.3, height=0.72, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12).shift(LEFT * 1.3 + UP * 0.5)
        reflect = RoundedRectangle(width=2.3, height=0.72, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.12).shift(RIGHT * 1.3 + UP * 0.5)
        gate = RoundedRectangle(width=2.3, height=0.72, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.12).shift(RIGHT * 4.0 + UP * 0.5)

        labels = VGroup(
            Text("seed tasks", color=WHITE).scale(0.27).move_to(seed),
            Text("synthetic data", color=WHITE).scale(0.24).move_to(synth),
            Text("reflection pass", color=WHITE).scale(0.24).move_to(reflect),
            Text("quality gate", color=WHITE).scale(0.26).move_to(gate),
        )
        self.play(FadeIn(VGroup(seed, synth, reflect, gate)), FadeIn(labels), run_time=2.0)

        arrows = VGroup(
            Arrow(seed.get_right(), synth.get_left(), buff=0.08, color=GREY_B),
            Arrow(synth.get_right(), reflect.get_left(), buff=0.08, color=GREY_B),
            Arrow(reflect.get_right(), gate.get_left(), buff=0.08, color=GREY_B),
        )
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.1), run_time=1.6)

        table = RoundedRectangle(width=5.0, height=1.7, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.10).to_edge(LEFT).shift(DOWN * 1.3)
        ttxt = Text("checks\nschema valid | no duplicates | safety tag | sample audit", color=WHITE).scale(0.25).move_to(table)
        self.play(FadeIn(table), FadeIn(ttxt), run_time=1.5)

        badge = RoundedRectangle(width=3.8, height=1.2, corner_radius=0.1, color=ORANGE).set_fill(ORANGE, opacity=0.10).to_edge(RIGHT).shift(DOWN * 1.3)
        btxt = Text("training-ready dataset\nversioned + traceable", color=WHITE).scale(0.27).move_to(badge)
        link = Arrow(table.get_right(), badge.get_left(), buff=0.12, color=ORANGE)
        self.play(Create(link), FadeIn(badge), FadeIn(btxt), run_time=1.7)

        loop = CurvedArrow(gate.get_bottom() + DOWN * 0.05, synth.get_bottom() + DOWN * 0.05, angle=-1.2, color=YELLOW)
        ltxt = Text("revise and regenerate", color=YELLOW).scale(0.23).next_to(loop, DOWN, buff=0.05)
        self.play(Create(loop), FadeIn(ltxt), run_time=1.2)

        self.play(Circumscribe(reflect, color=YELLOW, run_time=1.0))
        self.play(Circumscribe(gate, color=PURPLE, run_time=1.0))
        self.play(Circumscribe(badge, color=ORANGE, run_time=1.0))
        self.wait(14.1)
