from tkinter import *
from window import Window


class ExamMode(Window):
    def __init__(self, parent, directory):
        super().__init__(parent, directory)
        self.entry = Entry(self, width=5, font=("Montserrat", 60, "bold",), fg="#1F0B58")
        self.entry.place(relx=0.735, rely=0.445, relwidth=0.15, relheight=0.1)
        self.label = Label(self, width=6, font=("Montserrat", 60, "bold",), fg="#9597C6", bg="white", text="123456")
        self.label.place(relx=0.115, rely=0.445, relwidth=0.15, relheight=0.1)
        self.bind('<Escape>', self.on_close)

    def on_close(self, event):
        self.destroy()

