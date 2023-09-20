from turtle import Turtle, Screen

tim = Turtle()
tim.shape("triangle")


for i in range(10) :
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.forward(10)

