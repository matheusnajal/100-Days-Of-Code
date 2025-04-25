from turtle import Turtle
import random

COLORS = ["blue", "green", "yellow", "pink", "purple", "red", "orange"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Block:
    def __init__(self):
        self.all_block = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_block(self):
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            new_block = Turtle("square")
            new_block.shapesize(stretch_wid=1, stretch_len=2)
            new_block.penup()
            new_block.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_block.goto(300, random_y)
            self.all_block.append(new_block)

    def move_block(self):
        for block in self.all_block:
            block.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT