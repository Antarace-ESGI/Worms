from Constants import PROJECTILE_LIFE
from Physics.Bodies.Body import Body
from Physics.Vector import Vector


class Projectile(Body):
    def __init__(self, position: Vector, width: float, height: float, world=None):
        Body.__init__(self, position, width, height)
        self.life = 0
        self.world = world

    def tick(self, dt: float):
        self.position += self.linear_velocity * dt

        self.life += dt
        if self.world and self.life >= PROJECTILE_LIFE:
            self.destroy()

    def destroy(self):
        self.world.destroy(self)
