from Constants import PROJECTILE_LIFE
from Physics.Bodies.Body import Body
from Physics.Vector import Vector


class Projectile(Body):
    def __init__(self, position: Vector, width: float, height: float, world=None):
        Body.__init__(self, position, width, height)
        self.life = 0
        self.world = world
        self.start_position = position

    def tick(self, dt: float):
        self.life += dt

        self.position = self.start_position + self.linear_velocity.param(self.life / PROJECTILE_LIFE)

        if self.life >= PROJECTILE_LIFE:
            self.destroy()

    def destroy(self):
        if self.world:
            self.world.destroy(self)
