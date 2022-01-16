import pygame

from Constants import SPEED, GRAVITY, FRICTION
from Vector import Vector, Point, zero


class Body(object):
    def __init__(self, pos: Point, size: Point, has_gravity: bool = True):
        self._color = (255, 255, 255)
        self.pos = pos
        self._size = size
        self.velocity = Vector(zero(), zero())
        self._has_gravity = has_gravity
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y, self._size.x, self._size.y)
        return

    def apply_force(self, force: Point):
        self.velocity.x += force.x
        self.velocity.y += force.y
        pass

    def physics(self, world: "list[Body]", dt: float):
        self.rect = pygame.rect.Rect(self.pos.x, self.pos.y, self._size.x, self._size.y)

        if self._has_gravity:
            self.velocity.y += GRAVITY * dt * SPEED

        # Collisions
        for body in world:
            if body.velocity.intersect(self.velocity):
                print("intersect")

        self.pos += self.velocity

        self.velocity *= FRICTION

    def render(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self._color, self.rect)

        return

    def change_color(self, new_color):
        self._color = new_color
        return

    def handle_event(self, event: pygame.event):
        pass
