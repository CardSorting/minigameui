import pygame
import random
import numpy

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Game:
    def __init__(self, character, width=800, height=600):
        self.character = character
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Board Game')
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        self.turn = 1
        self.dice_result = 0
        self.dice_button = pygame.Rect(self.width // 2 - 50, self.height // 2 - 25, 100, 50)
        self.restart_button = pygame.Rect(self.width // 2 - 50, self.height - 100, 100, 50)
        self.message = ""
        self.message_duration = 0
        self.lives = 3
        self.game_over = False
        pygame.mixer.init()
        # Corrected sound initialization
        self.dice_roll_sound = self.create_sound(440, 0.5)  # Using built-in tone for dice roll
        self.minigame_sound = self.create_sound(659, 0.5)  # Using built-in tone for minigame
        self.bonus_turn_sound = self.create_sound(784, 0.5)  # Using built-in tone for bonus turn

    def create_sound(self, frequency, duration):
        sample_rate = 44100
        n_samples = int(sample_rate * duration)
        t = numpy.linspace(0, duration, n_samples, endpoint=False)
        wave = 0.5 * numpy.sin(2 * numpy.pi * frequency * t)
        wave = numpy.int16(wave * 32767)
        sound_buffer = numpy.zeros((n_samples, 2), dtype=numpy.int16)
        sound_buffer[:, 0] = wave  # left channel
        sound_buffer[:, 1] = wave  # right channel
        return pygame.sndarray.make_sound(sound_buffer)

    def start_game(self):
        print(f"Starting game with {self.character}...")
        self.main_game_loop()

    def roll_dice(self):
        self.dice_result = random.randint(1, 6)
        self.dice_roll_sound.play()
        print(f"Player rolled a {self.dice_result}")
        return self.dice_result

    def handle_minigame(self, dice_result):
        # Placeholder for mini-game logic
        print(f"Handling mini-game for dice roll {dice_result}.")
        # Simulate mini-game outcome
        minigame_won = random.choice([True, False])  # Randomly determine if the player wins or loses
        if minigame_won:
            self.message = f"Player won the mini-game for roll {dice_result}!"
            self.minigame_sound.play()
            self.turn += 1  # Advance to the next stage
        else:
            self.message = f"Player lost the mini-game for roll {dice_result}!"
            self.lives -= 1  # Lose a life
            if self.lives == 0:
                self.game_over = True
            self.minigame_sound.play()
        self.message_duration = 3000  # Display the message for 3 seconds

    def display_message(self, message):
        self.screen.fill(WHITE)
        text = self.big_font.render(message, True, RED)
        self.screen.blit(text, (self.width // 2 - text.get_width() // 2, self.height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(2000)

    def draw_button(self, rect, text):
        pygame.draw.rect(self.screen, BLUE, rect)
        button_text = self.font.render(text, True, WHITE)
        self.screen.blit(button_text, (rect.x + (rect.width - button_text.get_width()) // 2, rect.y + (rect.height - button_text.get_height()) // 2))

    def reset_game(self):
        self.turn = 1
        self.dice_result = 0
        self.message = ""
        self.message_duration = 0
        self.lives = 3
        self.game_over = False

    def main_game_loop(self):
        running = True
        last_message_time = pygame.time.get_ticks()
        while running:
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_over:
                        if self.restart_button.collidepoint(event.pos):
                            self.reset_game()
                    elif self.dice_button.collidepoint(event.pos):
                        dice_result = self.roll_dice()
                        self.handle_minigame(dice_result)

            self.screen.fill(WHITE)
            turn_text = self.font.render(f'Turn: {self.turn}', True, BLACK)
            char_text = self.font.render(f'Character: {self.character}', True, BLACK)
            dice_text = self.font.render(f'Dice Result: {self.dice_result}', True, BLACK)
            lives_text = self.font.render(f'Lives: {self.lives}', True, BLACK)

            self.screen.blit(turn_text, (10, 10))
            self.screen.blit(char_text, (10, 50))
            self.screen.blit(dice_text, (10, 90))
            self.screen.blit(lives_text, (10, 130))

            if self.game_over:
                game_over_text = self.big_font.render('Game Over!', True, RED)
                self.screen.blit(game_over_text, (self.width // 2 - game_over_text.get_width() // 2, self.height // 2 - game_over_text.get_height() // 2))
                self.draw_button(self.restart_button, "Restart")
            else:
                self.draw_button(self.dice_button, "Roll Dice")

            if self.message and current_time - last_message_time < self.message_duration:
                message_text = self.font.render(self.message, True, RED)
                self.screen.blit(message_text, (self.width // 2 - message_text.get_width() // 2, self.height - 100))
            else:
                self.message = ""
                last_message_time = current_time

            pygame.display.flip()

        pygame.quit()