from manim import *


class ReproducibilityGatesAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Add-On C: Reproducibility Gates", color=WHITE).scale(0.7).to_edge(UP)
        subtitle = Text("preflight -> tests -> seed lock -> artifact hash -> gate", color=TEAL).scale(0.32).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        env = RoundedRectangle(width=2.2, height=0.72, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12).shift(LEFT * 3.3 + UP * 0.5)
        tst = RoundedRectangle(width=2.2, height=0.72, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12).shift(LEFT * 1.1 + UP * 0.5)
        sed = RoundedRectangle(width=2.2, height=0.72, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.12).shift(RIGHT * 1.1 + UP * 0.5)
        hsh = RoundedRectangle(width=2.2, height=0.72, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.12).shift(RIGHT * 3.3 + UP * 0.5)

        labels = VGroup(
            Text("env check", color=WHITE).scale(0.29).move_to(env),
            Text("test pass", color=WHITE).scale(0.29).move_to(tst),
            Text("seed lock", color=WHITE).scale(0.29).move_to(sed),
            Text("artifact hash", color=WHITE).scale(0.25).move_to(hsh),
        )
        self.play(FadeIn(VGroup(env, tst, sed, hsh)), FadeIn(labels), run_time=2.0)

        arrows = VGroup(
            Arrow(env.get_right(), tst.get_left(), buff=0.08, color=GREY_B),
            Arrow(tst.get_right(), sed.get_left(), buff=0.08, color=GREY_B),
            Arrow(sed.get_right(), hsh.get_left(), buff=0.08, color=GREY_B),
        )
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.1), run_time=1.6)

        board = RoundedRectangle(width=4.6, height=1.7, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.10).to_edge(LEFT).shift(DOWN * 1.3)
        btxt = Text("gate report\npython=ok | tests=ok | seed=42 | ckpt=sha256", color=WHITE).scale(0.24).move_to(board)
        self.play(FadeIn(board), FadeIn(btxt), run_time=1.5)

        decision = RoundedRectangle(width=3.7, height=1.2, corner_radius=0.1, color=ORANGE).set_fill(ORANGE, opacity=0.10).to_edge(RIGHT).shift(DOWN * 1.3)
        dtxt = Text("release gate:\nPASS / BLOCK", color=WHITE).scale(0.28).move_to(decision)
        link = Arrow(board.get_right(), decision.get_left(), buff=0.12, color=ORANGE)
        self.play(Create(link), FadeIn(decision), FadeIn(dtxt), run_time=1.8)

        loop = CurvedArrow(decision.get_top() + UP * 0.08, tst.get_bottom() + DOWN * 0.08, angle=-1.2, color=YELLOW)
        ltxt = Text("if block: fix and rerun", color=YELLOW).scale(0.22).next_to(loop, DOWN, buff=0.05)
        self.play(Create(loop), FadeIn(ltxt), run_time=1.2)

        self.play(Circumscribe(env, color=BLUE, run_time=1.0))
        self.play(Circumscribe(tst, color=GREEN, run_time=1.0))
        self.play(Circumscribe(decision, color=ORANGE, run_time=1.0))
        self.wait(14.1)
