import tkinter as tk

# Um frame, em programação GUI, nada mais é que uma espécie de 'container', cujo propósito principal é armazenar
# e agrupar outros widgets.

window = tk.Tk()
frame = tk.Frame(background='black')
frame.pack(side=tk.BOTTOM)


w = tk.Label(frame, text = 'text1',)
w.pack(padx=5, pady=5,)

window.mainloop()