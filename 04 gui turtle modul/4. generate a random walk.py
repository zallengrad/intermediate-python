import turtle as t
import random

tim = t.Turtle()


########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90,180,270]
n_step = 10
# def random_step(n_steps):
for i in range(20):
        tim.speed(3)
        tim.pensize(10)
        tim.color(random.choice(colours))
        tim.forward(50)
        tim.setheading(random.choice(directions))

# for langkah in range(3, 20):
#     random_step(langkah)


