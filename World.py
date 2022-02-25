import pygame

from Body import Body
from Collisions import collide
from Constants import *


class World(object):
    def __init__(self):
        # Init game objects
        self.player = Body(Vector(128, 64), 64, 64, False, "p1")

        self.game_objects = [
            self.player,
            Body(Vector(128, 256), 64, 64, True, "p2"),
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

                collision = collide(body_a, body_b)
                print(collision)
                if collision:
                    body_b.is_colliding = True
                    body_a.is_colliding = True
                else:
                    body_b.is_colliding = False
                    body_a.is_colliding = False

                # if collision:
                #     if bodyA.static:
                #         bodyB.move(normal * depth)
                #     elif bodyB.static:
                #         bodyA.move(-normal * depth)
                #     else:
                #         bodyA.move(-normal * depth / 2)
                #         bodyB.move(normal * depth / 2)

    def render(self, screen):
        for obj in self.game_objects:
            obj.render(screen)
