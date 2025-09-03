from tkinter import *
window = Tk() 
window.geometry("520x520")
window.title("My First GUI")
libicon = PhotoImage(file='D:/libraryManager/libicon.png')
window.iconphoto(True, libicon)
# window.config(background="#9a8cdf")
photo = PhotoImage(file='D:/libraryManager/libicon.png')
label = Label(window,text="CAN YOU SHUT UP AND ,LEARN",
              font=("Times New Roman",20,'bold','underline'),
              fg="#c3002a",bg="#9a8cdf",
              padx=10,
              pady=10,
              relief=RAISED,
              borderwidth=3,
              bd=10,
              image=photo,
              compound='top')

label.pack()
window.mainloop()
