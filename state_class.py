from tkinter import messagebox
from turtle import Turtle
import pandas as pd


class State_Class(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.correct = 0
        self.states = 50
        self.checker_x = []

    def coords(self, x, y, name):
        if x in self.checker_x:
            messagebox.showinfo("HEHE", "already guessed that state")
        else:
            self.checker_x.append(x)
            self.goto(x, y)
            self.write(arg=name, move=False, align="center", font=("Courier", 10, "bold"))
            self.correct += 1

    def state_status(self):
        return f"{self.correct}/{self.states}"

    @staticmethod
    def create_csv(list_of_answered_state):
        d = {'missed states': list_of_answered_state}
        data_frame = pd.DataFrame(d)
        data_frame.to_csv('states_to_learn.csv', mode='w')
        pass
