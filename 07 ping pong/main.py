from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # dettect the collison with the wall
    if ball.ycor() == 290 or ball.ycor() == -290 :
        ball.bounce_y()
    # detec the collison with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() == 340:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() == -340:
            ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.r_point()

    if ball.xcor() < -350:
        ball.reset_position()
        score.l_point()

screen.exitonclick()