from Constants import *
from Physics.Bodies.Body import Body
from Physics.Bodies.Player import Player
from Physics.Vector import Vector, zero_vector
from Utils import draw_outline_rect
from math import sqrt, pow, cos, sin


def calculate_position(start_velocity: float, angle: float, life: float, start_pos: Vector):
    x = start_velocity * cos(angle) * life + start_pos.x
    y = (GRAVITY.y / 2) * pow(life, 2) + start_velocity * sin(angle) * life + start_pos.y

    return x, y


class Projectile(Body):
    def __init__(self, position: Vector, width: float, height: float, world=None, weapon_type=None, angle: float = 0, start_velocity: float = 1):
        Body.__init__(self, position, width, height)
        self.life = 0
        self.world = world
        self.start_position = position
        self.weapon_type = weapon_type
        self.start_velocity = start_velocity
        self.angle = angle

    def tick(self, dt: float):
        self.life += dt
        self.linear_velocity = zero_vector()

        self.position.x, self.position.y = calculate_position(self.start_velocity, self.angle, self.life, self.start_position)

        if self.life >= PROJECTILE_LIFE:
            self.destroy()

    def render(self, surface):
        color = GREEN_COLOR if self.weapon_type == "G" else BLUE_COLOR
        draw_outline_rect(surface, self.position.x - self.width / 2, self.position.y - self.height / 2, self.width, self.height, color, BLACK_COLOR, 1)

    def destroy(self):
        if self.world:
            if self.weapon_type == "G":
                self.__explosive_area(200.0)
            self.world.destroy(self)

    def collide(self, other, normal, depth):
        if isinstance(other, Player):
            if self.weapon_type == "G":
                other.health -= other.health
            else:
                other.health -= 1

        if self.world:
            if self.weapon_type == "G":
                self.__explosive_area(200.0)
            self.world.destroy(self)

    def __explosive_area(self, distance: float):
        for i in self.world.game_objects:
            if isinstance(i, Player):
                sum_x = pow(i.position.x - self.position.x, 2)
                sum_y = pow(i.position.y - self.position.y, 2)
                dist = sqrt(sum_x + sum_y)
                if dist <= distance:
                    i.health -= (MAX_HEALTH-((int(dist / 50)) * 2.0))

