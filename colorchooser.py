from tkinter import *
from tkinter import colorchooser

def color1():
    color = colorchooser.askcolor()
    colorhex = color[1]
    window.config(bg=colorhex)
def color():
    window.config(bg=colorchooser.askcolor()[1])
window = Tk()

window.geometry("600x800")

button = Button(window,
                text="choose color",
                command=color
)
button.pack()


















window.mainloop()