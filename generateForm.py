from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Welcome to FileMaker")
window.geometry('525x450')
window.configure(background = "gray")
LabelAppType = Label(window, width=40, text="Type of Application").grid(row=0, column=0)
inputAppType = Entry(window).grid(row=0, column=2)
LabelAppType = Label(window, width=40, text="Specify the port").grid(row=1, column=0)
inputAppType = Entry(window).grid(row=1, column=2)
LabelAppType = Label(window, width=40, text="Command To start the Server").grid(row=2, column=0)
inputAppType = Entry(window).grid(row=2, column=2)

ttk.Button(window, text="Submit").grid(row=3, column=0)
window.mainloop()