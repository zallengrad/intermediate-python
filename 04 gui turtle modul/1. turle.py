from turtle import Turtle

def kanan():
    tim.right(90)
    tim.forward(100)
def kiri():
    tim.left(90)
    tim.forward(100)

tim = Turtle()
tim.shape("triangle")

for i in range(4):
    tim.forward(100)
    tim.right(90)



# timmy_the_turtle.forward(100)
# kanan()
# kanan()
# kanan()
















screen = Screen()
screen.exitonclick()