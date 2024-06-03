import tkinter as tk

window = tk.Tk()

label = tk.Label(
    text="Python rocks!",
    fg="white", # textcolour
    bg="black", # background colour
    width=10,
    height=10
) # tk.Label to add text to window

button = tk.Button(
    text="Click me",
    width=25,
    height=5,
    bg="blue",
    fg="yellow"
)

label.pack() # .pack to add to window
button.pack()

window.mainloop()