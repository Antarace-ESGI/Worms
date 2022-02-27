import pygame
import time

from Constants import *
from Controls import controls, shoot_controls, shoot_positions
from Physics.Bodies.Body import Body
from Physics.Bodies.Player import Player
from Physics.Bodies.Projectile import calculate_position
from Physics.Collisions import resolve_collision, intersect_polygons


def render_projectile_path(screen, player):
    start_pos, start_velocity, angle = shoot_positions(player)
    previous_pos, life = start_pos, 0

    while life < PROJECTILE_LIFE:
        x, y = calculate_position(start_velocity, angle, life, start_pos)
        end_pos = Vector(x, y)
        pygame.draw.line(screen, BLACK_COLOR, previous_pos.to_tuple(), end_pos.to_tuple())
        previous_pos = end_pos
        life += 0.1


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
        if time.time() - self.turn_start >= TURN_DURATION:
            self.end_turn()

        controls(self.player1 if self.turn else self.player2, dt)

        # Movement step
        for obj in self.game_objects:
            if not obj.static:
                obj.tick(dt)

        collision_events = set()

        # Collision step
        for i in range(len(self.game_objects) - 1):
            body_a = self.game_objects[i]
            for j in range(i + 1, len(self.game_objects)):
                body_b = self.game_objects[j]

                collision, normal, depth = intersect_polygons(body_a.get_transformed_vertices(),
                                                              body_b.get_transformed_vertices())

                if collision:
                    collision_events.add((body_a, body_b, normal, depth))

                    if body_a.static:
                        body_b.move(normal * depth)
                    elif body_b.static:
                        body_a.move(-normal * depth)
                    else:
                        body_a.move(-normal * depth * 0.5)
                        body_b.move(normal * depth * 0.5)

                    resolve_collision(body_a, body_b, normal, depth)

        # Handle collision events
        for collision_event in collision_events:
            body_a, body_b, normal, depth = collision_event

            if body_a.static:
                body_b.collide(body_a, normal, depth)
            elif body_b.static:
                body_a.collide(body_b, normal, depth)
            else:
                body_a.collide(body_b, normal, depth)
                body_b.collide(body_a, normal, depth)

    def render(self, screen):
        screen.blit(self.text, self.timer)

        # Render timer
        self.text = self.font.render(f'{TURN_DURATION - int(time.time() - self.turn_start)}', True, (0, 0, 0))
        self.timer = self.text.get_rect().center = (WIDTH // 2, HEIGHT * 0.05)

        # Render game objects
        for obj in self.game_objects:
            obj.render(screen)

        # Render projectile path
        player = self.player1 if self.turn else self.player2

        if not player.has_shoot:
            render_projectile_path(screen, player)

    def tick_events(self, event):
        player = self.player1 if self.turn else self.player2

        if not player.has_shoot:
            projectile = shoot_controls(player, event, self)

            if projectile:
                self.game_objects.append(projectile)

    def destroy(self, body: Body):
        if body in self.game_objects:
            self.game_objects.remove(body)

    def end_turn(self):
        player = self.player1 if self.turn else self.player2
        player.has_shoot = False

        self.turn = not self.turn
        self.turn_start = time.time()
