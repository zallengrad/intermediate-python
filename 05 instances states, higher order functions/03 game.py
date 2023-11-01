from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Pilih Taruhanmu", prompt="Kura-Kura mana yang akan menang, pilih warna nya? : ")
color = ["red", "orange", "green", "yellow", "blue", "purple"]
position = [ -70, -40, -10, 20, 50, 80]
all_turtle = []

for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(-230, position[i])
    new_turtle.color(color[i])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 250 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"SELAMT Kamu menanggg,,, {winning_color} memenangkan permainan")
            else:
                print(f"KALAAAHHH!! {winning_color} memenangkan permainan")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()