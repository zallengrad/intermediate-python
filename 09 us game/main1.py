import turtle
from turtle import Turtle, Screen
import  pandas as pd

tl = Turtle()
screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tl.shape(image)

data = pd.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50 :
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct",
                                    prompt="What's another state name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = [ state for state in all_state if state not in guessed_states ]
        # for state in all_state:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("state to learn.csv")
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)



