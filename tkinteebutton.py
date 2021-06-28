from tkinter import *

root = Tk()
root.geometry("350x50")

f1 = Frame(root, bg="gray",borderwidth=9,relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")

f2 = Button(f1, bg="red",text="click")
f2.pack()

f3 = Button(f1, bg="red",text="click")
f3.pack()

f4 = Button(f1, bg="red",text="click")
f4.pack()


root.mainloop()