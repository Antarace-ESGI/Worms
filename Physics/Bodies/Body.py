from Constants import *
from Physics.Vector import zero_vector
from Utils import draw_outline_rect


def create_box_vertices(width: float, height: float):
    left = -width / 2
    right = left + width
    bottom = -height / 2
    top = bottom + height

    vertices = [
        Vector(left, top),
        Vector(right, top),
        Vector(right, bottom),
        Vector(left, bottom),
    ]

    return vertices


class Body(object):
    def __init__(self, position: Vector, width: float, height: float, static: bool = False):
        self.position = position + Vector(width / 2, height / 2)
        self.linear_velocity = zero_vector()
        self.vertices = create_box_vertices(width, height)
        self.width, self.height = width, height
        self.static = static

    def move(self, amount: Vector):
        self.position += amount

    def tick(self, dt: float):
        if not self.static:
            self.linear_velocity += GRAVITY * dt
        self.position += self.linear_velocity * dt

    def get_transformed_vertices(self):
        return [vertex + self.position for vertex in self.vertices]

    def render(self, surface):
        draw_outline_rect(surface, self.position.x - self.width / 2, self.position.y - self.height / 2, self.width, self.height, WHITE_COLOR, BLACK_COLOR, 1)

    def collide(self, body, normal, depth):
        pass

    def destroy(self):
        pass
