import pygame
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game Splash Screen')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Load splash screen image (optional)
# splash_image = pygame.image.load('splash_image.png')
# splash_image = pygame.transform.scale(splash_image, (WIDTH, HEIGHT))

# Splash Screen function
def show_splash_screen():
    screen.fill(WHITE)

    # Draw splash screen image (if any)
    # screen.blit(splash_image, (0, 0))

    # Draw game title
    title_text = font.render('My Board Game', True, BLACK)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(title_text, title_rect)

    # Draw start prompt
    start_text = small_font.render('Press any key to start', True, BLACK)
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(start_text, start_rect)

    pygame.display.flip()

    # Wait for user input
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

# Main function
def main():
    show_splash_screen()

    # Placeholder for the main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()