import tkinter as tk


# grid() locates widgets in a two dimensional grid using row and column absolute coordinates.


window = tk.Tk()

for x in range(3):
    for y in range(3):
        label = tk.Label(window, text=f"Row {x}\nColumn {y}",relief=tk.RAISED, borderwidth=1)
        label.grid(row=x, column=y,)

label = tk.Label(window, text=f"This is a wide label - 3 Column \n",relief=tk.RAISED, borderwidth=1)
label.grid(row=3, column=0, columnspan=3)

window.mainloop()