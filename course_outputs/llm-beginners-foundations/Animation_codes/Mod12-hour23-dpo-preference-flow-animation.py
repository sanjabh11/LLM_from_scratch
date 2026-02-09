from manim import *


class DPOPreferenceFlowAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Module 12: DPO Preference Flow", color=WHITE).scale(0.7).to_edge(UP)
        subtitle = Text("instruction -> chosen/rejected -> DPO loss", color=TEAL).scale(0.35).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        inst = RoundedRectangle(width=3.2, height=0.7, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12).shift(UP * 1.0)
        itxt = Text("Instruction prompt", color=WHITE).scale(0.28).move_to(inst)
        chosen = RoundedRectangle(width=3.0, height=0.7, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12).shift(LEFT * 2.3)
        ctxt = Text("Chosen response", color=WHITE).scale(0.27).move_to(chosen)
        rej = RoundedRectangle(width=3.0, height=0.7, corner_radius=0.1, color=RED).set_fill(RED, opacity=0.12).shift(RIGHT * 2.3)
        rtxt = Text("Rejected response", color=WHITE).scale(0.27).move_to(rej)

        a1 = Arrow(inst.get_bottom(), chosen.get_top(), buff=0.08, color=GREY_B)
        a2 = Arrow(inst.get_bottom(), rej.get_top(), buff=0.08, color=GREY_B)

        self.play(FadeIn(inst), FadeIn(itxt), run_time=1.3)
        self.play(Create(a1), Create(a2), FadeIn(chosen), FadeIn(ctxt), FadeIn(rej), FadeIn(rtxt), run_time=1.8)

        policy = RoundedRectangle(width=2.7, height=0.8, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.12).shift(DOWN * 0.6)
        ptxt = Text("Policy vs Reference\nlog-prob compare", color=WHITE).scale(0.24).move_to(policy)
        ac = Arrow(chosen.get_bottom(), policy.get_top() + LEFT * 0.5, buff=0.08, color=GREEN)
        ar = Arrow(rej.get_bottom(), policy.get_top() + RIGHT * 0.5, buff=0.08, color=RED)
        self.play(Create(ac), Create(ar), FadeIn(policy), FadeIn(ptxt), run_time=1.8)

        loss = RoundedRectangle(width=3.1, height=0.72, corner_radius=0.1, color=PURPLE).set_fill(PURPLE, opacity=0.12).to_edge(DOWN).shift(UP * 0.4)
        ltxt = Text("DPO loss: prefer chosen > rejected", color=WHITE).scale(0.25).move_to(loss)
        al = Arrow(policy.get_bottom(), loss.get_top(), buff=0.08, color=PURPLE)
        self.play(Create(al), FadeIn(loss), FadeIn(ltxt), run_time=1.6)

        upd = CurvedArrow(loss.get_left() + LEFT * 0.1, chosen.get_left() + LEFT * 0.4, angle=1.2, color=ORANGE)
        utxt = Text("update policy", color=ORANGE).scale(0.24).next_to(upd, LEFT, buff=0.05)
        self.play(Create(upd), FadeIn(utxt), run_time=1.2)

        self.play(Circumscribe(chosen, color=GREEN, run_time=1.0))
        self.play(Circumscribe(loss, color=PURPLE, run_time=1.0))
        self.wait(15.9)
