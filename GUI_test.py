from tkinter import *
from Calculadora_M4t3m4t1ca import *

M4t3m4t1c4 = Tk()
M4t3m4t1c4.geometry("300x400")
M4t3m4t1c4.resizable(True, True)
M4t3m4t1c4.title("M4t3m4t1c4")

e = Entry(M4t3m4t1c4, width= 35, borderwidth=3)
e.grid(row=0, columnspan=3, padx=20, pady=20)

#temporário

def button_add():
    return

# Definindo os botões

botao_1 = Button(M4t3m4t1c4, text="1", padx=20, pady=20, command=button_add)
botao_2 = Button(M4t3m4t1c4, text="2", padx=20, pady=20, command=button_add)
botao_3 = Button(M4t3m4t1c4, text="3", padx=20, pady=20, command=button_add)
botao_4 = Button(M4t3m4t1c4, text="4", padx=20, pady=20, command=button_add)
botao_5 = Button(M4t3m4t1c4, text="5", padx=20, pady=20, command=button_add)
botao_6 = Button(M4t3m4t1c4, text="6", padx=20, pady=20, command=button_add)
botao_7 = Button(M4t3m4t1c4, text="7", padx=20, pady=20, command=button_add)
botao_8 = Button(M4t3m4t1c4, text="8", padx=20, pady=20, command=button_add)
botao_9 = Button(M4t3m4t1c4, text="9", padx=20, pady=20, command=button_add)
botao_0 = Button(M4t3m4t1c4, text="0", padx=20, pady=20, command=button_add)

# Colocando os botões na tela

botao_1.grid(row=3, column=0)
botao_2.grid(row=3, column=1)
botao_3.grid(row=3, column=2)

botao_4.grid(row=2, column=0)
botao_5.grid(row=2, column=1)
botao_6.grid(row=2, column=2)

botao_7.grid(row=1, column=0)
botao_8.grid(row=1, column=1)
botao_9.grid(row=1, column=2)

botao_0.grid(row=4, column=0)

M4t3m4t1c4.mainloop()