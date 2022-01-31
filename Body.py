import pygame

from Constants import SPEED, GRAVITY, FRICTION
from Vector import Vector, Point, zero
from typing import Tuple


class Body(object):
    def __init__(self, pos: Point, size: Point, color: Tuple[int, int, int] = (255, 255, 255), has_gravity: bool = True,
                 has_friction=True):
        self._color = color
        self.pos = pos
        self._size = size
        self.velocity = Vector(zero(), zero())
        self._has_gravity = has_gravity
        self._has_friction = has_friction
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

        self.pos += self.velocity

        if self._has_friction:
            self.velocity *= FRICTION

    def render(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self._color, self.rect)

        vec = self.velocity.clone() * 100
        pygame.draw.line(surface, (0, 0, 0), self.pos.to_tuple(), (self.pos + vec).to_tuple())

        return

    def change_color(self, new_color):
        self._color = new_color
        return

    def handle_event(self, event: pygame.event):
        pass
