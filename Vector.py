import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, a: Point, b: Point):
        self._a = a
        self._b = b

        self.x = b.x - a.x
        self.y = b.y - a.y

    def scalar(self, vec: "Vector"):
        return self.x * vec.x + self.y * vec.y

    def norm(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def angle(self, vec: "Vector"):
        s = self.scalar(vec)

        sign = self.x * vec.y - vec.x * self.y  # déterminant d'une matrice

        sign = -1 if sign < 0 else 1

        return math.acos(s / (self.norm() * vec.norm())) * sign

    def mult_scalar(self, sca: float):
        vec = Vector(self._a, self._b)

        vec.x *= sca
        vec.y *= sca

        return vec

    def __add__(self, other: "Vector|Point"):
        vec = Vector(self._a, self._b)

        vec.x += other.x
        vec.y += other.y

        return vec

    """Calcul non correct"""
    def proj(self, vec: "Vector"):
        s = self.scalar(vec)

        f = s / vec.norm()

        return vec.mult_scalar(f) + self._a

    def sym(self, vec: "Vector"):
        # TODO: implement method
        return vec

    """Paramétrisation d'un vecteur
    :param k Constant number between 0 and 1
    :returns Point on the Vector at k
    """
    def param(self, k: float):
        x = (1 - k) * self._a.x + k * self._b.x
        y = (1 - k) * self._a.y + k * self._b.y
        return Point(x, y)

    def intersect(self, vec: "Vector"):
        # TODO: implement method
        return vec