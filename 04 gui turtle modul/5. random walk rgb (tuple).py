import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb = (r, g, b)
    return rgb

########### Challenge 5 - Random Walk Tuple RGB ########
directions = [0, 90,180, 270]

# def random_step(n_steps):
for i in range(50):
        tim.speed(3)
        tim.pensize(10)
        tim.color(random_color())
        tim.forward(50)
        tim.setheading(random.choice(directions))

# for langkah in range(3, 20):
#     random_step(langkah)


