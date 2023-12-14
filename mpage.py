import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ast

# Создание основного окна

def on_escape(event):
    window.destroy()

def new_win():
    window.destroy()
    import sign

window = tk.Tk()
window.title('Hello Movies')

window.state('zoomed')
window.config(bg='#070B15')
window.bind("<Escape>", on_escape)

find=PhotoImage(file='Group 10.png')
img_label = Label(image=find)

button=Button(window,image=find,command=new_win,border=0,bg='#070B15',borderwidth=0,activebackground="#070B15").place(anchor='center', relx=0.5, rely=0.66)



img=PhotoImage(file='header logo.png')
Label(window,image=img,border=0,bg='#070B15').place(anchor='center', relx=0.51, rely=0.4)

img2=PhotoImage(file='Group 5.png')
Label(window,image=img2,border=0,bg='#070B15').place(anchor='center', relx=0.51, rely=0.51)

img3=PhotoImage(file='123.png')
Label(window,image=img3,border=0,bg='#070B15').place(anchor='center', relx=0.51, rely=0.6)

img4=PhotoImage(file='Fill 2.png')
Label(window,image=img4,border=0,bg='#070B15').place(anchor='center', relx=0.2, rely=0.7)

img5=PhotoImage(file='Group 2.png')
Label(window,image=img5,border=0,bg='#070B15').place(anchor='center', relx=0.88, rely=0.8)


window.mainloop()
