from manim import *


class AttentionScoreFlowAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Scene 1: intro
        title = Text("Ch3 Attention Score Flow", color=WHITE).scale(0.72).to_edge(UP)
        subtitle = Text("query-key matching -> weighted context", color=TEAL).scale(0.42).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.8)

        # Scene 2: token row
        tokens = ["The", "drone", "tracks", "it"]
        row = VGroup(
            *[
                RoundedRectangle(width=1.0, height=0.58, corner_radius=0.1, color=BLUE).set_fill(BLUE, opacity=0.12).add(
                    Text(t, color=WHITE).scale(0.31)
                )
                for t in tokens
            ]
        ).arrange(RIGHT, buff=0.16).shift(UP * 0.9)
        self.play(LaggedStart(*[FadeIn(x, shift=UP * 0.15) for x in row], lag_ratio=0.14), run_time=2.3)
        self.wait(1.3)

        # Scene 3: Q, K, V projections
        q = Text("Q", color=YELLOW).scale(0.6).next_to(row[3], DOWN, buff=0.28)
        k1 = Text("K", color=GREEN).scale(0.6).next_to(row[1], DOWN, buff=0.28)
        k2 = Text("K", color=GREEN).scale(0.6).next_to(row[2], DOWN, buff=0.28)
        a1 = Arrow(q.get_top(), row[3].get_bottom(), buff=0.05, color=YELLOW)
        b1 = Arrow(k1.get_top(), row[1].get_bottom(), buff=0.05, color=GREEN)
        b2 = Arrow(k2.get_top(), row[2].get_bottom(), buff=0.05, color=GREEN)
        self.play(FadeIn(q), FadeIn(k1), FadeIn(k2), Create(a1), Create(b1), Create(b2), run_time=2.4)
        self.wait(1.6)

        # Scene 4: score matrix and softmax (using Text to avoid LaTeX)
        def make_text_matrix(values, color):
            rows = VGroup()
            for row in values:
                row_text = Text("  ".join(row), color=color, font="Menlo").scale(0.24)
                rows.add(row_text)
            return rows.arrange(DOWN, buff=0.08)
        
        score_vals = [["1.9", "0.4", "-0.6", "0.1"], ["0.7", "1.1", "0.0", "-0.3"], ["0.2", "0.5", "1.5", "0.2"], ["0.1", "0.8", "0.9", "1.3"]]
        prob_vals = [["0.62", "0.18", "0.09", "0.11"], ["0.24", "0.36", "0.21", "0.19"], ["0.11", "0.15", "0.58", "0.16"], ["0.10", "0.28", "0.31", "0.31"]]
        
        mat = make_text_matrix(score_vals, WHITE).to_edge(LEFT).shift(DOWN * 0.5)
        mat_lbl = Text("scores = QK^T / sqrt(d)", color=WHITE).scale(0.32).next_to(mat, UP, buff=0.1)
        probs = make_text_matrix(prob_vals, TEAL).to_edge(RIGHT).shift(DOWN * 0.5)
        probs_lbl = Text("softmax(scores)", color=TEAL).scale(0.32).next_to(probs, UP, buff=0.1)
        arrow = Arrow(mat.get_right(), probs.get_left(), buff=0.15, color=TEAL)
        self.play(Create(mat), FadeIn(mat_lbl), run_time=2.2)
        self.play(Create(arrow), Create(probs), FadeIn(probs_lbl), run_time=2.3)
        self.wait(1.8)

        # Scene 5: weighted sum output
        out = Text("context vector for 'it'", color=YELLOW).scale(0.42).to_edge(DOWN)
        note = Text("higher weights -> stronger influence", color=GREEN).scale(0.32).next_to(out, UP, buff=0.12)
        self.play(Write(out), FadeIn(note, shift=UP * 0.15), run_time=1.8)
        self.play(Circumscribe(probs, color=TEAL, run_time=1.3))
        self.wait(8.4)
