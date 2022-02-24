import math


def zero_vector():
    return Vector(0, 0)


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def clone(self):
        vec = Vector(self.x, self.y)
        return vec

    def scalar(self, vec: "Vector"):
        return self.x * vec.x + self.y * vec.y

    def norm(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        length = self.length()
        return Vector(self.x / length, self.y / length)

    def dot(self, other: "Vector"):
        return self.x * other.x + self.y * other.y

    def angle(self, vec: "Vector"):
        s = self.scalar(vec)
        sign = self.x * vec.y - vec.x * self.y  # déterminant d'une matrice
        sign = -1 if sign < 0 else 1
        return math.acos(s / (self.norm() * vec.norm())) * sign

    def __mul__(self, other: "Vector|float|int"):
        result = self.clone()

        if isinstance(other, Vector):
            result.x *= other.x
            result.y *= other.y
        else:
            result.x *= other
            result.y *= other

        return result

    def __imul__(self, other: "Vector|float|int"):
        if isinstance(other, Vector):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other

        return self

    def __div__(self, other: "Vector|float|int"):
        result = self.clone()

        if isinstance(other, Vector):
            result.x /= other.x
            result.y /= other.y
        else:
            result.x /= other
            result.y /= other

        return result

    def __idiv__(self, other: "Vector|float|int"):
        if isinstance(other, Vector):
            self.x /= other.x
            self.y /= other.y
        else:
            self.x /= other
            self.y /= other

        return self

    def __add__(self, other: "Vector|float|int"):
        result = self.clone()

        if isinstance(other, Vector):
            result.x += other.x
            result.y += other.y
        else:
            result.x += other
            result.y += other

        return result

    def __iadd__(self, other: "Vector|float|int"):
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other

        return self

    def __sub__(self, other: "Vector|float|int"):
        result = self.clone()

        if isinstance(other, Vector):
            result.x -= other.x
            result.y -= other.y
        else:
            result.x -= other
            result.y -= other

        return result

    def __isub__(self, other: "Vector|float|int"):
        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other

        return self

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def to_tuple(self):
        return self.x, self.y
