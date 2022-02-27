import sys
import pygame
from Constants import MAX_FPS, SIZE
from Physics.World import World


def main():
    # Initialization
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    world = World()
    dt = 0

    while True:
        # Handle events
        for event in pygame.event.get():
            # Handle global events
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    world.canPlay = True
                    main()
            world.tick_events(event)

        if world.canPlay:
            # Clear the screen
            screen.fill((140, 180, 255))

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
