
import pygame,random,time,psycopg2,json
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
FOOD_DURATION = {"apple": 50, "banana": 40, "cherry": 35}
FOOD_COLORS = {"apple": RED, "banana": (255, 255, 0), "cherry": (255, 0, 255)}

# Wall management
wall_list = []

# Initialize game variables
snake_position = [90, 30]
snake_body = [[90, 30], [75, 30]]
direction = 'RIGHT'
score = 0
# Initialize last food spawn time
last_food_spawn_time = time.time()  # Track last food spawn time

def should_spawn_food():
    global last_food_spawn_time
    current_time = time.time()
    if current_time - last_food_spawn_time >= 5:
        last_food_spawn_time = current_time
        print("Spawning new food")  # Debug statement
        return True
    return False

# Wall class for level management
class Wall:
    def __init__(self, level):
        self.body = []
        file_path = f"/Users/temirbekboltay/Desktop/lab-10/snake/levels/level_{level}.txt"
        with open(file_path, "r") as file:
            for y in range(WINDOW_Y // SIZE + 1):
                for x in range(WINDOW_X // SIZE + 1):
                    if file.read(1) == '#':
                        self.body.append((x, y))

    def draw(self, game_window):
        for x, y in self.body:
            pygame.draw.rect(game_window, (226, 135, 67), pygame.Rect(x * SIZE, y * SIZE, SIZE, SIZE))

# Choose food type based on probabilities
def choose_food():
    return random.choices(list(FOOD_PROBABILITIES.keys()), weights=FOOD_PROBABILITIES.values())[0]

def spawn_food():
    while True:
        food_type = choose_food()
        x = random.randrange(1, WINDOW_X // SIZE) * SIZE
        y = random.randrange(1, WINDOW_Y // SIZE) * SIZE
        if (x // SIZE, y // SIZE) not in wall_list:
            print(f"Food spawned: {food_type} at ({x}, {y})")  # Debug statement
            return {
                "type": food_type,
                "position": [x, y],
                "color": FOOD_COLORS[food_type],
                "score": FOOD_SCORES[food_type],
                "timer": FOOD_DURATION[food_type]
            }
        
def save_game_state(username, snake_body, snake_position, score, level, direction, foods, snake_speed, filename='final_game_state.json'):
    # Constructing the dictionary with the game state
    state = {
        "username": username,
        "snake_body": snake_body,
        "snake_position": snake_position,
        "score": score,
        "level": level,
        "direction": direction,
        "foods": foods,
        "snake_speed": snake_speed
    }

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # Save or update the game state in the database
        cur.execute("INSERT INTO game_state (username, state) VALUES (%s, %s) ON CONFLICT (username) DO UPDATE SET state = %s",
                    (username, json.dumps(state), json.dumps(state)))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Database error: {error}")
    finally:
        if conn:
            cur.close()
            conn.close()
    
    # Serializing the state to a JSON formatted string
    state_json = json.dumps(state, indent=4)
    
    # Writing to a file
    with open(filename, 'w') as file:
        file.write(state_json)

# Specific game state example with a username
username = "Player1"
snake_body = [[200, 200], [185, 200], [170, 200]]
snake_position = [200, 200]
score = 30
level = 3
direction = 'RIGHT'
foods = [{'type': 'apple', 'position': [300, 200]}, {'type': 'cherry', 'position': [150, 200]}]
snake_speed = 12

# Save to JSON file
save_game_state(username, snake_body, snake_position, score, level, direction, foods, snake_speed)

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
    
    running = True
    while running: 
        # Spawn food immediately if not spawned yet
        if not first_food_spawned:
            new_food = spawn_food()
            foods.append(new_food)
            first_food_spawned = True

        # Check if food should spawn
        if should_spawn_food():
            new_food = spawn_food()
            foods.append(new_food)
            
        for food in foods[:]:
            pygame.draw.rect(game_window, food["color"], pygame.Rect(food["position"][0], food["position"][1], SIZE, SIZE))
            food["timer"] -= 1
            if food["timer"] <= 0:
                foods.remove(food)

        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    is_paused = not is_paused
                elif not is_paused:  # Handle direction keys only when not paused
                    if event.key == pygame.K_UP and direction != 'DOWN':
                        direction = 'UP'
                    elif event.key == pygame.K_DOWN and direction != 'UP':
                        direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                        direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                        direction = 'RIGHT'

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

            # Update snake's position in the body list
            snake_body.pop()
            snake_body.insert(0, list(snake_position))
            
            # Check for food collision and score updates
            for food in foods:
                if food["position"] == snake_position:
                    score += food["score"]
                    fruits_eaten += 1
                    foods.remove(food)
                    break

            # Check level advancement
            if fruits_eaten == 5:
                level += 1
                snake_speed += 2
                snake_position = [90, 30]
                direction = 'RIGHT'
                snake_body = [[90, 30], [75, 30]]
                fruits_eaten = 0
            
            # Check for game over conditions
            if (snake_position[0] < 0 or snake_position[0] >= WINDOW_X or 
                snake_position[1] < 0 or snake_position[1] >= WINDOW_Y or
                snake_position in snake_body[1:]):
                running = False
                break
            
            # Clear game window for next frame
            game_window.fill(BLACK)
            wall = Wall(level)
            wall.draw(game_window)
            for pos in snake_body:
                pygame.draw.rect(game_window, GREEN, pygame.Rect(pos[0], pos[1], SIZE, SIZE))

            # Display grid lines, score, and level
            draw_grid(game_window)
            show_score(game_window, WHITE, 'times new roman', 20, score)
            display_level(game_window, WHITE, level)

        else:
            display_pause_message(game_window)
        
        # Update display and set FPS
        pygame.display.update()
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
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        # Check if the username exists
        cur.execute("SELECT score, level FROM user_score WHERE username=%s", (username,))
        result = cur.fetchone()
        
        # Update or insert the user's score and level
        if result:
            if score > result[0] and level > result[1]:
                cur.execute("UPDATE user_score SET score=%s, level=%s WHERE username=%s", (score, level, username))
        else:
            cur.execute("INSERT INTO user_score (username, score, level) VALUES (%s, %s, %s)", (username, score, level))
        
        conn.commit()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            cur.close()
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