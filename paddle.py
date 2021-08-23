from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(0)
        self.shapesize(1, 6)
        self.goto(0, -250)

    def move_left(self):
        self.backward(25)

    def move_right(self):
        self.forward(25)

    def restart_paddle(self):
        self.goto(0, -250)
