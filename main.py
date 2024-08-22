import pygame

from constants import *


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    should_run = True

    while should_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                should_run = False
        screen.fill((0, 0, 0))
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
