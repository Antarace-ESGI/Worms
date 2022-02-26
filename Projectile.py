from Body import Body
from Constants import PROJECTILE_LIFE
from Vector import Vector


class Projectile(Body):
    def __init__(self, position: Vector, width: float, height: float, static: bool = False, destroy=None):
        Body.__init__(self, position, width, height, static, destroy)
        self.life = 0

    def tick(self, dt: float):
        Body.tick(self, dt)
        self.life += dt
        if self.destroy and self.life >= PROJECTILE_LIFE:
            self.destroy(self)
