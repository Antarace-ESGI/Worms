import pygame
from Constants import GRAVITY
from Vector import Vector, zero_vector


def create_box_vertices(width: float, height: float):
    left = -width / 2
    right = left + width
    bottom = -height / 2
    top = bottom + height

    vertices = [Vector(left, top), Vector(right, top), Vector(right, bottom), Vector(left, bottom)]

    return vertices


class Body(object):
    def __init__(self, position: Vector, width: float, height: float, static: bool = False, name: str = "Body"):
        self.position = position
        self.linear_velocity = zero_vector()
        self.vertices = create_box_vertices(width, height)
        self.width, self.height = width, height
        self.static = static
        self.name = name

    def move(self, amount):
        self.position += amount

    def tick(self, dt: float):
        self.vertices = create_box_vertices(self.width, self.height)
        if not self.static:
            self.linear_velocity += GRAVITY * dt
        self.position += self.linear_velocity * dt

    def render(self, surface):
        rect = pygame.rect.Rect(self.position.x, self.position.y, self.width, self.height)
        pygame.draw.rect(surface, (255, 255, 255), rect)
