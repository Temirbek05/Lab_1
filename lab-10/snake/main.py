import pygame
import random
import time
import psycopg2
from config import config
from authentication import authenticate_user

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SIZE = 15  # Block size
WINDOW_X = 600
WINDOW_Y = 450
SNAKE_SPEED = 8

# Fonts and clock
font = pygame.font.Font(None, 32)
fps = pygame.time.Clock()

# Authentication screen setup
auth_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("User Authentication")

# Food properties and probabilities
FOOD_PROBABILITIES = {"apple": 0.4, "banana": 0.3, "cherry": 0.3}
FOOD_SCORES = {"apple": 1, "banana": 2, "cherry": 3}
FOOD_DURATION = {"apple": 45, "banana": 40, "cherry": 35}
FOOD_COLORS = {"apple": RED, "banana": (255, 255, 0), "cherry": (255, 0, 255)}

# Wall management
wall_list = []

# Initialize game variables
snake_position = [90, 30]
snake_body = [[90, 30], [75, 30]]
direction = 'RIGHT'
score = 0

# Initialize last food spawn time
last_food_spawn_time = time.time()

def should_spawn_food():
    global last_food_spawn_time
    current_time = time.time()
    if current_time - last_food_spawn_time >= 5:
        last_food_spawn_time = current_time
        return True
    return False

