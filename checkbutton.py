from tkinter import *
window = Tk()

window.geometry("600x600")

def display():
    if(x.get()=="yes"):
        print("You agree")
    else:
        print("you dont agree")

x= StringVar()
photo = PhotoImage(file='D:\libraryManager\images.png')
check_button = Checkbutton(window,
                           text="I agree to the terms and conditions",
                           font=("Arial",20),
                           variable = x,
                           onvalue="yes",
                           offvalue="no",
                           command=display,
                           fg='#00FF00',
                           bg='#000000',
                           activebackground='#000000',
                           activeforeground='#00FF00',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound=LEFT
                        
                           )



check_button.pack()








window.mainloop()