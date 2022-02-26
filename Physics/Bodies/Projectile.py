from Constants import *
from Physics.Bodies.Body import Body
from Physics.Bodies.Player import Player
from Physics.Vector import Vector
from Utils import draw_outline_rect


class Projectile(Body):
    def __init__(self, position: Vector, width: float, height: float, world=None, weapon_type=None):
        Body.__init__(self, position, width, height)
        self.life = 0
        self.world = world
        self.start_position = position
        self.weapon_type = weapon_type

    def tick(self, dt: float):
        self.life += dt

        self.position = self.start_position + self.linear_velocity.param(self.life / PROJECTILE_LIFE)

        if self.weapon_type == "G":
            self.linear_velocity += GRAVITY * dt

        if self.life >= PROJECTILE_LIFE:
            self.destroy()

    def render(self, surface):
        color = GREEN_COLOR if self.weapon_type == "G" else BLUE_COLOR
        draw_outline_rect(surface, self.position.x - self.width / 2, self.position.y - self.height / 2, self.width, self.height, color, BLACK_COLOR, 1)

    def destroy(self):
        if self.world:
            self.world.destroy(self)

    def collide(self, other, normal, depth):
        if isinstance(other, Player):
            other.health -= 1

        if self.world:
            self.world.destroy(self)
