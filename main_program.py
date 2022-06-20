from tkinter import *
from PIL import ImageTk, Image
from PIL.Image import Resampling

root = Tk()
root.title('Чёрынй ящик')
menu = Menu(root, bg="#505050")

width = root.winfo_screenwidth()
height = root.winfo_screenwidth() * 9 // 16
# root.geometry('{}x{}+0+0'.format(width, height))
root.state('zoomed')
root.resizable(0, 0)
image = Image.open('backgrounds/normal_mode.png')
image = image.resize((width, height), Resampling.LANCZOS)
image = ImageTk.PhotoImage(image)

canvas = Canvas(root, width=width, height=height)
canvas.create_image(0, 0, anchor="nw", image=image)
canvas.pack()

root.mainloop()
