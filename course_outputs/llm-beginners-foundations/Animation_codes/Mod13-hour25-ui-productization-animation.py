from manim import *


class UIProductizationAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Add-On A: UI Productization Flow", color=WHITE).scale(0.7).to_edge(UP)
        subtitle = Text("artifact -> app init -> user message -> model response", color=TEAL).scale(0.33).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        art = RoundedRectangle(width=2.4, height=0.72, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12).shift(LEFT * 3.2 + UP * 0.6)
        at = Text("model artifact", color=WHITE).scale(0.27).move_to(art)
        app = RoundedRectangle(width=2.4, height=0.72, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12).shift(UP * 0.6)
        ap = Text("Chainlit app", color=WHITE).scale(0.29).move_to(app)
        usr = RoundedRectangle(width=2.4, height=0.72, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.12).shift(RIGHT * 3.2 + UP * 0.6)
        ut = Text("user request", color=WHITE).scale(0.29).move_to(usr)

        a1 = Arrow(art.get_right(), app.get_left(), buff=0.08, color=GREY_B)
        a2 = Arrow(usr.get_left(), app.get_right(), buff=0.08, color=GREY_B)
        self.play(FadeIn(art), FadeIn(at), FadeIn(app), FadeIn(ap), FadeIn(usr), FadeIn(ut), run_time=2.0)
        self.play(Create(a1), Create(a2), run_time=1.4)

        lanes = VGroup(
            RoundedRectangle(width=2.1, height=0.58, corner_radius=0.08, color=BLUE).set_fill(BLUE, opacity=0.10),
            RoundedRectangle(width=2.1, height=0.58, corner_radius=0.08, color=ORANGE).set_fill(ORANGE, opacity=0.10),
            RoundedRectangle(width=2.1, height=0.58, corner_radius=0.08, color=PURPLE).set_fill(PURPLE, opacity=0.10),
        ).arrange(DOWN, buff=0.16).shift(LEFT * 3.1 + DOWN * 1.3)
        lane_labels = VGroup(
            Text("Gen UI", color=WHITE).scale(0.25).move_to(lanes[0]),
            Text("Classifier UI", color=WHITE).scale(0.24).move_to(lanes[1]),
            Text("Instruction UI", color=WHITE).scale(0.23).move_to(lanes[2]),
        )
        self.play(FadeIn(lanes), FadeIn(lane_labels), run_time=1.4)

        out = RoundedRectangle(width=4.5, height=1.0, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.12).shift(RIGHT * 2.5 + DOWN * 1.3)
        ot = Text("task-specific response\n(text / label / assistant reply)", color=WHITE).scale(0.26).move_to(out)
        flow = Arrow(lanes.get_right(), out.get_left(), buff=0.12, color=TEAL)
        self.play(Create(flow), FadeIn(out), FadeIn(ot), run_time=1.8)

        checks = VGroup(
            Text("checkpoint exists", color=YELLOW).scale(0.22),
            Text("config matches", color=YELLOW).scale(0.22),
            Text("startup smoke pass", color=YELLOW).scale(0.22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.06).to_edge(DOWN).shift(UP * 0.15)
        self.play(FadeIn(checks, shift=UP * 0.05), run_time=1.2)

        self.play(Circumscribe(app, color=GREEN, run_time=1.0))
        self.play(Circumscribe(out, color=TEAL, run_time=1.0))
        self.wait(15.8)
