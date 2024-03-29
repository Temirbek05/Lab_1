
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

x = 320
y = 240

clock = pygame.time.Clock()
pygame.display.set_caption("Ball game")

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 20
    if pressed[pygame.K_DOWN]: y += 20
    if pressed[pygame.K_LEFT]: x -= 20
    if pressed[pygame.K_RIGHT]: x += 20

    x = max(25, min(x, 615))
    y = max(25, min(y, 455))

    pygame.draw.circle(screen, 'Red', (x, y), 25)
    pygame.display.update()
    clock.tick(25)        
pygame.quit()
