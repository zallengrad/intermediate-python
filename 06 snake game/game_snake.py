from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboarrd import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.bgcolor('red')
screen.title("ULO ULONAN")
screen.tracer(0)

snake = Snake()
food = Food()
score =ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

#     deteksi tabrakan makanan dan ular

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        print("nyam nyam")

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.GameOver()
    # mati menyentuh ekor
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            game_is_on = False
            score.GameOver()

screen.exitonclick()