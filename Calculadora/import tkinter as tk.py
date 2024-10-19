#Importe a biblioteca tkinter
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk


#cor gradiente
def create_gradient(width, height, colors):
    gradient = Image.new("RGB", (width, height), color=0)
    draw = ImageDraw.Draw(gradient)
    step = width / (len(colors) - 1)
    for i in range(len(colors) - 1):
        start = (int(i * step), 0)
        end = (int((i + 1) * step), height)
        draw.rectangle([start, end], fill=colors[i], outline=None)
    return gradient

def update_gradient():
    global gradient_image
    gradient_image = create_gradient(janela.winfo_width(), janela.winfo_height(), ['#000000', '#6495ED'])
    photo = ImageTk.PhotoImage(gradient_image)
    canvas.create_image(0, 0, image=photo, anchor=tk.NW)
    canvas.image = photo

#Crie uma Janela

janela = tk.Tk()
janela.title('Calculadora')
janela.geometry("600x800")
canvas = tk.Canvas(janela, width=400, height=300)
canvas.pack(fill=tk.BOTH, expand=tk.YES)

gradient_image = create_gradient(400, 300, ['#000000', '#6495ED'])
photo = ImageTk.PhotoImage(gradient_image)
canvas.create_image(0, 0, image=photo, anchor=tk.NW)
canvas.image = photo

janela.bind("<Configure>", lambda event: update_gradient())
janela.mainloop()

#Criar botão para digitar operações e resultados




#Definições das funções
#Soma
def soma():
    #variáveis
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    respostas = num1 + num2
    #código
    print("O resultado é: ", respostas)

#Subtração
def subtracao():
    #variáveis
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    respostas = num1 - num2
    print("O resultado é: ", respostas)

#Multiplicação
def multiplicacao():
    #variáveis
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    respostas = num1 * num2
    #código
    print("O resultado é: ", respostas)

#Divisão
def divisao():
    #variáveis
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    respostas = num1 / num2
    #código
    print("O resultado é: ", respostas)

#Porcentagem
def porcentagem():
    #variáveis
    num1 = float(input("Digite a porcentagem (apenas o número): "))
    num2 = float(input("Digite o número: "))
    respostas = (num1 / 100) * num2
    #código
    print("O resultado é: ", respostas)

#Raiz quadrada
def raiz_quadrada():
    #importar matemática
    import math
    #variáveis
    num1 = float(input("Digite o número: "))
    respostas = math.sqrt(num1)
    #código
    print("O resultado é: ", respostas)

#Potenciação
def potenciacao():
    #variáveis
    num1 = float(input("Digite o número: "))
    num2 = float(input("Digite o expoente: "))
    respostas = num1 ** num2
    #código
    print("O resultado é: ", respostas)

#Exiba a interface gráfica