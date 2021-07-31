from tkinter import *

root = Tk()

root.title("grid layout")

Python = Button(root , text="Python" , width=15)
Javascrip = Button(root , text="Javascrip" , width=15)
C = Button(root , text="C" , width=15)
PHP = Button(root , text="PHP" , width=15)

Python.grid(row=0, column=0)
Javascrip.grid(row=0, column=1)
C.grid(row=1, column=0)
PHP.grid(row=1, column=1)



root.mainloop()