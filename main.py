from manim import *

GROUP = VGroup()


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


def play_and_fade(self, tex: VGroup, also: [MathTex] = [], secs: int = 1):
    also.append(tex)

    self.play(*[Write(obj) for obj in also])
    self.wait(secs)
    self.play(*[FadeOut(obj) for obj in also])


def play_and_keep(self, tex: MathTex, secs: int = 0.5, desp: int = 1) -> VGroup:
    global GROUP
    self.play(GROUP.animate.shift(UP*desp))
    GROUP.add(tex if len(GROUP) == 0 else tex.next_to(
        GROUP[len(GROUP)-1], DOWN))

    self.wait(secs)
    self.play(Write(GROUP[len(GROUP)-1]))
    self.wait(secs)


def pad(self, tex: MathTex, also: [MathTex] = [], secs: int = 1):
    play_and_fade(self, tex, also, secs)


class Expo1_1B(Scene):
    def construct(self):
        self: Scene

        self.wait(1)

        text1 = MathTex(r"\text{Ejercicio 1}").shift(UP)
        text2 = MathTex(
            r"\text{Archivo 1B - Problema 2:41}").next_to(text1, DOWN)
        text3 = MathTex(r"\text{Julio 2022}").next_to(text2, DOWN)

        self.play(Write(text1), Write(text2), Write(text3))

        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        pad(self, VGroup(
            Text(
                "Demuestre que el límite no existe\n", font_size=23.0
            ).shift(UP/2),
            MathTex(
                r"""\lim_{(x,y)\to(0,0)}\frac{x y^2}{y^4+x^2}"""
            ).shift(DOWN/2)
        ))

        gen7 = VGroup(
            Text(
                "Primero evaluaremos el limite de la forma: \n", font_size=23.0
            ).shift(UP / 2),
            MathTex(
                r"""\lim_{(x,y)\to(0,0)}\frac{x y^2}{y^4+x^2} \text{ donde } x := y"""
            ).shift(DOWN / 2)
        )
        # gen7m = MathTex(r"").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r"""
            \frac{y y^2}{y^4+y^2}
        """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(r"""
                    \frac{y^2y}{y^2(y^2+1)}
                """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(r"""
            \frac{0}{0^2+1}
        """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(r"""
                    \frac{0}{1} = 0
                """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = VGroup(
            Text(
                "Ahora evaluaremos el limite de la forma: \n", font_size=23.0
            ).shift(UP / 2),
            MathTex(
                r"""\lim_{(x,y)\to(0,0)}\frac{x y^2}{y^4+x^2} \text{ donde } x := y^2"""
            ).shift(DOWN / 2)
        )
        # gen7m = MathTex(r"").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r"""
                    \frac{y^2 y^2}{y^4+{y^2}^2}
                """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(r"""
                            \frac{y^4}{y^4+y^4}
                        """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(r"""
                                    \frac{y^4}{y^4(1+1)}
                                """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(r"""
                                            \frac{1}{2}
                                        """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = VGroup(
            MathTex(
                r"""\text{Cuando nos aproximamos por } x := y^2 \text{ el limite tiende a } \frac{1}{2}""", font_size=35.0
            ).shift(UP / 2),
            MathTex(
                r"""\text{Cuando nos aproximamos por } x := y \text{ el limite tiende a } 0""", font_size=35.0
            ).shift(DOWN / 2),
        )
        # gen7m = MathTex(r"").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = VGroup(
            MathTex(
                r"""\text{Por lo tanto, el límite no existe.}""", font_size=35.0
            ),
        )
        # gen7m = MathTex(r"").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        self.play(*[FadeOut(obj) for obj in self.mobjects])


class Expo2_1B(Scene):
    def construct(self):
        self: Scene

        self.wait(1)

        text1 = MathTex(r"\text{Ejercicio 2}").shift(UP)
        text2 = MathTex(
            r"\text{Archivo 1B - Problema 3:54}").next_to(text1, DOWN)
        text3 = MathTex(r"\text{Julio 2022}").next_to(text2, DOWN)

        self.play(Write(text1), Write(text2), Write(text3))

        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        pad(self, VGroup(
            Text(
                "Calcule el límite\n", font_size=23.0
            ).shift(UP/2),
            MathTex(
                r"""\lim_{(x,y)\to(1,1)}\left(\frac{x^2-1}{x-1}+\frac{y-1}{y^2-1}\right)"""
            ).shift(DOWN/2)
        ))

        gen7 = VGroup(
            Text(
                "Intentamos evaluar el limite directamente\n", font_size=23.0
            ).shift(UP / 2),
            MathTex(
                r"""=\left(\frac{1^2-1}{1-1}+\frac{1-1}{1^2-1}\right)"""
            ).shift(DOWN / 2)
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(
            r"""\left(\frac{0}{0}+\frac{0}{0}\right)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = VGroup(
            Text(
                "Obtenemos una indeterminacion, asi que simplificamos\n", font_size=23.0
            ).shift(UP / 2),
            MathTex(
                r"""\lim_{(x,y)\to(1,1)}\left(\frac{x^2-1}{x-1}+\frac{y-1}{y^2-1}\right)"""
            ).shift(DOWN / 2)
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(
            r"""\lim_{(x,y)\to(1,1)}\left(\frac{(x^2-1)(x+1)}{(x-1)(x+1)}+\frac{(y-1)(y+1)}{(y^2-1)(y+1)}\right)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""\lim_{(x,y)\to(1,1)}\left(\frac{(x^2-1)(x+1)}{(x^2-1)}+\frac{(y^2-1)}{(y^2-1)(y+1)}\right)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""\lim_{(x,y)\to(1,1)}\left((x+1)+\frac{1}{y+1}\right)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""\left((1+1)+\frac{1}{1+1}\right)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""\left(2+\frac{1}{2}\right)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""\left(\frac{4}{2}+\frac{1}{2}\right)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""\frac{5}{2}"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        self.play(*[FadeOut(obj) for obj in self.mobjects])


class Expo3_1B(Scene):
    def construct(self):
        self: Scene

        self.wait(1)

        text1 = MathTex(r"\text{Ejercicio 3}").shift(UP)
        text2 = MathTex(
            r"\text{Archivo 1B - Problema 4:13}").next_to(text1, DOWN)
        text3 = MathTex(r"\text{Julio 2022}").next_to(text2, DOWN)

        self.play(Write(text1), Write(text2), Write(text3))

        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        pad(self, VGroup(
            (x0 := Text(
                "Calcule la derivada en la dirección indicada y evalue en el punto\n", font_size=23.0
            ).shift(UP)),
            (x1 := MathTex(
                r"""f(x, y, z)=x \arctan{(y+z)}"""
            ).next_to(x0, DOWN)),
            (x2 := MathTex(
                r"""\text{Direccion: } i+j-k"""
            ).next_to(x1, DOWN)),
            MathTex(
                r"""\text{En el punto: } P(1,0,1)"""
            ).next_to(x2, DOWN)
        ))

        gen7 = VGroup(
            (x1 := Text(
                "Primero obtenemos el vector de direccion\n", font_size=23.0
            ).shift(UP)),
            MathTex(
                r"""i+j-k"""
            ).next_to(x1, DOWN)
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(
            r"""\left(1,0,0\right)+\left(0,1,0\right)-\left(0,0,1\right)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""\left(1,1,-1\right)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = VGroup(
            (x1 := Text(
                "Para obtener la derivada usaremos\n", font_size=23.0
            ).shift(UP)),
            MathTex(
                r"""\lim_{h\to 0}\frac{f(\vec{x}+h\vec{u})-f(\vec{h})}{h}"""
            ).next_to(x1, DOWN)
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = VGroup(
            (x1 := Text(
                "Dividiremos el problema en varios\n", font_size=23.0
            ).shift(UP)),
            (x2 := Text(
                "Primero calculamos\n", font_size=23.0
            ).next_to(x1, DOWN)),
            MathTex(
                r"""\vec{x} + h\vec{u}"""
            ).next_to(x2, DOWN)
        )

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(
            r"""\left(x, y, z\right) + h \left(1, 1, -1\right)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""\left(x, y, z\right) + \left(h, h, -h\right)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""\left(x+h, y+h, z-h\right)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = VGroup(
            (x1 := Text(
                "Ahora\n", font_size=23.0
            ).shift(UP)),
            MathTex(
                r"""f(\vec{x}+h\vec{u})"""
            ).next_to(x1, DOWN)
        )

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(
            r"""f(x+h, y+h, z-h)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""(x+h)\arctan(y+h+z-h)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""(x+h)\arctan(y+z)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = VGroup(
            (x1 := Text(
                "Con esto, planteamos el límite\n", font_size=23.0
            ).shift(UP)),
            MathTex(
                r"""\lim_{h\to 0}\frac{f(\vec{x}+h\vec{u})-f(\vec{h})}{h}"""
            ).next_to(x1, DOWN)
        )

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(
            r"""\lim_{h\to 0}\frac{(x+h)\arctan(y+z)-x\arctan(y+z)}{h}"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""\lim_{h\to 0}\frac{x\arctan(y+z)+h\arctan(y+z)-x\arctan(y+z)}{h}"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""\lim_{h\to 0}\frac{h\arctan(y+z)}{h}"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""\lim_{h\to 0}\arctan(y+z)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(
            r"""\arctan(y+z)"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = VGroup(
            (x1 := Text(
                "Evaluamos la derivada en el punto (1,0,1)\n", font_size=23.0
            ).shift(UP)),
            MathTex(
                r"""\arctan(0+1)"""
            ).next_to(x1, DOWN)
        )

        self.play(*[obj.animate.shift(UP * 3) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(
            r"""\frac{\pi}{4}"""
        )
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        self.play(*[FadeOut(obj) for obj in self.mobjects])


class Expo1_2A(Scene):
    def construct(self):
        self: Scene

        self.wait(1)

        text1 = MathTex(r"\text{Ejercicio 1}").shift(UP)
        text2 = MathTex(
            r"\text{Archivo 2A - Problema 5:5}").next_to(text1, DOWN)
        text3 = MathTex(r"\text{Julio 2022}").next_to(text2, DOWN)

        self.play(Write(text1), Write(text2), Write(text3))

        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        pad(self, VGroup(
            Text(
                "Calcule la matriz Jacobiana en el punto que se indica\n", font_size=23.0
            ).shift(UP/2),
            MathTex(
                r"""x_0 = (1, 1,\pi)"""
            ).shift(DOWN / 3),
            MathTex(
                r"""f(x,y,z) = (x^2 + xy, x\sin{(yz)})"""
            ).shift(DOWN)
        ).shift(UP))

        gen7 = MathTex(r"""
            \text{Primero calculamos el Jacobiano}
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r"""
            \text{J}_f = 
\left(
\begin{array}{ccc}
\frac{ \partial_{\left(x^2 + xy\right)}}{\partial x} & \frac{ \partial_{\left(x^2 + xy\right)}}{\partial y} & \frac{ \partial_{\left(x^2 + xy\right)}}{\partial z} \\
\frac{ \partial_{\left(x\sin{(yz)}\right)}}{\partial x} & \frac{ \partial_{\left(x\sin{(yz)}\right)}}{\partial y} & \frac{ \partial_{\left(x\sin{(yz)}\right)}}{\partial z} \\
\end{array}
\right)
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
\left(
\begin{array}{ccc}
2x+y & x & 0 \\
\sin{(yz)} & xz\cos{(yz)} & xy\cos{(yz)} \\
\end{array}
\right)
        """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(r""" 
\text{Y ahora evaluamos } \text{J}_f(1, 1, \pi)
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
\left(
\begin{array}{ccc}
2(1)+(1) & (1) & 0 \\
\sin{(1\cdot\pi)} & (1\cdot\pi)\cos{(1\cdot\pi)} & (1\cdot1)\cos{(1\cdot\pi)} \\
\end{array}
\right)
        """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(r""" 
\left(
\begin{array}{ccc}
2+1 & 1 & 0 \\
\sin{\pi} & \pi\cos{\pi} & \cos{\pi} \\
\end{array}
\right)
        """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(r""" 
\left(
\begin{array}{ccc}
3 & 1 & 0 \\
0 & -\pi & -1 \\
\end{array}
\right)
        """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        self.play(*[FadeOut(obj) for obj in self.mobjects])


class Expo2_2A(Scene):
    def construct(self):
        self: Scene

        self.wait(1)

        text1 = MathTex(r"\text{Ejercicio 2}").shift(UP)
        text2 = MathTex(
            r"\text{Archivo 2A - Problema 3:7}").next_to(text1, DOWN)
        text3 = MathTex(r"\text{Julio 2022}").next_to(text2, DOWN)

        self.play(Write(text1), Write(text2), Write(text3))

        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        pad(self, VGroup(
            Text(
                "Utilizando multiplicadores de Lagrange,\n"
                "encuentre los valores extremos indicados", font_size=23.0
            ).shift(UP/2),
            MathTex(
                r"""\text{Restriccion: } 2x + y = 100"""
            ).shift(DOWN / 3),
            MathTex(
                r"""\text{Optimizar: } f(x,y) = 2x+2xy+y"""
            ).shift(DOWN)).shift(UP), secs=3.5)

        gen7 = MathTex(r"""
            \text{Construimos } g(x, y) \text{ a partir de la restriccion}
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
g(x,y) =  2x + y - 100
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
\nabla_f = \lambda \nabla_g
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
\nabla_{(x,y)}(2x+2xy+y) = \lambda \nabla_{(x,y)}(2x + y - 100)
        """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(r""" 
(2+2y, 2x+1) = \lambda (2, 1)
        """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(r""" 
(2+2y, 2x+1) = (2 \lambda , \lambda)
        """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(r""" 
2+2y = 2 \lambda\\
2x+1=\lambda
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
\frac{2+2y}{2} = \lambda\\
2x+1=\lambda
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
1+y = \lambda\\
2x+1=\lambda
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
1+y =2x+1
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
y =2x
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
\text{Sustituimos en la restriccion}
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
2x + 2x = 100
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
x = 100/4 = 25
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
\text{Y ahora obtenemos y}
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
y =2(25) = 50
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
\text{Por ultimo evaluamos } f(25, 50)
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
f(25, 50) = 2\cdot25+2\cdot25\cdot50+50
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = MathTex(r""" 
2600
        """)
        gen7m = MathTex(r"=").next_to(gen7, LEFT)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        gen7 = MathTex(r""" 
\therefore \text{ el punto máximo es } (25, 50, 2600)
        """)

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7), Write(gen7m))
        self.wait(1)

        self.play(*[FadeOut(obj) for obj in self.mobjects])


class Expo1_1A(Scene):
    def construct(self):
        self: Scene

        self.wait(1)

        text1 = MathTex(r"\text{Ejercicio 1}").shift(UP)
        text2 = MathTex(
            r"\text{Archivo 1A - Problema 1:1}").next_to(text1, DOWN)
        text3 = MathTex(r"\text{Julio 2022}").next_to(text2, DOWN)

        self.play(Write(text1), Write(text2), Write(text3))

        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        pad(self, VGroup(
            (x0 := Text(
                "Dibuje las curvas de nivel correspondientes a c\n", font_size=23.0
            ).shift(UP)),
            (x1 := MathTex(
                r"""f(x, y)=x-y"""
            ).next_to(x0, DOWN)),
            MathTex(
                r"""\text{c} = -2, 0, 2"""
            ).next_to(x1, DOWN),
        ))

        gen7 = VGroup(
            MathTex(
                r"""x-y = -2"""
            )
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = VGroup(
            MathTex(
                r"""-x+y = 2"""
            )
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = VGroup(
            MathTex(
                r"""y = 2+x"""
            )
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = VGroup(
            MathTex(
                r"""f(x, 2+x) = x - 2 - x"""
            )
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = VGroup(
            MathTex(
                r"""f(x, 2+x) = - 2"""
            )
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
        )

        graph = FunctionGraph(
            lambda x: -2,
            color=YELLOW
        )

        self.play(*[FadeOut(obj) for obj in self.mobjects])
        self.play(FadeIn(gen7), Write(graph))
        self.wait(1)

        graph2 = FunctionGraph(
            lambda x: 0,
            color=RED
        )

        graph3 = FunctionGraph(
            lambda x: 2,
            color=ORANGE
        )

        self.play(FadeIn(graph2), Write(graph3))

        self.wait(5)

        self.play(*[FadeOut(obj) for obj in self.mobjects])


class Expo2_1A(Scene):
    def construct(self):
        self: Scene

        self.wait(1)

        text1 = MathTex(r"\text{Ejercicio 2}").shift(UP)
        text2 = MathTex(
            r"\text{Archivo 1A - Problema 3:39}").next_to(text1, DOWN)
        text3 = MathTex(r"\text{Julio 2022}").next_to(text2, DOWN)

        self.play(Write(text1), Write(text2), Write(text3))

        self.wait(3)
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        pad(self, VGroup(
            Text(
                "Un metal solido ocupa una región en el espacio 3D\n"
                "\n"
                "La temperatura T  en el punto (x,y,z) en el solido\n"
                "\n"
                "es inversamente proporcional a la distancia al origen.", font_size=23.0
            )
        ), secs=10)

        gen7 = VGroup(
            MathTex(
                r"""\text{Distancia: } \sqrt{x^2 + y^2 + z^2}"""
            )
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = VGroup(
            MathTex(
                r"""T(x,y,z) = \frac{k}{  \sqrt{x^2 + y^2 + z^2}}"""
            )
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = VGroup(
            (x1 := Text(
                "Sabemos que en (1,2,1) la temperatura es 50.\n", font_size=23.0
            ).shift(UP)),
            MathTex(
                r"""50 = \frac{k}{  \sqrt{1^2 + 2^2 + 1^2}}"""
            ).next_to(x1, DOWN)
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = VGroup(
            MathTex(
                r"""
                    50 = \frac{k}{  \sqrt{1 + 4 + 1}}
                """
            )
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = VGroup(
            MathTex(
                r"""
                    50\sqrt{6} = k
                """
            )
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = VGroup(
            MathTex(
                r"""T(x,y,z) = \frac{50\sqrt{6}}{  \sqrt{x^2 + y^2 + z^2}}"""
            )
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = VGroup(
            MathTex(
                r"""T(4,0,3) = \frac{50\sqrt{6}}{  \sqrt{4^2 + 0^2 + 3^2}}"""
            )
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = VGroup(
            MathTex(
                r"""T(4,0,3) = \frac{50\sqrt{6}}{  \sqrt{25}}"""
            )
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        gen7 = VGroup(
            MathTex(
                r"""T(4,0,3) = 10\sqrt{6}"""
            )
        )

        self.play(*[obj.animate.shift(UP * 2) for obj in self.mobjects])
        self.play(Write(gen7))
        self.wait(1)

        self.play(*[FadeOut(obj) for obj in self.mobjects])
