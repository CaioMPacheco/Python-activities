import os
def limpar():
    os.system('cls')
limpar()

def atividade_1():
    # X para sair
    while True:
        sair = input("Digite um número ou aperte 'x' para encerrar): ")
        if sair.lower() == 'x':
            print("Programa encerrado.")
            break
        #Variável número
        número = float(sair)

        #Código
        if número > 0:
            print(f"O número {número} é positivo.")
        elif número < 0:
            print(f"O número {número} é negativo.")
        else:
            print(f"O número {número} é zero.")
atividade_1()

def atividade_2():
     # X para sair
    while True:
        sair = input("Digite um número ou aperte 'x' para encerrar: ")
        if sair.lower() == 'x':
            print("Programa encerrado.")
            break
        #Variável número
        número = int(sair)

        #Código
        if número % 2 == 0:
            print(f"O número {número} é par")
        else:
            print(f"O número {número} é ímpar")
atividade_2()

def atividade_3():
    #Variáveis
    soma = 0
    for i in range(1, 101):
        soma += i 
    #Código
    print(f"A soma dos números de 1 a 100 é: {soma}")
atividade_3()

def atividade_4():
    #Variáveis
    número = int(input("Digite um número: "))
    #Código
    if número % 2 == 0:
            print(f"O número {número} é par")
            print(f"E os 5 primeiros números ímpares são {primeiros_impar} ")
    else:
            print(f"O número {número} é ímpar")
            print(f"E os 5 primeiros números ímpares são {primeiros_impar} ")
atividade_4()

def atividade_5():
    #variáveis
    valor_1 = int(input("Qual o primeiro número :"))
    valor_2 = int(input("Qual o segundo número :"))
    valor_3 = int(input("Qual o terceiro número :"))

    #código
    if valor_1 >= valor_2 >= valor_3:
        print(f"O menor número é o {valor_3}")
        for i  in range(1, valor_3 + 1):
            if i % 2 == 0:
                print(f"{i} é par!")
            else:
                print(f"{i} é ímpar!")
    elif valor_1 >= valor_3 >= valor_2:
        print(f"O menor número é o {valor_2}")
        for i  in range(1, valor_2 + 1):
            if i % 2 == 0:
                print(f"{i} é par!")
            else:
                print(f"{i} é ímpar!")
    elif valor_2 >= valor_1 >= valor_3:
        print(f"O menor número é o {valor_3}")
        for i  in range(1, valor_3 + 1):
            if i % 2 == 0:
                print(f"{i} é par!")
            else:
                print(f"{i} é ímpar!")
    elif valor_2 >= valor_3 >= valor_1:
        print(f"O menor número é o {valor_1}")
        for i  in range(1, valor_1 + 1):
            if i % 2 == 0:
                print(f"{i} é par!")
            else:
                print(f"{i} é ímpar!")
    elif valor_3 >= valor_2 >= valor_1:
        print(f"O menor número é o {valor_1}")
        for i  in range(1, valor_1 + 1):
            if i % 2 == 0:
                print(f"{i} é par!")
            else:
                print(f"{i} é ímpar!")
    elif valor_3 >= valor_1 >= valor_2:
        print(f"O menor número é o {valor_2}")
        for i  in range(1, valor_2 + 1):
            if i % 2 == 0:
                print(f"{i} é par!")
            else:
                print(f"{i} é ímpar!")
atividade_5()

def atividade_6():
    #Variáveis
    número_1 = int(input("Digite o primeiro número: "))
    número_2 = int(input("Digite o segundo número: "))
    soma = 0
    #Código
    if número_1 > número_2:
        número_1, número_2 = número_2, número_1
    for i in range(número_1, número_2 + 1):
        if i % 2 == 0:
            print(f"{i}")
            soma += i

    print(f"A soma desses números é {soma}")
atividade_6()

def atividade_7():
    #Variáveis
    soma = 0
    for i in range(1, 101):
        if i % 2 != 0:
            soma += i
    print(f"A soma dos números ímpares de 0 a 100 é {soma}")
atividade_7()

def atividade_8():
    #Variáveis
    nome = str(input("Por favor digite um apelido para você: "))
    número = len(nome) * 3
    certo = False
    Tentativa = 0

    #Código
    print("Por favor tente adivinha um número de 1 a 100")
    while not certo:
        chute = int(input("Digite o número: "))
        Tentativa += 1

        if número > 100:
            (número - número) + 49
        
        if chute == número:
            print(f"Parabéns você acertou, o número secreto era {número} e você utilizou {Tentativa} tentativas")
            print("Se quiser jogar novamente, use outro apelido!")
            certo = True
        elif chute > número:
            print("O número secreto é menor. ")
        elif chute < número:
            print("O número secreto é maior. ")
atividade_8()

def atividade_9():
    #Código
    while True:
        aperte_x = input("Aperte X para parar o processamento: ")
        if aperte_x == 'x':
            print("Você parou o processo!")
            break
        else:
            aperte_x
atividade_9()

def atividade_10():
    #Variáveis
    nome = str(input("Por favor digite seu nome completo: "))
    vogais = "aeiouAEIOU"
    contar_vogais = 0
    contar_consoante = 0

    #Código
    for i in nome:
        if i.isalpha():
            if i in vogais:
                contar_vogais += 1
            else:
                contar_consoante += 1
    
    letras = (contar_consoante + contar_vogais) 

    print(f"Seu nome completo tem {letras} letras, sendo elas {contar_vogais} vogais e {contar_consoante} consoantes!!")
atividade_10()