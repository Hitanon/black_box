from tkinter import *
from PIL import Image, ImageTk


class PopUP(Toplevel):
    def __init__(self, parent, directory):
        super().__init__(parent)

        self.grab_set()
        self.focus_set()

        self.resizable(0, 0)
        self.width = 600
        self.height = 400
        self.title('Чёрный ящик')
        self.overrideredirect(1)

        # self.update_idletasks()
        x = self.winfo_screenwidth() // 2 - 300
        y = self.winfo_screenheight() // 2 - 200
        self.geometry("+{}+{}".format(x, y))

        self.canvas = Canvas(self, bg='white', width=self.width, height=self.height)
        self.canvas.pack()

        pil_image = Image.open(directory)
        self.image = ImageTk.PhotoImage(pil_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.image)


