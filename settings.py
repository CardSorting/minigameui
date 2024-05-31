import pygame

class Settings:
    def __init__(self, screen, small_font, white, black, gray, hover_gray, width, height):
        self.screen = screen
        self.small_font = small_font
        self.WHITE = white
        self.BLACK = black
        self.GRAY = gray
        self.HOVER_GRAY = hover_gray
        self.WIDTH = width
        self.HEIGHT = height

    def draw_text(self, text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        surface.blit(text_obj, text_rect)

    def display_settings(self):
        running = True
        while running:
            self.screen.fill(self.WHITE)
            self.draw_text('Settings Menu', self.small_font, self.BLACK, self.screen, self.WIDTH // 2, self.HEIGHT // 2 - 50)
            self.draw_text('Press ESC to return', self.small_font, self.GRAY, self.screen, self.WIDTH // 2, self.HEIGHT // 2 + 50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.flip()