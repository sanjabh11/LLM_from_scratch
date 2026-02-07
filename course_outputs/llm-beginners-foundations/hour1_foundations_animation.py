from manim import *


class FoundationsRoadmapAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Scene 1: Course scope map
        title = Text("AI -> GenAI -> LLMs", color=WHITE).scale(0.9).to_edge(UP)
        subtitle = Text("Beginner Roadmap (2 Hours)", color=TEAL).scale(0.5).next_to(title, DOWN)
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.wait(1)

        # Scene 2: LLM lifecycle pipeline
        labels = ["Text Data", "Tokens", "Embeddings", "Transformer", "Output"]
        boxes = VGroup(
            *[
                RoundedRectangle(width=1.9, height=0.8, corner_radius=0.15, color=BLUE).add(
                    Text(lbl, color=WHITE).scale(0.32)
                )
                for lbl in labels
            ]
        ).arrange(RIGHT, buff=0.25).scale(0.9).next_to(subtitle, DOWN, buff=0.8)
        arrows = VGroup(*[Arrow(boxes[i].get_right(), boxes[i + 1].get_left(), buff=0.08, color=GREEN) for i in range(4)])
        self.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.15), run_time=3)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.15), run_time=2)
        self.wait(1)

        # Scene 3: Repository path for first module
        repo_title = Text("Repository Path for Today", color=TEAL).scale(0.48).to_edge(LEFT).shift(UP * 1.2)
        setup_box = SurroundingRectangle(Text("setup/", color=WHITE).scale(0.44), color=BLUE, buff=0.12)
        ch1_box = SurroundingRectangle(Text("ch01/", color=WHITE).scale(0.44), color=PURPLE, buff=0.12)
        app_box = SurroundingRectangle(Text("appendix-A/", color=WHITE).scale(0.44), color=GREEN, buff=0.12)
        labels_group = VGroup(
            VGroup(setup_box, Text("setup/", color=WHITE).scale(0.44).move_to(setup_box)),
            VGroup(ch1_box, Text("ch01/", color=WHITE).scale(0.44).move_to(ch1_box)),
            VGroup(app_box, Text("appendix-A/", color=WHITE).scale(0.44).move_to(app_box)),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(repo_title, DOWN, aligned_edge=LEFT, buff=0.35)
        self.play(Write(repo_title), run_time=1)
        self.play(LaggedStart(*[FadeIn(g, shift=RIGHT * 0.2) for g in labels_group], lag_ratio=0.2), run_time=2)
        self.wait(1)

        # Scene 4: Beginner progression
        start = Circle(radius=0.32, color=BLUE).set_fill(BLUE, opacity=0.2)
        mid = Circle(radius=0.32, color=TEAL).set_fill(TEAL, opacity=0.2)
        end = Circle(radius=0.32, color=GREEN).set_fill(GREEN, opacity=0.2)
        progress = VGroup(start, mid, end).arrange(RIGHT, buff=1.0).to_edge(DOWN).shift(UP * 0.5)
        tags = VGroup(
            Text("Python Basics", color=WHITE).scale(0.32).next_to(start, DOWN, buff=0.15),
            Text("Tensor Thinking", color=WHITE).scale(0.32).next_to(mid, DOWN, buff=0.15),
            Text("Train Tiny Model", color=WHITE).scale(0.32).next_to(end, DOWN, buff=0.15),
        )
        links = VGroup(
            Arrow(start.get_right(), mid.get_left(), buff=0.08, color=WHITE),
            Arrow(mid.get_right(), end.get_left(), buff=0.08, color=WHITE),
        )
        self.play(FadeIn(progress), FadeIn(tags), run_time=1.8)
        self.play(Create(links), run_time=1.2)
        self.wait(1)

        # Scene 5: Summary lock-in
        summary = Text("Goal: Understand before coding", color=YELLOW).scale(0.55).to_edge(DOWN)
        self.play(Circumscribe(boxes[2], color=TEAL, run_time=1.5))
        self.play(Write(summary), run_time=1.5)
        self.wait(2)

