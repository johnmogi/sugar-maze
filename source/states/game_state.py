import pygame
import random
from .base_state import BaseState
from ..constants import *

class GameState(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.Font(None, 48)  # Increased font size for emojis
        self.grid = [[EMOJI_UNKNOWN for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.grid[1][1] = EMOJI_START  # Starting position
        self.player_pos = [1, 1]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            new_pos = self.player_pos.copy()
            if event.key == pygame.K_UP and self.player_pos[0] > 0:
                new_pos[0] -= 1
            elif event.key == pygame.K_DOWN and self.player_pos[0] < GRID_SIZE - 1:
                new_pos[0] += 1
            elif event.key == pygame.K_LEFT and self.player_pos[1] > 0:
                new_pos[1] -= 1
            elif event.key == pygame.K_RIGHT and self.player_pos[1] < GRID_SIZE - 1:
                new_pos[1] += 1
            elif event.key == pygame.K_ESCAPE:
                self.game.change_state(STATE_MENU)

            if new_pos != self.player_pos:
                self.move_player(new_pos)

    def move_player(self, new_pos):
        # Reveal the new room
        if self.grid[new_pos[0]][new_pos[1]] == EMOJI_UNKNOWN:
            self.grid[new_pos[0]][new_pos[1]] = random.choice([
                EMOJI_MONSTER,
                EMOJI_TRAP,
                EMOJI_LOOT,
                EMOJI_EMPTY
            ])
        self.player_pos = new_pos

    def draw(self, screen):
        # Draw grid
        cell_size = ROOM_SIZE
        start_x = (WINDOW_WIDTH - (GRID_SIZE * cell_size)) // 2
        start_y = (WINDOW_HEIGHT - (GRID_SIZE * cell_size)) // 2

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x = start_x + j * cell_size
                y = start_y + i * cell_size
                
                # Draw cell
                pygame.draw.rect(screen, WHITE, (x, y, cell_size, cell_size), 2)
                
                # Draw cell content
                cell_content = self.grid[i][j]
                text = self.font.render(cell_content, True, WHITE)
                text_x = x + (cell_size - text.get_width()) // 2
                text_y = y + (cell_size - text.get_height()) // 2
                screen.blit(text, (text_x, text_y))

                # Draw player on current position
                if [i, j] == self.player_pos:
                    player = self.font.render(EMOJI_PLAYER, True, WHITE)
                    player_x = x + (cell_size - player.get_width()) // 2
                    player_y = y + (cell_size - player.get_height()) // 2
                    screen.blit(player, (player_x, player_y))

        # Draw legend
        legend = [
            f"{EMOJI_START} - Start",
            f"{EMOJI_MONSTER} - Monster",
            f"{EMOJI_TRAP} - Trap",
            f"{EMOJI_LOOT} - Loot",
            f"{EMOJI_EMPTY} - Empty",
            f"{EMOJI_UNKNOWN} - Unknown",
            f"{EMOJI_PLAYER} - Player"
        ]
        legend_y = start_y + (GRID_SIZE * cell_size) + 20
        for text in legend:
            rendered_text = self.font.render(text, True, GRAY)
            screen.blit(rendered_text, (start_x, legend_y))
            legend_y += 40  # Increased spacing for better readability
