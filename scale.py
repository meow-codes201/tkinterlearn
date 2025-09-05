from tkinter import *
def submit():
    print("temperature is :",scale.get(),"degree celsius")
window = Tk()
f = PhotoImage(file='D:/libraryManager/flame.png')
flame = f.subsample(50,50)
flameLabel = Label(window,image=flame)
flameLabel.pack()







window.geometry("600x800")
window.title("Scale Widget")

scale = Scale(window,from_=100,to=0,
              orient=VERTICAL,
              length=400,
              font=("Consolas",20),
              tickinterval=10,
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='black'
       
              
              )
scale.set((scale['from']-scale['to'])/2 + scale['to'])
scale.pack()
c = PhotoImage(file='D:/libraryManager/ice.png')
ice = c.subsample(15,15)
iceLabel = Label(window,image=ice)
iceLabel.pack()

button = Button(window,text='submit',
                command=submit)
button.pack()





window.mainloop()
