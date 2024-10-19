import os
def limpar():
    os.system('cls')

limpar()
#Exercício 1
#Variáveis
def exercício_1():
    a = float(input("Qual o valor de a? : "))
    b = float(input("Qual o valor de b? : "))
    c = float(input("Qual o valor de c? : "))
    soma = a + b + c
    #Operação

    if soma <= c :
        print(f"O valor da soma é {soma} e ela é menor do que o valor de {c}")
    else:
        print(f"O valor da soma é {soma} e é maior do que {c}")

#Exercício 2
#Variáveis
def exercício_2():
    a = int(input("Qual o valor de a? : "))
    b = int(input("Qual o valor de b? : "))
    soma = a + b
    multiplicação = a * b

    #Operação

    if a == b:
        c = soma
        print(f"O valor da soma é {c}")
    else:
        c = multiplicação
        print(f"O valor da multiplicação é {c}")

#Exercício 3
#Variáveis
def exercício_3():
    número = int(input("Qual o número que você quer saber sucessor e antecessor? : "))
    antecessor = número - 1
    sucessor = número + 1

    print(f"O antecessor é {antecessor}.\nO sucessor é {sucessor}.")

#Exercício 4
#Variáveis
def exercício_4():
    salário = float(input("Qual o seu salário?: "))
    salário_mínimo = 1293.20
    valor_final = salário/salário_mínimo
    if salário < 0 :
        print("Impossível fazer essa conta!")
    
    else:
        print(f"Você recebe {valor_final:.2f} salários mínimos")

#Exercício 5
#Variáveis
def exercício_5():
    número = float(input("Qual o número :"))
    desconto = 5/100 * número
    final = número - desconto

    if número < 0:
        print("Impossível fazer sua operação!")

    elif desconto == 0:
        print(f"O final é {número}.")
    elif desconto < 0:
        print("Impossível fazer sua operação!")
    else:
        print(f"O final é {final}.")

#Exercício 6
#Variáveis
def exercício_6():
    número1 = int(input("Qual o primeiro número"))
    número2 = int(input("Qual o segundo número"))
    
    if número1 > número2 :
        print(f"{número1} é maior do que {número2}")
    elif número1 == número2:
        print(f"Os dois são iguais")
    else:
        print(f"{número2} é maior do que {número1}")

#Exercício 7
#Variáveis
def exercício_7():
    while True:
        número1 = int(input("Qual o primeiro número :"))
        número2 = int(input("Qual o segundo número :"))
        número3 = int(input('Qual o terceiro número :'))

        #Código
        if número1 == número2 or número2 == número3 or número3 == número1 :
            print("Não é possível fazer está operação com número negativos!")
            input("Aperte ENTER para tentar novamente!")
            limpar()
            break
        else:
            valores = [número1, número2, número3]
            valores.sort(reverse=True)
            print("Os valores em ordem decrescente são : ")
            #colocoar em uma lista que irá ficar um abaixo do outro.
            for lista in valores:
                print(lista)


#Exercício 8
def exercício_8():
        #Variáveis
        número1 = int(input("Qual o primeiro número :"))
        número2 = int(input("Qual o segundo número :"))
        número3 = int(input('Qual o terceiro número :'))
        media = (número1 + número2 + número3)/3

    
        #Código
        if número1 == número2 or número2 == número3 or número3 == número1 :
            print(f"A sua média é: {número1}")
            input("Aperte ENTER para voltar")
            limpar()
        else:
            print(f"Sua média é {media}")
            input("Aperte ENTER para voltar")
            
#Exercício 9
def exercício_9():
        #Variáveis
        número = int(input("Qual o número que você quer o fatorial :"))
        resultado = 1

        #Código
        for fatorial in range(1, número + 1):
            resultado *= fatorial
        if número < 0 :
            print("Impossível fazer com um número negativo!")
            input("aperte Enter para voltar")
            limpar()
        else:
            print(f"{número} em fatorial é : {resultado}")

def exercício_10():
    #Entrada de valores
    numero = int(input("Digite um número inteiro positivo: "))
    #Testa se o numero é menor ou igual a 1
    if numero <= 1:
        print(F"\n {numero} não é um número primo.")
    else:
    #Teste para saber se o numero é primo
     for i in range(2, int(numero**0.5) + 1):
        #Se o número for divisível por algum número menor que ele mesmo, não é primo
        if numero % i == 0:
            print(f"{numero} não é primo.")
            break
        #Se o numero for divisivel somente por ele mesmo e 1, é primo
     else:
        print(f"{numero} é primo.")

#Menu de escolha
print("--------------------------------------------------------------------------")
print("                               EXERCÍCIOS                                 ")
print("                             By:Caio Pacheco                              ")
print("--------------------------------------------------------------------------")

print("╔═══════════════════════════════════════════════════════════════╗\n"
      "║              Escolha o exercício que deseja                   ║\n"
      "║                                                               ║\n"
      "║ 1 - Exercício 1: Soma de A e B e comparação com C             ║\n"
      "║ 2 - Exercício 2: Soma se A e B forem iguais, senão multiplica ║\n"
      "║ 3 - Exercício 3: Antecessor e sucessor de um número           ║\n"
      "║ 4 - Exercício 4: Quantos salários mínimos um usuário ganha    ║\n"
      "║ 5 - Exercício 5: Reajuste de valor com 5%                     ║\n"
      "║ 6 - Exercício 6: Identificar qual número é maior              ║\n"
      "║ 7 - Exercício 7: Ordenar três números em ordem decrescente    ║\n"
      "║ 8 - Exercício 8: Média aritmética de três números             ║\n"
      "║ 9 - Exercício 9: Cálculo do fatorial de um número             ║\n"
      "║ 10 - Exercício 10: Verificar se um número é primo             ║\n"
      "╚═══════════════════════════════════════════════════════════════╝")

#variável para escolher exercício
exercício = input("Qual exercício você quer: ")
limpar()

if exercício == "1":
    exercício_1()
elif exercício == "2":
    exercício_2()
elif exercício == "3":
    exercício_3()
elif exercício == "4":
    exercício_4()
elif exercício == "5":
    exercício_5()
elif exercício == "6":
    exercício_6()
elif exercício == "7":
    exercício_7()
elif exercício == "8":
    exercício_8()
elif exercício == "9":
    exercício_9()
elif exercício == "10":
    exercício_10()
