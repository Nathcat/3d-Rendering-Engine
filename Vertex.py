import numpy as np


class Vertex:
    def __init__(self, position):
        self.x, self.y, self.z = position

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def flatten(self, camera):
        position = self.get_3d_position()
        camera_position = camera.get_3d_position()

        new_vertex_position = position - camera_position

        depth = new_vertex_position[2]

        offset = depth / camera_position[2]

        position_flattened = np.array([new_vertex_position[0], new_vertex_position[1]], dtype='float64')
        position_flattened *= np.abs(offset)

        return tuple(position_flattened)

    def get_3d_position(self):
        return np.array([self.x, self.y, self.z])
