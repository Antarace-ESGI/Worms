import math
import pygame

from Constants import SPEED, WEAPONS
from Physics.Bodies.Projectile import Projectile
from Physics.Vector import Vector


def controls(player, dt: float):
    keys = pygame.key.get_pressed()

    player.move(Vector(
        (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * dt * SPEED,
        (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * dt * SPEED
    ))


def shoot_positions(player):
    x, y = pygame.mouse.get_pos()
    angle = math.atan2(y - player.position.y, x - player.position.x)

    start_pos = Vector(player.position.x + math.cos(angle) * player.width,
                       player.position.y + math.sin(angle) * player.height)

    velocity = 200 if player.current_weapon == "G" else 500

    return start_pos, velocity, angle


def shoot_controls(player, event, world=None):
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:  # left click
            pos, vel, angle = shoot_positions(player)

            projectile = Projectile(pos, 16, 16, world=world, weapon_type=player.current_weapon, start_velocity=vel, angle=angle)
            projectile.linear_velocity = vel

            player.has_shoot = True

            return projectile
        elif event.button == 4:  # mouse wheel down
            player.current_weapon = WEAPONS[0]
        elif event.button == 5:  # mouse wheel up
            player.current_weapon = WEAPONS[1]
