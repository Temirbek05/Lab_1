# import pygame, random, time, psycopg2
# from config import config

# # Initialize pygame
# pygame.init()
# # Set screen dimensions
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

# # Set colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # Set fonts
# font = pygame.font.Font("Verdana", 32)

# # Create the screen
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("User Authentication")

# # Set the speed of the snake
# snake_speed = 8

# # Define a variable to keep track of the time
# last_food_spawn_time = time.time()

# # Define the probabilities for each type of food
# food_probabilities = {
#     "apple": 0.4,   # Adjusted probabilities
#     "banana": 0.3,
#     "cherry": 0.3
# }

# # Define the scores for each type of food
# food_scores = {
#     "apple": 1,
#     "banana": 2,
#     "cherry": 3
# }

# # Define the time duration for each type of food (in seconds)
# food_duration = {
#     "apple": 10,
#     "banana": 5,
#     "cherry": 3
# }

# # Define colors for each type of food
# food_colors = {
#     "apple": (255, 0, 0),   # Red
#     "banana": (255, 255, 0),  # Yellow
#     "cherry": (255, 0, 255)  # Magenta
# }


# def save(name, score, level):
#     sql = "SELECT * FROM user_score WHERE user_name=%s"
#     conn = None
#     try:
#         params = config()
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#         cur.execute(sql, (name,))
#         result = cur.fetchone()
#         if result:
#             sql = """SELECT score, level FROM user_score WHERE user_name=%s"""
#             cur.execute(sql, (name,))
#             result = cur.fetchone()
#             score_prev = result[0]
#             level_prev = result[1]
#             if score > score_prev and level > level_prev:
#                 sql = """UPDATE user_score SET score=%s, level=%s WHERE user_name=%s;"""
#                 cur.execute(sql, (score, level, name,))
#         else:
#             sql = """INSERT INTO users(user_name) VALUES(%s);
#             INSERT INTO user_score(user_name, score, level) VALUES(%s, %s, %s);"""
#             cur.execute(sql, (name, name, score, level,))
#         conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             cur.close()
#             conn.close()

# def read(username):
#     sql = """SELECT score, level FROM user_score WHERE user_name=%s;"""
#     conn = None
#     try:
#         params = config()
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#         cur.execute(sql, (username,))
#         result = cur.fetchone()
#         if result:
#             score = result[0]
#             level = result[1]
#         else:
#             score = 0
#             level = 0
#         conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#     return score, level
    

# # Function to check if a new food item should be spawned
# def should_spawn_food():
#     global last_food_spawn_time
    
#     # Check if enough time has elapsed since the last food spawn
#     if time.time() - last_food_spawn_time >= 5:
#         last_food_spawn_time = time.time()
#         return True
#     else:
#         return False

# # Define a list to hold wall block coordinates (initialize as empty list if no walls initially)
# wall_list = []

# # Function to check if a food item overlaps with any wall block within the buffer zone
# def is_food_position_valid(food_position, wall_blocks):
#     # Calculate the integer grid coordinates of the food position
#     food_x = food_position[0] // size
#     food_y = food_position[1] // size
    
#     # Check if the food position is within any wall block
#     for wall_block in wall_blocks:
#         if (food_x, food_y) == wall_block:
#             return False
    
#     return True

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# # Function to spawn a new food item
# def spawn_food():
#     while True:
#         food_type = choose_food()
#         food_position = [random.randrange(1, (window_x // size)) * size,
#                          random.randrange(1, (window_y // size)) * size]
        
#         # Check if the food position is within the wall's coordinates for the current level
#         if not any(wall_block == (food_position[0] // size, food_position[1] // size) for wall_block in wall.body):
#             break
        
#     food_color = food_colors[food_type]
#     food_score = food_scores[food_type]
#     food_timer = food_duration[food_type]
#     return {"type": food_type, "position": food_position, "color": food_color, "score": food_score, "timer": food_timer}

# # Add new food to the foods list
# foods = []

# # Define a Wall class to represent walls in the game
# class Wall:  # Define a Wall class
#     def __init__(self, level):  # Define a Wall class
#         self.body = []  # Initialize Wall body
#         self.list = []  # Initialize Wall list