# Wall class for level management
class Wall:
    def __init__(self, level):
        self.body = []
        file_path = f"/Users/temirbekboltay/Desktop/lab-10/snake/levels/level_{level}.txt"
        try:
            with open(file_path, "r") as file:
                for y in range(WINDOW_Y // SIZE + 1):
                    for x in range(WINDOW_X // SIZE + 1):
                        if file.read(1) == '#':
                            self.body.append((x, y))
        except FileNotFoundError:
            print(f"Error: Level file {file_path} not found.")

    def draw(self, game_window):
        for x, y in self.body:
            pygame.draw.rect(game_window, (226, 135, 67), pygame.Rect(x * SIZE, y * SIZE, SIZE, SIZE))

# Choose food type based on probabilities
def choose_food():
    return random.choices(list(FOOD_PROBABILITIES.keys()), weights=FOOD_PROBABILITIES.values())[0]

def spawn_food(wall):
    while True:
        food_type = choose_food()
        x = random.randrange(1, WINDOW_X // SIZE) * SIZE
        y = random.randrange(1, WINDOW_Y // SIZE) * SIZE
        
        # Check if the chosen position is on a wall
        is_valid_position = True
        for wall_x, wall_y in wall.body:
            if (x // SIZE == wall_x) and (y // SIZE == wall_y):
                is_valid_position = False
                break
        
        if is_valid_position:
            return {
                "type": food_type,
                "position": [x, y],
                "color": FOOD_COLORS[food_type],
                "score": FOOD_SCORES[food_type],
                "timer": FOOD_DURATION[food_type]
            }

def display_pause_message(game_window):
    pause_font = pygame.font.SysFont('arial', 36)
    pause_surf = pause_font.render('Game Paused - Press P to Resume', True, WHITE)
    pause_rect = pause_surf.get_rect(center=(WINDOW_X / 2, WINDOW_Y / 2))
    game_window.blit(pause_surf, pause_rect)

is_paused = False

# Main game loop
def game_loop(username):
    global is_paused, snake_position, snake_body, direction, score

    # Initialize game window
    game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    pygame.display.set_caption("Snake")

    snake_speed = SNAKE_SPEED
    foods = []

    level = 1
    fruits_eaten = 0
    
    first_food_spawned = False 
    
    # Initialize wall
    wall = Wall(level)
    
    running = True
    while running:
        # Spawn food immediately if not spawned yet
        if not first_food_spawned:
            new_food = spawn_food(wall)
            foods.append(new_food)
            first_food_spawned = True
 
        # Check if food should spawn
        if should_spawn_food() and len(foods) == 0:
            new_food = spawn_food(wall)
            foods.append(new_food)

        if not foods:
            new_food = spawn_food(wall)
            foods.append(new_food)
 
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    is_paused = not is_paused
                elif not is_paused:
                    if event.key == pygame.K_UP and direction != 'DOWN':
                        direction = 'UP'
                    elif event.key == pygame.K_DOWN and direction != 'UP':
                        direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                        direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                        direction = 'RIGHT'

        # Move the snake and perform other game logic only if the game is not paused
        if not is_paused:
            # Move snake based on direction
            if direction == 'UP':
                snake_position[1] -= SIZE
            elif direction == 'DOWN':
                snake_position[1] += SIZE
            elif direction == 'LEFT':
                snake_position[0] -= SIZE
            elif direction == 'RIGHT':
                snake_position[0] += SIZE
            
            # Check for food collision and score updates
            for food in foods[:]:
                if food["position"] == snake_position:
                    score += food["score"]
                    fruits_eaten += 1
                    foods.remove(food)
                    snake_body.insert(0, list(snake_position))
                    break
            
            # Move the snake body
            else:
                snake_body.pop()
                snake_body.insert(0, list(snake_position))

            # Check for collisions with walls
            if any(snake_position == [wall_x * SIZE, wall_y * SIZE] for wall_x, wall_y in wall.body):
                running = False
            
            # Clear game window for the next frame
            game_window.fill(BLACK)

            # Check level advancement
            if fruits_eaten == 5:
                level += 1
                snake_speed += 2
                snake_position = [90, 30]
                direction = 'RIGHT'
                snake_body = [[90, 30], [75, 30]]
                fruits_eaten = 0
                
                # Update wall when level advances
                wall = Wall(level)
            
            # Draw walls
            wall.draw(game_window)
            # Draw snake body
            for pos in snake_body:
                pygame.draw.rect(game_window, GREEN, pygame.Rect(pos[0], pos[1], SIZE, SIZE))

            # Display grid lines, score, and level
            draw_grid(game_window)
            show_score(game_window, WHITE, 'times new roman', 20, score)
            display_level(game_window, WHITE, level)

        else:
            # If the game is paused, display the pause message
            display_pause_message(game_window)

        # Draw all foods regardless of whether the game is paused or not
        for food in foods[:]:
            pygame.draw.rect(game_window, food["color"], pygame.Rect(food["position"][0], food["position"][1], SIZE, SIZE))
            food["timer"] -= 1
            if food["timer"] <= 0:
                foods.remove(food)

        # Update display at the end of each loop iteration
        pygame.display.update()
        
        # Control the frame rate using the current snake speed
        fps.tick(snake_speed)

    # Save score at game over
    save_score(username, score, level)
    game_over(score)

# Function to display grid lines
def draw_grid(game_window):
    for x in range(0, WINDOW_X, SIZE):
        for y in range(0, WINDOW_Y, SIZE):
            pygame.draw.rect(game_window, (28, 18, 48), pygame.Rect(x, y, SIZE, SIZE), 1)

# Display score on the screen
def show_score(game_window, color, font, size, score):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score: {score}', True, color)
    game_window.blit(score_surface, (10, 10))

# Display level on the screen
def display_level(game_window, color, level):
    level_font = pygame.font.SysFont("Arial", 24)
    level_text = level_font.render(f'Level: {level}', True, color)
    game_window.blit(level_text, (WINDOW_X - 120, 10))

# Save player's score and level
def save_score(username, score, level):
    conn = None
    cur = None
    try:
        # Get database connection parameters from config
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Check if the username exists in the snake_users table
        cur.execute("SELECT * FROM snake_users WHERE username=%s", (username,))
        user_exists = cur.fetchone()
        
        # If the username doesn't exist in the snake_users table, insert it
        if not user_exists:
            cur.execute("INSERT INTO snake_users (username) VALUES (%s)", (username,))
        
        # Check if the username exists in the user_records table
        cur.execute("SELECT score, level FROM user_records WHERE username=%s", (username,))
        result = cur.fetchone()
        
        # Update or insert the user's score and level
        if result:
            if score > result[0] or level > result[1]:
                cur.execute("UPDATE user_records SET score=%s, level=%s WHERE username=%s", (score, level, username))
        else:
            cur.execute("INSERT INTO user_records (username, score, level) VALUES (%s, %s, %s)", (username, score, level))
        
        # Commit the changes to the database
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # Close the cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()

# Game over scenario
def game_over(score):
    game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render(f'Your Score is: {score}', True, RED)
    game_over_rect = game_over_surface.get_rect(center=(WINDOW_X / 2, WINDOW_Y / 2))
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()

# Main authentication loop
def authentication_loop():
    global auth_screen
    user_text = ''
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    # Authenticate the user
                    if authenticate_user(user_text):
                        game_loop(user_text)
                    else:
                        print("Authentication failed.")
                        user_text = ''
                else:
                    user_text += event.unicode

        # Clear the screen and render the UI
        auth_screen.fill(BLACK)
        display_auth_ui(auth_screen, user_text)
        pygame.display.update()

        # Limit frame rate
        fps.tick(30)

# Function to render authentication UI
def display_auth_ui(auth_screen, user_text):
    input_box = pygame.Rect(200, 250, 400, 40)
    pygame.draw.rect(auth_screen, WHITE, input_box, 2)
    text_surface = font.render(user_text, True, WHITE)
    auth_screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

# Entry point
if __name__ == '__main__':
    authentication_loop()
