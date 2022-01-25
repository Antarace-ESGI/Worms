import sys
import time
import pygame

from Body import Body
from Constants import SPEED, MAX_FPS
from Vector import Point, zero


def controls(player, dt):
    keys = pygame.key.get_pressed()

    player.apply_force(Point(
        (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * dt * SPEED,
        (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * dt * SPEED
    ))


def main():
    # Initialization
    pygame.init()
    size = width, height = 640, 360
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    player1 = Body(zero(), Point(64, 64), (255, 0, 0), False)
    player2 = Body(zero(), Point(64, 64), (0, 255, 0), False)
    floor = Body(Point(0, height - 10), Point(width, 10), (255, 255, 255), False)

    game_objects = [
        player1,
        player2,
        floor,
    ]

    dt = 0

    turn = True
    turn_start = time.time()
    turn_duration = 5

    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render(f'{turn_duration}', True, (0, 0, 0))
    timer = text.get_rect().center = (width // 2, height * 0.05)

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
        screen.blit(text, timer)

        # Render game objects
        for obj in game_objects:
            obj.physics(game_objects, dt)
            obj.render(screen)

        # Compare actual time with time at the beginning of this turn
        if int(time.time() - turn_start) == turn_duration:
            turn = not turn
            turn_start = time.time()

        # Multiplayer turn by turn
        if turn:
            controls(player1, dt)
        else:
            controls(player2, dt)

        # Display the timer
        text = font.render(f'{turn_duration - int(time.time() - turn_start)}', True, (0, 0, 0))

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
