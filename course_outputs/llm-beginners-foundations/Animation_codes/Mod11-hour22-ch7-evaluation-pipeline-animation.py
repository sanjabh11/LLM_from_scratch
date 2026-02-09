from manim import *


class Ch7EvaluationPipelineAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Module 11: Evaluation Pipeline", color=WHITE).scale(0.72).to_edge(UP)
        subtitle = Text("responses -> rubric judge -> scores -> analysis", color=TEAL).scale(0.35).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        src = RoundedRectangle(width=3.0, height=0.8, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12).shift(LEFT * 3.2 + UP * 0.5)
        st = Text("response JSON", color=WHITE).scale(0.29).move_to(src)
        judge = RoundedRectangle(width=3.0, height=0.8, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12).shift(UP * 0.5)
        jt = Text("rubric judge model", color=WHITE).scale(0.27).move_to(judge)
        score = RoundedRectangle(width=3.0, height=0.8, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.12).shift(RIGHT * 3.2 + UP * 0.5)
        sct = Text("scores (0-100)", color=WHITE).scale(0.29).move_to(score)

        a1 = Arrow(src.get_right(), judge.get_left(), buff=0.08, color=GREY_B)
        a2 = Arrow(judge.get_right(), score.get_left(), buff=0.08, color=GREY_B)
        self.play(FadeIn(src), FadeIn(st), run_time=1.2)
        self.play(Create(a1), FadeIn(judge), FadeIn(jt), run_time=1.4)
        self.play(Create(a2), FadeIn(score), FadeIn(sct), run_time=1.4)

        # Custom bar chart to avoid LaTeX
        bar_data = [("run1", 45, BLUE), ("run2", 52, GREEN), ("run3", 63, YELLOW), ("run4", 58, PURPLE)]
        chart_bars = VGroup()
        chart_labels = VGroup()
        max_val = 80
        for i, (name, val, col) in enumerate(bar_data):
            bar = Rectangle(width=0.65, height=val / max_val * 2.0, color=col).set_fill(col, opacity=0.7)
            bar.move_to(RIGHT * (i * 0.85 - 1.2))
            bar.align_to(ORIGIN, DOWN)
            label = Text(name, color=WHITE).scale(0.18).next_to(bar, DOWN, buff=0.05)
            val_txt = Text(str(val), color=WHITE).scale(0.16).next_to(bar, UP, buff=0.03)
            chart_bars.add(bar)
            chart_labels.add(VGroup(label, val_txt))
        bars = VGroup(chart_bars, chart_labels).scale(0.62).to_edge(LEFT).shift(DOWN * 1.3)
        bt = Text("average score trend", color=WHITE).scale(0.25).next_to(bars, UP, buff=0.08)
        self.play(Create(bars), FadeIn(bt), run_time=2.0)

        feedback = RoundedRectangle(width=4.4, height=1.0, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.10).to_edge(RIGHT).shift(DOWN * 1.35)
        ft = Text("error slices -> data cleanup\n-> retrain / revise", color=WHITE).scale(0.27).move_to(feedback)
        loop = CurvedArrow(feedback.get_top() + UP * 0.1, judge.get_bottom() + DOWN * 0.1, angle=-1.2, color=PURPLE)
        self.play(FadeIn(feedback), FadeIn(ft), run_time=1.6)
        self.play(Create(loop), run_time=1.2)

        det = Text("deterministic eval settings (seed/temp)", color=ORANGE).scale(0.24).to_edge(DOWN)
        self.play(FadeIn(det), run_time=1.0)

        self.play(Circumscribe(score, color=YELLOW, run_time=1.0))
        self.play(Circumscribe(feedback, color=PURPLE, run_time=1.0))
        self.wait(13.8)
