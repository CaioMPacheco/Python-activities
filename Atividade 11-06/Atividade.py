 #importar matemática
import math
import os

#limpar a tela
def limpar():
    os.system('cls')
limpar()

#Atividade 1
def ativiade_1():
    #Variáveis
    primeiro_número = float(input("Qual o primeiro número: "))
    segundo_número = float(input("Qual o segundo número: "))

    #Código
    if primeiro_número > segundo_número:
        print(f"O {primeiro_número} é maior do que o {segundo_número} !")
    elif segundo_número > primeiro_número:
        print(f"O {segundo_número} é maior do que o {primeiro_número} !")
    else:
        print(f"Os números {primeiro_número} e {segundo_número} são iguais")

def atividade_2():
    #Variáveis
    import math
    número = float(input("Digite um número: "))

    #Código
    if número > 0:
        print(f"O número {número} é positivo e a sua raiz é {número ** 0.5:.2f} !")
    else:
        print(f"O número {número} é negativo, então é inválido")

def atividade_3():
    #Variáveis
    número = float(input("Digite um número: "))
    número_ao_quadrado = número ** 2

    #Código
    if número > 0:
        print(f"O número {número} é positivo e a sua raiz é {número ** 0.5:.2f}!")
    elif número < 0:
        print(f"O número {número} é negativo e ele ao quadrado é igual a -{número_ao_quadrado}")

def atividade_4():
    #Variáveis
    número = float(input("Digite um número: "))
    número_ao_quadrado = número ** 2

    #Código
    if número > 0:
        print(f"O número {número} é positivo e a sua raiz é {número ** 0.5:.2f} e ele elevado ao quadrado é {número_ao_quadrado}")
    else:
        print(f"O número {número} é inválido")

def atividade_5():
    #Variáveis
    número = int(input("Digite um número: "))
    
    #Código
    if número % 2 == 0:
        print(f"O número {número} é par")
    else:
        print(f"O número {número} é ímpar")

#Menu de escolha

print("--------------------------------------------------------------------------")
print("                               EXERCÍCIOS                                 ")
print("                             By:Caio Pacheco                              ")
print("--------------------------------------------------------------------------")

print("╔═══════════════════════════════════════════════════════════════════════════════════╗\n"
      "║              Escolha o exercício que deseja                                       ║\n"
      "║                                                                                   ║\n"
      "║ 1 - Exercício 1: Saber qual número entre dois é maior                             ║\n"
      "║ 2 - Exercício 2: Saber raiz quadrada de um número positivo                        ║\n"
      "║ 3 - Exercício 3: Saber raiz quadrada do número positivo e o quadrado do negativo  ║\n"
      "║ 4 - Exercício 4: Saber raiz quadrada e quadrado do número positivo                ║\n"
      "║ 5 - Exercício 5: Saber se é impar ou par                                          ║\n"
      "╚═══════════════════════════════════════════════════════════════════════════════════╝")

#variável para escolher exercício
exercício = input("Qual exercício você quer: ")
limpar()

if exercício == "1":
    ativiade_1()
elif exercício == "2":
    atividade_2()
elif exercício == "3":
    atividade_3()
elif exercício == "4":
    atividade_4()
elif exercício == "5":
    atividade_5()