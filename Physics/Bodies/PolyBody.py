import pygame

from Constants import WHITE_COLOR, BLACK_COLOR
from Physics.Bodies.Body import Body
from Physics.Vector import Vector
from RandomPolygon import generate_polygon
from typing import Tuple


def create_random_poly_vertices(center: Tuple[float, float], radius: int):
    return generate_polygon(center=center,
                            avg_radius=radius,
                            irregularity=0.35,
                            spikiness=0.2,
                            num_vertices=16)


class PolyBody(Body):
    def __init__(self, position: Vector, radius: int):
        Body.__init__(self, position, radius, radius, False)
        self.position = position
        self.vertices = create_random_poly_vertices(position.to_tuple(), radius)

    def tick(self, dt: float):
        Body.tick(self, dt)

    def render(self, surface):
        vertices = []
        transformed_vertices = self.get_transformed_vertices()
        for vertex in transformed_vertices:
            vertices.append(vertex.to_tuple())

        pygame.draw.polygon(surface, WHITE_COLOR, vertices)

        # for vertex in transformed_vertices:
        #     pygame.draw.line(surface, BLACK_COLOR, self.position.to_tuple(), vertex.to_tuple())
