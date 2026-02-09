from manim import *


class KVCacheThroughputAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Ch4 Bonus: KV Cache Throughput", color=WHITE).scale(0.72).to_edge(UP)
        subtitle = Text("reuse K/V, decode faster", color=TEAL).scale(0.4).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        baseline = VGroup(
            RoundedRectangle(width=2.6, height=0.7, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12),
            Text("No Cache", color=WHITE).scale(0.34),
        )
        cached = VGroup(
            RoundedRectangle(width=2.6, height=0.7, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12),
            Text("KV Cache", color=WHITE).scale(0.34),
        )
        baseline[1].move_to(baseline[0])
        cached[1].move_to(cached[0])
        lanes = VGroup(baseline, cached).arrange(DOWN, buff=1.2).shift(UP * 0.2)

        self.play(FadeIn(lanes[0]), FadeIn(lanes[1]), run_time=1.8)

        t1 = Text("Step t: full prompt -> compute all K/V", color=BLUE).scale(0.3).next_to(lanes[0], RIGHT, buff=0.5)
        t2 = Text("Step t+1: recompute full prompt again", color=BLUE).scale(0.3).next_to(t1, DOWN, aligned_edge=LEFT)
        c1 = Text("Step t: initialize cache from prompt", color=GREEN).scale(0.3).next_to(lanes[1], RIGHT, buff=0.5)
        c2 = Text("Step t+1: compute only new token", color=GREEN).scale(0.3).next_to(c1, DOWN, aligned_edge=LEFT)

        self.play(Write(t1), Write(c1), run_time=2.0)
        self.play(Write(t2), Write(c2), run_time=1.9)
        self.wait(1.2)

        seq = VGroup(*[
            RoundedRectangle(width=0.75, height=0.5, corner_radius=0.08, color=YELLOW).set_fill(YELLOW, opacity=0.15).add(
                Text(str(v), color=WHITE).scale(0.24)
            )
            for v in [15496, 11, 314, 716]
        ]).arrange(RIGHT, buff=0.08).to_edge(LEFT).shift(DOWN * 2.1)
        new_tok = RoundedRectangle(width=0.75, height=0.5, corner_radius=0.08, color=PURPLE).set_fill(PURPLE, opacity=0.2).add(
            Text("new", color=WHITE).scale(0.24)
        ).next_to(seq, RIGHT, buff=0.08)
        cache_box = RoundedRectangle(width=3.3, height=0.7, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12).to_edge(RIGHT).shift(DOWN * 2.1)
        cache_lbl = Text("cache_k / cache_v", color=GREEN).scale(0.3).move_to(cache_box)
        arr1 = Arrow(seq.get_right(), cache_box.get_left(), buff=0.1, color=GREY_B)
        arr2 = Arrow(new_tok.get_right(), cache_box.get_left(), buff=0.1, color=PURPLE)

        self.play(LaggedStart(*[FadeIn(s, shift=UP * 0.1) for s in seq], lag_ratio=0.08), run_time=1.8)
        self.play(FadeIn(cache_box), FadeIn(cache_lbl), Create(arr1), run_time=1.8)
        self.play(FadeIn(new_tok, shift=RIGHT * 0.1), Create(arr2), run_time=1.3)
        self.wait(1.3)

        # Custom bar chart to avoid LaTeX
        bar_data = [("No cache", 28, BLUE), ("KV cache", 53, GREEN)]
        chart_bars = VGroup()
        chart_labels = VGroup()
        for i, (name, val, col) in enumerate(bar_data):
            bar = Rectangle(width=0.9, height=val * 0.033, color=col).set_fill(col, opacity=0.7)
            bar.move_to(RIGHT * (i * 1.2 - 0.6))
            bar.align_to(ORIGIN, DOWN)
            label = Text(name, color=WHITE).scale(0.22).next_to(bar, DOWN, buff=0.08)
            val_txt = Text(str(val), color=WHITE).scale(0.22).next_to(bar, UP, buff=0.05)
            chart_bars.add(bar)
            chart_labels.add(VGroup(label, val_txt))
        chart = VGroup(chart_bars, chart_labels).scale(0.62).to_edge(RIGHT).shift(UP * 0.75)
        chart_lbl = Text("tokens/sec (illustrative)", color=WHITE).scale(0.28).next_to(chart, UP, buff=0.1)
        self.play(Create(chart), FadeIn(chart_lbl), run_time=2.2)
        self.play(Circumscribe(chart_bars[1], color=YELLOW, run_time=1.2))
        self.wait(9.1)
