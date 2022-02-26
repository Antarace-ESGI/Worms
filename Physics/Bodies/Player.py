import pygame

from Constants import *
from Physics.Bodies.Body import Body
from Physics.Vector import Vector
from Utils import draw_outline_rect


class Player(Body):
    def __init__(self, position: Vector, width: float, height: float):
        Body.__init__(self, position, width, height)
        self.health = MAX_HEALTH
        self.has_shoot = False
        self.current_weapon = WEAPONS[0]

    def tick(self, dt: float):
        Body.tick(self, dt)

    def render(self, surface):
        Body.render(self, surface)
        health_percentage = self.health / MAX_HEALTH

        draw_outline_rect(surface, self.position.x - self.width / 2 + 1, self.position.y - self.height + 1,
                          health_percentage * self.width - 2, 8,
                          RED_COLOR, WHITE_COLOR, 1)

        weapon = pygame.rect.Rect(self.position.x + self.width / 2 - 20, self.position.y - 5, 10, 10)
        pygame.draw.rect(surface, GREEN_COLOR if self.current_weapon == "G" else BLUE_COLOR, weapon)
