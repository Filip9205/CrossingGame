from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.goto(x=0, y=-280)
        self.left(90)

    def move(self):
        self.forward(20)
