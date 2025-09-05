from tkinter import *
from tkinter import colorchooser

def color():
    color = colorchooser.askcolor()
    print(color)

window = Tk()

window.geometry("600x800")

button = Button(window,
                text="choose color",
                command=color
)
button.pack()


















window.mainloop()