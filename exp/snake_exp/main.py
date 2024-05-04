import pygame
import time
from settings import *
from game_functions import should_spawn_food, spawn_food
from database import save_game_state, save_score
from authentication import authenticate_user

def main():
    pygame.init()
    font = pygame.font.SysFont('Arial', 24)
    fps = pygame.time.Clock()
    game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    pygame.display.set_caption("Snake")

    # Game variables
    snake_position = [90, 30]
    snake_body = [[90, 30], [75, 30]]
    direction = 'RIGHT'
    score = 0
    level = 1
    snake_speed = SNAKE_SPEED
    foods = []
    wall_list = []  # This should be populated based on level
    last_food_spawn_time = time.time()
    is_paused = False
    running = True

    # Main game loop
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    is_paused = not is_paused
                if not is_paused:
                    if event.key == pygame.K_UP and direction != 'DOWN':
                        direction = 'UP'
                    elif event.key == pygame.K_DOWN and direction != 'UP':
                        direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                        direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                        direction = 'RIGHT'

        if not is_paused:
            # Update game state
            # Move the snake
            if direction == 'UP':
                snake_position[1] -= SIZE
            elif direction == 'DOWN':
                snake_position[1] += SIZE
            elif direction == 'LEFT':
                snake_position[0] -= SIZE
            elif direction == 'RIGHT':
                snake_position[0] += SIZE

            # Check for food collision
            for food in foods[:]:  # Use a slice to clone the list for safe removal
                if food["position"] == snake_position:
                    score += food["score"]
                    foods.remove(food)
                    snake_body.insert(0, list(snake_position))  # Grow snake
                    break
            else:
                snake_body.pop()  # Move the snake
                snake_body.insert(0, list(snake_position))

            # Check for food spawning
            spawn, last_food_spawn_time = should_spawn_food(last_food_spawn_time)
            if spawn:
                new_food = spawn_food(wall_list, WINDOW_X, SIZE)
                foods.append(new_food)

            # Render the game state
            game_window.fill(BLACK)
            for food in foods:
                pygame.draw.rect(game_window, food["color"], pygame.Rect(food["position"][0], food["position"][1], SIZE, SIZE))
            for pos in snake_body:
                pygame.draw.rect(game_window, GREEN, pygame.Rect(pos[0], pos[1], SIZE, SIZE))
            show_score(game_window, score, font)

        else:
            display_pause_message(game_window, font)

        pygame.display.update()
        fps.tick(snake_speed)

    pygame.quit()

def show_score(game_window, score, font):
    score_surface = font.render(f'Score: {score}', True, WHITE)
    game_window.blit(score_surface, (10, 10))

def display_pause_message(game_window, font):
    pause_text = "Game Paused - Press P to Resume"
    pause_surf = font.render(pause_text, True, WHITE)
    pause_rect = pause_surf.get_rect(center=(WINDOW_X / 2, WINDOW_Y / 2))
    game_window.blit(pause_surf, pause_rect)

if __name__ == '__main__':
    main()
