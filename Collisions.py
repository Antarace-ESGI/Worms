import math
from Vector import Vector
from Body import Body


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


def intersect_vertices(vertices_a: list[Vector], vertices_b: list[Vector]):
    length = len(vertices_a)

    for i in range(length):
        va = vertices_a[i]
        vb = vertices_a[(i + 1) % length]

        edge = vb - va
        normal = Vector(-edge.y, edge.x)

        min_a, max_a = project_vertices(vertices_a, normal)
        min_b, max_b = project_vertices(vertices_b, normal)

        if min_a >= max_b or min_b >= max_a:
            return False

    return True


def intersect_polygons(vertices_a: list[Vector], vertices_b: list[Vector]):
    a = intersect_vertices(vertices_a, vertices_b)
    if not a:
        return False

    b = intersect_vertices(vertices_b, vertices_a)
    if not b:
        return False

    return True


def collide(body_a: Body, body_b: Body):
    return intersect_polygons(body_a.get_transformed_vertices(), body_b.get_transformed_vertices())
