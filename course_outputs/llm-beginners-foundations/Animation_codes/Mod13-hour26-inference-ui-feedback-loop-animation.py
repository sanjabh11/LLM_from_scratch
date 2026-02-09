from manim import *


class InferenceUIFeedbackLoopAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Add-On A: UI Feedback Loop", color=WHITE).scale(0.72).to_edge(UP)
        subtitle = Text("demo -> feedback -> fix -> redeploy", color=TEAL).scale(0.35).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        demo = RoundedRectangle(width=2.2, height=0.72, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12).shift(LEFT * 3.3 + UP * 0.6)
        dtx = Text("Live demo", color=WHITE).scale(0.29).move_to(demo)
        fb = RoundedRectangle(width=2.2, height=0.72, corner_radius=0.1, color=ORANGE).set_fill(ORANGE, opacity=0.12).shift(LEFT * 1.1 + UP * 0.6)
        ftx = Text("Feedback", color=WHITE).scale(0.29).move_to(fb)
        fix = RoundedRectangle(width=2.2, height=0.72, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.12).shift(RIGHT * 1.1 + UP * 0.6)
        xtx = Text("Fix", color=WHITE).scale(0.29).move_to(fix)
        rel = RoundedRectangle(width=2.2, height=0.72, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12).shift(RIGHT * 3.3 + UP * 0.6)
        rtx = Text("Redeploy", color=WHITE).scale(0.28).move_to(rel)

        arr = VGroup(
            Arrow(demo.get_right(), fb.get_left(), buff=0.07, color=GREY_B),
            Arrow(fb.get_right(), fix.get_left(), buff=0.07, color=GREY_B),
            Arrow(fix.get_right(), rel.get_left(), buff=0.07, color=GREY_B),
        )
        self.play(FadeIn(VGroup(demo, fb, fix, rel)), FadeIn(VGroup(dtx, ftx, xtx, rtx)), run_time=2.0)
        self.play(LaggedStart(*[Create(a) for a in arr], lag_ratio=0.1), run_time=1.6)

        board = RoundedRectangle(width=4.2, height=1.5, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.10).to_edge(LEFT).shift(DOWN * 1.2)
        btxt = Text("Issue board\n- correctness\n- latency\n- UX clarity\n- robustness", color=WHITE).scale(0.24).move_to(board)
        self.play(FadeIn(board), FadeIn(btxt), run_time=1.5)

        metrics = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 100, 20],
            x_length=4.2,
            y_length=2.1,
            axis_config={"color": GREY_B},
        ).to_edge(RIGHT).shift(DOWN * 1.2)
        curve = metrics.plot(lambda x: 35 + 5 * x, x_range=[0, 10], color=GREEN)
        mt = Text("demo quality score", color=GREEN).scale(0.24).next_to(metrics, UP, buff=0.06)
        self.play(Create(metrics), Create(curve), FadeIn(mt), run_time=2.0)

        loop = CurvedArrow(rel.get_bottom() + DOWN * 0.05, demo.get_bottom() + DOWN * 0.05, angle=-1.3, color=TEAL)
        ltx = Text("next iteration", color=TEAL).scale(0.24).next_to(loop, DOWN, buff=0.05)
        self.play(Create(loop), FadeIn(ltx), run_time=1.2)

        self.play(Circumscribe(board, color=YELLOW, run_time=1.0))
        self.play(Circumscribe(curve, color=GREEN, run_time=1.0))
        self.wait(15.3)
