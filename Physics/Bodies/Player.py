import pygame

from Constants import MAX_HEALTH, RED, WHITE
from Physics.Bodies.Body import Body
from Physics.Bodies.Projectile import Projectile
from Physics.Vector import Vector


class Player(Body):
    def __init__(self, position: Vector, width: float, height: float):
        Body.__init__(self, position, width, height)
        self.health = MAX_HEALTH
        self.has_shoot = False

    def tick(self, dt: float):
        Body.tick(self, dt)

    def render(self, surface):
        Body.render(self, surface)
        health_percentage = self.health / MAX_HEALTH
        outline_rect = pygame.rect.Rect(self.position.x - self.width / 2, self.position.y - self.height, health_percentage * self.width, 10)
        rect = pygame.rect.Rect(self.position.x - self.width / 2 + 1, self.position.y - self.height + 1, health_percentage * self.width - 2, 8)
        pygame.draw.rect(surface, WHITE, outline_rect)
        pygame.draw.rect(surface, RED, rect)

    def collide(self, other, normal, depth):
        if isinstance(other, Projectile):
            self.health -= 1
            other.destroy()
