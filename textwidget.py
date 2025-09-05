from tkinter import *
def submit():
    input = text.get("1.0",END)
    print(input)
window = Tk()
window.geometry("600x800")

text = Text(window,
            bg="light yellow",
            fg="red",
            font=("Ink Free",30),
            height=10,
            width=40
            )

text.pack()

button = Button(window,
                text="get",
                command=submit)
button.pack()







window.mainloop()