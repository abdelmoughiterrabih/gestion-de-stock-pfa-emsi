import tkinter as tk
import sqlite3
from tkinter import Image, Tk, Label, Entry, Button, messagebox, Toplevel, ttk
from PIL import ImageTk, Image
import mainapp
import subprocess
import threading



    
# Connect to the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create the user table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')


def save_user_data():
     username = username_entry.get()
     password = password_entry.get()
 

     if not (username and password ):
        messagebox.showerror("Error", "Please Complete All Fields")
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        return

        
    # Insertion des données dans la base de données
    
     conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
     conn.commit()
      
    # Affichage d'un message de confirmation
     messagebox.showinfo("Confirmation", "Registration Successful")
     username_entry.delete(0, 'end')
     password_entry.delete(0, 'end')
    
thread = threading.Thread(target=save_user_data)
thread.start()    


# Define functions to handle user input and database interaction
def Login():
    username = username_entry.get()
    password = password_entry.get()
    if not(username and password ):  
        messagebox.showerror('Error', 'Please Complete All Fields')
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        return
        # check if user exists in database
    cursor = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    rows = list(cursor)
    
    if len(rows) > 0:
        messagebox.showinfo("Success", "Login Successful.")
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        
        if cursor: 
          root.destroy()
          mainapp.main()
        
    else:
            # show error message
         error = messagebox.showerror("Error", "Invalid Username Or Password!")
         username_entry.delete(0, 'end')
         password_entry.delete(0, 'end')
         
def go_to_login():
    root.destroy()
    import login2  
         
root = tk.Tk()
root.title("Signup")
root.geometry('900x900')
root.configure(bg="#643843",width=70)
root.resizable(False,False)
frame = tk.Frame(bg='black')



# Centrer le frame
frame.pack(side="top", expand=True, padx=20, pady=20)         
         
# Create labels and entries for the login form
login_label = tk.Label(frame, text="Create Your Account", bg='black', fg="#99627A", font=("Jokerman", 30))
username_label = tk.Label(frame, text="Username", bg='black', fg="#FFFFFF", font=("NSimSun", 16))
username_entry = tk.Entry(frame, font=("NSimSun", 16))
password_entry = tk.Entry(frame, show="*", font=("NSimSun", 16))
password_label = tk.Label(frame, text="Password", bg='black', fg="#FFFFFF", font=("NSimSun", 16))



# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)



login_button = tk.Button(
    frame, text="Signup", bg="#C88EA7", fg="#FFFFFF", font=("Jokerman", 16), command=save_user_data)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
signup_button = tk.Button(
    frame, text="<<GO BACK TO LOGIN", bg="black", fg="white", font=("Jokerman", 10), command=go_to_login)
signup_button.grid(row=3, column=0, columnspan=2, pady=30)
# Create buttons for login and signup

signup_button.place(x=5,y=320)
style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 16))



# Run the GUI main loop
root.mainloop()
