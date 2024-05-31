import pygame
import sys
from character_manager import CharacterManager
from game import Game
from settings import Settings

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Board Game Main Menu')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
HOVER_GRAY = (150, 150, 150)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Menu options
menu_options = ["Start Game", "Settings", "Exit"]
selected_option = 0

# Characters
characters = ["Wizard", "Knight", "Dragon"]
character_manager = CharacterManager(characters)

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Function to handle main menu
def main_menu():
    global selected_option

    while True:
        screen.fill(WHITE)

        # Draw title
        draw_text('Board Game', font, BLACK, screen, WIDTH // 2, HEIGHT // 2 - 150)

        # Draw menu options
        menu_rects = []
        for i, option in enumerate(menu_options):
            color = HOVER_GRAY if i == selected_option else BLACK
            text_obj = small_font.render(option, True, color)
            text_rect = text_obj.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 50))
            screen.blit(text_obj, text_rect)
            menu_rects.append((text_rect, option))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                if event.key == pygame.K_RETURN:
                    handle_menu_selection(menu_options[selected_option])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = event.pos
                    for rect, option in menu_rects:
                        if rect.collidepoint(mouse_pos):
                            handle_menu_selection(option)

        pygame.display.flip()

def handle_menu_selection(option):
    if option == "Start Game":
        selected_character = character_manager.select_character(screen, font, small_font, (WHITE, BLACK, HOVER_GRAY), (WIDTH, HEIGHT))
        game = Game(selected_character)
        game.start_game()
    elif option == "Settings":
        settings = Settings(screen, small_font, WHITE, BLACK, GRAY, HOVER_GRAY, WIDTH, HEIGHT)
        settings.display_settings()
    elif option == "Exit":
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    main_menu()