import pygame

GRAVITY = 9.81
SPEED = 10


class Body(object):
    def __init__(self, pos: pygame.math.Vector2, size: pygame.math.Vector2, has_gravity: bool = True):
        self._color = (255, 255, 255)
        self._pos = pos
        self._size = size
        self._velocity = pygame.math.Vector2(0, 0)
        self._has_gravity = has_gravity
        self.rect = pygame.rect.Rect(self._pos.x, self._pos.y, self._size.x, self._size.y)
        return

    def apply_force(self, force: pygame.math.Vector2):
        self._velocity += force
        pass

    def physics(self, world: "list[Body]", dt):
        self.rect = pygame.rect.Rect(self._pos.x, self._pos.y, self._size.x, self._size.y)

        if self._has_gravity:
            self._velocity.y += GRAVITY * dt

        for obj in world:
            if obj is not self and self.rect.colliderect(obj.rect):
                self._velocity = self._velocity.rotate(180)
                obj._velocity = obj._velocity.rotate(180)

        self._pos += self._velocity * dt * SPEED

    def render(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self._color, self.rect)

        return

    def change_color(self, new_color):
        self._color = new_color
        return

    def handle_event(self, event: pygame.event):
        pass
