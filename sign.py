from tkinter import *
from tkinter import messagebox
import ast
import psycopg2 as pg

conn = pg.connect(
host='localhost',
database='postgres',
port=5432,
user='postgres',
password='12345'
    )

def on_escape(event):
    root.destroy()


root = Tk()

root.title("SignIn")

root.geometry('925x500+300+200')
root.state('zoomed')
root.configure(bg='#070B15')
root.bind("<Escape>", on_escape)
root.resizable(False, False)

def login_user():
    username = user.get()
    password = password_.get()

    try:
        with conn.cursor() as mycursor:
            mycursor.execute("""
                SELECT * FROM users_password WHERE username = %s AND password = %s;
            """, (username, password))
            result = mycursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login successful!")
            root.destroy()
            import recommender
        else:
            messagebox.showerror("Error", "Login failed. Check username and password.")
    except Exception as e:
        messagebox.showerror("Error", f"Error during login: {str(e)}")
 #####################################################   
def signup_command():
    root1=Toplevel(root)
    root1.title("SignUp")
    root1.geometry('925x500+300+200')
    root1.state('zoomed')
    root1.configure(bg='#070B15')
    root1.bind("<Escape>", on_escape)
    root1.resizable(False, False)

    def database_connect():
        username = user.get()
        password = password_.get()
        confirm_password = conform.get()
        if not username or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        try:
            with conn.cursor() as check_cursor:
                check_cursor.execute("SELECT * FROM users_password WHERE username = %s;", (username,))
                existing_user = check_cursor.fetchone()

            if existing_user:
                messagebox.showerror("Error", "Username already exists. Choose a different username.")
                return 
        
            with conn.cursor() as mycursor:
                mycursor.execute("""
                    INSERT INTO users_password  VALUES (%s, %s);
                """, (username, password))
            conn.commit()
            messagebox.showinfo("Success", "User registered successfully")
            root1.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error registering user: {str(e)}")
    
    def sign():
        root1.destroy()


    frame=Frame(root1,width =608, height = 750, bg ='#0B0F1F')
    frame.place(x=480,y=50)

    heading=Label(frame, text='Sign up',fg="#E0F2FE",bg='#0B0F1F', font=('Microsoft Yahei UI Light', 23, 'bold'))
    heading.place(x=240,y=100)

    def on_enter(e): 
        user.delete(0, 'end') 
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Username')

    user=Entry(frame, width=25,fg='#E0F2FE', border=0,bg='#0B0F1F', font=('Microsoft Yahei UI Light',11))
    user.place(x=160,y=200)
    user.insert(0, 'Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave) 

    Frame(frame,width=295,height=2,bg='white').place(x=155,y=227)      

    def on_enter(e): 
        password_.delete(0, 'end') 
    def on_leave(e):
        if password_.get()=='':
            password_.insert(0,'Password') 

    password_=Entry(frame, width=25,fg='#E0F2FE', border=0,bg='#0B0F1F', font=('Microsoft Yahei UI Light',11))
    password_.place(x=160,y=280)
    password_.insert(0, 'Password')
    password_.bind("<FocusIn>",on_enter)
    password_.bind("<FocusOut>",on_leave)  

    Frame(frame,width=295,height=2,bg='white').place(x=155,y=307)  

    def on_enter(e): 
        conform.delete(0, 'end') 
    def on_leave(e):
        if conform.get()=='':
            conform.insert(0,'Conform Password') 

    conform=Entry(frame, width=25,fg='#E0F2FE', border=0,bg='#0B0F1F', font=('Microsoft Yahei UI Light',11))
    conform.place(x=160,y=360)
    conform.insert(0, 'Confirm Password')
    conform.bind("<FocusIn>",on_enter)
    conform.bind("<FocusOut>",on_leave)  

    Frame(frame,width=295,height=2,bg='white').place(x=155,y=387)  


    Button(frame, width=41,pady=7, text='Sign up', bg='#FBBF24', border=0, fg='#070B15',command=database_connect).place(x=158, y=440)
    label = Label(frame, text='I have an account', fg='#E0F2FE', bg='#0B0F1F', font=('Microsoft Yahei UI Light',9))
    label.place(x=220, y=500)

    signin=Button(frame,width=6,text='Sign in', border=0,bg='#0B0F1F', cursor='hand2', fg='#E0F2FE',command=sign)
    signin.place(x=330,y=501)

# Start the mainloop
    root1.mainloop()
    

#####################################################

frame=Frame(root,width =608, height = 600, bg ='#0B0F1F')
frame.place(x=480,y=100)

heading=Label(frame, text='Sign In',fg="#E0F2FE",bg='#0B0F1F', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=240,y=100)

def on_enter(e): 
    user.delete(0, 'end') 
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user=Entry(frame, width=25,fg='#E0F2FE', border=0,bg='#0B0F1F', font=('Microsoft Yahei UI Light',11))
user.place(x=160,y=220)
user.insert(0, 'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave) 

Frame(frame,width=295,height=2,bg='white').place(x=155,y=247)    

def on_enter(e): 
    password_.delete(0, 'end') 
def on_leave(e):
    if password_.get()=='':
        password_.insert(0,'Password') 

password_=Entry(frame, width=25,fg='#E0F2FE', border=0,bg='#0B0F1F', font=('Microsoft Yahei UI Light',11))
password_.place(x=160,y=320)
password_.insert(0, 'Password')
password_.bind("<FocusIn>",on_enter)
password_.bind("<FocusOut>",on_leave)  

Frame(frame,width=295,height=2,bg='white').place(x=155,y=347)  


Button(frame, width=41,pady=7, text='Sign in', bg='#FBBF24', border=0, fg='#070B15',command=login_user).place(x=158, y=440)
label = Label(frame, text='Don\'t Have An Account?', fg='#E0F2FE', bg='#0B0F1F', font=('Microsoft Yahei UI Light',9))
label.place(x=190, y=500)

signin=Button(frame,width=6,text='Sign Up', border=0,bg='#0B0F1F', cursor='hand2', fg='#E0F2FE',command=signup_command)
signin.place(x=340,y=501)
# Start the mainloop
root.mainloop()
