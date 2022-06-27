from tkinter import *
from pop_up_window import PopUP


class TryWindow(PopUP):
    def __init__(self, parent, directory):
        super().__init__(parent, directory)
        self.bind('<Down>', self.on_close)

    def on_close(self, event):
        self.destroy()
