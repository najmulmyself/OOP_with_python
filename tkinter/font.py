import tkinter
import tkinter.font as font


# There are two ways we can use font Widget in tkinter | tuple and font object
from tkinter import *
# from typing import Optional
root = Tk()

# tuple method given below


# if we want to use font  we can pass a tuple and tuple can take 3 arg. (Optional) | font-family,font-size,font-style
lbl = Label(root , text="Python" , font=("Helvetica","20")) 

# if we want to use font object method we have to import tkinter.font;
font = font.Font(family="Serif" , size="18" , weight="bold")
lbl2 = Label(root , text="Javascript" , font=font) 


lbl.pack()
lbl2.pack()

root.mainloop()