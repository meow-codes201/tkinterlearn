from tkinter import *

def order():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("You have ordered :")
    for item in food:
        print(item)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())
def remove():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

window.geometry("600x800")
window.title("Listbox Widget")

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Constantia',20),
                  width=12,
                  selectmode=MULTIPLE
                
                  )
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Pasta")
listbox.insert(3,"Garlic Bread")
listbox.insert(4,"Soup")
listbox.insert(5,"Salad")
listbox.insert(6,"Ice Cream")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

entry_button = Button(window,
                text="add",
                command=add)

entry_button.pack()


remove_button = Button(window,
                text="remove",
                command=remove)

remove_button.pack()


button = Button(window,
                text="Order Now",
                command=order)
button.pack()




window.mainloop()



