from manim import *


class PretrainingLoopAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Ch5 Core: Pretraining Loop", color=WHITE).scale(0.74).to_edge(UP)
        subtitle = Text("batch -> loss -> backprop -> update -> eval", color=TEAL).scale(0.38).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        boxes = VGroup(
            RoundedRectangle(width=1.6, height=0.62, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12),
            RoundedRectangle(width=1.6, height=0.62, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12),
            RoundedRectangle(width=1.8, height=0.62, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.12),
            RoundedRectangle(width=1.6, height=0.62, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.12),
            RoundedRectangle(width=1.6, height=0.62, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.12),
        ).arrange(RIGHT, buff=0.22).shift(UP * 0.5)

        labels = VGroup(
            Text("Batch", color=WHITE).scale(0.3).move_to(boxes[0]),
            Text("Forward", color=WHITE).scale(0.3).move_to(boxes[1]),
            Text("Cross-Entropy", color=WHITE).scale(0.26).move_to(boxes[2]),
            Text("Backward", color=WHITE).scale(0.3).move_to(boxes[3]),
            Text("Step", color=WHITE).scale(0.3).move_to(boxes[4]),
        )

        arrows = VGroup(*[
            Arrow(boxes[i].get_right(), boxes[i + 1].get_left(), buff=0.05, color=GREY_B)
            for i in range(4)
        ])

        self.play(FadeIn(boxes), FadeIn(labels), run_time=2.1)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.12), run_time=1.7)
        self.wait(1.2)

        eval_box = RoundedRectangle(width=2.1, height=0.62, corner_radius=0.1, color=ORANGE).set_fill(ORANGE, opacity=0.12).next_to(boxes[2], DOWN, buff=1.0)
        eval_lbl = Text("Periodic Eval", color=WHITE).scale(0.3).move_to(eval_box)
        branch1 = Arrow(boxes[2].get_bottom(), eval_box.get_top(), buff=0.06, color=ORANGE)
        branch2 = CurvedArrow(eval_box.get_right() + RIGHT * 0.05, boxes[4].get_bottom() + DOWN * 0.05, angle=-1.1, color=ORANGE)
        self.play(Create(branch1), FadeIn(eval_box), FadeIn(eval_lbl), run_time=1.9)
        self.play(Create(branch2), run_time=1.3)

        metrics = Axes(
            x_range=[0, 10, 2],
            y_range=[0.5, 3.0, 0.5],
            x_length=4.2,
            y_length=2.1,
            axis_config={"color": GREY_B},
        ).to_edge(DOWN).shift(UP * 0.2)
        loss_curve = metrics.plot(lambda x: 2.6 / (x + 1) + 0.6, x_range=[0, 10], color=GREEN)
        val_curve = metrics.plot(lambda x: 2.9 / (x + 1) + 0.7, x_range=[0, 10], color=YELLOW)
        leg1 = Text("train", color=GREEN).scale(0.25).next_to(metrics, RIGHT, buff=0.1).shift(UP * 0.2)
        leg2 = Text("val", color=YELLOW).scale(0.25).next_to(leg1, DOWN, aligned_edge=LEFT)
        self.play(Create(metrics), run_time=1.5)
        self.play(Create(loss_curve), Create(val_curve), FadeIn(leg1), FadeIn(leg2), run_time=2.2)

        self.play(Circumscribe(boxes[2], color=YELLOW, run_time=1.1))
        self.play(Circumscribe(eval_box, color=ORANGE, run_time=1.1))
        self.wait(11.5)
