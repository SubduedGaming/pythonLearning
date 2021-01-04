#imports
import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text = "Hello Twat")
greeting.pack()

label = tk.Label(
    text = "Name", 
    foreground="green",
    background="blue",
    height=10,
    width=40
    )
#label.pack()

button = tk.Button(
    text = "Click Me!!",
    width = 40,
    height = 30,
    bg = "green",
    fg = "blue"
)


entry = tk.Entry(
    fg="green",
    bg="blue",
    width=50
)

entry.pack()

name = entry.get()



window.mainloop()
