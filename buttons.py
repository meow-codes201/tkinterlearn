from tkinter import *
count = 0
def click():
    global count
    count +=1
    print("Button clicked",count,"times")
window = Tk()
window.geometry("600x600")
photo = PhotoImage(file='D:/libraryManager/Facebook_like_thumb.png')
photo = photo.subsample(5, 5) 
button = Button(window,
                text='click',
                command=click,
                font=("Comic Sans",30),
                fg="#FFFFFF",
                bg='black',
                activeforeground="#FFFFFF",
                activebackground="#000000",
                state=ACTIVE,
                image=photo,
                compound='bottom')

button.pack()

window.mainloop()