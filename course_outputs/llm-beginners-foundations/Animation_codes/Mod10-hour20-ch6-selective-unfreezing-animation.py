from manim import *


class Ch6SelectiveUnfreezingAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Module 10: Selective Unfreezing", color=WHITE).scale(0.72).to_edge(UP)
        subtitle = Text("freeze backbone, train head + last block", color=TEAL).scale(0.36).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        blocks = VGroup(*[
            RoundedRectangle(width=3.0, height=0.42, corner_radius=0.07, color=BLUE).set_fill(BLUE, opacity=0.08)
            for _ in range(6)
        ]).arrange(DOWN, buff=0.08).shift(LEFT * 2.4)
        b_lbl = Text("GPT backbone blocks", color=WHITE).scale(0.27).next_to(blocks, UP, buff=0.1)

        frozen = VGroup(*blocks[:5])
        trainable = blocks[5]
        trainable.set_fill(GREEN, opacity=0.22).set_stroke(color=GREEN)

        head = RoundedRectangle(width=2.3, height=0.7, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.15).next_to(blocks, RIGHT, buff=0.7)
        h_lbl = Text("2-class head", color=WHITE).scale(0.3).move_to(head)
        link = Arrow(trainable.get_right(), head.get_left(), buff=0.08, color=GREY_B)

        self.play(FadeIn(blocks), FadeIn(b_lbl), run_time=1.8)
        self.play(Create(link), FadeIn(head), FadeIn(h_lbl), run_time=1.5)

        lock_marks = VGroup(*[Text("frozen", color=BLUE).scale(0.22).next_to(b, LEFT, buff=0.08) for b in frozen])
        tr_mark = Text("trainable", color=GREEN).scale(0.24).next_to(trainable, LEFT, buff=0.08)
        self.play(LaggedStart(*[FadeIn(t, shift=RIGHT * 0.05) for t in lock_marks], lag_ratio=0.08), run_time=1.4)
        self.play(FadeIn(tr_mark, shift=RIGHT * 0.05), run_time=0.8)

        grad = Arrow(head.get_bottom(), trainable.get_top(), buff=0.05, color=ORANGE)
        grad_lbl = Text("gradient flow", color=ORANGE).scale(0.24).next_to(grad, RIGHT, buff=0.08)
        self.play(Create(grad), FadeIn(grad_lbl), run_time=1.2)

        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0.4, 1.0, 0.1],
            x_length=4.5,
            y_length=2.1,
            axis_config={"color": GREY_B},
        ).to_edge(RIGHT).shift(DOWN * 1.2)
        acc = axes.plot(lambda x: 0.52 + 0.04 * x - 0.0015 * x * x, x_range=[0, 10], color=GREEN)
        a_lbl = Text("validation accuracy", color=GREEN).scale(0.24).next_to(axes, UP, buff=0.08)
        self.play(Create(axes), Create(acc), FadeIn(a_lbl), run_time=1.9)

        summary = RoundedRectangle(width=6.7, height=0.65, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.12).to_edge(DOWN)
        s_txt = Text("Efficient adaptation: fewer trainable params, faster stable finetune", color=WHITE).scale(0.27).move_to(summary)
        self.play(FadeIn(summary), FadeIn(s_txt), run_time=1.5)

        self.play(Circumscribe(trainable, color=GREEN, run_time=1.0))
        self.play(Circumscribe(head, color=YELLOW, run_time=1.0))
        self.wait(13.5)
