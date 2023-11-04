import turtle
from turtle import Turtle, Screen
import  pandas as pd

tl = Turtle()
screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tl.shape(image)

answer_state = screen.textinput(title="Guess The State", prompt="What's another state name?")
answer_state.lower()

data = pd.read_csv("50_states.csv")
state = data.state.to_list()

# series = data.x.to_list()

choose = data[data.state == answer_state]
x      = choose.x.to_list()
y      = choose.y.to_list()

print(int(x))

data_series_int = x.astype(int)

# print(y)
# print(series)

# for i in state :
#     if answer_state == i.lower() :
#         text = Turtle()
#         print(answer_state)
#         text.penup()
#         text.goto(x[0], y[0])
#         text.write(arg=answer_state)
#
#     else:
#         pass

# if answer_state in state:
#     text = Turtle()
#     print(answer_state)
#     text.hideturtle()
#     text.penup()
#     choose = data[data.state == answer_state]
#     text.goto(int(choose.x, choose.y))
#     text.write(arg=answer_state)


# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# tl.onscreenclick(get_mouse_click_coor)
# tl.mainloop()


screen.exitonclick()
