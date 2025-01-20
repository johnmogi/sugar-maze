import pygame
from .base_state import BaseState
from ..constants import *

class SplashState(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.Font(None, 74)
        self.title_text = self.font.render("SUGARBOUND", True, WHITE)
        self.subtitle_font = pygame.font.Font(None, 36)
        self.subtitle_text = self.subtitle_font.render("The Labyrinth of Sweets", True, PINK)
        self.start_text = self.subtitle_font.render("Press SPACE to Start", True, GRAY)
        self.timer = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game.change_state(STATE_MENU)

    def update(self):
        self.timer += 1

    def draw(self, screen):
        # Center the title
        title_x = (WINDOW_WIDTH - self.title_text.get_width()) // 2
        title_y = WINDOW_HEIGHT // 3
        screen.blit(self.title_text, (title_x, title_y))

        # Center the subtitle
        subtitle_x = (WINDOW_WIDTH - self.subtitle_text.get_width()) // 2
        subtitle_y = title_y + 80
        screen.blit(self.subtitle_text, (subtitle_x, subtitle_y))

        # Make the "Press SPACE" text blink
        if (self.timer // 30) % 2:  # Blinks every half second
            start_x = (WINDOW_WIDTH - self.start_text.get_width()) // 2
            start_y = subtitle_y + 100
            screen.blit(self.start_text, (start_x, start_y))
