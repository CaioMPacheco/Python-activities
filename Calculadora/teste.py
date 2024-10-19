# Importando bibliotecas
import tkinter as tk

# Criando Janela principal
janela = tk.Tk()
janela.resizable(width=False, height=False)  # Tirando modo tela cheia
janela.geometry('400x600')  # Tamanho da janela
janela.title('Calculadora Python')  # Título da janela
janela.configure(bg='gray')

# Textos na janela
titulo = tk.Label(janela, text='Calculadora', font='Arial 20 bold', bg='gray')
titulo.grid(column=0, row=0, columnspan=3, padx=10, pady=0)

# Espaço em branco
espaco_branco = tk.Label(janela, text='', bg='gray')
espaco_branco.grid(column=0, row=1, padx=10, pady=90)

# Botões
botoes = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '0', '+', '-',
    'x', '÷', ',',
    'C'
]

# Função para processar cliques nos botões
def botao_clicado(valor):
    print("Botão clicado:", valor)

row_num = 2
col_num = 0
for botao_text in botoes:
    botao = tk.Button(janela, text=botao_text, width=10, height=5, font='Arial 9 bold', bg='gray', borderwidth='5', fg='white', justify='center', command=lambda valor=botao_text: botao_clicado(valor))
    botao.grid(column=col_num, row=row_num, padx=7, pady=3)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

janela.mainloop()  # Repetição para janela não fechar