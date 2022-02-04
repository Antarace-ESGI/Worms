import math
import sys
import time
import pygame

from Body import Body
from Constants import SPEED, MAX_FPS, FLOOR_HEIGHT
from Vector import Point, zero


game_objects: list[Body] = []


def controls(player, dt):
    keys = pygame.key.get_pressed()

    player.apply_force(Point(
        (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * dt * SPEED,
        (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * dt * SPEED
    ))


def shoot_controls(player, event):
    if event.type == pygame.MOUSEBUTTONUP:
        x, y = pygame.mouse.get_pos()
        angle = math.atan2(y - player.pos.y, x - player.pos.x)

        pos = Point(player.pos.x + math.cos(angle) * player.size.x + player.size.x / 2, player.pos.y + math.sin(angle) * player.size.y + player.size.y / 2)
        projectile = Body(pos, Point(16, 16), (255, 255, 255), True, False)
        projectile.velocity.x = math.cos(angle) * 0.1
        projectile.velocity.y = math.sin(angle) * 0.1
        game_objects.append(projectile)


def main():
    # Initialization
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    player1 = Body(zero(), Point(64, 64), (255, 0, 0), True, False)
    player2 = Body(Point(256, 0), Point(64, 64), (0, 255, 0), True, False)
    floor = Body(Point(0, height - FLOOR_HEIGHT), Point(width, FLOOR_HEIGHT), (255, 255, 255), False)

    game_objects.append(player1)
    game_objects.append(player2)
    game_objects.append(floor)

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

            # Handle shoot controls
            if turn:
                shoot_controls(player1, event)
            else:
                shoot_controls(player2, event)

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
