from turtle import Turtle
import random

COLORS = ["#393E41", "#D3D0CB", "#E2C044", "#587B7F", "#E84855", "#B56B45"]


class Rectangles(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.show = False
        self.shape("square")
        self.shapesize(1, 2.5)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(x, y)
