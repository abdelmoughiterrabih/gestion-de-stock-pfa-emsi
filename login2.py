import tkinter as tk
import sqlite3
from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel, ttk
import mainapp

# Connect to the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create the user table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')

root = tk.Tk()
root.title("Login/Signup")
root.geometry('500x300+50+50')
root.configure(bg="#99FFFF")

# Create labels and entries for the login form
login_label_username = tk.Label(root, text="Username:", font=(17), background="#99FFFF")
login_entry_username = tk.Entry(root, font=(17))
login_label_password = tk.Label(root, text="Password:", font=(17), background="#99FFFF")
login_entry_password = tk.Entry(root, show="*", font=(17))

login_label_username.grid(row=0, column=0, padx=10, pady=10)
login_label_password.grid(row=0, column=0, padx=10, pady=10)

# Create labels and entries for the signup form
signup_label_username = tk.Label(root, text="Username:", font=(17), background="#99FFFF")
signup_entry_username = tk.Entry(root, font=(17))
signup_label_password = tk.Label(root, text="Password:", font=(17), background="#99FFFF")
signup_entry_password = tk.Entry(root, show="*", font=(17))

signup_label_username.grid(row=0, column=0, padx=10, pady=10)
signup_label_password.grid(row=0, column=0, padx=10, pady=10)

# Define functions to handle user input and database interaction
def login():
    username = login_entry_username.get()
    password = login_entry_password.get()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    if c.fetchone() is not None:
        # Login successful
        login_status.config(text="Login successful")
        messagebox.showinfo(title='Login status', message='Login successful.')
        root.destroy()  # Close the login window
        mainapp_window = Toplevel()  # Create the mainapp window
        mainapp.main(master=mainapp_window)  # Launch the mainapp with the mainapp window as the master

        
    else:
        # Login failed
        login_status.config(text="Username/Password is incorrect")
        messagebox.showerror(title='Login error', message='Username/Password is incorrect.')

def signup():
    username = signup_entry_username.get()
    password = signup_entry_password.get()
    try:
        c.execute('INSERT INTO users VALUES (?, ?)', (username, password))
        conn.commit()
        signup_status.config(text="Signup successful")
        messagebox.showinfo(title='SIGNUP status', message='signup successful.')
    except sqlite3.IntegrityError:
        signup_status.config(text="Username already exists")
        messagebox.showinfo(title='SIGNUP error', message='username already in use.')

# Create buttons for login and signup

style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 16))

login_button = ttk.Button(root, text="Login", command=login, style="Custom.TButton")
signup_button = ttk.Button(root, text="Signup", command=signup, style="Custom.TButton")


# Create labels for status messages
login_status = tk.Label(root, text="", background="#99FFFF")
signup_status = tk.Label(root, text="", background="#99FFFF")

# Place the widgets in the GUI
login_label_username.grid(row=0, column=0)
login_entry_username.grid(row=0, column=1)
login_label_password.grid(row=1, column=0)
login_entry_password.grid(row=1, column=1)
login_button.grid(row=2, column=0,pady=7, padx=10)
login_status.grid(row=2, column=1)

signup_label_username.grid(row=3, column=0)
signup_entry_username.grid(row=3, column=1)
signup_label_password.grid(row=4, column=0)
signup_entry_password.grid(row=4, column=1)
signup_button.grid(row=5, column=0,pady=7, padx=10)
signup_status.grid(row=5, column=1)

# Run the GUI main loop
root.mainloop()
