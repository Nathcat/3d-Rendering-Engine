
from Vertex import *
from RenderingEngine import *


vertices = [Vertex((-1, -1, -1)),
            Vertex((1, -1, -1)),
            Vertex((1, -1, 1)),
            Vertex((-1, -1, 1)),
            Vertex((-1, -1, -1)),]

engine = Engine(vertices, (0, 0, 5))

engine.render()
