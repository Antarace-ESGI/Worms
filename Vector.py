import math


def zero():
    return Point(0, 0)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other: float):
        self.x *= other
        self.y *= other

        return self

    def __add__(self, other: "Point"):
        self.x += other.x
        self.y += other.y

        return self


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

    def __mul__(self, other: float):
        self.x *= other
        self.y *= other

        return self

    def __add__(self, other: "Vector|Point"):
        self.x += other.x
        self.y += other.y

        return self

    """Calcul non correct"""
    def proj(self, vec: "Vector"):
        s = self.scalar(vec)

        f = s / vec.norm()

        return vec * f + self._a

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

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
