import pygame
import random
import time
import psycopg2
from config import config
from snake.create_table_user_score import create_table

# Initialize pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

user_text = ''

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set fonts
font = pygame.font.Font(None, 32)

clock = pygame.time.Clock()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("User Authentication")

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

def save(name, score, level):
    sql_select = "SELECT * FROM user_score WHERE username=%s"
    sql_insert = "INSERT INTO user_score(username, score, level) VALUES(%s, %s, %s)"
    sql_update = "UPDATE user_score SET score=%s, level=%s WHERE username=%s"
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql_select, (name,))
        result = cur.fetchone()
        if result:
            score_prev, level_prev = result[2], result[3]
            if score > score_prev and level > level_prev:
                cur.execute(sql_update, (score, level, name))
        else:
            cur.execute(sql_insert, (name, score, level))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()

def read(username):
    score, level = 0, 0
    sql = "SELECT score, level FROM user_score WHERE username=%s"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (username,))
        result = cur.fetchone()
        if result:
            score, level = result[0], result[1]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()
    return score, level


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
        f = open("/Users/temirbekboltay/Desktop/lab-10/snake/levels/level_{}.txt".format(level), 'r')  # Load the appropriate map file based on the level

        for y, line in enumerate(f):
            for x, c in enumerate(line):
                if c == '#':
                    self.body.append((x, y))  # Add wall block coordinates to the wall body list

    def draw(self, screen):  # Define a method to draw the wall
        for block in self.body:
            rect = pygame.Rect(block[0] * size, block[1] * size, size, size)
            pygame.draw.rect(screen, BLACK, rect)

# Define a Snake class
class Snake:
    def __init__(self):
        self.body = [Point(3, 5), Point(4, 5), Point(5, 5)]  # Initialize the snake body with three segments
        self.direction = "RIGHT"  # Set the initial direction of the snake
        self.change_to = self.direction  # Initialize the change_to attribute

    # Define a method to control the movement of the snake
    def change_direction_to(self, dir):
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    # Define a method to move the snake
    def move(self, food_position):
        if self.direction == "RIGHT":
            self.head = Point(self.body[0].x + 1, self.body[0].y)
        if self.direction == "LEFT":
            self.head = Point(self.body[0].x - 1, self.body[0].y)
        if self.direction == "UP":
            self.head = Point(self.body[0].x, self.body[0].y - 1)
        if self.direction == "DOWN":
            self.head = Point(self.body[0].x, self.body[0].y + 1)

        self.body.insert(0, self.head)  # Insert a new head segment to the front of the snake body

        if self.body[0].x == food_position[0] / size and self.body[0].y == food_position[1] / size:
            return True
        else:
            self.body.pop()  # Remove the last segment of the snake body
            return False

    # Define a method to check for collisions with the walls
    def hit_walls(self):
        if self.body[0].x >= window_x // size or self.body[0].x < 0 or self.body[0].y >= window_y // size or self.body[0].y < 0:
            return True

        for block in self.body[1:]:
            if self.body[0].x == block.x and self.body[0].y == block.y:
                return True

        for block in wall.body:
            if self.body[0].x == block[0] and self.body[0].y == block[1]:
                return True

        return False

    # Define a method to check for collisions with the walls
    def hit_walls(self):
        if self.body[0].x >= window_x // size or self.body[0].x < 0 or self.body[0].y >= window_y // size or self.body[0].y < 0:
            return True

        for block in self.body[1:]:
            if self.body[0].x == block.x and self.body[0].y == block.y:
                return True

        for block in wall.body:
            if self.body[0].x == block[0] and self.body[0].y == block[1]:
                return True

        return False

    # Define a method to check for collisions with the snake itself
    def collide(self):
        for block in self.body[1:]:
            if self.body[0].x == block.x and self.body[0].y == block.y:
                return True
        return False


def choose_food():
    food_type = random.choices(list(food_probabilities.keys()), list(food_probabilities.values()))[0]
    return food_type

def show_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [0, 0])

def show_level(level):
    level_text = font.render("Level: " + str(level), True, WHITE)
    screen.blit(level_text, [0, 30])

def show_game_over():
    over_text = font.render("GAME OVER", True, WHITE)
    screen.blit(over_text, [SCREEN_WIDTH // 2 - over_text.get_width() // 2, SCREEN_HEIGHT // 2 - over_text.get_height() // 2])

def play_game(username):
    # Initialize the snake object
    snake = Snake()

    # Initialize the wall object
    global wall
    wall = Wall(1)

    # Initialize the size of the snake segments and the food
    global size
    size = 20

    # Initialize the window dimensions
    global window_x, window_y
    window_x, window_y = 600, 400

    # Set the initial score and level
    score, level = read(username)

    # Initialize the game loop variable
    game_over = False

    # Initialize the direction variable
    direction = 1

    # Set the initial food type and position
    food = spawn_food()

    while not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction_to("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction_to("RIGHT")
                elif event.key == pygame.K_UP:
                    snake.change_direction_to("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction_to("DOWN")

        screen.fill(BLACK)  # Fill the screen with black color

        # Move the snake
        if snake.move(food['position']):
            score += food['score']
            food = spawn_food()

        # Check for collisions with the walls or the snake itself
        if snake.hit_walls() or snake.collide():
            game_over = True

        # Draw the wall
        wall.draw(screen)

        # Draw the snake
        for block in snake.body:
            rect = pygame.Rect(block.x * size, block.y * size, size, size)
            pygame.draw.rect(screen, WHITE, rect)

        # Draw the food
        pygame.draw.rect(screen, food['color'], pygame.Rect(food['position'][0], food['position'][1], size, size))

        show_score(score)
        show_level(level)

        pygame.display.update()
        pygame.time.Clock().tick(snake_speed)

    # Save score and level to the database
    save(username, score, level)

    # Display game over message
    show_game_over()
    pygame.display.update()
    time.sleep(2)

# Main function
def main():
    create_table()
    global user_text
    username = ""
    user_prompt = True
    while user_prompt:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                user_prompt = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    user_prompt = False
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode
        font = pygame.font.Font(None, 36)
        user_text = font.render(username, True, WHITE)
        screen.blit(user_text, [10, 10])
        pygame.display.flip()
        clock.tick(30)
    play_game(username)

# Call the main function
main()

pygame.quit()
