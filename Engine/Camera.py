import numpy as np
import matplotlib.pyplot as plt


class Camera:
    def __init__(self, position):
        self.x, self.y, self.z = position

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def get_3d_position(self):
        return np.array([self.x, self.y, self.z])

    def render(self, vertices):
        for x in range(0, len(vertices)):
            vertices[x] = vertices[x].flatten(self)

        x = []
        y = []

        for i in range(0, len(vertices)):
            x_, y_ = vertices[i]
            x.append(x_)
            y.append(y_)

        plt.plot(x, y)
        plt.show()
