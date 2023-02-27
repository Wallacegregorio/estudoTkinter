import tkinter as tk

window = tk.Tk()

w = tk.Label(window, text="text 1",)
w.pack(padx=20, pady=20, side=tk.LEFT)
w = tk.Label(window, text="text 2",)
w.pack(padx=20, pady=20, side=tk.LEFT)
w = tk.Label(window, text="text 3",)
w.pack(padx=20, pady=20, side=tk.LEFT)


window.mainloop()



if __name__ == '__main__':
    pass
