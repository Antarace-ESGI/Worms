import sys
import pygame

MAX_FPS = 60


class Body(object):
    def __init__(self, pos, size):
        self._color = (255, 255, 255)
        self._pos = pos
        self._size = size
        return

    def render(self, surface, dt):
        pygame.draw.rect(surface, self._color, (self._pos + self._size))

        keys = pygame.key.get_pressed()

        self._pos[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * dt
        self._pos[1] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * dt

        return

    def change_color(self, new_color):
        self._color = new_color
        return

    def handle_event(self, event):
        pass


def main():
    # Initialization
    pygame.init()
    size = width, height = 640, 360
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    game_objects = [
        Body([0, 0], [64, 64])
    ]

    while True:
        # Handle events
        for event in pygame.event.get():
            # Let game objects handle events they care about
            for obj in game_objects:
                obj.handle_event(event)

            # Handle global events
            if event.type == pygame.QUIT:
                quit_game()

        # Clear the screen
        screen.fill((140, 180, 255))

        # Render game objects
        for obj in game_objects:
            obj.render(screen, clock.get_time())

        # Complete the frame
        pygame.display.update()
        clock.tick(MAX_FPS)


def quit_game(status=0):
    pygame.quit()
    sys.exit(status)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        quit_game()
