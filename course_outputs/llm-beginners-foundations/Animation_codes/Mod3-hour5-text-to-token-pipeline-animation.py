from manim import *


class TextToTokenPipelineAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        # Scene 1: Title
        title = Text("Ch2: Text -> Tokens -> IDs -> Embeddings", color=WHITE).scale(0.62).to_edge(UP)
        subtitle = Text("Data pipeline before model training", color=TEAL).scale(0.42).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.8)

        # Scene 2: Raw text into subwords
        raw = Text("unbelievable mission report", color=WHITE).scale(0.52).shift(UP * 0.95)
        self.play(Write(raw), run_time=1.6)

        tokens = VGroup(
            *[
                RoundedRectangle(width=1.35, height=0.58, corner_radius=0.1, color=BLUE).add(
                    Text(t, color=WHITE).scale(0.3)
                )
                for t in ["un", "believ", "able", " mission", " report"]
            ]
        ).arrange(RIGHT, buff=0.14).scale(0.86).shift(DOWN * 0.15)
        self.play(TransformFromCopy(raw, tokens), run_time=2.3)
        self.wait(1.8)

        # Scene 3: Token IDs
        ids = [418, 9211, 517, 2291, 4738]
        id_boxes = VGroup(
            *[
                RoundedRectangle(width=1.0, height=0.48, corner_radius=0.08, color=TEAL).set_fill(TEAL, opacity=0.15).add(
                    Text(str(i), color=WHITE).scale(0.28)
                )
                for i in ids
            ]
        ).arrange(RIGHT, buff=0.2).scale(0.9).next_to(tokens, DOWN, buff=0.45)
        arrows = VGroup(*[Arrow(tokens[i].get_bottom(), id_boxes[i].get_top(), buff=0.06, color=GREY_B) for i in range(len(ids))])
        self.play(Create(arrows), FadeIn(id_boxes), run_time=2.2)
        id_title = Text("Vocabulary lookup converts tokens to IDs", color=GREEN).scale(0.34).next_to(id_boxes, DOWN, buff=0.18)
        self.play(FadeIn(id_title, shift=UP * 0.15), run_time=1.0)
        self.wait(1.8)

        # Scene 4: IDs to embedding vectors
        emb_title = Text("Embedding lookup (ID -> dense vector)", color=YELLOW).scale(0.36).to_edge(LEFT).shift(DOWN * 0.45)
        vec_card = RoundedRectangle(width=4.8, height=2.1, corner_radius=0.12, color=PURPLE).set_fill(PURPLE, opacity=0.08)
        vec_card.to_edge(RIGHT).shift(DOWN * 0.35)
        # Use Text instead of Matrix to avoid LaTeX dependency
        mat_text = VGroup(
            Text("[ 0.12  -0.44   0.91  ... ]", color=WHITE, font="Menlo").scale(0.28),
            Text("[-0.03   0.52  -0.11  ... ]", color=WHITE, font="Menlo").scale(0.28),
            Text("[ 0.66   0.08  -0.25  ... ]", color=WHITE, font="Menlo").scale(0.28),
        ).arrange(DOWN, buff=0.15).move_to(vec_card)
        self.play(Write(emb_title), Create(vec_card), FadeIn(mat_text), run_time=2.8)
        self.wait(2.0)

        # Scene 5: Final tensor shape
        shape = Text("(batch, seq, dim) = (1, 5, 768)", color=WHITE, font="Menlo").scale(0.55).to_edge(DOWN)
        note = Text("Model consumes tensors, not raw text", color=GREEN).scale(0.34).next_to(shape, UP, buff=0.12)
        self.play(Write(shape), FadeIn(note, shift=UP * 0.15), run_time=1.9)
        self.play(Circumscribe(id_boxes, color=TEAL, run_time=1.3))
        self.wait(6.7)
