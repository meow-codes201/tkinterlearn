from tkinter import *

food = ["Tandoori Chicken","Fried fish","Mutton biryani"]
def order():
    if(x.get() == 0):
        print("You have ordered Tandoori Chicken")
    elif(x.get() == 1):
        print("You have ordered Fried fish")
    elif(x.get() == 2):
        print("You have ordered Mutton biryani")

window =  Tk()
Tandoori = PhotoImage(file="D:/libraryManager/chicken.png")
Tandoori_Chicken = Tandoori.subsample(20,20)
Fried = PhotoImage(file="D:/libraryManager/ff.png")
Fried_fish = Fried.subsample(20,20)
Mutton = PhotoImage(file="D:/libraryManager/biryani.png")
Mutton_biryani = Mutton.subsample(2,2)

foodImages = [Tandoori_Chicken,Fried_fish,Mutton_biryani]
x = IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(window,text=food[index],variable=x,value=index,
                              padx=25,
                              pady=15,
                              font=("Impact",50),
                              image=foodImages[index],
                              compound = RIGHT,
                              indicatoron=0,
                              width=630,
                              command=order
                              )
                              
    
    radiobutton.pack(anchor='w')













window.mainloop()