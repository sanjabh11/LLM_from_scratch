from manim import *


class CheckpointAndGenerationAnimation(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        title = Text("Ch5 Core: Checkpoint -> Generation", color=WHITE).scale(0.7).to_edge(UP)
        subtitle = Text("save weights, reload model, decode text", color=TEAL).scale(0.36).next_to(title, DOWN)
        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.2)
        self.wait(1.6)

        model_box = RoundedRectangle(width=2.6, height=1.0, corner_radius=0.12, color=GREEN).set_fill(GREEN, opacity=0.12).shift(LEFT * 3.2)
        model_lbl = Text("GPTModel\n(trained)", color=WHITE).scale(0.28).move_to(model_box)

        ckpt_box = RoundedRectangle(width=2.6, height=1.0, corner_radius=0.12, color=BLUE).set_fill(BLUE, opacity=0.12)
        ckpt_lbl = Text("model.pth\n(state_dict)", color=WHITE).scale(0.28).move_to(ckpt_box)

        load_box = RoundedRectangle(width=2.9, height=1.0, corner_radius=0.12, color=PURPLE).set_fill(PURPLE, opacity=0.12).shift(RIGHT * 3.3)
        load_lbl = Text("Reload +\nGenerate", color=WHITE).scale(0.29).move_to(load_box)

        arr1 = Arrow(model_box.get_right(), ckpt_box.get_left(), buff=0.08, color=GREY_B)
        arr2 = Arrow(ckpt_box.get_right(), load_box.get_left(), buff=0.08, color=GREY_B)

        self.play(FadeIn(model_box), FadeIn(model_lbl), run_time=1.5)
        self.play(Create(arr1), FadeIn(ckpt_box), FadeIn(ckpt_lbl), run_time=1.8)
        self.play(Create(arr2), FadeIn(load_box), FadeIn(load_lbl), run_time=1.8)
        self.wait(1.3)

        prompt = RoundedRectangle(width=3.6, height=0.62, corner_radius=0.1, color=YELLOW).set_fill(YELLOW, opacity=0.14).to_edge(LEFT).shift(DOWN * 1.6)
        p_lbl = Text('Prompt: "Every effort moves you"', color=WHITE).scale(0.28).move_to(prompt)
        gen = RoundedRectangle(width=4.8, height=0.95, corner_radius=0.1, color=TEAL).set_fill(TEAL, opacity=0.12).to_edge(RIGHT).shift(DOWN * 1.7)
        g_lbl = Text("Generated continuation\n(top-k + temperature)", color=WHITE).scale(0.28).move_to(gen)
        arr3 = Arrow(prompt.get_right(), gen.get_left(), buff=0.1, color=YELLOW)

        self.play(FadeIn(prompt), FadeIn(p_lbl), run_time=1.4)
        self.play(Create(arr3), FadeIn(gen), FadeIn(g_lbl), run_time=1.8)

        knobs = VGroup(
            RoundedRectangle(width=1.6, height=0.5, corner_radius=0.08, color=ORANGE).set_fill(ORANGE, opacity=0.12),
            RoundedRectangle(width=1.6, height=0.5, corner_radius=0.08, color=ORANGE).set_fill(ORANGE, opacity=0.12),
        ).arrange(RIGHT, buff=0.25).next_to(gen, UP, buff=0.25)
        k_lbl = Text("top_k=50", color=WHITE).scale(0.25).move_to(knobs[0])
        t_lbl = Text("temp=1.0", color=WHITE).scale(0.25).move_to(knobs[1])
        self.play(FadeIn(knobs), FadeIn(k_lbl), FadeIn(t_lbl), run_time=1.6)

        verify = RoundedRectangle(width=6.6, height=0.65, corner_radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.12).to_edge(DOWN)
        v_lbl = Text("Validate shapes and config match before loading weights", color=WHITE).scale(0.28).move_to(verify)
        self.play(FadeIn(verify), FadeIn(v_lbl), run_time=1.7)

        self.play(Circumscribe(ckpt_box, color=BLUE, run_time=1.0))
        self.play(Circumscribe(load_box, color=PURPLE, run_time=1.0))
        self.wait(10.7)
