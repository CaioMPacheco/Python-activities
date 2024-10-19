import os
def limpar():
    os.system('cls')

limpar()

#Atividade 1
def atividade_1():
    #variáveis
    pergunta_letra = input("Digite uma letra para saber se é vogal ou consoante: ")

    #código
    if pergunta_letra == "a" or "A":
        print(f"A letra {pergunta_letra} é uma vogal!")
    elif pergunta_letra == "e" or "E":
        print(f"A letra {pergunta_letra} é uma vogal!")
    elif pergunta_letra == "i" or "I":
        print(f"A letra {pergunta_letra} é uma vogal!")
    elif pergunta_letra == "o" or "O":
        print(f"A letra {pergunta_letra} é uma vogal!")
    elif pergunta_letra == "u" or "U":
        print(f"A letra {pergunta_letra} é uma vogal!")  
    else:
        print(f"A letra {pergunta_letra} é uma consoante!")

def atividade_2():
    #variáveis
    valor_1 = int(input("Qual o primeiro número :"))
    valor_2 = int(input("Qual o segundo número :"))
    valor_3 = int(input("Qual o terceiro número :"))

    #código
    if valor_1 > valor_2 and valor_1 > valor_3:
        print (f"O maior número é {valor_1}")
    elif valor_1 < valor_2 and valor_2 > valor_3:
        print (f"O maior número é {valor_2}")
    elif valor_1 < valor_3 and valor_2 < valor_3:
        print (f"O maior número é {valor_3}")
    elif valor_1 == valor_2 and valor_2 == valor_3:
        print ("Esses número são iguais !")
    elif valor_1 == valor_2 or valor_2 == valor_3 or valor_1 == valor_3:
        print ("Existem caractéres iguais !")
    else:
        print ("Não é possível fazer operação com esse caracter!")

def atividade_3():
    #variáveis
    valor_1 = int(input("Qual o primeiro número :"))
    valor_2 = int(input("Qual o segundo número :"))
    valor_3 = int(input("Qual o terceiro número :"))

    #código
    if valor_1 >= valor_2 >= valor_3:
        print(f"O maior número é {valor_1} e o menor número é o {valor_3}")
    elif valor_1 >= valor_3 >= valor_2:
        print(f"O maior número é {valor_1} e o menor número é o {valor_2}")
    elif valor_2 >= valor_1 >= valor_3:
        print(f"O maior número é {valor_2} e o menor número é o {valor_3}")
    elif valor_2 >= valor_2 >= valor_1:
        print(f"O maior número é {valor_2} e o menor número é o {valor_1}")
    elif valor_3 >= valor_2 >= valor_1:
        print(f"O maior número é {valor_3} e o menor número é o {valor_1}")
    elif valor_3 >= valor_1 >= valor_2:
        print(f"O maior número é {valor_3} e o menor número é o {valor_2}")
        
def atividade_4():
    #variáveis
    valor_1 = int(input("Qual o primeiro número :"))
    valor_2 = int(input("Qual o segundo número :"))
    troca = valor_1
    valor_1 = valor_2
    valor_2 = troca

    #código
    print(f"O valor da primeira varíavel agora é {valor_1}\nE a segunda variável agora é {valor_2}")

atividade_3()