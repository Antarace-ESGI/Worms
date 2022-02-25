import pygame
from Constants import *
from Vector import Vector, zero_vector


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
    def __init__(self, position: Vector, width: float, height: float, static: bool = False, name: str = "Body"):
        self.position = position + Vector(width / 2, height / 2)
        self.linear_velocity = zero_vector()
        self.vertices = create_box_vertices(width, height)
        self.width, self.height = width, height
        self.static = static
        self.name = name
        self.is_colliding = False

    def move(self, amount: Vector):
        self.position += amount

    def tick(self, dt: float):
        if not self.static:
            self.linear_velocity += GRAVITY * dt
        self.position += self.linear_velocity * dt

    def get_transformed_vertices(self):
        return [vertex + self.position for vertex in self.vertices]

    def render(self, surface):
        color = RED if self.is_colliding else WHITE
        rect = pygame.rect.Rect(self.position.x - self.width / 2, self.position.y - self.height / 2, self.width, self.height)
        outline_rect = pygame.rect.Rect(self.position.x - self.width / 2 - 1, self.position.y - self.height / 2 - 1, self.width + 2, self.height + 2)
        pygame.draw.rect(surface, BLACK, outline_rect)
        pygame.draw.rect(surface, color, rect)
