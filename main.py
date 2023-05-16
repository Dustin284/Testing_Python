import os
from tkinter import *
from tkinter import ttk

def convert_to_pdf():
    os.system("python3 picture_to_pdf.py 1")

root = Tk()
root.title("Startseite • Multitool")
root.geometry("550x450")
Button1 = ttk.Button(root, text='Picture to PDF', width=25, command=convert_to_pdf)
Button1.pack()

root.mainloop()