from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=270)
        self.level = 1
        self.score()

    def score(self):
        self.write(f"Level: {self.level}", font=("Arial", 15, "bold"), align="left")

    def update_score(self):
        self.level += 1
        self.clear()
        self.score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over", font=("Arial", 15, "bold"), align="center")
