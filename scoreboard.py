from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.lives = 3
        self.color("white")
        self.penup()
        self.hideturtle()

        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Lives:{self.lives}", align="center", font=("Courier", 18, "normal"))

    def update(self):
        self.lives -= 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "normal"))

    def winner(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"YOU WIN!", align="center", font=("Courier", 24, "normal"))