#         # Load the appropriate map file based on the level
#         f = open("/Users/temirbekboltay/Desktop/lab-10/snake/levels/level_{}.txt".format(level), "r")  # Load the appropriate map file based on the level
        
#         # Parse the map file and create walls or obstacles accordingly
#         for y in range(window_y // 15 + 1):
#             for x in range(window_x // 15 + 1):
#                 if f.read(1) == '#':  # Parse the map file and create walls or obstacles accordingly
#                     self.body.append(Point(x, y))
#                     self.list.append([x, y])

#     def draw(self):  # Method to draw the wall on the game window
#         for point in self.body:
#             rect = pygame.Rect(15 * point.x, size * point.y, size, size)
#             pygame.draw.rect(game_window, (226, 135, 67), rect)


# # Function to randomly select a food type based on probabilities
# def choose_food():
#     food_types = list(food_probabilities.keys())
#     return random.choices(food_types, weights=food_probabilities.values())[0]

# # Set the size of each block in the game window
# size = 15

# # Define the size of the game window
# window_x = 600
# window_y = 450

# # Define colors using RGB values
# black = pygame.Color(0, 0, 0)
# white = pygame.Color(255, 255, 255)
# green = pygame.Color(0, 255, 0)
# red = pygame.Color(255, 0, 0)

# # Set fruit spawn state
# fruit_spawn = True  # > Set fruit spawn state

# # Set the title of the game window
# pygame.display.set_caption('Snake')

# # Create the game window
# game_window = pygame.display.set_mode((window_x, window_y))

# # Set the controller for Frames Per Second (FPS)
# fps = pygame.time.Clock()

# # Set the initial position of the snake
# snake_position = [210, 345]

# # Set the initial body of the snake with 4 blocks
# snake_body = [[90, 30], [75, 30]]


# # Set the initial position of the fruit (random)
# fruit_position = [random.randrange(1, (window_x // size)) * size,  # > Set the initial position of the fruit (random)
#                   random.randrange(1, (window_y // size)) * size]


# # Set the initial direction of the snake
# direction = 'RIGHT'
# change_to = direction

# # Initialize the score
# score = 0

# # Function to display the score on the game window
# def show_score(color, font, size):
#     score_font = pygame.font.SysFont(font, size)
#     score_surface = score_font.render('Score : ' + str(score), True, color)
#     score_rect = score_surface.get_rect()
#     game_window.blit(score_surface, score_rect)

# # Function to handle game over scenario
# def game_over():
#     my_font = pygame.font.SysFont('times new roman', 50)
#     game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
#     game_over_rect = game_over_surface.get_rect()
#     game_over_rect.midtop = (window_x / 2, window_y / 4)
#     game_window.blit(game_over_surface, game_over_rect)
#     pygame.display.flip()
#     time.sleep(2)
#     pygame.quit()
#     quit()

# # Function to draw grid lines on the game window
# def drawGrid():  # > Function to draw grid lines on the game window
#     for x in range(0, window_x, size):
#         for y in range(0, window_y, size):
#             rect = pygame.Rect(x, y, size, size)
#             pygame.draw.rect(game_window, (28, 18, 48), rect, 1)

# font = pygame.font.SysFont("Verdana", 200)
# font_small = pygame.font.SysFont("Verdana", 60)
# font_smaller = pygame.font.SysFont("Verdana", 30)
# font_smallest = pygame.font.SysFont("Verdana", 20)

# gameover = font_small.render("Game over!", True, "Black")
# gameover_rect = gameover.get_rect().center

# startgame = font_smallest.render("Press ENTER to play", True, "White")
# startgame_rect = startgame.get_rect().center

# pause_txt = font_small.render("PAUSED", True, (0, 150, 255))
# pause_txt_rect = pause_txt.get_rect().center

# save_txt = font_smaller.render("Press CTRL + S to save", True, (0, 150, 255))
# save_txt_rect = save_txt.get_rect().center

# FOODROT = pygame.USEREVENT + 1

# enter = False
# paused = False

# level = 1  # > Set initial level
# fruits_eaten = 0  # > Initialize fruits eaten count

