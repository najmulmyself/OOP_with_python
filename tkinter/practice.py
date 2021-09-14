from tkinter import *

def miles_to_kilo():
    entry_value = entry.get()
    newvalue = int(entry_value) * 1.60934
    how_many.config(text=newvalue)
    text = " "
    entry.config(text=text)

window = Tk()
window.config(padx=20, pady=20)

entry = Entry(width=20)
entry.grid(column=1 , row=0)

label_mile = Label(text="Miles")
label_mile.grid(column=2 , row=0)
label_equal = Label(text="is Equal to")
label_equal.grid(column=0 , row=1)

how_many = Label(text="0")
how_many.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

btn = Button(text="Calculate" ,  command=miles_to_kilo )
btn.grid(column=1, row=2)

window.mainloop()
