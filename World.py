from Collisions import collide
from Vector import Vector, zero_vector
from Constants import FLOOR_HEIGHT, HEIGHT, WIDTH
from Body import Body


class World(object):
    def __init__(self):
        # Init game objects
        self.game_objects = [
            Body(zero_vector(), 64, 64, False, "p1"),
            Body(Vector(512, 64), 64, 64, False, "p2"),
            Body(Vector(0, HEIGHT - FLOOR_HEIGHT), WIDTH, FLOOR_HEIGHT, True, "floor"),
        ]

    def tick(self, dt: float):
        # Movement step
        for obj in self.game_objects:
            if not obj.static:
                obj.tick(dt)

        # Collision step
        for bodyA in self.game_objects:
            if bodyA.static:
                continue

            for bodyB in self.game_objects:
                if bodyB.static or bodyA == bodyB:
                    continue

                collision, normal, depth = collide(bodyA, bodyB)

                # if collision:
                #     bodyA.move(-normal * depth * 0.5)

    def render(self, screen):
        for obj in self.game_objects:
            obj.render(screen)
