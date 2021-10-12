import tkinter as tk
import time
borderwidth = 5
window = tk.Tk()
frame_a = tk.Frame(relief=tk.SUNKEN, borderwidth=borderwidth)
frame_b = tk.Frame(relief=tk.SUNKEN, borderwidth=borderwidth)
label1 = tk.Label(text="Frame A", master=frame_a, bg="black", fg="white")
label2 = tk.Label(text="Frame B", master=frame_b, bg="black", fg="white")
label1.pack()
label2.pack()
frame_a.pack(fill=tk.BOTH)
frame_b.pack(fill=tk.BOTH)


window.mainloop()