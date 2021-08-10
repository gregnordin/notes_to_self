from manim import *


class Slices(ThreeDScene):

    x_axis_label = "$x$"
    y_axis_label = "$y$"
    z_axis_label = "$z$"
    basis_i_color = GREEN
    basis_j_color = RED
    basis_k_color = GOLD

    def create_matrix(self, np_matrix):

        m = Matrix(np_matrix)

        m.scale(0.5)
        m.set_column_colors(self.basis_i_color,
                            self.basis_j_color, self.basis_k_color)

        m.to_corner(UP + LEFT)

        return m

    def construct(self):

        # axes & camera
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())
        self.add(axes)

        # matrix
        M = np.array([
            [3, 0, 0],
            [0, 3, 0],
            [0, 0, 0.5]
        ])
        matrix = self.create_matrix(M)
        self.add_fixed_in_frame_mobjects(matrix)

        # cube
        cube = Cube(side_length=1, fill_color=BLUE,
                    stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        # Animation
        self.wait(0.5)
        self.play(
            FadeIn(cube),
        )
        self.wait()

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
        )
        self.wait()
