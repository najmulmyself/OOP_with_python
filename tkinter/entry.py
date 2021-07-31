from tkinter import *

root = Tk()
root.title("Entry - Text Field")

label = Label(root , text="Name")
textfield = Entry(root)
# entry field only allow single line text
# there are few method with entry Widget | get() | insert(index , text) | delete(first, last)

label.grid(row=0 , column=0)
textfield.grid(row=0 , column=1)

root.mainloop()