import tkinter as tk
from tkinter import *
from tkinter import LabelFrame, Frame

def print_uppercase():
    print("UPPERCASE")

root = tk.Tk()
root.title("Task01")
root.geometry("400x400")
root.resizable(False,False)

bg = tk.PhotoImage(file=r"C:\Users\jason\python\EpitechJour8\Image2.gif")

label_frame = LabelFrame(root, text='LabelFrame', width=400, height=400)
label_frame.place(relx=0.1, rely=0.1)

background_label = tk.Label(label_frame, image=bg)
background_label.place(relwidth=1, relheight=1)

inner_frame = Frame(label_frame,)
inner_frame.pack(padx=50, pady=25)

label = tk.Label(inner_frame, text='Salut')
label.pack(padx=10, pady=10)

entry = tk.Entry(inner_frame)
entry.pack()

button= tk.Button(inner_frame,text='bouton',command=print_uppercase)
button.pack()



root.mainloop()
