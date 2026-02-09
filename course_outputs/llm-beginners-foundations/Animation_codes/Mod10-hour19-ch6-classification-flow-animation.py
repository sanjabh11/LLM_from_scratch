from manim import *


class Ch6ClassificationFlowAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Module 10: Ch6 Classification Flow", color=WHITE).scale(0.7).to_edge(UP)
        subtitle = Text("text -> tokens -> GPT -> class logits -> loss", color=TEAL).scale(0.35).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        steps = VGroup(
            RoundedRectangle(width=1.6, height=0.62, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12),
            RoundedRectangle(width=1.6, height=0.62, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12),
            RoundedRectangle(width=1.8, height=0.62, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.12),
            RoundedRectangle(width=1.8, height=0.62, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.12),
            RoundedRectangle(width=1.4, height=0.62, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.12),
        ).arrange(RIGHT, buff=0.2).shift(UP * 0.4)

        labels = VGroup(
            Text("Text", color=WHITE).scale(0.3).move_to(steps[0]),
            Text("Tokens", color=WHITE).scale(0.3).move_to(steps[1]),
            Text("GPT", color=WHITE).scale(0.3).move_to(steps[2]),
            Text("Class logits", color=WHITE).scale(0.25).move_to(steps[3]),
            Text("Loss", color=WHITE).scale(0.3).move_to(steps[4]),
        )
        arrows = VGroup(*[Arrow(steps[i].get_right(), steps[i + 1].get_left(), buff=0.05, color=GREY_B) for i in range(4)])
        self.play(FadeIn(steps), FadeIn(labels), run_time=2.0)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.1), run_time=1.6)

        msg = RoundedRectangle(width=3.8, height=0.58, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12).to_edge(LEFT).shift(DOWN * 1.6)
        msg_t = Text("'Free prize claim now'", color=WHITE).scale(0.27).move_to(msg)
        tok = VGroup(*[
            RoundedRectangle(width=0.68, height=0.45, corner_radius=0.08, color=GREEN).set_fill(GREEN, opacity=0.12).add(Text(str(v), color=WHITE).scale(0.21))
            for v in [1363, 9801, 2266, 783]
        ]).arrange(RIGHT, buff=0.08).next_to(msg, RIGHT, buff=0.2)
        self.play(FadeIn(msg), FadeIn(msg_t), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(t, shift=UP * 0.05) for t in tok], lag_ratio=0.08), run_time=1.5)

        # Custom bar chart to avoid LaTeX
        bar_data = [("ham", 0.18, BLUE), ("spam", 0.82, RED)]
        chart_bars = VGroup()
        chart_labels = VGroup()
        for i, (name, val, col) in enumerate(bar_data):
            bar = Rectangle(width=0.8, height=val * 1.6, color=col).set_fill(col, opacity=0.7)
            bar.move_to(RIGHT * (i * 1.1 - 0.55))
            bar.align_to(ORIGIN, DOWN)
            label = Text(name, color=WHITE).scale(0.22).next_to(bar, DOWN, buff=0.06)
            val_txt = Text(f"{val:.2f}", color=WHITE).scale(0.18).next_to(bar, UP, buff=0.04)
            chart_bars.add(bar)
            chart_labels.add(VGroup(label, val_txt))
        bars = VGroup(chart_bars, chart_labels).scale(0.58).to_edge(RIGHT).shift(DOWN * 1.3)
        btxt = Text("argmax -> spam", color=YELLOW).scale(0.28).next_to(bars, DOWN, buff=0.08)
        self.play(Create(bars), FadeIn(btxt), run_time=2.0)

        update = CurvedArrow(steps[4].get_bottom() + DOWN * 0.1, steps[2].get_bottom() + DOWN * 0.1, angle=-1.2, color=ORANGE)
        utxt = Text("backprop update (selected params)", color=ORANGE).scale(0.24).next_to(update, DOWN, buff=0.05)
        self.play(Create(update), FadeIn(utxt), run_time=1.4)

        self.play(Circumscribe(steps[3], color=PURPLE, run_time=1.0))
        self.play(Circumscribe(chart_bars[1], color=RED, run_time=1.0))
        self.wait(13.9)
