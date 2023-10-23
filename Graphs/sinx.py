from manim import *
import numpy as np

class cisname(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=YELLOW)

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        Name = Tex('Designed by Uttam').scale(1.5)

        self.play(Create(axes),run_time =3)
        self.play(Create(axes_labels), run_time = 2)
        self.play(Create(sin_graph),run_time = 4)

        self.play(Write(sin_label), run_time =1)
        self.play(Transform(sin_graph, cos_graph), run_time = 4)
        self.play(Transform(sin_label,cos_label), run_time = 2)

        group1  = Group(axes, axes_labels , sin_graph, cos_graph , sin_label , cos_label )
        self.play(Transform(group1, Name), run_time = 1.5)

        self.wait()
        
    
      