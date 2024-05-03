import psycopg2
import pygame 
from user import authenticate_user 

pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set fonts
font = pygame.font.Font(None, 32)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("User Authentication")


def run_authentication_screen(screen):
    username = ""
    password = ""
    input_box1 = pygame.Rect(300, 200, 200, 32)
    input_box2 = pygame.Rect(300, 300, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text1 = ''
    text2 = ''
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box1.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                if input_box2.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        # Authenticate user
                        user_id = authenticate_user(username, password)
                        if user_id:
                            print("User authenticated successfully!")
                            done = True  # Exit authentication loop
                        else:
                            print("Authentication failed. Please try again.")
                            # Clear input fields or display error message
                    elif event.key == pygame.K_BACKSPACE:
                        if input_box1.collidepoint(pygame.mouse.get_pos()):
                            username = username[:-1]
                        else:
                            password = password[:-1]
                    else:
                        if input_box1.collidepoint(pygame.mouse.get_pos()):
                            username += event.unicode
                        else:
                            password += event.unicode
            color = color_active if active else color_inactive
        screen.fill(WHITE)
        # Render input boxes
        pygame.draw.rect(screen, color, input_box1, 2)
        pygame.draw.rect(screen, color, input_box2, 2)
        # Render text
        txt_surface1 = font.render(username, True, color)
        txt_surface2 = font.render('*' * len(password), True, color)
        width = max(200, txt_surface1.get_width() + 10)
        input_box1.w = width
        input_box2.w = width
        screen.blit(txt_surface1, (input_box1.x + 5, input_box1.y + 5))
        screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y + 5))
        pygame.display.flip()
        pygame.time.wait(30)
