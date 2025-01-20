import pygame
import sys
from src.game import Game
from src.constants import WINDOW_WIDTH, WINDOW_HEIGHT, TITLE, FPS

def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    # Create game instance
    game = Game(screen)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            game.handle_event(event)

        # Update game state
        game.update()

        # Draw everything
        game.draw()
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
