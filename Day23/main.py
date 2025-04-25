import time
from turtle import Screen
from player import Player
from blocks import Block
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
block = Block()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    block.create_block()
    block.move_block()

    for blocks in block.all_block:
        if blocks.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()
    
    if player.is_at_finish_line():
        player.go_to_start()
        block.level_up()
        scoreboard.increase_level()

screen.exitonclick()