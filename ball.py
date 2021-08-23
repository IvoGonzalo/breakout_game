from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, -225)
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collision_y(self):
        self.y_move *= -1

    def collision_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, -225)
        self.x_move = 10
        self.x_move *= -1
        self.y_move *= -1

    def increase_speed(self):
        self.y_move += 2
        print(self.y_move)
