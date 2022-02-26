import math

from Constants import FRICTION
from Physics.Bodies.Body import Body
from Physics.Vector import Vector, zero_vector


def resolve_collision(body_a: Body, body_b: Body, normal: Vector, depth: float):
    dampen = normal.abs()
    dampen *= FRICTION
    body_b.linear_velocity *= dampen
    body_a.linear_velocity *= dampen


def project_vertices(vertices: list[Vector], axis: Vector):
    low = math.inf
    upper = -math.inf

    for v in vertices:
        proj = v.dot(axis)

        if proj < low:
            low = proj
        if proj > upper:
            upper = proj

    return low, upper


def intersect_vertices(vertices_a: list[Vector], vertices_b: list[Vector], normal: Vector = zero_vector(), depth: float = math.inf):
    length = len(vertices_a)

    for i in range(length):
        va = vertices_a[i]
        vb = vertices_a[(i + 1) % length]

        edge = vb - va
        axis = Vector(-edge.y, edge.x)

        # Check for collision
        min_a, max_a = project_vertices(vertices_a, axis)
        min_b, max_b = project_vertices(vertices_b, axis)

        if min_a >= max_b or min_b >= max_a:
            return False, zero_vector(), 0

        # Collision resolving
        axis_depth = min(max_b - min_a, max_a - min_b)

        if axis_depth < depth:
            depth = axis_depth
            normal = axis

    return True, normal, depth


def arithmetic_mean(vertices: list[Vector]):
    sum_x, sum_y, length = 0, 0, len(vertices)

    for vertex in vertices:
        sum_x += vertex.x
        sum_y += vertex.y

    return Vector(sum_x / length, sum_y / length)


def intersect_polygons(vertices_a: list[Vector], vertices_b: list[Vector]):
    collision, normal, depth = intersect_vertices(vertices_a, vertices_b)
    if not collision:
        return False, normal, depth

    collision, normal, depth = intersect_vertices(vertices_b, vertices_a, normal, depth)
    if not collision:
        return False, normal, depth

    depth /= normal.length()
    normal = normal.normalize()

    center_a = arithmetic_mean(vertices_a)
    center_b = arithmetic_mean(vertices_b)

    direction = center_b - center_a
    if direction.dot(normal) < 0:
        normal = -normal

    return True, normal, depth
