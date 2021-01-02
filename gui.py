#imports
import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text = "Hello Twat")
greeting.pack()

label = tk.Label(
    text = "Hey Everybody", 
    foreground="green",
    background="blue",
    height=10,
    width=40
    )
#label.pack()

window.mainloop()
