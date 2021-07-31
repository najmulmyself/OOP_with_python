from tkinter import *

root = Tk()
# changing the title 
root.title("Practicing GUI") 

# root.geometry("500 * 300") 
# not working bcz of asterics sign

labelobj = Label(root , text="Hello There! Im new in Python & learning GUI" , fg="red")

# here we created an object called labelobj and we must pass the parent window where we want to show the Label

learn = Button(root , text="Learn more" , bg="red" , fg="white" , bd=1)

# lets explore more button using grid

# Python = Button(root , text="Python" , width=5)
# Javascrip = Button(root , text="Javascrip" , width=5)
# C = Button(root , text="C" , width=5)
# PHP = Button(root , text="PHP" , width=5)

# labelobj.pack(side=RIGHT)
# There are 3 geometry manager . we can control layout through these. pack() , place () , grid()

labelobj.pack()
learn.pack()

# geometry layout wont run with pack method

# using grid
# Python.grid(row=0, column=0)
# Javascrip.grid(row=0, column=1)
# C.grid(row=1, column=0)
# PHP.grid(row=1, column=1)

root.mainloop()
# mainloop method simply render the gui