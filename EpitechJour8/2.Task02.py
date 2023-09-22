from tkinter import *
from tkinter import LabelFrame, Frame
import tkinter as tk

root = tk.Tk()
root.title("Task01")
root.resizable(False,False)

bg = tk.PhotoImage(file=r"C:\Users\jason\python\EpitechJour8\Image2.gif")

canvas= Canvas(root,width=200,height=200,bg="ivory")
canvas.pack()

background_label = tk.Label(canvas, image=bg)
background_label.place(relwidth=1, relheight=1)

root.mainloop()