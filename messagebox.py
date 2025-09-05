from tkinter import *
from tkinter import messagebox
def click():
    # messagebox.showinfo(title='info message',message='You are a human')
    # messagebox.showwarning(title='warning!',message='You have a VIRUS!!!!')
    # messagebox.showerror(title='error',message='something went wrong')
    
    # if (messagebox.askokcancel(title='ask ok cancel',message='do you want to continue?')):
    #     print("you want to continue")
    # else:
    #     print("you want to stop")
    # if (messagebox.askyesno(title='ask yes or no',message='do you like cake?')):
    #     print("i you like cake too")
    # else:
        # print("why do you not like cake?")
    # answer = messagebox.askquestion(title='ask question',message='Do you code?')
    # if answer== 'yes':
    #     print("you are a programmer")
    # else:
    #     print("you are not a programmer")
    ans = messagebox.askyesnocancel(title='ask yes no cancel',
                                    message='do you like icecream?',
                                    icon='info'
                                    )
    if ans == True:
        print("you like icecream")
    elif ans == False:
        print("you do not like icecream")
    else:
        print("you cancelled")

window = Tk()

window.geometry("200x200")

button = Button(window,
                text ="click me",
                command=click
                
)
button.pack()


window.mainloop()