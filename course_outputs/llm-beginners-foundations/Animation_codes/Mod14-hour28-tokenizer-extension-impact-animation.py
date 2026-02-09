from manim import *


class TokenizerExtensionImpactAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Add-On B: Tokenizer Extension Impact", color=WHITE).scale(0.7).to_edge(UP)
        subtitle = Text("before/after token split -> sequence length -> throughput effect", color=TEAL).scale(0.31).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        before = RoundedRectangle(width=5.8, height=1.0, corner_radius=0.1, color=RED).set_fill(RED, opacity=0.10).to_edge(LEFT).shift(UP * 0.5)
        btxt = Text("Before: [micro][seg][men][ta][tion][token][izer]", color=WHITE).scale(0.27).move_to(before)
        after = RoundedRectangle(width=5.8, height=1.0, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.10).to_edge(RIGHT).shift(UP * 0.5)
        atxt = Text("After: [microsegmentation][tokenizer]", color=WHITE).scale(0.29).move_to(after)
        self.play(FadeIn(before), FadeIn(btxt), run_time=1.4)
        self.play(FadeIn(after), FadeIn(atxt), run_time=1.4)

        a = Arrow(before.get_right(), after.get_left(), buff=0.14, color=GREY_B)
        self.play(Create(a), run_time=1.0)

        chart = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 14, 2],
            x_length=4.0,
            y_length=2.2,
            axis_config={"color": GREY_B},
        ).to_edge(LEFT).shift(DOWN * 1.6 + RIGHT * 0.4)
        bars = VGroup(
            Rectangle(width=0.6, height=1.8, color=RED, fill_opacity=0.6).move_to(chart.c2p(0.8, 3.8), aligned_edge=DOWN),
            Rectangle(width=0.6, height=0.8, color=GREEN, fill_opacity=0.6).move_to(chart.c2p(2.0, 2.8), aligned_edge=DOWN),
        )
        bl = VGroup(
            Text("before", color=RED).scale(0.22).next_to(bars[0], DOWN, buff=0.08),
            Text("after", color=GREEN).scale(0.22).next_to(bars[1], DOWN, buff=0.08),
        )
        yl = Text("tokens / phrase", color=WHITE).scale(0.22).next_to(chart, UP, buff=0.06)
        self.play(Create(chart), FadeIn(bars), FadeIn(bl), FadeIn(yl), run_time=2.0)

        board = RoundedRectangle(width=5.3, height=2.0, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.10).to_edge(RIGHT).shift(DOWN * 1.5)
        tips = Text(
            "checks\n- re-tokenize datasets\n- resize embeddings\n- version tokenizer\n- run A/B eval",
            color=WHITE,
        ).scale(0.25).move_to(board)
        self.play(FadeIn(board), FadeIn(tips), run_time=1.6)

        arc = CurvedArrow(after.get_bottom() + DOWN * 0.08, board.get_top() + UP * 0.08, angle=-1.0, color=TEAL)
        ltxt = Text("pipeline update required", color=TEAL).scale(0.22).next_to(arc, RIGHT, buff=0.04)
        self.play(Create(arc), FadeIn(ltxt), run_time=1.2)

        self.play(Circumscribe(after, color=GREEN, run_time=1.0))
        self.play(Circumscribe(board, color=BLUE, run_time=1.0))
        self.play(Circumscribe(bars, color=YELLOW, run_time=1.0))
        self.wait(13.0)
