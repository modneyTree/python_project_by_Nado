import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=4, values=values)
combobox.pack()
combobox.set("카드 결제일")
def btncmd():
    pass

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()