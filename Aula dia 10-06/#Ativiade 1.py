import os
def limpar():
    os.system('cls')

#Ativiade 1
def atividade_1():
    #Variáveis
    distancia = float(input("Quantos quilômetros foram rodados?"))
    valor_total = (distancia * 2.70) + 5.90

    #Código
    print("O valor total da corrida é de R$ {:.2f}".format(valor_total))

#Atividade 2
def atividade_2():
    #Variáveis
    velocidade_carro = float(input("Qual era a velocidade do carro?"))
    multa = 50 + (velocidade_carro - 100) * 8

    #Código
    if velocidade_carro > 100:
        print(f"Você foi multado em R$ {multa} por ultrapassar {velocidade_carro - 100} KM do permitido")
    else:
        print("Você não foi multado")

#Atividade 3
def atividade_3():
    #Variáveis
    ano_pergunta = int(input("Qual o ano que você quer saber se é bissexto: "))
    bissexto = ano_pergunta % 4 and ano_pergunta % 400

    #Código
    if bissexto == 0:
        print(f"O ano {ano_pergunta} é bissexto")
    else:
        print(f"O ano {ano_pergunta} não é bissexto")

#Atividade 4
def atividade_4():
    #Variáveis
    salário = float(input("Qual o salário: "))
    aumento_15 = salário * 0.15 + salário
    aumento_30 = salário * 0.3 + salário

    #Código
    if salário > 1420:
        print(f"Seu novo salário será de R${aumento_15:.2f}")
    else:
        print(f"Seu novo salário é de R${aumento_30:.2f}")


#Menu de escolha
print("--------------------------------------------------------------------------")
print("                               EXERCÍCIOS                                 ")
print("                             By:Caio Pacheco                              ")
print("--------------------------------------------------------------------------")

print("╔═══════════════════════════════════════════════════════════════╗\n"
      "║              Escolha o exercício que deseja                   ║\n"
      "║                                                               ║\n"
      "║ 1 - Exercício 1: Saber preço da corrida de taxi               ║\n"
      "║ 2 - Exercício 2: Saber se o carro foi multado ou não          ║\n"
      "║ 3 - Exercício 3: Saber se o ano é bissexto                    ║\n"
      "║ 4 - Exercício 4: Saber quanto de aumento recebeu              ║\n"
      "╚═══════════════════════════════════════════════════════════════╝")

#variável para escolher exercício
exercício = input("Qual exercício você quer: ")
limpar()

if exercício == "1":
    atividade_1()
elif exercício == "2":
    atividade_2()
elif exercício == "3":
    atividade_3()
elif exercício == "4":
    atividade_4()