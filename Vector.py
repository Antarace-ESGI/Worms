import math


def zero():
    return Point(0, 0)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)

    def __mul__(self, other: float):
        self.x *= other
        self.y *= other

        return self

    def __add__(self, other: "Point"):
        self.x += other.x
        self.y += other.y

        return self

    def add_scalar(self, other: float):
        self.x += other
        self.y += other

        return self

    def mul_vector(self, vec: "Vector"):
        self.x *= vec.x
        self.y *= vec.y

        return self

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def to_tuple(self):
        return self.x, self.y


class Vector:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

        self.x = b.x - a.x
        self.y = b.y - a.y

    def clone(self):
        vec = Vector(self.a.clone(), self.b.clone())
        vec.x = self.x
        vec.y = self.y
        return vec

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

    def mul_point(self, other: Point):
        self.x *= other.x
        self.y *= other.y

        return self

    def __add__(self, other: "Vector|Point"):
        self.x += other.x
        self.y += other.y

        return self

    """Calcul non correct"""
    def proj(self, vec: "Vector"):
        norm = vec.norm()
        if norm == 0:
            norm = 1

        f = self.scalar(vec) / pow(norm, 2)

        return self.a.clone().add_scalar(f).mul_vector(vec)

    """Paramétrisation d'un vecteur
    :param k Constant number between 0 and 1
    :returns Point on the Vector at k
    """
    def param(self, k: float):
        x = (1 - k) * self.a.x + k * self.b.x
        y = (1 - k) * self.a.y + k * self.b.y
        return Point(x, y)

    def sym(self, vec: "Vector"):
        # TODO: implement method
        return vec

    def intersect(self, vec: "Vector"):
        # TODO: implement method
        return vec

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def to_tuple(self):
        return self.x, self.y
