import tkinter as tk
import string
import requests
import psycopg2 as pg
from tkinter import ttk
from tkinter import Scrollbar
import time
from tkinter import font
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import linear_kernel
import difflib
import tkinter.ttk as ttk
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


global search_bar, frame, Rentry

conn = pg.connect(
     host='localhost',
     database='postgres',
     port=5432,
     user='postgres',
     password='12345'
    )
cur = conn.cursor()

frame = None
tv = None
def search_records():
    global frame, tv

    if frame is None:
   
     frame = tk.Frame(window,width=600, height=240, bg='#0B0F1F')
     frame.pack(side="bottom")
     label1 = tk.Label(frame, text="Movies",fg="white",bg='#0B0F1F', font=('Microsoft Yahei UI Light', 10, 'bold'))
     label1.place(x=2,y=1)
    
 
    if tv is None:
     tv = ttk.Treeview(frame, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings", height="10")
     tv.place(relheight=1, relwidth=1)
     scrollbar = ttk.Scrollbar(tv,orient="horizontal", command=tv.xview)
     scrollbar.pack(side='bottom', fill='x')
     tv.configure(xscrollcommand=scrollbar.set)
    
     
    else:
     tv.delete(*tv.get_children())
    column_headings = ["Id", "Title", "Genre", "Language", "Overview", "Popularity", "Release data", "Vote average", "Vote count"]
    for i, heading in enumerate(column_headings, start=1):
      tv.heading(i, text=heading)
    
    tv.column(1, width=60)  
    tv.column(2, width= 100)
    tv.column(3, width=150) 
    tv.column(4, width=60)
    tv.column(6, width=65)
    tv.column(7, width=65)
    tv.column(8, width=67)
    tv.column(9, width=65)

    tv.heading(1, text="Id")
    tv.heading(2, text="Title")
    tv.heading(3, text="Genre")
    tv.heading(4, text="Language")
    tv.heading(5, text="Overview")
    tv.heading(6, text="Popularity")
    tv.heading(7, text="Release data")
    tv.heading(8, text="Vote average")
    tv.heading(9, text="Vote count")
   
    records = search_bar.get()
    sql = ("SELECT * FROM movies WHERE Title LIKE %s " ,("%" + records + "%",))
    cur.execute(*sql)
    users = cur.fetchall()
    total=cur.rowcount
    print("Total Data entries" + str(total))
   
    for row in users:
        tv.insert('','end', values=row)
    
def seeall():
    
    new_window = tk.Toplevel(window)
    new_window.title('Movies')
    new_window.geometry("1050x700+260+90")
    new_window.config(bg='#070B15')

    

    cur = conn.cursor()

    query = "SELECT * FROM movies"
    cur.execute(query)
    data = cur.fetchall()
    total=cur.rowcount
    print("Total Data entries" + str(total))


    frm = tk.Frame(new_window)
    frm.place(x = 20, y = 20, width = 1020)

    

    tv = ttk.Treeview(frm, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings", height="32")
    tv.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    tv.pack()

    column_headings = ["Id", "Title", "Genre", "Language", "Overview", "Popularity", "Release data", "Vote average", "Vote count"]
    for i, heading in enumerate(column_headings, start=1):
     tv.heading(i, text=heading)

    tv.column(1, width=30)  
    tv.column(2, width=120) 
    tv.column(3, width=150) 
    tv.column(4, width=40)
    tv.column(5, width=60) 
    tv.column(6, width=65)
    tv.column(7, width=65)
    tv.column(8, width=55)
    tv.column(9, width=50)

    vsb = Scrollbar(frm, orient="vertical", command=tv.yview)
    vsb.pack(side='right',fill="y")

    tv.configure(yscrollcommand=vsb.set)

    tv.heading(1, text="Id")
    tv.heading(2, text="Title")
    tv.heading(3, text="Genre")
    tv.heading(4, text="Language")
    tv.heading(5, text="Overview")
    tv.heading(6, text="Popularity")
    tv.heading(7, text="Release data")
    tv.heading(8, text="Vote average")
    tv.heading(9, text="Vote count")


    for i in data:
        tv.insert('', 'end', values=i)
    
    
    new_window.resizable(False,False)
    new_window.mainloop()

    
def shows():
    new_w = tk.Toplevel(window)
    new_w.title('TV_Shows')
    new_w.geometry("1050x700+260+90")
    new_w.config(bg='#070B15')

    

    cur = conn.cursor()

    query = "SELECT * FROM tv_shows"
    cur.execute(query)
    data = cur.fetchall()
    total=cur.rowcount
    print("Total Data entries" + str(total))


    frm = tk.Frame(new_w)
    frm.place(x = 20, y = 20, width = 1020)

    

    tv = ttk.Treeview(frm, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12), show="headings", height="32")
    tv.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    tv.pack()

    column_headings = ["No","Id", "Title", "Year", "Age", "IMDB", "Rotten Tomatoes", "Netflix", "Hulu", "Prime Video","Disney","Type"]
    for i, heading in enumerate(column_headings, start=1):
     tv.heading(i, text=heading)

    tv.column(1, width=30)  
    tv.column(2, width=30)  
    tv.column(3, width=100) 
    tv.column(4, width=60)
    tv.column(5, width=30)  
    tv.column(6, width=65)
    tv.column(7, width=65)
    tv.column(8, width=67)
    tv.column(9, width=65)
    tv.column(10, width=65)
    tv.column(11, width=65)
    tv.column(12, width=65)

    vsb = Scrollbar(frm, orient="vertical", command=tv.yview)
    vsb.pack(side='right',fill="y")

    tv.configure(yscrollcommand=vsb.set)

    tv.heading(1, text="No")
    tv.heading(2, text="Id")
    tv.heading(3, text="Title")
    tv.heading(4, text="Year")
    tv.heading(5, text="Age")
    tv.heading(6, text="IMDB")
    tv.heading(7, text="Rotten Tomatoes")
    tv.heading(8, text="Netflix")
    tv.heading(9, text="Hulu")
    tv.heading(10, text="Prime Video")
    tv.heading(11, text="Disney")
    tv.heading(12, text="Type")


    for i in data:
        tv.insert('', 'end', values=i)
    
    
    new_w.resizable(False,False)
    new_w.mainloop()
#############################3
direc = None

def dir():
   global direc
   new_d = tk.Toplevel(window)
   new_d.title('Director')
   new_d.state('zoomed')
   new_d.config(bg='#070B15')
   label1 = tk.Label(new_d, width =50, text='Ranking the directors movies', font=('Garamond', 50))
   label1.config(fg='#F1F5F9')
   label1.config(bg='#070B15')
   label1.place(anchor='center', relx=0.5, y=150)

   direc=tk.PhotoImage(file='Wes Anderson.png')
   dibtn = tk.Button(new_d, image=direc, border=0, cursor='hand2', activebackground="#070B15",command = Wes)
   dibtn.place(anchor='center', x=230, y=420, width=280, height=270)

   direct=tk.PhotoImage(file='david.png')
   dibt = tk.Button(new_d, image=direct, border=0, cursor='hand2', activebackground="#070B15",command = Dav)
   dibt.place(anchor='center', x=590, y=420, width=280, height=270)

   direcn=tk.PhotoImage(file='nolan.png')
   dibtk = tk.Button(new_d, image=direcn, border=0, cursor='hand2', activebackground="#070B15",command=Nolan)
   dibtk.place(anchor='center', x=950, y=420, width=280, height=270)

   directt=tk.PhotoImage(file='tarantino.png')
   dibtt = tk.Button(new_d, image=directt, border=0, cursor='hand2', activebackground="#070B15",command=Tarantino)
   dibtt.place(anchor='center', x=1310, y=420, width=280, height=270)

   new_d.resizable(False,False)
   new_d.mainloop()

top3 = None
def Wes():
   global top3
   new_d = tk.Toplevel(window)
   new_d.title('Director')
   new_d.state('zoomed')
   new_d.config(bg='#070B15')

   label1 = tk.Label(new_d, width =50, text='Wes Anderson movies - Top 3', font=('Garamond', 45))
   label1.config(fg='#F1F5F9')
   label1.config(bg='#070B15')
   label1.place(anchor='center', relx=0.5, y=150)
###############################################
   frame = tk.Frame(new_d, width=420, height=230, bg='#0B0F1F')
   frame.place(x = 70, y = 350)

   top3 =tk.PhotoImage(file='fox.png')
   label =tk.Label(frame,image=top3)
   label.place(x=1, y=2)

   label = tk.Label(frame, text='Fantastic Mr. Fox', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',16))
   label.place(x=200, y=2)
   label1 = tk.Label(frame, text='8.0', fg='green',bg='#0B0F1F', font=('Microsoft Yahei UI Light',12,'bold'))
   label1.place(x=200, y=50)
   label1 = tk.Label(frame, text='2009, animated film', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=85)
   label1 = tk.Label(frame, text='drama 1 hr 27 min', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=115)
   label1 = tk.Label(frame, text='UK, USA 12+', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=145)
   label1 = tk.Label(frame, text='Directed by: Wes Anderson', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=175)
##################################################
   frame1 = tk.Frame(new_d, width=420, height=230, bg='#0B0F1F')
   frame1.place(x = 550, y = 350)

   top2 =tk.PhotoImage(file='moon.png')
   label =tk.Label(frame1,image=top2)
   label.place(x=1, y=2)

   label = tk.Label(frame1, text='Moonrise Kingdom', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',16))
   label.place(x=200, y=2)
   label1 = tk.Label(frame1, text='7.7', fg='green',bg='#0B0F1F', font=('Microsoft Yahei UI Light',12,'bold'))
   label1.place(x=200, y=50)
   label1 = tk.Label(frame1, text='2012, family, comedy', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=85)
   label1 = tk.Label(frame1, text='1 h 30 min', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=115)
   label1 = tk.Label(frame1, text='USA 18+', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=145)
   label1 = tk.Label(frame1, text='Directed by: Wes Anderson', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=175)
#########################################################
   frame1 = tk.Frame(new_d, width=420, height=230, bg='#0B0F1F')
   frame1.place(x = 1030, y = 350)

   top1 =tk.PhotoImage(file='hotel.png')
   label =tk.Label(frame1,image=top1)
   label.place(x=1, y=2)

   label = tk.Label(frame1, text='The Grand Budapest\nHotel', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',16))
   label.place(x=180, y=2)
   label1 = tk.Label(frame1, text='7.9', fg='green',bg='#0B0F1F', font=('Microsoft Yahei UI Light',12,'bold'))
   label1.place(x=200, y=50)
   label1 = tk.Label(frame1, text='2014, comedy, adventure', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=85)
   label1 = tk.Label(frame1, text='1 h 40 min', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=115)
   label1 = tk.Label(frame1, text='USA, Germany 16+', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=145)
   label1 = tk.Label(frame1, text='Directed by: Wes Anderson', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=175)
#############################################
   new_d.resizable(False,False)
   new_d.mainloop()
#########################################3
def Dav():
   global top3
   new_d = tk.Toplevel(window)
   new_d.title('Director')
   new_d.state('zoomed')
   new_d.config(bg='#070B15')

   label1 = tk.Label(new_d, width =50, text='David Fincher movies - Top 3', font=('Garamond', 45))
   label1.config(fg='#F1F5F9')
   label1.config(bg='#070B15')
   label1.place(anchor='center', relx=0.5, y=150)
###############################################
   frame = tk.Frame(new_d, width=420, height=230, bg='#0B0F1F')
   frame.place(x = 70, y = 350)

   top3 =tk.PhotoImage(file='social.png')
   label =tk.Label(frame,image=top3)
   label.place(x=1, y=2)

   label = tk.Label(frame, text='The Social Network', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',16))
   label.place(x=200, y=2)
   label1 = tk.Label(frame, text='7.7', fg='green',bg='#0B0F1F', font=('Microsoft Yahei UI Light',12,'bold'))
   label1.place(x=200, y=50)
   label1 = tk.Label(frame, text='2010, drama, biography', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=85)
   label1 = tk.Label(frame, text='2 h', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=115)
   label1 = tk.Label(frame, text='USA 12+', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=145)
   label1 = tk.Label(frame, text='Directed by: David Fincher', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=175)
##################################################
   frame1 = tk.Frame(new_d, width=420, height=230, bg='#0B0F1F')
   frame1.place(x = 550, y = 350)

   top2 =tk.PhotoImage(file='seven.png')
   label =tk.Label(frame1,image=top2)
   label.place(x=1, y=2)

   label = tk.Label(frame1, text='Seven', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',16))
   label.place(x=200, y=2)
   label1 = tk.Label(frame1, text='8.3', fg='green',bg='#0B0F1F', font=('Microsoft Yahei UI Light',12,'bold'))
   label1.place(x=200, y=50)
   label1 = tk.Label(frame1, text='1995, thriller, drama', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=85)
   label1 = tk.Label(frame1, text='2 h 7 min', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=115)
   label1 = tk.Label(frame1, text='USA 18+', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=145)
   label1 = tk.Label(frame1, text='Directed by: David Fincher', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=175)
#########################################################
   frame1 = tk.Frame(new_d, width=420, height=230, bg='#0B0F1F')
   frame1.place(x = 1030, y = 350)

   top1 =tk.PhotoImage(file='zod.png')
   label =tk.Label(frame1,image=top1)
   label.place(x=1, y=2)

   label = tk.Label(frame1, text='Zodiac', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',16))
   label.place(x=200, y=2)
   label1 = tk.Label(frame1, text='7.3', fg='green',bg='#0B0F1F', font=('Microsoft Yahei UI Light',12,'bold'))
   label1.place(x=200, y=50)
   label1 = tk.Label(frame1, text='2007, thriller, detective', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=85)
   label1 = tk.Label(frame1, text='2 h 38 min', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=115)
   label1 = tk.Label(frame1, text='USA 18+', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=145)
   label1 = tk.Label(frame1, text='Directed by: David Fincher', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=175)
#############################################
   new_d.resizable(False,False)
   new_d.mainloop()

def Nolan():
   global top3
   new_d = tk.Toplevel(window)
   new_d.title('Director')
   new_d.state('zoomed')
   new_d.config(bg='#070B15')

   label1 = tk.Label(new_d, width =50, text='Christopher Nolan movies - Top 3', font=('Garamond', 45))
   label1.config(fg='#F1F5F9')
   label1.config(bg='#070B15')
   label1.place(anchor='center', relx=0.5, y=150)
###############################################
   frame = tk.Frame(new_d, width=420, height=230, bg='#0B0F1F')
   frame.place(x = 70, y = 350)

   top3 =tk.PhotoImage(file='dark.png')
   label =tk.Label(frame,image=top3)
   label.place(x=1, y=2)

   label = tk.Label(frame, text='The Dark Knight', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',16))
   label.place(x=200, y=2)
   label1 = tk.Label(frame, text='9.0', fg='green',bg='#0B0F1F', font=('Microsoft Yahei UI Light',12,'bold'))
   label1.place(x=200, y=50)
   label1 = tk.Label(frame, text='2008, Action, Crime, Drama', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=85)
   label1 = tk.Label(frame, text='2 h 32 min', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=115)
   label1 = tk.Label(frame, text='USA, UK 12+', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=145)
   label1 = tk.Label(frame, text='Directed by: C. Nolan', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=175)
##################################################
   frame1 = tk.Frame(new_d, width=420, height=230, bg='#0B0F1F')
   frame1.place(x = 550, y = 350)

   top2 =tk.PhotoImage(file='interstellar.png')
   label =tk.Label(frame1,image=top2)
   label.place(x=1, y=2)

   label = tk.Label(frame1, text='Interstellar', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',16))
   label.place(x=200, y=2)
   label1 = tk.Label(frame1, text='8.7', fg='green',bg='#0B0F1F', font=('Microsoft Yahei UI Light',12,'bold'))
   label1.place(x=200, y=50)
   label1 = tk.Label(frame1, text='2014, Adventure, Sci-Fi', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=85)
   label1 = tk.Label(frame1, text='2 h 49 min', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=115)
   label1 = tk.Label(frame1, text='USA, UK, Canada 16+', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=145)
   label1 = tk.Label(frame1, text='Directed by: C. Nolan', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=175)
#########################################################
   frame1 = tk.Frame(new_d, width=420, height=230, bg='#0B0F1F')
   frame1.place(x = 1030, y = 350)

   top1 =tk.PhotoImage(file='inception.png')
   label =tk.Label(frame1,image=top1)
   label.place(x=1, y=2)

   label = tk.Label(frame1, text='Inception', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',16))
   label.place(x=200, y=2)
   label1 = tk.Label(frame1, text='8.8', fg='green',bg='#0B0F1F', font=('Microsoft Yahei UI Light',12,'bold'))
   label1.place(x=200, y=50)
   label1 = tk.Label(frame1, text='2010, Action, Sci-Fi', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=85)
   label1 = tk.Label(frame1, text='2 h 28 min', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=115)
   label1 = tk.Label(frame1, text='USA, UK 12+', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=145)
   label1 = tk.Label(frame1, text='Directed by: C. Nolan', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=175)
#############################################
   new_d.resizable(False,False)
   new_d.mainloop()

def Tarantino():
   global top3
   new_d = tk.Toplevel(window)
   new_d.title('Director')
   new_d.state('zoomed')
   new_d.config(bg='#070B15')

   label1 = tk.Label(new_d, width =50, text='Quentin Tarantino movies - Top 3', font=('Garamond', 45))
   label1.config(fg='#F1F5F9')
   label1.config(bg='#070B15')
   label1.place(anchor='center', relx=0.5, y=150)
###############################################
   frame = tk.Frame(new_d, width=420, height=230, bg='#0B0F1F')
   frame.place(x = 70, y = 350)

   top3 =tk.PhotoImage(file='pulp.png')
   label =tk.Label(frame,image=top3)
   label.place(x=1, y=2)

   label = tk.Label(frame, text='Pulp Fiction', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',16))
   label.place(x=200, y=2)
   label1 = tk.Label(frame, text='8.7', fg='green',bg='#0B0F1F', font=('Microsoft Yahei UI Light',12,'bold'))
   label1.place(x=200, y=50)
   label1 = tk.Label(frame, text='1994, Crime, Drama', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=85)
   label1 = tk.Label(frame, text='2 h 34 min', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=115)
   label1 = tk.Label(frame, text='USA 18+', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=145)
   label1 = tk.Label(frame, text='Directed by: Q. Tarantino', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=175)
##################################################
   frame1 = tk.Frame(new_d, width=420, height=230, bg='#0B0F1F')
   frame1.place(x = 550, y = 350)

   top2 =tk.PhotoImage(file='django.png')
   label =tk.Label(frame1,image=top2)
   label.place(x=1, y=2)

   label = tk.Label(frame1, text='Django Unchained', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',16))
   label.place(x=200, y=2)
   label1 = tk.Label(frame1, text='8.2', fg='green',bg='#0B0F1F', font=('Microsoft Yahei UI Light',12,'bold'))
   label1.place(x=200, y=50)
   label1 = tk.Label(frame1, text='2012, Western, Action', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=85)
   label1 = tk.Label(frame1, text='2 h 45 min', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=115)
   label1 = tk.Label(frame1, text='USA 18+', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=145)
   label1 = tk.Label(frame1, text='Directed by: Q. Tarantino', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=175)
#########################################################
   frame1 = tk.Frame(new_d, width=420, height=230, bg='#0B0F1F')
   frame1.place(x = 1030, y = 350)

   top1 =tk.PhotoImage(file='kill.png')
   label =tk.Label(frame1,image=top1)
   label.place(x=1, y=2)

   label = tk.Label(frame1, text='Kill Bill:\nThe Whole Bloody Affair', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',13))
   label.place(x=200, y=2)
   label1 = tk.Label(frame1, text='8.2', fg='green',bg='#0B0F1F', font=('Microsoft Yahei UI Light',12,'bold'))
   label1.place(x=200, y=50)
   label1 = tk.Label(frame1, text='2006, Action, Crime', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=85)
   label1 = tk.Label(frame1, text='4 h 7 min', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=115)
   label1 = tk.Label(frame1, text='USA 18+', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=145)
   label1 = tk.Label(frame1, text='Directed by: Q. Tarantino', fg='white', bg='#0B0F1F', font=('Microsoft Yahei UI Light',12))
   label1.place(x=200, y=175)
#############################################
   new_d.resizable(False,False)
   new_d.mainloop()


def recomm():
   import recommendation_sys
  


def on_escape(event):
    window.destroy()


window = tk.Tk()
window.title('Movie recommender')

window.state('zoomed')
window.config(bg='#070B15')
window.bind("<Escape>", on_escape)
window.bind('<Return>', lambda event=None: search_records())




def click(*args): 
    search_bar.delete(0, 'end') 

label = tk.Label(window, width =776, text='Need help finding the \n movie?', font=('Inter', 60))
label.config(fg='#F1F5F9')
label.config(bg='#070B15')
label.place(anchor='center', relx=0.51, rely=0.4)

label1 = tk.Label(window, width =515, text='Search for your movie through a huge movie library', font=('Inter', 20))
label1.config(fg='#BAE6FD')
label1.config(bg='#070B15')
label1.place(anchor='center', relx=0.5, rely=0.55)




search_bar =tk.Entry(window, bg='#0F172A', fg='#475569', font=('Inter', 16),)
search_bar.place(width=570, height=37, anchor='center', relx=0.515, rely=0.631)
search_bar.insert(0, 'Search for your movie')
search_bar.bind("<Button-1>", click) 

search_button_image = tk.PhotoImage(file='search.png')
# Create the search button
search_button = tk.Button(image=search_button_image,activebackground="#070B15",command=search_records)
search_button.place(width=40, height=39,relx=0.3, rely=0.61)
search_button.config(bg="#0F172A")



movies=tk.PhotoImage(file='Movies.png')
seeallbtn = tk.Button(image=movies,border=0,cursor='hand2',activebackground="#070B15",command=seeall)
seeallbtn.config(bg="#070B15")
seeallbtn.place(anchor='center',x=530, y=582, width=150)

tv_shows=tk.PhotoImage(file='TV shows.png')
tvbtn = tk.Button(image=tv_shows,border=0,cursor='hand2',activebackground="#070B15",command=shows)
tvbtn.config(bg="#070B15")
tvbtn.place(anchor='center',x=660, y=582, width=150)

director=tk.PhotoImage(file='director.png')
dbtn = tk.Button(image=director,border=0,cursor='hand2',activebackground="#070B15",command = dir)
dbtn.config(bg="#070B15")
dbtn.place(anchor='center',x=800, y=582, width=150)

recommendation=tk.PhotoImage(file='recommendation.png')
dbtnrec = tk.Button(image=recommendation,border=0,cursor='hand2',activebackground="#070B15",command = recomm)
dbtnrec.config(bg="#070B15")
dbtnrec.place(anchor='center',x=1007, y=582, width=240)




window.mainloop()
