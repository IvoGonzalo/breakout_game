from turtle import Screen
from paddle import Paddle
from ball import Ball
from rectangles import Rectangles
from scoreboard import Scoreboard
import time

x = -365
y = 150
score = 0
rectangles = []
restart = True

screen = Screen()

screen.bgcolor("#1E2019")
screen.setup(width=800, height=600)
screen.title("BREAKOUT")
screen.tracer(0)

for _ in range(5):
    for _ in range(13):
        rectangle = Rectangles(x, y)
        rectangles.append(rectangle)
        x += 60
    y += 30
    x = -365

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if restart:
        ball.move_ball()

    # Detect collision with wall
    if ball.xcor() > 375 or ball.xcor() < -375:
        ball.collision_x()
    if ball.ycor() > 280:
        ball.collision_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 65 and ball.ycor() < -230:
        ball.collision_y()
        if ball.y_move == 22:
            pass
        else:
            ball.increase_speed()

    # Detect collision with rectangle
    for rectangle in rectangles:
        if not rectangle.show:
            if ball.distance(rectangle) < 40:
                rectangle.show = True
                rectangle.color("#1E2019")
                ball.collision_y()
                score += 1

    # Restart ball
    if ball.ycor() < -320:
        paddle.goto(0, -250)
        ball.reset_ball()
        scoreboard.update()

    # Finish game
    if scoreboard.lives < 0:
        scoreboard.game_over()
        paddle.restart_paddle()
        ball.reset_ball()
    if score == 65:
        scoreboard.winner()
        ball.reset_ball()
        paddle.restart_paddle()

screen.exitonclick()
