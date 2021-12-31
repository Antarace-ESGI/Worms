import sys
import pygame

from Body import Body

MAX_FPS = 60


def controls(player, dt):
    keys = pygame.key.get_pressed()

    player.apply_force(pygame.math.Vector2(
        (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * dt,
        (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * dt
    ))


def main():
    # Initialization
    pygame.init()
    size = width, height = 640, 360
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    player = Body(pygame.math.Vector2(0, 0), pygame.math.Vector2(64, 64))
    floor = Body(pygame.math.Vector2(0, height - 10), pygame.math.Vector2(width, 10), False)

    game_objects = [
        player,
        floor,
    ]

    dt = 0

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
            obj.physics(game_objects, dt)
            obj.render(screen)
        controls(player, dt)

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
