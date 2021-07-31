# to show image a third party module called "Pillow" will do everything for us. we need to install it first by "pip install Pillow"
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Shown")
lbl = Label(root , text="ImgHere")

img = Image.open("testshot.png")
picture = ImageTk.PhotoImage(img)

python = Label(root , image=picture)

lbl.pack()
python.pack( )

img.show()

root.mainloop()