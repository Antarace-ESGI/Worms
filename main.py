import sys
import time
import pygame
from Constants import MAX_FPS, SIZE, WIDTH, HEIGHT
from World import World


def main():
    # Initialization
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    world = World()

    dt = 0

    turn = True
    turn_start = time.time()
    turn_duration = 5

    font = pygame.font.Font("freesansbold.ttf", 24)
    text = font.render(f'{turn_duration}', True, (0, 0, 0))
    timer = text.get_rect().center = (WIDTH // 2, HEIGHT * 0.05)

    while True:
        # Handle events
        for event in pygame.event.get():
            # Handle global events
            if event.type == pygame.QUIT:
                quit_game()

        # Clear the screen
        screen.fill((140, 180, 255))
        screen.blit(text, timer)

        world.tick(dt)
        world.render(screen)

        # Complete the frame
        pygame.display.update()
        dt = clock.tick(MAX_FPS) / 1000.0


def quit_game(status=0):
    pygame.quit()
    sys.exit(status)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        quit_game()
