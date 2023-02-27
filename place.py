import tkinter as tk

# place() places widgets in a two dimensional grid using x and y absolute coordinates.

window = tk.Tk()

w = tk.Label(window, text="text 1",)
w.place(x=0, y=0)
w = tk.Label(window, text="text 2",)
w.place(x=50, y=0)
w = tk.Label(window, text="text 3",)
w.place(x=100, y=0)


window.mainloop()
