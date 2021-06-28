from tkinter import *

root = Tk()

root.geometry("100x50")


f1 = Label(text="hello_world" , relief=SUNKEN,bg="red",fg="white",font="comicsensms 10 bold", borderwidth=3)
f1.pack(side=LEFT,fill="y")

root.mainloop()