from tkinter import *

root = Tk()
# changing the title 
root.title("Practicing GUI") 

# root.geometry("500 * 300") 
# not working bcz of asterics sign

labelobj = Label(root , text="Hello There! Im new in Python & learning GUI" , fg="red")

# here we created an object called labelobj and we must pass the parent window where we want to show the Label

labelobj.pack()
root.mainloop()
# mainloop method simply render the gui