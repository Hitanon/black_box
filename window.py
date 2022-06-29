from tkinter import *
from PIL import Image, ImageTk
from PIL.Image import Resampling


class Window(Toplevel):
    def __init__(self, parent, directory):
        super().__init__(parent)

        self.grab_set()
        self.focus_set()

        self.wm_attributes('-fullscreen', True)
        self.state('zoomed')
        self.resizable(0, 0)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenwidth() * 9 // 16

        self.canvas = Canvas(self, bg='white', width=self.width, height=self.height)
        self.canvas.pack()

        pil_image = Image.open(directory)
        pil_image = pil_image.resize((self.width, self.height), Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(pil_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image)



