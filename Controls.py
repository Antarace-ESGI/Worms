import math

import pygame

from Body import Body
from Constants import SPEED
from Projectile import Projectile
from Vector import Vector


def controls(player, dt: float):
    keys = pygame.key.get_pressed()

    player.move(Vector(
        (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * dt * SPEED,
        (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * dt * SPEED
    ))


def shoot_controls(player, event, destroy=None):
    if event.type == pygame.MOUSEBUTTONUP:
        x, y = pygame.mouse.get_pos()
        angle = math.atan2(y - player.position.y, x - player.position.x)

        pos = Vector(player.position.x + math.cos(angle) * player.width,
                     player.position.y + math.sin(angle) * player.height)
        projectile = Projectile(pos, 16, 16, destroy=destroy)
        projectile.linear_velocity.x = math.cos(angle) * 100
        projectile.linear_velocity.y = math.sin(angle) * 100
        return projectile
