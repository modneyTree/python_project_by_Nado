from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

def btncmd():
    pass

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()