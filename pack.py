import tkinter as tk

# pack() organizes widgets in horizontal and vertical boxes that are limited to left, right, top, bottom positions.
# Each box is offset and relative to each other.

window = tk.Tk()

w = tk.Label(window, text="text 1",)
w.pack(padx=20, pady=20, side=tk.LEFT)
w = tk.Label(window, text="text 2",)
w.pack(padx=20, pady=20, side=tk.LEFT)
w = tk.Label(window, text="text 3",)
w.pack(padx=20, pady=20, side=tk.LEFT)


window.mainloop()
