import turtle as t
import random

s = t.Screen()
tim = t.Turtle()

color = ["firebrick", "orange", "gold", "blue"]



def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.color(random.choice(color))
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range (3,11):
    draw_shape(shape_side_n)