import os
def limpar():
    os.system('cls')

#Atividade 1
def atividade_1():
    #Variáveis
        ordem = input("Digite apenas notas de 0 a 10.\nAperte ENTER para continuar")
        número1 = int(input("Qual a primeira nota :"))
        número2 = int(input("Qual a segunda nota :"))
        número3 = int(input('Qual a terceira nota :'))
        media = (número1 + número2 + número3)/3

        #Código
        if media >= 7:
            print(f"Sua média é {media}, parabéns você foi aprovado!")
        else:
            print(f"Sua média foi {media}, você reprovou, estude mais na próxima!")

def atividade_2():
    #Variáveis
    celsius = float(input("Digite a temperatura em celsius: "))
    fahrenheit = (celsius * 1,8) + 32

    #Código
    print(f"A temperatura {celsius} em Fahrenheit é {fahrenheit}")

def atividade_3():
    #Variaveis
      numero = int(input("Qual número você deseja conferir se é positivo, negativo ou zero: "))
    #Código
      if numero == 0:
        print(f"O número {numero} é igual a zero.")
      elif numero > 0:
        print(f"O número {numero} é positivo.")
      else:
        print(f"O número {numero} é negativo.")

def atividade_4():
    #Variaveis        
        salario = float(input("Qual seu salário atual: "))
        aumento = float(input("Qual o valor do seu aumento: "))    
    #Código
        print(f"Seu novo salário é igual a R${salario+aumento:.2f}.")

def Atividade5():
#Variaveis
    idade = int(input("Qual sua idade: "))
#Código
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

def Atividade6():
#Variaveis
    primeiro_valor = float(input("Qual o 1º valor: "))
    segundo_valor = float(input("Qual o 2º valor: "))
    terceiro_valor = float(input("Qual o 3º valor: "))
#Código
    print(f"O maior valor dentre {primeiro_valor}, {segundo_valor} e {terceiro_valor} é igual a {max(primeiro_valor, segundo_valor, terceiro_valor)}") 

def Atividade7():
#Variaveis
    peso = float(input("Qual seu peso em Kgs: "))
    altura = float(input("Qual sua altura em Metros: "))
    imc = peso / (altura ** 2)
#Código
    if imc < 18.5:
        print(f"Seu imc é {imc:.2f} portanto você está abaixo do peso.")
    elif imc <= 24.9:
        print(f"Seu imc é {imc:.2f} portanto você está em um peso normal.")  
    elif imc <= 29.9:
        print(f"Seu imc é {imc:.2f} portanto você está em sobrepeso.")  
    elif imc <= 39.9:
        print(f"Seu imc é {imc:.2f} portanto você está em estado de obesidade.")  
    else:
        print(f"Seu imc é {imc:.2f} portanto você está em estado de obesidade mórbida.")  

def Atividade8():
#Variaveis
    numero = int(input("Qual o 1º valor: "))
    numero2 = int(input("Qual o 1º valor: "))
#Código
    print(f"A adição é igual a {numero + numero2}\nA subtração é igual a {numero - numero2}\n"
    "A divisão é igual a {numero/numero2}\nA multiplicação é igual a {numero * numero2}")

def Atividade9():
#Variaveis
    idade = int(input("Qual a sua idade: "))
#Código
    if idade <= 2:
        print(f"Você tem {idade} anos de idade, portanto é um bebê.")
    elif idade <= 12:
        print(f"Você tem {idade} anos de idade, portanto é um criança.")
    elif idade <= 17:
        print(f"Você tem {idade} anos de idade, portanto é um adolescente.")
    elif idade <= 64:
        print(f"Você tem {idade} anos de idade, portanto é um adulto.")
    elif idade > 64:
        print(f"Você tem {idade} anos de idade, portanto é um idoso.")
    else:
        print("Coloque o valor em números")

def Atividade10():
#Variaveis
    lado1 = float(input("Qual a medida do 1º lado: "))
    lado2 = float(input("Qual a medida do 2º lado: "))
    lado3 = float(input("Qual a medida do 3º lado: "))
#Código
    if lado1 == lado2 == lado3:
        print(f"Este triângulo é um triângulo equilatero.")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print(f"Este triângulo é um triângulo isósceles.")
    elif lado1 < 0 or lado2 < 0 or lado3 < 0:
        print("Não é possível fazer um triângulo com estes valores.")
    else:
        print("Este triângulo é um triângulo escaleno.")

def Atividade11():
#Variaveis
    preco = float(input("Qual o preço do produto: "))
    desconto = float(input("Quantos % será descontado do produto: "))
    porcentagem = (desconto / 100) * preco
#Código
    print(f"O novo valor deste produto é igual a {preco - porcentagem}")

def Atividade12():
#Variaveis
    nome1 = input("QuaL o nome da primeira pessoa: ").capitalize()
    idade1 = int(input(f"Qual a idade de {nome1}: "))
    nome2 = input("QuaL o nome da segunda pessoa: ").capitalize()
    idade2 = int(input(f"Qual a idade de {nome2}: "))
#Código
    if idade1 > idade2:
        print(f"{nome1} é mais velho doque {nome2}.")
    else:
        print(f"{nome2} é mais velho doque {nome1}.")

def Atividade13():
#Variaveis
    valor_pago = float(input("Qual o valor pago pelo cliente: "))
    valor_do_produto = float(input("Qual o valor do produto: "))
#Código
    print(f"O troco do cliente é R${valor_pago - valor_do_produto:.2f}")