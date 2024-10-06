import turtle

from tkinter import messagebox

import pandas as pd

from state_class import State_Class

sc = State_Class()
screen = turtle.Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
screen.addshape("blank_states_img.gif")
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")

answer_state = []

states_data_list = states_data.state.to_list()
while True:

    answer = screen.textinput(title=f"Guess the State {sc.state_status()}", prompt="STATE NAME:").title()

    if answer in states_data_list:
        state_answer = states_data[states_data.state == answer]
        x = int(state_answer.x.iloc[0])
        y = int(state_answer.y.iloc[0])
        state_name = str(state_answer.state.iloc[0])
        sc.coords(x, y, state_name)
        answer_state.append(state_name)

    if answer not in states_data_list and not answer == "Exit":
        messagebox.showinfo("Incorrect", "State not found (maybe wrong spelling)")

    if answer == "Exit":
        missing_state = [state for state in states_data_list if state not in answer_state]
        sc.create_csv(missing_state)
        break
