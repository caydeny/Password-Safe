import tkinter as tk
from tkinter import messagebox
import sqlite3

class KeyGuardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Key Guard")
        self.root.geometry("400x300")
        
        self.login_frame()

    def create_master_login(self):
        username = self.username_entry.get()
        master_password = self.password_entry.get()

        if username and master_password:
            try:
                conn = sqlite3.connect('key_guard.db')
                cursor = conn.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS master_login (
                                  username TEXT PRIMARY KEY,
                                  password TEXT)''')
                cursor.execute("INSERT INTO master_login (username, password) VALUES (?, ?)",
                               (username, master_password))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Account created successfully!")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists!")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please fill in both fields")


    def login_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Login Form").pack(pady=10)

        tk.Label(frame, text="Username").pack()
        self.username_entry = tk.Entry(frame)
        self.username_entry.pack()

        tk.Label(frame, text="Master Password").pack()
        self.password_entry = tk.Entry(frame, show='*')
        self.password_entry.pack()

        save_button = tk.Button(frame, text="Login", command=self.create_master_login)
        save_button.pack(pady=10)

        create_account_button = tk.Button(frame, text="Create Account", command=self.create_account_frame)
        create_account_button.pack(pady=10)


    def create_account_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(frame, text="Create Account Form").pack(pady=10)

        tk.Label(frame, text="Username").pack()
        self.new_username_entry = tk.Entry(frame)  # Use a different variable name
        self.new_username_entry.pack()

        tk.Label(frame, text="Master Password").pack()
        self.new_password_entry = tk.Entry(frame, show='*')  # Use a different variable name
        self.new_password_entry.pack()

        save_button = tk.Button(frame, text="Save")
        save_button.pack(pady=10)

if __name__ == "__main__":
    window = tk.Tk()
    app = KeyGuardApp(window)
    window.mainloop()
