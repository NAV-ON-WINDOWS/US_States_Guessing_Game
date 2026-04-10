import pandas as pd
import turtle as t

screen = t.Screen()
screen.title("U.S. STATES GAME")

img = "blank_states_img.gif"
t.addshape(img)

tim = t.Turtle()
tim.shape(img)

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(
        title=f"{len(guessed_states)}/50",
        prompt="Enter the name of the state"
    ).title()

    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        break

    if answer in all_states:
        guessed_states.append(answer)
        tpen = t.Turtle()
        tpen.hideturtle()
        tpen.penup()
        state_data = data[data.state == answer]
        tpen.goto(state_data["x"].item(), state_data["y"].item())
        tpen.write(answer)