from tkinter import *
from window import Window


class NormalMode(Window):
    def __init__(self, parent, directory='backgrounds/normal_mode.png'):
        super().__init__(parent, directory)
        self.entry = Entry(self, width=4, font=("Montserrat", 60, "bold",), fg="#1F0B58")
        self.entry.place(relx=0.115, rely=0.445, relwidth=0.15, relheight=0.1)
        self.label = Label(self, width=6, font=("Montserrat", 60, "bold",), fg="#9597C6", bg="white")
        self.label.place(relx=0.735, rely=0.445, relwidth=0.15, relheight=0.1)
