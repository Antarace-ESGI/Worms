import math
from Vector import Vector, zero_vector
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


def intersect_polygons(center_a: Vector, vertices_a: list[Vector], center_b: Vector, vertices_b: list[Vector]):
    normal = zero_vector()
    depth = math.inf

    for i in range(len(vertices_a)):
        va = vertices_a[i]
        vb = vertices_a[(i + 1) % len(vertices_a)]

        edge = vb - va
        axis = Vector(-edge.y, edge.x)
        axis = axis.normalize()

        min_a, max_a = project_vertices(vertices_a, axis)
        min_b, max_b = project_vertices(vertices_b, axis)

        if min_a >= max_b or min_b >= max_a:
            return False, normal, depth

        axis_depth = min(max_b - min_a, max_a - min_b)

        if axis_depth < depth:
            depth = axis_depth
            normal = axis

    for i in range(len(vertices_b)):
        va = vertices_b[i]
        vb = vertices_b[(i + 1) % len(vertices_b)]

        edge = vb - va
        axis = Vector(-edge.y, edge.x)
        axis = axis.normalize()

        min_a, max_a = project_vertices(vertices_a, axis)
        min_b, max_b = project_vertices(vertices_b, axis)

        if min_a >= max_b or min_b >= max_a:
            return False, normal, depth

        axis_depth = min(max_b - min_a, max_a - min_b)

        if axis_depth < depth:
            depth = axis_depth
            normal = axis

    direction = center_b - center_a

    if direction.dot(normal) < 0:
        normal = -normal

    return True, normal, depth


def collide(body_a: Body, body_b: Body):
    return intersect_polygons(body_a.position, body_a.vertices, body_b.position, body_a.vertices)
