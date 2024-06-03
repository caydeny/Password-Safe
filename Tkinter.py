import tkinter as tk

window = tk.Tk() # root of application
window.title("Key Guard")
window.geometry("750x400")
window.configure(bg='#333333')

# Creating widgets
login_label = tk.Label(window, text="Login")

username_label = tk.Label(window, text="Username")
username_entry = tk.Entry(window)

password_label = tk.Label(window, text="Password")
password_entry = tk.Entry(window, show="*")

login_button = tk.Button(window, text="Login")

# Placing widgets
login_label.grid(row=0, column=0, columnspan=2)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2)

window.mainloop()