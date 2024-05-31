import pygame

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simple Mini-Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

player = pygame.Rect(50, 50, 50, 50)
target = pygame.Rect(random.randint(0, WIDTH-50), random.randint(0, HEIGHT-50), 50, 50)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    if player.colliderect(target):
        print("You won the mini-game!")
        target.x = random.randint(0, WIDTH-50)
        target.y = random.randint(0, HEIGHT-50)

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player)
    pygame.draw.rect(screen, RED, target)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()