from manim import *


class DPOLORACapstoneLoopAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Module 12: DPO + LoRA Capstone Loop", color=WHITE).scale(0.7).to_edge(UP)
        subtitle = Text("align -> efficient adapt -> evaluate -> gate", color=TEAL).scale(0.35).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        sft = RoundedRectangle(width=2.1, height=0.7, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12).shift(LEFT * 3.2 + UP * 0.5)
        dpo = RoundedRectangle(width=2.1, height=0.7, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12).shift(LEFT * 1.0 + UP * 0.5)
        lora = RoundedRectangle(width=2.1, height=0.7, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.12).shift(RIGHT * 1.2 + UP * 0.5)
        evalb = RoundedRectangle(width=2.1, height=0.7, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.12).shift(RIGHT * 3.4 + UP * 0.5)

        labels = VGroup(
            Text("SFT base", color=WHITE).scale(0.28).move_to(sft),
            Text("DPO", color=WHITE).scale(0.3).move_to(dpo),
            Text("LoRA", color=WHITE).scale(0.3).move_to(lora),
            Text("Eval", color=WHITE).scale(0.3).move_to(evalb),
        )

        arr = VGroup(
            Arrow(sft.get_right(), dpo.get_left(), buff=0.08, color=GREY_B),
            Arrow(dpo.get_right(), lora.get_left(), buff=0.08, color=GREY_B),
            Arrow(lora.get_right(), evalb.get_left(), buff=0.08, color=GREY_B),
        )
        self.play(FadeIn(VGroup(sft, dpo, lora, evalb)), FadeIn(labels), run_time=2.0)
        self.play(LaggedStart(*[Create(a) for a in arr], lag_ratio=0.1), run_time=1.6)

        metrics = RoundedRectangle(width=3.8, height=1.2, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.10).to_edge(LEFT).shift(DOWN * 1.2)
        mtxt = Text("quality score\nruntime\nmemory\ntrainable params", color=WHITE).scale(0.25).move_to(metrics)
        self.play(FadeIn(metrics), FadeIn(mtxt), run_time=1.4)

        gate = RoundedRectangle(width=4.2, height=1.2, corner_radius=0.1, color=ORANGE).set_fill(ORANGE, opacity=0.10).to_edge(RIGHT).shift(DOWN * 1.2)
        gtxt = Text("Capstone gates:\nData pass\nStability pass\nQuality pass", color=WHITE).scale(0.25).move_to(gate)
        self.play(FadeIn(gate), FadeIn(gtxt), run_time=1.5)

        loop = CurvedArrow(gate.get_top() + UP * 0.1, dpo.get_bottom() + DOWN * 0.1, angle=-1.2, color=ORANGE)
        ltxt = Text("iterate", color=ORANGE).scale(0.24).next_to(loop, DOWN, buff=0.05)
        self.play(Create(loop), FadeIn(ltxt), run_time=1.2)

        self.play(Circumscribe(dpo, color=GREEN, run_time=1.0))
        self.play(Circumscribe(lora, color=YELLOW, run_time=1.0))
        self.play(Circumscribe(gate, color=ORANGE, run_time=1.0))
        self.wait(14.9)
