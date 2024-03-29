import pygame
import datetime
pygame.init()

def rot_center(image, angle, x, y):

    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=(x, y))

    return rotated_image, new_rect

pygame.display.set_caption("Clock")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

bg = pygame.image.load('/Users/temirbekboltay/Desktop/lab-7/Image/background.jpg')
min_h = pygame.image.load('/Users/temirbekboltay/Desktop/lab-7/Image/min.jpg')
sec_h = pygame.image.load('/Users/temirbekboltay/Desktop/lab-7/Image/sec.jpg')

screen.blit(bg, (0,0))
screen.blit(min_h, (250,150))
screen.blit(sec_h, (250,150))

font = pygame.font.Font(None, 64)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    now = datetime.datetime.now()
    sec = now.second
    min = now.minute

    clock_display = font.render("{:02d}:{:02d}".format(min, sec), True, (0, 0, 0))

    angle_sec = sec * 6 
    angle_min = min * 6 + (angle_sec) / 60

    sec_hand, rect_sec = rot_center(sec_h, angle_sec, 400, 300)
    min_hand, rect_min = rot_center(min_h, angle_min, 400, 300)

    screen.blit(bg, (0,0))
    screen.blit(sec_hand, rect_sec)
    screen.blit(min_hand, rect_min)
    screen.blit(clock_display, (0, 0))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()