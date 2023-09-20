import turtle as t
from turtle import Screen
import random

t.colormode(255)
tim = t.Turtle()
color_list = [ (202, 166, 109), (240, 246, 241), (152, 73, 47), (236, 238, 244), (170, 153, 41),
 (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75),
 (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31),
 (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182),
 (19, 71, 63), (175, 192, 212)]


def posisi():
    tim.penup()
    tim.setheading(225)
    tim.fd(300)
    tim.setheading(0)
    tim.pendown()
def maju():
    for i in range(10):
        random_color = random.choice(color_list)
        tim.dot(20, random_color)
        tim.penup()
        tim.fd(50)
        tim.pendown()
        # tim.dot(20, random_color)
def halauan_kanan():
    tim.penup()
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(180)
    tim.fd(50)
    tim.pendown()
def halauan_kiri():
    tim.penup()
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(0)
    tim.fd(50)
    tim.pendown()

posisi()

for i in range(5):
    maju()
    halauan_kanan()
    maju()
    halauan_kiri()

screen = t.Screen()
screen.exitonclick()


