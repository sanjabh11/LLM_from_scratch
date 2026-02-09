from manim import *


class AttentionAlternativesTradeoffAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Ch4 Bonus: Attention Trade-off Map", color=WHITE).scale(0.7).to_edge(UP)
        subtitle = Text("MHA, GQA, MLA, SWA, MoE, Delta-style", color=TEAL).scale(0.35).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            x_length=6.2,
            y_length=3.6,
            axis_config={"color": GREY_B},
        ).shift(DOWN * 0.2)
        x_lbl = Text("lower memory ->", color=WHITE).scale(0.28).next_to(axes.x_axis, DOWN)
        y_lbl = Text("higher complexity ->", color=WHITE).scale(0.28).rotate(PI / 2).next_to(axes.y_axis, LEFT)
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=2.2)

        points = {
            "MHA": (2.0, 2.2, BLUE),
            "GQA": (4.2, 3.2, GREEN),
            "MLA": (6.2, 4.8, YELLOW),
            "SWA": (5.4, 3.9, PURPLE),
            "MoE": (6.8, 6.3, ORANGE),
            "Delta": (8.2, 7.2, RED),
        }

        dots = VGroup()
        labels = VGroup()
        for name, (xv, yv, col) in points.items():
            d = Dot(axes.c2p(xv, yv), color=col, radius=0.08)
            l = Text(name, color=WHITE).scale(0.27).next_to(d, UP, buff=0.08)
            dots.add(d)
            labels.add(l)

        self.play(LaggedStart(*[FadeIn(d, scale=0.7) for d in dots], lag_ratio=0.12), run_time=2.0)
        self.play(LaggedStart(*[FadeIn(l, shift=UP * 0.05) for l in labels], lag_ratio=0.12), run_time=1.5)
        self.wait(1.2)

        mem_brace = Brace(VGroup(dots[1], dots[2], dots[3]), DOWN, color=GREEN)
        mem_lbl = Text("memory-aware variants", color=GREEN).scale(0.28).next_to(mem_brace, DOWN, buff=0.08)
        sparse_brace = Brace(VGroup(dots[4], dots[5]), RIGHT, color=ORANGE)
        sparse_lbl = Text("higher integration complexity", color=ORANGE).scale(0.26).next_to(sparse_brace, RIGHT, buff=0.08)
        self.play(GrowFromCenter(mem_brace), FadeIn(mem_lbl), run_time=1.8)
        self.play(GrowFromCenter(sparse_brace), FadeIn(sparse_lbl), run_time=1.7)

        decision = RoundedRectangle(width=6.7, height=0.85, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.12).to_edge(DOWN)
        decision_txt = Text("Pick variant by bottleneck: memory, latency, quality risk, complexity budget", color=WHITE).scale(0.28).move_to(decision)
        self.play(FadeIn(decision), FadeIn(decision_txt), run_time=2.0)

        self.play(Circumscribe(dots[1], color=GREEN, run_time=1.0))
        self.play(Circumscribe(dots[2], color=YELLOW, run_time=1.0))
        self.play(Circumscribe(dots[5], color=RED, run_time=1.0))
        self.wait(10.2)
