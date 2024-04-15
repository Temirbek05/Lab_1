import pygame
import time
import random

# Set the speed of the snake
snake_speed = 8

# Define a variable to keep track of the time
last_food_spawn_time = time.time()

# Define the probabilities for each type of food
food_probabilities = {
    "apple": 0.4,   # Adjusted probabilities
    "banana": 0.3,
    "cherry": 0.3
}

# Define the scores for each type of food
food_scores = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}

# Define the time duration for each type of food (in seconds)
food_duration = {
    "apple": 10,
    "banana": 5,
    "cherry": 3
}

# Define colors for each type of food
food_colors = {
    "apple": (255, 0, 0),   # Red
    "banana": (255, 255, 0),  # Yellow
    "cherry": (255, 0, 255)  # Magenta
}

# Function to check if a new food item should be spawned
def should_spawn_food():
    global last_food_spawn_time
    
    # Check if enough time has elapsed since the last food spawn
    if time.time() - last_food_spawn_time >= 5:
        last_food_spawn_time = time.time()
        return True
    else:
        return False

# Function to randomly select a food type based on probabilities
def choose_food():
    food_types = list(food_probabilities.keys())
    return random.choices(food_types, weights=food_probabilities.values())[0]

# Function to spawn a new food item
def spawn_food():
    while True:
        food_type = choose_food()
        food_position = [random.randrange(1, (window_x // size)) * size,
                         random.randrange(1, (window_y // size)) * size]
        
        # Check if the food position is within the wall's coordinates
        if not any(wall_block == (food_position[0] // size, food_position[1] // size) for wall_block in wall.list):
            break
        
    food_color = food_colors[food_type]
    food_score = food_scores[food_type]
    food_timer = food_duration[food_type]
    return {"type": food_type, "position": food_position, "color": food_color, "score": food_score, "timer": food_timer}

# Set the size of each block in the game window
size = 15

# Define the size of the game window
window_x = 600
window_y = 450

# Define colors using RGB values
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

# Initialize pygame
pygame.init()

# Set the title of the game window
pygame.display.set_caption('Snake')

# Create the game window
game_window = pygame.display.set_mode((window_x, window_y))

# Set the controller for Frames Per Second (FPS)
fps = pygame.time.Clock()

# Set the initial position of the snake
snake_position = [210, 345]

# Set the initial body of the snake with 4 blocks
snake_body = [[90, 30], [75, 30]]

# Set the initial direction of the snake
direction = 'RIGHT'
change_to = direction

# Initialize the score
score = 0

# List to hold active food items
foods = []

# Function to display the score on the game window
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# Function to handle game over scenario
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
running = True
while running:
    # Spawn new food if probability condition is met
    if random.random() < 0.8:
        foods.append(spawn_food())
        
    # Update and remove existing food items
    for food in foods[:]:
        pygame.draw.rect(game_window, food["color"], pygame.Rect(food["position"][0], food["position"][1], size, size))
        food["timer"] -= 1
        if food["timer"] <= 0:
            foods.remove(food)

    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Update snake direction based on key input
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_position[1] -= 15
    if direction == 'DOWN':
        snake_position[1] += 15
    if direction == 'LEFT':
        snake_position[0] -= 15
    if direction == 'RIGHT':
        snake_position[0] += 15

    # Mechanism to grow the snake's body and increase score when it eats fruit
    snake_body.insert(0, list(snake_position))
    for food in foods:
        if snake_position[0] == food["position"][0] and snake_position[1] == food["position"][1]:
            score += food["score"]
            foods.remove(food)

    # Draw the snake on the game window
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], size, size))

    # Display the score continuously
    show_score(white, 'times new roman', 20)

    # Refresh the game screen
    pygame.display.update()
    fps.tick(snake_speed)