# # Main game loop
# index = 0  # Initial level
# prev_snake_position = [90, 30]  # Initial snake positionrunning = True
# running = True
# while running:
#     wall = Wall(index)  # > Create wall object
#     last_snake_position = snake_position.copy()  # > Store the last snake position

#     # Spawn new food if probability condition is met
#     if random.random() < 0.8:
#         foods.append(spawn_food())

#     for food in foods[:]:
#         pygame.draw.rect(game_window, food["color"], pygame.Rect(food["position"][0], food["position"][1], size, size))
#         food["timer"] -= 1
#         if food["timer"] <= 0:
#             foods.remove(food)
    

#     # Event handling loop
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#             pygame.quit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 change_to = 'UP'
#             elif event.key == pygame.K_DOWN:
#                 change_to = 'DOWN'
#             elif event.key == pygame.K_LEFT:
#                 change_to = 'LEFT'
#             elif event.key == pygame.K_RIGHT:
#                 change_to = 'RIGHT'

#     # Update snake direction based on key input
#     if change_to == 'UP' and direction != 'DOWN':
#         direction = 'UP'
#     if change_to == 'DOWN' and direction != 'UP':
#         direction = 'DOWN'
#     if change_to == 'LEFT' and direction != 'RIGHT':
#         direction = 'LEFT'
#     if change_to == 'RIGHT' and direction != 'LEFT':
#         direction = 'RIGHT'

#     # Move the snake
#     if direction == 'UP':
#         snake_position[1] -= 15
#     if direction == 'DOWN':
#         snake_position[1] += 15
#     if direction == 'LEFT':
#         snake_position[0] -= 15
#     if direction == 'RIGHT':
#         snake_position[0] += 15


#     snake_body.insert(0, list(snake_position))
#     if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
#         score += 10
#         fruits_eaten += 1
#         fruit_spawn = False
#     else:
#         snake_body.pop()

    
#     # Spawn a new fruit if the previous one is eaten
#     if not fruit_spawn:
#         fruit_position = [random.randrange(1, (window_x // size)) * size,
#                           random.randrange(1, (window_y // size)) * size]
        
#     fruit_spawn = True
#     # Draw the snake on the game window
#     game_window.fill(black)

#     if fruits_eaten == 5:  # If snake has eaten 4
#         index += 1  # > Move to the next level
#         snake_speed += 2  # > Increase speed
#         prev_snake_position = snake_position[:]  # > Store previous snake position
#         snake_position = [210, 240]  # > Reset snake position
#         direction = 'RIGHT'  # > Reset direction
#         fruits_eaten = 0  # > Reset fruits eaten count
#     # Draw walls
#     wall = Wall(index)  # > Load the appropriate map for the current level
#     wall.draw()  # > Draw walls

#     for pos in snake_body:
#         pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], size, size))
#     pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], size, size))

#        # Game Over conditions
#     if snake_position[0] < 0 or snake_position[0] > window_x - 15:
#         game_over()
#     if snake_position[1] < 0 or snake_position[1] > window_y - 15:
#         game_over()
#     for block in snake_body[1:]:
#         if snake_position[0] == block[0] and snake_position[1] == block[1]:
#             game_over()
#     for wall_block in wall.body:
#         if snake_position[0] == 15 * wall_block.x and snake_position[1] == size * wall_block.y:
#             game_over()

#     drawGrid()  # > Draw grid lines

#     # Display the score continuously
#     show_score(white, 'times new roman', 20)  # Display the score continuously

#     # Display the level on the top right
#     level_text = pygame.font.SysFont("Arial", 24).render("Level: " + str(index), True, white)
#     level_rect = level_text.get_rect()
#     level_rect.topright = (window_x - 10, 10)
#     game_window.blit(level_text, level_rect)
#     # Refresh the game screen
#     pygame.display.update()
#     fps.tick(snake_speed)

import pygame, random, time, psycopg2
from config import config

BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400
FPS = 5

