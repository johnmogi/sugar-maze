# Window Settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TITLE = "Sugarbound: The Labyrinth of Sweets"
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
PINK = (255, 192, 203)

# Game Settings
GRID_SIZE = 3
ROOM_SIZE = 150

# States
STATE_SPLASH = "splash"
STATE_MENU = "menu"
STATE_CHARACTER_CREATE = "character_create"
STATE_GAME = "game"
STATE_COMBAT = "combat"

# Combat Actions
ACTION_HAMMER = "hammer"
ACTION_ARROW = "arrow"
ACTION_POTION = "potion"

# Character Classes
CLASSES = {
    "Fighter": {"strength": 3, "defense": 2, "intelligence": 1, "agility": 1, "luck": 1},
    "Mage": {"strength": 1, "defense": 1, "intelligence": 3, "agility": 2, "luck": 1},
    "Druid": {"strength": 2, "defense": 2, "intelligence": 2, "agility": 1, "luck": 1},
    "Goblin": {"strength": 1, "defense": 1, "intelligence": 1, "agility": 3, "luck": 2},
    "Sugar Knight": {"strength": 2, "defense": 3, "intelligence": 1, "agility": 1, "luck": 1}
}
