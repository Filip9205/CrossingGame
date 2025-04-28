from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars
import time

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=600)
screen.title("Crossing Game")

player = Player()
scoreboard = Scoreboard()

cars = Cars()

screen.listen()
screen.onkey(key="Up", fun=player.move)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    if player.ycor() > 290:
        player.goto(x=0, y=-280)
        scoreboard.update_score()
        cars.increase_car_speed()
    # Collision with car
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
