import pygame

class CharacterManager:
    def __init__(self, characters):
        self.characters = characters
        self.selected_character = 0

    def draw_text(self, text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        surface.blit(text_obj, text_rect)

    def select_character(self, screen, font, small_font, colors, dimensions):
        WHITE, BLACK, HOVER_GRAY = colors
        WIDTH, HEIGHT = dimensions

        selecting = True
        while selecting:
            screen.fill(WHITE)

            # Draw character selection prompt
            self.draw_text('Select Your Character', font, BLACK, screen, WIDTH // 2, HEIGHT // 2 - 150)

            # Draw character options
            char_rects = []
            for i, character in enumerate(self.characters):
                color = HOVER_GRAY if i == self.selected_character else BLACK
                text_obj = small_font.render(character, True, color)
                text_rect = text_obj.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 50))
                screen.blit(text_obj, text_rect)
                char_rects.append((text_rect, character))

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_character = (self.selected_character - 1) % len(self.characters)
                    if event.key == pygame.K_DOWN:
                        self.selected_character = (self.selected_character + 1) % len(self.characters)
                    if event.key == pygame.K_RETURN:
                        return self.characters[self.selected_character]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_pos = event.pos
                        for rect, character in char_rects:
                            if rect.collidepoint(mouse_pos):
                                return character

            pygame.display.flip()