BLOCK_SIZE = 20
MAX_LEVEL = 2
user_text = ''

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class Wall:
    def __init__(self, level):
        self.body = []
        self.list = []

        f = open("/Users/temirbekboltay/Desktop/lab-10/snake/levels/level_{}.txt".format(level), "r")
        
        for y in range(0, HEIGHT//BLOCK_SIZE + 1):
            for x in range(0, WIDTH//BLOCK_SIZE + 1):
                if f.read(1) == '#':
                    self.body.append(Point(x, y))
                    self.list.append([x, y])

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (226,135,67), rect)


class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        self.list = [[10, 11]]
        self.dx = 0
        self.dy = 0
        self.level = 0
        self.last_x = 10
        self.last_y = 11

    def move(self):
        self.last_x = self.body[-1].x
        self.last_y = self.body[-1].y
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
            self.list[i][0] = self.list[i-1][0]
            self.list[i][1] = self.list[i-1][1]

        self.body[0].x += self.dx 
        self.body[0].y += self.dy
        self.list[0][0] += self.dx 
        self.list[0][1] += self.dy

    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255, 0, 0), rect)


        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)

    def check_collision(self, food):
        global wall, snake, score
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                if food.value[0] == 1:
                    score += 1
                    self.body.append(Point(snake.last_x, snake.last_y))
                    self.list.append([snake.last_x, snake.last_y])
                elif food.value[0] == 2:
                    score += 2
                    self.body.append(Point(snake.last_x, snake.last_y))
                    self.list.append([snake.last_x, snake.last_y])
                    self.body.append(Point(snake.last_x, snake.last_y))
                    self.list.append([snake.last_x, snake.last_y])
                food.relocate(wall, self)

# snake = Snake()
# wall = Wall(snake.level)

def check_per():
    global wall, snake
    f = True
    while f:
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        if [x, y] not in wall.list and [x, y] not in snake.list:
            return Point(x, y)
class Food:
    def __init__(self):
        self.location = check_per()
        self.value = random.choices([1, 2], weights=[80, 20], k = 1)
        if self.value[0] == 1:
            self.R = 0
            self.G = 255
            self.B = 0
        elif self.value[0] == 2:
            self.R = 255
            self.G = 215
            self.B = 0

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        if self.value[0] == 1:
            pygame.draw.rect(SCREEN, (self.R, self.G, self.B), rect)
        else:
            pygame.draw.rect(SCREEN, (self.R, self.G, self.B), rect)
    def update_color(self):
        if self.R > 0:
            self.R -= 3
            if self.R < 0:
                self.R = 0
        if self.G > 0:
            self.G -= 3
            if self.G < 0:
                self.G = 0
        if self.B > 0:
            self.B -= 3
            if self.B < 0:
                self.B = 0

    def relocate(self, wall, snake):
        f = True
        while f:
            x = random.randint(0, 19)
            y = random.randint(0, 19)
            if [x, y] not in wall.list and [x, y] not in snake.list:
                self.location = Point(x, y)
                f = False
                self.value = random.choices([1, 2], weights=[80, 20], k = 1)
                if self.value[0] == 1:
                    self.R = 0
                    self.G = 255
                    self.B = 0
                elif self.value[0] == 2:
                    self.R = 255
                    self.G = 215
                    self.B = 0


def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)

#Quit game if snake hits wall or borders or itself
def game_over(wall, snake):
    for i in range(len(wall.body)):
        if snake.body[0].x == wall.body[i].x and snake.body[0].y == wall.body[i].y:
            return False
    if snake.body[0].x < 0 or snake.body[0].x > 19 or snake.body[0].y < 0 or snake.body[0].y > 19:
        return False
    for i in range(1, len(snake.body)):
        if snake.body[0].x == snake.body[i].x and snake.body[0].y == snake.body[i].y:
            return False
    return True

def save(username, score):
    """Save or update the user's score in the database."""
    sql = "SELECT user_score FROM snake_scores WHERE user=%s"
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (username,))
        result = cur.fetchone()
        if result:
            # Update score if the new score is higher than the existing one
            if score > result[0]:
                update_sql = """UPDATE snake_scores SET user_score=%s WHERE user=%s;"""
                cur.execute(update_sql, (score, username,))
        else:
            # Insert new user and score
            insert_sql = """INSERT INTO snake_scores(user, user_score) VALUES(%s, %s);"""
            cur.execute(insert_sql, (username, score,))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()

