from manim import *


def animate_change(self, text, text0, text3, text3_pos, offset, n1, n2):
    text_b = MathTex(r"-2 {(" + str(n1) + "})} + {(" +
                     str(n2) + ")}").next_to(text, DOWN).shift(DOWN)

    if offset == 5:
        text3[0][9 + offset:9 + offset + 2].set_color(YELLOW)
        text3[0][1 + offset:1 + offset + 2].set_color(YELLOW)
        text_b[0][3:5].set_color(YELLOW)
        text_b[0][8:10].set_color(YELLOW)
    else:
        text3[0][10 + offset].set_color(YELLOW)
        text3[0][2 + offset].set_color(YELLOW)
        text_b[0][3].set_color(YELLOW)
        text_b[0][7].set_color(YELLOW)

    self.play(AnimationGroup(Transform(text0, text3), FadeIn(text_b)))
    self.wait(0.5)
    self.play(AnimationGroup(Transform(text0, text3_pos), FadeOut(text_b)))
    self.wait(0.1)

    if offset == 5:
        text3[0][9 + offset:9 + offset + 2].set_color(WHITE)
        text3[0][1 + offset:1 + offset + 2].set_color(WHITE)
    else:
        text3[0][10 + offset].set_color(WHITE)
        text3[0][2 + offset].set_color(WHITE)

    self.play(Transform(text0, text3_pos))


class Expo1(Scene):
    def construct(self):
        self: Scene

        #corona = ImageMobject("./Intro.jpg")
        # corona.scale(0.4)

        # self.play(FadeIn(corona))

        self.wait(3)

        self.play(*[FadeOut(obj) for obj in self.mobjects])

        text1 = MathTex(r"\text{Ejercicio}").shift(UP)
        text2 = MathTex(r"\text{Archivo 1 - Problema 1D}").next_to(text1, DOWN)
        text3 = MathTex(r"\text{Mayo 2022}").next_to(text2, DOWN)

        self.play(Write(text1), Write(text2), Write(text3))

        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        text0 = Text(
            "Resolver los siguientes sistemas de ecuaciones por medio\n"
            "de Gauss y de interpretacion geometrica del conjunto solucion", font_size=23.0
        )
