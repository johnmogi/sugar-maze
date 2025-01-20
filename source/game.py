import pygame
from .constants import *
from .states.splash_state import SplashState
from .states.menu_state import MenuState
from .states.character_create_state import CharacterCreateState
from .states.game_state import GameState

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.current_state = None
        self.states = {
            STATE_SPLASH: SplashState(self),
            STATE_MENU: MenuState(self),
            STATE_CHARACTER_CREATE: CharacterCreateState(self),
            STATE_GAME: GameState(self)
        }
        self.change_state(STATE_SPLASH)

    def change_state(self, state_name):
        self.current_state = self.states[state_name]
        self.current_state.enter()

    def handle_event(self, event):
        self.current_state.handle_event(event)

    def update(self):
        self.current_state.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.current_state.draw(self.screen)
