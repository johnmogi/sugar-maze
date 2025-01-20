import pygame
import sys
from .base_state import BaseState
from ..constants import *

class MenuState(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.Font(None, 48)
        self.options = ["🎮 Start Game", "⚙️ Options", "🚪 Exit"]
        self.selected = 0
        self.texts = []
        self.update_text()

    def update_text(self):
        self.texts = []
        for i, option in enumerate(self.options):
            color = PINK if i == self.selected else WHITE
            self.texts.append(self.font.render(option, True, color))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected = (self.selected - 1) % len(self.options)
                self.update_text()
            elif event.key == pygame.K_DOWN:
                self.selected = (self.selected + 1) % len(self.options)
                self.update_text()
            elif event.key == pygame.K_RETURN:
                if self.selected == 0:  # Start Game
                    self.game.change_state(STATE_CHARACTER_CREATE)
                elif self.selected == 1:  # Options
                    pass  # TODO: Implement options menu
                elif self.selected == 2:  # Exit
                    pygame.quit()
                    sys.exit()

    def draw(self, screen):
        # Draw title
        title = self.font.render("🍭 Sugarbound 🍬", True, PINK)
        subtitle = pygame.font.Font(None, 36).render("The Labyrinth of Sweets", True, WHITE)
        
        title_x = (WINDOW_WIDTH - title.get_width()) // 2
        subtitle_x = (WINDOW_WIDTH - subtitle.get_width()) // 2
        
        screen.blit(title, (title_x, 100))
        screen.blit(subtitle, (subtitle_x, 150))

        # Draw menu options
        for i, text in enumerate(self.texts):
            x = (WINDOW_WIDTH - text.get_width()) // 2
            y = WINDOW_HEIGHT // 2 - (len(self.texts) * 60) // 2 + i * 60
            screen.blit(text, (x, y))

        # Draw controls hint
        controls = pygame.font.Font(None, 32).render("⬆️⬇️ to select, ENTER to confirm", True, GRAY)
        controls_x = (WINDOW_WIDTH - controls.get_width()) // 2
        screen.blit(controls, (controls_x, WINDOW_HEIGHT - 50))
