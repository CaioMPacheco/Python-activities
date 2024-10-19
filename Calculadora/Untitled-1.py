# Importando bibliotecas
import math
from tkinter import *
import os
import tkinter as tk

# Criando Janela principal
janela = tk.Tk()
janela.resizable(width=False, height=False)  # Tirando modo tela cheia
janela.geometry('375x600')  # Tamanho da janela
janela.title('Calculadora Python')  # Título da janela
janela.configure(bg='gray')

# Textos na janela Concertar
'''titulo = Label(janela, text='Calculadora', font='Arial 20 bold', bg='gray')
titulo.grid(column=0, row=0, columnspan=3, padx=10, pady=0)'''


# Botões
caixa_número = Entry(janela, width=35,font='Arial 10 bold', bg='gray',borderwidth='5',fg='white', justify='center' )
caixa_número.grid(column=0, row=0, columnspan=4, padx=3, pady=3)

espaço_branco = Label(janela, text="", bg="gray")
espaço_branco.grid(column=0, row=1, columnspan=4, rowspan=4, pady=75)

numero1 = Button(janela, text='1', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center',)  # botão número 1
numero1.grid(column=0, row=10, padx=3, pady=3,)

numero2 = Button(janela, text='2', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center')  # botão número 2
numero2.grid(column=1, row=10, padx=3, pady=3)

numero3 = Button(janela, text='3', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center')  # botão número 3
numero3.grid(column=2, row=10, padx=3, pady=3)

numero4 = Button(janela, text='4', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center')  # botão número 4
numero4.grid(column=0, row=15, padx=3, pady=3)

numero5 = Button(janela, text='5', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center')  # botão número 5
numero5.grid(column=1, row=15, padx=3, pady=3)

numero6 = Button(janela, text='6', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center')  # botão número 6
numero6.grid(column=2, row=15, padx=3, pady=3)

numero7 = Button(janela, text='7', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center')  # botão número 7
numero7.grid(column=0, row=20, padx=3, pady=3)

numero8 = Button(janela, text='8', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center')  # botão número 8
numero8.grid(column=1, row=20, padx=3, pady=3)

numero9 = Button(janela, text='9', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center')  # botão número 9
numero9.grid(column=2, row=20, padx=3, pady=3)

numero0 = Button(janela, text='0', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center')  # botão número 0
numero0.grid(column=1, row=25, padx=3, pady=3)

botaosoma = Button(janela, text='+', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center') #Botão + = Soma
botaosoma.grid(column=3, row=10, padx=3, pady=3)

botaosubstração = Button(janela, text='-', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center') #Botão - = Subtração
botaosubstração.grid(column=3, row=15, padx=3, pady=3)

botaomultiplicação = Button(janela, text='x', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center') #Botão X = Multiplicação
botaomultiplicação.grid(column=3, row=20, padx=3, pady=3)

botaodivisão = Button(janela, text='÷', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center') #Botão ÷ = Divisão
botaodivisão.grid(column=3, row=25, padx=3, pady=3)

botaovirgula = Button(janela, text=',', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center') #Botão , = Colocar vírgula
botaovirgula.grid(column=2, row=25, padx=3, pady=3)

botaolimpar = Button(janela, text='C', width=10, height=5, font='Arial 9 bold', bg='gray',borderwidth='5',fg='white', justify='center') #Botão C = Limpar
botaolimpar.grid(column=0, row=25, padx=3, pady=3)



janela.mainloop()  # Repetição para janela não fechar