def read(username):
    """Read the user's score from the database and calculate level from score."""
    sql = """SELECT user_score FROM snake_scores WHERE user=%s;"""
    conn = None
    score = 0  # Default score if no records found
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (username,))
        result = cur.fetchone()
        if result:
            score = result[0]
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()
    
    # Example logic to derive level from score, this will need to be adjusted based on your game's rules
    level = score // 100  # Assuming each 100 points increases the level by 1
    return score, level

    

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
SCREEN.fill(BLACK)

# food = Food()

level = 1
score = 0
font = pygame.font.SysFont("Verdana", 200)
font_small = pygame.font.SysFont("Verdana", 60)
font_smaller = pygame.font.SysFont("Verdana", 30)
font_smallest = pygame.font.SysFont("Verdana", 20)

gameover = font_small.render("Game over!", True, "Black")
gameover_rect = gameover.get_rect().center

startgame = font_smallest.render("Press ENTER to play", True, "White")
startgame_rect = startgame.get_rect().center

pause_txt = font_small.render("PAUSED", True, (0, 150, 255))
pause_txt_rect = pause_txt.get_rect().center

save_txt = font_smaller.render("Press CTRL + S to save", True, (0, 150, 255))
save_txt_rect = save_txt.get_rect().center

FOODROT = pygame.USEREVENT + 1

enter = False
paused = False

running = True
while running:
    pressed = pygame.key.get_pressed()
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not enter:
                enter = True
                score, level = read(user_text)
                snake = Snake()
                score = (level - 1) * 7
                wall = Wall(snake.level)
                food = Food()
                snake.level = level % MAX_LEVEL
                FPS += level
                pygame.time.set_timer(FOODROT, 100)
            if enter:
                if event.key == pygame.K_SPACE:
                    if paused == True:
                        paused = False
                    else:
                        paused = True
                if paused == True:
                    if event.key == pygame.K_s and ctrl_held:
                        save(user_text, score, level)
                if event.key == pygame.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1
            else:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        if event.type == FOODROT and not paused:
            food.update_color()
            pygame.display.update()
            if food.R == 0 and food.G == 0 and food.B == 0:
                food.relocate(wall, snake)
    if not enter:
        username = font_smallest.render(f"Enter your nickname: {user_text}", True, "White")
        username_rect = username.get_rect().center
        SCREEN.fill(BLACK)
        SCREEN.blit(username, (200-username_rect[0], 200-username_rect[1]))
        SCREEN.blit(startgame, (200-startgame_rect[0], 220-startgame_rect[1]))
        pygame.display.update()
    if enter:
        if not paused:
            snake.move()

        #If game ends
        if not game_over(wall, snake):
            SCREEN.fill((0, 150, 255))
            SCREEN.blit(gameover, (200-gameover_rect[0], 180-gameover_rect[1]))
            scr = font_smaller.render(f"Your score is {score}", True, "Black")
            scr_rect = scr.get_rect().center
            SCREEN.blit(scr, (200-scr_rect[0], 220-scr_rect[1]))
            pygame.display.update()
            time.sleep(2)
            running = False
            pygame.quit()

        #Grow snake when it collects food
        snake.check_collision(food)

        #Level progression
        if len(snake.body) > 6:
            newLevel = (snake.level + 1) % MAX_LEVEL
            snake = Snake()
            snake.level = newLevel
            wall = Wall(snake.level)
            food.location = Point(3, 10)
            level += 1
            FPS += 1   
        #Show current level
        SCREEN.fill(BLACK)
        level_txt = font.render(f"{level}", True, (255, 255, 255))
        level_rect = level_txt.get_rect().center
        SCREEN.blit(level_txt, (200-level_rect[0], 200-level_rect[1]))
        snake.draw()
        food.draw()
        wall.draw()
        drawGrid()
        if paused:
            SCREEN.blit(pause_txt, (200-pause_txt_rect[0], 200-pause_txt_rect[1]))
            SCREEN.blit(save_txt, (200-save_txt_rect[0], 250-save_txt_rect[1]))
        pygame.display.update()
        CLOCK.tick(FPS)

pygame.quit()
quit()