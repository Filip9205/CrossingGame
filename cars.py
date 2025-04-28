from turtle import Turtle
import random
import time

COLORS = ["red", "yellow", "blue", "green", "purple"]


class Cars:

    def __init__(self):
        self.all_cars = []
        self.speed = 5

    def create_car(self):
        random_chance = random.randint(1, 7)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_car_speed(self):
        self.speed += 2.5
