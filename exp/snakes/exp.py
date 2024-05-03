import psycopg2
import pygame
import time
import random
import sys
import authentication  # Import the authentication module
from user import authenticate_user, record_score
from high_scores import display_high_scores

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


# Run authentication screen first
authentication.run_authentication_screen(screen)

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

# Define a list to hold wall block coordinates (initialize as empty list if no walls initially)
wall_list = []

# Function to check if a food item overlaps with any wall block within the buffer zone
def is_food_position_valid(food_position, wall_blocks):
    # Calculate the integer grid coordinates of the food position
    food_x = food_position[0] // size
    food_y = food_position[1] // size
    
    # Check if the food position is within any wall block
    for wall_block in wall_blocks:
        if (food_x, food_y) == wall_block:
            return False
    
    return True

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Function to spawn a new food item
def spawn_food():
    while True:
        food_type = choose_food()
        food_position = [random.randrange(1, (window_x // size)) * size,
                         random.randrange(1, (window_y // size)) * size]
        
        # Check if the food position is within the wall's coordinates for the current level
        if not any(wall_block == (food_position[0] // size, food_position[1] // size) for wall_block in wall.body):
            break
        
    food_color = food_colors[food_type]
    food_score = food_scores[food_type]
    food_timer = food_duration[food_type]
    return {"type": food_type, "position": food_position, "color": food_color, "score": food_score, "timer": food_timer}

# Add new food to the foods list
foods = []

# Define a Wall class to represent walls in the game
class Wall:  # Define a Wall class
    def __init__(self, level):  # Define a Wall class
        self.body = []  # Initialize Wall body
        self.list = []  # Initialize Wall list

        # Load the appropriate map file based on the level
        f = open("/Users/temirbekboltay/Desktop/lab-10/snake/levels/level_{}.txt".format(level), "r")  # Load the appropriate map file based on the level
        
        # Parse the map file and create walls or obstacles accordingly
        for y in range(window_y // 15 + 1):
            for x in range(window_x // 15 + 1):
                if f.read(1) == '#':  # Parse the map file and create walls or obstacles accordingly
                    self.body.append(Point(x, y))
                    self.list.append([x, y])

    def draw(self):  # Method to draw the wall on the game window
        for point in self.body:
            rect = pygame.Rect(15 * point.x, size * point.y, size, size)
            pygame.draw.rect(game_window, (226, 135, 67), rect)


# Function to randomly select a food type based on probabilities
def choose_food():
    food_types = list(food_probabilities.keys())
    return random.choices(food_types, weights=food_probabilities.values())[0]

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

# Set fruit spawn state
fruit_spawn = True  # > Set fruit spawn state

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


# Set the initial position of the fruit (random)
fruit_position = [random.randrange(1, (window_x // size)) * size,  # > Set the initial position of the fruit (random)
                  random.randrange(1, (window_y // size)) * size]


# Set the initial direction of the snake
direction = 'RIGHT'
change_to = direction

# Initialize the score
score = 0

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

# Function to draw grid lines on the game window
def drawGrid():  # > Function to draw grid lines on the game window
    for x in range(0, window_x, size):
        for y in range(0, window_y, size):
            rect = pygame.Rect(x, y, size, size)
            pygame.draw.rect(game_window, (28, 18, 48), rect, 1)

level = 1  # > Set initial level
fruits_eaten = 0  # > Initialize fruits eaten count


# Main game loop
index = 0  # Initial level
prev_snake_position = [90, 30]  # Initial snake positionrunning = True
running = True

while running:
    wall = Wall(index)  # > Create wall object
    last_snake_position = snake_position.copy()  # > Store the last snake position

    # Spawn new food if probability condition is met
    if random.random() < 0.8:
        foods.append(spawn_food())

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


    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruits_eaten += 1
        fruit_spawn = False
    else:
        snake_body.pop()

    
    # Spawn a new fruit if the previous one is eaten
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // size)) * size,
                          random.randrange(1, (window_y // size)) * size]
        
    fruit_spawn = True
    # Draw the snake on the game window
    game_window.fill(black)

    if fruits_eaten == 5:  # If snake has eaten 4
        index += 1  # > Move to the next level
        snake_speed += 2  # > Increase speed
        prev_snake_position = snake_position[:]  # > Store previous snake position
        snake_position = [210, 240]  # > Reset snake position
        direction = 'RIGHT'  # > Reset direction
        fruits_eaten = 0  # > Reset fruits eaten count
    # Draw walls
    wall = Wall(index)  # > Load the appropriate map for the current level
    wall.draw()  # > Draw walls

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], size, size))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], size, size))

       # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 15:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 15:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    for wall_block in wall.body:
        if snake_position[0] == 15 * wall_block.x and snake_position[1] == size * wall_block.y:
            game_over()

    drawGrid()  # > Draw grid lines

    # Display the score continuously
    show_score(white, 'times new roman', 20)  # Display the score continuously

    # Display the level on the top right
    level_text = pygame.font.SysFont("Arial", 24).render("Level: " + str(index), True, white)
    level_rect = level_text.get_rect()
    level_rect.topright = (window_x - 10, 10)
    game_window.blit(level_text, level_rect)
    # Refresh the game screen
    pygame.display.update()
    fps.tick(snake_speed)
