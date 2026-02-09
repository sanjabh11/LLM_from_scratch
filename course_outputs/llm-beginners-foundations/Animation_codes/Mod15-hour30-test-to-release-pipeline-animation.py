from manim import *


class TestToReleasePipelineAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Add-On C: Test-to-Release Pipeline", color=WHITE).scale(0.69).to_edge(UP)
        subtitle = Text("run suites -> triage -> patch -> rerun -> approve", color=TEAL).scale(0.33).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        runn = RoundedRectangle(width=2.1, height=0.72, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12).shift(LEFT * 4.0 + UP * 0.5)
        tri = RoundedRectangle(width=2.1, height=0.72, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.12).shift(LEFT * 1.3 + UP * 0.5)
        fix = RoundedRectangle(width=2.1, height=0.72, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.12).shift(RIGHT * 1.3 + UP * 0.5)
        rel = RoundedRectangle(width=2.1, height=0.72, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12).shift(RIGHT * 4.0 + UP * 0.5)

        txt = VGroup(
            Text("run tests", color=WHITE).scale(0.28).move_to(runn),
            Text("triage", color=WHITE).scale(0.30).move_to(tri),
            Text("patch", color=WHITE).scale(0.30).move_to(fix),
            Text("release", color=WHITE).scale(0.30).move_to(rel),
        )
        self.play(FadeIn(VGroup(runn, tri, fix, rel)), FadeIn(txt), run_time=2.0)

        arr = VGroup(
            Arrow(runn.get_right(), tri.get_left(), buff=0.08, color=GREY_B),
            Arrow(tri.get_right(), fix.get_left(), buff=0.08, color=GREY_B),
            Arrow(fix.get_right(), rel.get_left(), buff=0.08, color=GREY_B),
        )
        self.play(LaggedStart(*[Create(a) for a in arr], lag_ratio=0.1), run_time=1.6)

        issues = RoundedRectangle(width=4.5, height=1.7, corner_radius=0.1, color=RED).set_fill(RED, opacity=0.10).to_edge(LEFT).shift(DOWN * 1.3)
        itxt = Text("triage board\n- env mismatch\n- shape mismatch\n- launch mismatch", color=WHITE).scale(0.24).move_to(issues)
        self.play(FadeIn(issues), FadeIn(itxt), run_time=1.5)

        metrics = RoundedRectangle(width=4.1, height=1.7, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.10).to_edge(RIGHT).shift(DOWN * 1.3)
        mtxt = Text("release evidence\npass rate | runtime | hash | decision", color=WHITE).scale(0.24).move_to(metrics)
        self.play(FadeIn(metrics), FadeIn(mtxt), run_time=1.5)

        bridge = Arrow(issues.get_right(), metrics.get_left(), buff=0.12, color=TEAL)
        self.play(Create(bridge), run_time=1.0)

        loop = CurvedArrow(rel.get_bottom() + DOWN * 0.08, tri.get_bottom() + DOWN * 0.08, angle=-1.2, color=ORANGE)
        ltxt = Text("failed gate -> iterate", color=ORANGE).scale(0.22).next_to(loop, DOWN, buff=0.05)
        self.play(Create(loop), FadeIn(ltxt), run_time=1.2)

        self.play(Circumscribe(tri, color=YELLOW, run_time=1.0))
        self.play(Circumscribe(fix, color=PURPLE, run_time=1.0))
        self.play(Circumscribe(metrics, color=TEAL, run_time=1.0))
        self.wait(13.8)
