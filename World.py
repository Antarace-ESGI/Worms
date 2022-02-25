import pygame

from Body import Body
from Collisions import collide, resolve_collision
from Constants import *


class World(object):
    def __init__(self):
        # Init game objects
        self.player = Body(Vector(128, 256), 64, 64, False, "p1")

        self.game_objects = [
            self.player,
            Body(Vector(128, 64), 64, 64, False, "p2"),
            Body(Vector(0, HEIGHT - FLOOR_HEIGHT), WIDTH, FLOOR_HEIGHT, True, "floor"),
        ]

    def controls(self, dt: float):
        keys = pygame.key.get_pressed()

        self.player.move(Vector(
            (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * dt * SPEED,
            (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * dt * SPEED
        ))

    def tick(self, dt: float):
        # Movement step
        for obj in self.game_objects:
            if not obj.static:
                obj.tick(dt)

        self.controls(dt)

        # Collision step
        for i in range(len(self.game_objects) - 1):
            body_a = self.game_objects[i]
            for j in range(i + 1, len(self.game_objects)):
                body_b = self.game_objects[j]

                collision, normal, depth = collide(body_a, body_b)

                if collision:
                    if body_a.static:
                        body_b.move(normal * depth)
                    elif body_b.static:
                        body_a.move(-normal * depth)
                    else:
                        body_a.move(-normal * depth * 0.5)
                        body_b.move(normal * depth * 0.5)

                    resolve_collision(body_a, body_b, normal, depth)

    def render(self, screen):
        for obj in self.game_objects:
            obj.render(screen)
