import tkinter as tk

def inserir_numero(numero):
    atual = caixa_número.get()
    caixa_número.delete(0, tk.END)
    caixa_número.insert(tk.END, atual + numero)

def realizar_operacao(operacao):
    global valor_atual
    valor_atual = float(caixa_número.get())
    caixa_número.delete(0, tk.END)
    operacoes[operacao]()

def somar():
    global valor_atual
    valor_atual += float(caixa_número.get())
    caixa_número.delete(0, tk.END)
    caixa_número.insert(tk.END, str(valor_atual))

def subtrair():
    global valor_atual
    valor_atual -= float(caixa_número.get())
    caixa_número.delete(0, tk.END)
    caixa_número.insert(tk.END, str(valor_atual))

def multiplicar():
    global valor_atual
    valor_atual *= float(caixa_número.get())
    caixa_número.delete(0, tk.END)
    caixa_número.insert(tk.END, str(valor_atual))

def dividir():
    global valor_atual
    divisor = float(caixa_número.get())
    if divisor != 0:
        valor_atual /= divisor
        caixa_número.delete(0, tk.END)
        caixa_número.insert(tk.END, str(valor_atual))
    else:
        caixa_número.delete(0, tk.END)
        caixa_número.insert(tk.END, "Erro")

def limpar():
    caixa_número.delete(0, tk.END)

janela = tk.Tk()
janela.resizable(width=False, height=False)
janela.geometry('375x600')
janela.title('Calculadora Python')
janela.configure(bg='gray')

caixa_número = tk.Entry(janela, width=35, font='Arial 10 bold', bg='white', borderwidth='5', fg='black', justify='right')
caixa_número.grid(column=0, row=0, columnspan=4, padx=10, pady=10)

botoes = [
    ('7', 1, 1), ('8', 1, 2), ('9', 1, 3), ('/', 1, 4),
    ('4', 2, 1), ('5', 2, 2), ('6', 2, 3), ('*', 2, 4),
    ('1', 3, 1), ('2', 3, 2), ('3', 3, 3), ('-', 3, 4),
    ('0', 4, 1), ('C', 4, 2), ('=', 4, 3), ('+', 4, 4)
]

for (texto, linha, coluna) in botoes:
    if texto == '=':
        cmd = lambda t=texto: realizar_operacao(t)
    elif texto == 'C':
        cmd = limpar
    else:
        cmd = lambda t=texto: inserir_numero(t)

    tk.Button(janela, text=texto, width=10, height=5, font='Arial 9 bold', bg='gray', borderwidth='5', fg='white', command=cmd).grid(row=linha, column=coluna, padx=5, pady=5)

valor_atual = 0
operacoes = {'+': somar, '-': subtrair, '*': multiplicar, '/': dividir}

janela.mainloop()