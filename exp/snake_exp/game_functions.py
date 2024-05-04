import pygame
import random
import time
from settings import *

def should_spawn_food(last_food_spawn_time):
    current_time = time.time()
    if current_time - last_food_spawn_time >= 5:
        return True, current_time
    return False, last_food_spawn_time

def spawn_food(wall_list, WINDOW_X, SIZE):
    while True:
        food_type = random.choices(list(FOOD_PROBABILITIES.keys()), weights=FOOD_PROBABILITIES.values())[0]
        x = random.randrange(1, WINDOW_X // SIZE) * SIZE
        y = random.randrange(1, WINDOW_Y // SIZE) * SIZE
        if (x // SIZE, y // SIZE) not in wall_list:
            return {
                "type": food_type,
                "position": [x, y],
                "color": FOOD_COLORS[food_type],
                "score": FOOD_SCORES[food_type],
                "timer": FOOD_DURATION[food_type]
            }
