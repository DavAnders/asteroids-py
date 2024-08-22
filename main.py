import pygame

from asteroid import *
from asteroidfield import *
from constants import *
from player import *


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Window Dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # FPS clock / Delta Time
    game_clock = pygame.time.Clock()
    dt = 0

    # Infinite loop condition
    should_run = True

    # Groups and containers
    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()
    Player.containers = (group_updatable, group_drawable)
    Asteroid.containers = (group_updatable, group_drawable, group_asteroids)

    # Player
    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    # AsteroidField (added only to the updatable group)
    AsteroidField.containers = (group_updatable,)
    asteroid_field = AsteroidField()

    while should_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                should_run = False

        screen.fill((0, 0, 0))

        # Update rotation/position, render player
        for obj in group_updatable:
            obj.update(dt)
        for obj in group_drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000  # 1/60 of a second / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
