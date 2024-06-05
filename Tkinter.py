import tkinter as tk
from tkinter import messagebox
import sqlite3

def verify_login():
    username = username_entry.get()
    master_password = password_entry.get()

    conn = sqlite3.connect('master_login.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Master_Login WHERE username = ? AND master_password = ?', 
                   (username, master_password))
    result = cursor.fetchone()
    conn.close()

    if result:
        show_frame(dashboard_frame)
    else:
        messagebox.showwarning("Login Error", "Invalid username or password")

        
# Function to create a new master login
def create_master_login():
    username = username_entry.get()
    master_password = password_entry.get()

    if username and master_password:
        conn = sqlite3.connect('master_login.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Master_Login
                        (username TEXT, master_password TEXT)''')
        cursor.execute('''INSERT INTO Master_Login (username, master_password) VALUES (?, ?)''', 
                        (username, master_password))
        conn.commit()
        conn.close()
        show_frame(login_frame)
    else:
        messagebox.showwarning("Input Error", "Both fields are required!")

# ----------------------------------- FRAMES ---------------------------------------------------------------

def show_frame(frame):
    frame.kraise()

def login_frame(window):
    frame = tk.Frame(window)
    tk.Label(frame, text="Username").pack(pady=5)
    global username_entry
    username_entry = tk.Entry(frame)
    username_entry.pack(pady=5)

    tk.Label(frame, text="Master Password").pack(pady=5)
    global password_entry
    password_entry = tk.Entry(frame, show='*')
    password_entry.pack(pady=5)

    login_button = tk.Button(frame, text="Login", command=verify_login)
    login_button.pack(pady=5)

    create_account_button = tk.Button(frame, text="Create Account", command=lambda: show_frame(create_account_frame))
    create_account_button.pack(pady=5)
    return frame

# Function to create the create account frame
def create_account_frame(window):
    frame = tk.Frame(window)
    tk.Label(frame, text="Create Account").pack(pady=5)
    tk.Label(frame, text="Username").pack(pady=5)
    global username_entry
    username_entry = tk.Entry(frame)
    username_entry.pack(pady=5)

    tk.Label(frame, text="Master Password").pack(pady=5)
    global password_entry
    password_entry = tk.Entry(frame, show='*')
    password_entry.pack(pady=5)

    save_button = tk.Button(frame, text="Save", command=create_master_login)
    save_button.pack(pady=5)

    back_to_login_button = tk.Button(frame, text="Back to Login", command=lambda: show_frame(login_frame))
    back_to_login_button.pack(pady=5)
    return frame

# Function to create the dashboard frame
def create_dashboard_frame(window):
    frame = tk.Frame(window)
    tk.Label(frame, text="Welcome to the Dashboard!").pack(pady=5)

    logout_button = tk.Button(frame, text="Logout", command=lambda: show_frame(login_frame))
    logout_button.pack(pady=5)
    return frame

def reset_master_password_frame(window):
    frame = tk.Frame(window)
    tk.Label(frame, text="Reset Password").pack(pady=5)
    




# ------------------------------------------------------------------------------------------------------------------------------

# Create the main window
window = tk.Tk()
window.title("Key Guard")
window.geometry("700x350")

# Create frames
login_frame = login_frame(window)
create_account_frame = create_account_frame(window)
create_dashboard_frame = create_dashboard_frame(window)
reset_master_password_frame = reset_master_password_frame(window)

# Place frames in the grid
for frame in (login_frame, create_account_frame, create_dashboard_frame, ):
    frame.grid(row=0, column=0, sticky='news')

# Show initial frame
show_frame(login_frame)

# Run the application
window.mainloop()
