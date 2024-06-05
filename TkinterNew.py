import tkinter as tk
from tkinter import messagebox
import sqlite3

class KeyGuardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Key Guard")
        self.geometry("500x300")

        self.frames = {}
        for F in (LoginFrame, CreateAccountFrame, ForgotPasswordFrame):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="news")

        self.show_frame("LoginFrame")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Login Form").pack(pady=10)

        tk.Label(self, text="Username").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Master Password").pack()
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack()

        save_button = tk.Button(self, text="Login", command=self.login)
        save_button.pack(pady=10)

        create_account_button = tk.Button(self, text="Create Account", 
                                          command=lambda: controller.show_frame("CreateAccountFrame"))
        create_account_button.pack(pady=10)

        forgot_password_button = tk.Button(self, text="Forgot Password", command=lambda:self.controller.show_frame("ForgotPasswordFrame"))
        forgot_password_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            try:
                conn = sqlite3.connect('key_guard.db')
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM master_login WHERE username=? AND password=?', (username, password))
                if cursor.fetchone():
                    messagebox.showinfo("Success", "Login successful!")
                else:
                    messagebox.showerror("Error", "Invalid credentials!")
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please fill in both fields")

class CreateAccountFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Create Account Form").pack(pady=10)

        tk.Label(self, text="Username").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Master Password").pack()
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack()

        save_button = tk.Button(self, text="Save", command=self.create_account)
        save_button.pack(pady=10)

        back_button = tk.Button(self, text="Back", command=lambda:self.controller.show_frame("LoginFrame"))
        back_button.pack(pady=10)

    def create_account(self):
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
                self.controller.show_frame("LoginFrame")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists!")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please fill in both fields")

class ForgotPasswordFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Forgot Password Form").pack(pady=10)

        tk.Label(self, text="Username").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="New Master Password").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        save_button = tk.Button(self, text="Save")
        save_button.pack(pady=10)

        back_button = tk.Button(self, text="Back", command=lambda:self.controller.show_frame("LoginFrame"))
        back_button.pack(pady=10)



    def reset_password(self):        
        username = self.username_entry.get()
        master_password = self.password_entry.get()






if __name__ == "__main__":
    app = KeyGuardApp()
    app.mainloop()
