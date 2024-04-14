from tkinter import *
from tkinter import messagebox

window = Tk()

entry = Entry(window, width=50)
entry.pack()



def click():
    messagebox.showinfo(title="Enter symbol number", message='hehe')
    


button = Button(window, command = click, text="Ok")
button.pack()

window.mainloop()