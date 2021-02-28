from Vertex import *
from Camera import *


class Engine:
    def __init__(self, vertices, camera_position):
        self.vertices = vertices
        self.camera = Camera(camera_position)
        self.version = "0.1"

    def render(self):
        self.camera.render(self.vertices)

    def __str__(self):
        return f"3D Rendering Engine by Nathcat, Version: {self.version}, Vertices: {self.vertices}, Camera: {self.camera}"
