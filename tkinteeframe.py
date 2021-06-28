from tkinter import *

root = Tk()
root.geometry("350x50")

f1 = Frame(root, bg="gray",borderwidth=9,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

f2 = Frame(root, bg="gray",borderwidth=8,relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l = Label(f1, text="open frame")
l.pack(pady=142)

l2 = Label(f2,text="top frame",font="helvetica 9 bold",fg="red",pady=20)
l2.pack()


root.mainloop()