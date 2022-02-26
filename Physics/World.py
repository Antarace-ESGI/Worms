import time
import pygame

from Physics.Bodies.Body import Body
from Constants import *
from Controls import controls, shoot_controls
from Physics.Bodies.Player import Player
from Physics.Collisions import resolve_collision, collide


class World(object):
    def __init__(self):
        self.turn = False
        self.turn_start = time.time()
        self.font = pygame.font.Font("freesansbold.ttf", 24)
        self.text = self.font.render(f'{TURN_DURATION}', True, (0, 0, 0))
        self.timer = self.text.get_rect().center = (WIDTH // 2, HEIGHT * 0.05)

        # Init game objects
        self.player1 = Player(Vector(WIDTH / 2 - 32, 256), 64, 64)
        self.player2 = Player(Vector(WIDTH / 2 - 32, 64), 64, 64)

        self.game_objects = [
            self.player1,
            self.player2,
            Body(Vector(0, HEIGHT - FLOOR_HEIGHT), WIDTH, FLOOR_HEIGHT, True),
        ]

    def tick(self, dt: float):
        if int(time.time() - self.turn_start) == TURN_DURATION:
            self.turn = not self.turn
            self. turn_start = time.time()

        controls(self.player1 if self.turn else self.player2, dt)

        # Movement step
        for obj in self.game_objects:
            if not obj.static:
                obj.tick(dt)

        # Collision step
        for i in range(len(self.game_objects) - 1):
            body_a = self.game_objects[i]
            for j in range(i + 1, len(self.game_objects)):
                body_b = self.game_objects[j]

                collision, normal, depth = collide(body_a, body_b)

                if collision:
                    if body_a.static:
                        body_b.move(normal * depth)
                        body_b.collide(body_a, normal, depth)
                    elif body_b.static:
                        body_a.move(-normal * depth)
                        body_a.collide(body_b, normal, depth)
                    else:
                        body_a.collide(body_b, normal, depth)
                        body_b.collide(body_a, normal, depth)
                        body_a.move(-normal * depth * 0.5)
                        body_b.move(normal * depth * 0.5)

                    resolve_collision(body_a, body_b, normal, depth)

    def render(self, screen):
        screen.blit(self.text, self.timer)

        self.text = self.font.render(f'{TURN_DURATION - int(time.time() - self.turn_start)}', True, (0, 0, 0))
        self.timer = self.text.get_rect().center = (WIDTH // 2, HEIGHT * 0.05)

        # Render game objects
        for obj in self.game_objects:
            obj.render(screen)

    def tick_events(self, event):
        projectile = shoot_controls(self.player1 if self.turn else self.player2, event, self)
        if projectile:
            self.game_objects.append(projectile)

    def destroy(self, body: Body):
        self.game_objects.remove(body)
