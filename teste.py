from tkinter import*

janela = Tk()
janela.title("Olá mundo")
janela.geometry('250x250')

label = Label (janela, text = "Primeiro entry")
label.grid (column = 0, row = 0)

entrada = Entry(janela,width=10)
entrada.grid(column=1, row=0)

janela.mainloop()