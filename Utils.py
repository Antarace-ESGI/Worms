import pygame


def draw_outline_rect(surface, x, y, width, height, color, outline_color, border_width):
    outline_rect = pygame.rect.Rect(x - border_width, y - border_width, width + border_width * 2, height + border_width * 2)
    rect = pygame.rect.Rect(x, y, width, height)
    pygame.draw.rect(surface, outline_color, outline_rect)
    pygame.draw.rect(surface, color, rect)