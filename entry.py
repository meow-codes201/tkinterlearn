from tkinter import *
def submit():
    username = entry.get()
    print("Hello",username)
    entry.config(state=DISABLED)
def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1,END)
window = Tk()
window.geometry("600x600")

entry = Entry(window,
              font=('Arial',50),
              fg='black',
              bg='violet',
              show='*'
              )
#show is usually used for password fields
entry.insert(0,'Username')
submit_button = Button(window,
                text='Submit',
                command=submit)
submit_button.pack(side=RIGHT)
entry.pack(side=LEFT) #display


delete_button = Button(window,
                text='delete',
                command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                text='backspace',
                command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()
