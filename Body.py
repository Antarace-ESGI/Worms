import pygame

GRAVITY = 9.81
SPEED = 10


class Body(object):
    def __init__(self, pos, size):
        self._color = (255, 255, 255)
        self._pos = pos
        self._size = size
        self._velocity = pygame.math.Vector2(0, 0)
        return

    def apply_force(self, force):
        self._velocity += force
        pass

    def physics(self, world, dt):
        #self._velocity += pygame.math.Vector2(0, GRAVITY)
        self._pos[0] += self._velocity.x * dt * SPEED
        self._pos[1] += self._velocity.y * dt * SPEED

    def render(self, surface):
        pygame.draw.rect(surface, self._color, (self._pos + self._size))

        return

    def change_color(self, new_color):
        self._color = new_color
        return

    def handle_event(self, event):
        pass