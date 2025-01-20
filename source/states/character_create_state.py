import pygame
import random
from .base_state import BaseState
from ..constants import *

class CharacterCreateState(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 48)
        self.generate_character()

    def generate_character(self):
        self.character = {
            "class": random.choice(list(CLASSES.keys())),
            "stats": {},
            "equipment": ["Basic Sword", "Leather Armor"]
        }
        self.character["stats"] = CLASSES[self.character["class"]]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.generate_character()
            elif event.key == pygame.K_RETURN:
                self.game.change_state(STATE_GAME)
            elif event.key == pygame.K_ESCAPE:
                self.game.change_state(STATE_MENU)

    def draw(self, screen):
        # Draw title
        title = self.title_font.render("Character Creation", True, WHITE)
        screen.blit(title, ((WINDOW_WIDTH - title.get_width()) // 2, 50))

        # Draw character info
        y = 150
        class_text = self.font.render(f"Class: {self.character['class']}", True, WHITE)
        screen.blit(class_text, (50, y))
        
        y += 50
        for stat, value in self.character["stats"].items():
            stat_text = self.font.render(f"{stat.capitalize()}: {value}", True, WHITE)
            screen.blit(stat_text, (50, y))
            y += 30

        y += 20
        equipment_title = self.font.render("Equipment:", True, WHITE)
        screen.blit(equipment_title, (50, y))
        y += 30
        for item in self.character["equipment"]:
            item_text = self.font.render(f"- {item}", True, WHITE)
            screen.blit(item_text, (50, y))
            y += 30

        # Draw instructions
        instructions = [
            "SPACE - Reroll Character",
            "ENTER - Start Game",
            "ESC - Back to Menu"
        ]
        y = WINDOW_HEIGHT - 120
        for instruction in instructions:
            text = self.font.render(instruction, True, GRAY)
            screen.blit(text, (50, y))
            y += 30
