from manim import *


class SpeedAndTuningLadderAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Module 8: Speed + Tuning Ladder", color=WHITE).scale(0.72).to_edge(UP)
        subtitle = Text("baseline -> optimized -> distributed -> tuned", color=TEAL).scale(0.36).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        steps = VGroup(
            RoundedRectangle(width=2.2, height=0.72, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12),
            RoundedRectangle(width=2.2, height=0.72, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12),
            RoundedRectangle(width=2.2, height=0.72, corner_radius=0.1, color=ORANGE).set_fill(ORANGE, opacity=0.12),
            RoundedRectangle(width=2.2, height=0.72, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.12),
        ).arrange(DOWN, buff=0.5).shift(LEFT * 3.2)

        labels = VGroup(
            Text("00_orig", color=WHITE).scale(0.3).move_to(steps[0]),
            Text("01_opt_single_gpu", color=WHITE).scale(0.24).move_to(steps[1]),
            Text("02_opt_multi_gpu_ddp", color=WHITE).scale(0.23).move_to(steps[2]),
            Text("hparam_search", color=WHITE).scale(0.27).move_to(steps[3]),
        )
        self.play(FadeIn(steps), FadeIn(labels), run_time=2.0)

        arrows = VGroup(*[
            Arrow(steps[i].get_bottom(), steps[i + 1].get_top(), buff=0.08, color=GREY_B)
            for i in range(3)
        ])
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.15), run_time=1.7)

        # Custom bar chart to avoid LaTeX
        bar_data = [("base", 12.5, BLUE), ("opt1", 142.1, GREEN), ("ddp", 419.2, ORANGE)]
        chart_bars = VGroup()
        chart_labels = VGroup()
        max_val = 450
        for i, (name, val, col) in enumerate(bar_data):
            bar = Rectangle(width=0.7, height=val / max_val * 2.4, color=col).set_fill(col, opacity=0.7)
            bar.move_to(RIGHT * (i * 0.95 - 0.95))
            bar.align_to(ORIGIN, DOWN)
            label = Text(name, color=WHITE).scale(0.2).next_to(bar, DOWN, buff=0.06)
            val_txt = Text(str(int(val)), color=WHITE).scale(0.18).next_to(bar, UP, buff=0.04)
            chart_bars.add(bar)
            chart_labels.add(VGroup(label, val_txt))
        chart = VGroup(chart_bars, chart_labels).scale(0.62).to_edge(RIGHT).shift(UP * 0.7)
        clbl = Text("tokens/sec (illustrative)", color=WHITE).scale(0.26).next_to(chart, UP, buff=0.1)
        self.play(Create(chart), FadeIn(clbl), run_time=2.1)
        self.wait(1.2)

        tune_box = RoundedRectangle(width=4.5, height=1.2, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.10).to_edge(RIGHT).shift(DOWN * 1.3)
        grid = Text("Grid Search\n(batch, lr, warmup, wd)", color=WHITE).scale(0.29).move_to(tune_box)
        pick = Text("select best val loss", color=YELLOW).scale(0.25).next_to(tune_box, DOWN, buff=0.12)
        self.play(FadeIn(tune_box), FadeIn(grid), run_time=1.7)
        self.play(FadeIn(pick), run_time=0.9)

        link = Arrow(steps[3].get_right(), tune_box.get_left(), buff=0.1, color=PURPLE)
        self.play(Create(link), run_time=1.0)

        summary = RoundedRectangle(width=7.0, height=0.7, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.12).to_edge(DOWN)
        stxt = Text("Goal: maximize quality-per-compute under stable training constraints", color=WHITE).scale(0.28).move_to(summary)
        self.play(FadeIn(summary), FadeIn(stxt), run_time=1.4)

        self.play(Circumscribe(steps[1], color=GREEN, run_time=1.0))
        self.play(Circumscribe(tune_box, color=PURPLE, run_time=1.0))
        self.wait(11.6)
