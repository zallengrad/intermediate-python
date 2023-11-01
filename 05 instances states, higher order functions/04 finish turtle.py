from turtle import Turtle, Screen
import random

race = False
tim = Turtle()
screen = Screen()
screen.setup(600,600)
pop_up = screen.textinput("GAME TEBAK TEBAKAN", "pilih tebak warna yang menang : red, green, yellow, blue, purple")

tim.penup()
tim.goto(-200,200)
tim.pendown()
tim.forward(400)
tim.penup()


# tim.goto(-150,-250)
tim.setheading(90)

position = [-100, -50, 0, 50, 100]
color =  ["red", "green", "yellow", "blue", "purple"]
all_turtle = []

for i in range(0,5):
    tom = Turtle(shape="turtle")
    tom.color(color[i])
    tom.penup()
    tom.setheading(90)
    tom.goto(position[i],-250)
    all_turtle.append(tom)

if pop_up:
    race = True

while race :
    for jalan in all_turtle:
        if jalan.ycor() > 180 :
            race = False
            winning_color = jalan.pencolor()
            if winning_color == pop_up:
                # screen.textinput("YAYYYY KAMU MENANG DALAM TEBAKAN INI")
                print("YAYYYY KAMU MENANG DALAM TEBAKAN INI")
            else :
                # screen.textinput("TETOOOTTT KALAAHHH HEHE :V")
                print("TETOOOTTT KALAAHHH HEHE :V")
        balapan = random.randint(0,10)
        jalan.forward(balapan)




screen.exitonclick()