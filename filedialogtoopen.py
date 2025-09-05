from tkinter import *
from tkinter import filedialog
def openFile():
    filepath = filedialog.askopenfilename(initialdir="D:\\libraryManager\\",
                                          title="open file,okay?",
                                          filetypes=(("text files","*.txt"),
                                                     ("all files","*.*"))
                                          )
    file = open(filepath,'r')
    print(file.read())
    file.close()
window = Tk()
window.geometry("600x800")
window.title("File Dialog to Open File")

button = Button(window,
                text="Open File",
                command=openFile)

button.pack()












window.mainloop()