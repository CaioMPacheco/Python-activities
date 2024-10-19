import os

def limpar():
    os.system("cls")

limpar() # Limpar tela

#Atividade 1
def atividade_1():
    #Variáveis
    pergunta_1 = input("Você telefonou para a vítima?  (S/N): ").lower().strip()
    pergunta_2 = input("Esteve no local do crime?  (S/N): ").lower().strip()
    pergunta_3 = input("Mora perto da vítima?  (S/ N): ").lower().strip()
    pergunta_4 = input("Devia para a vítima?  (S/N) : ").lower().strip()
    pergunta_5 = input("Já trabalhou com a vítima?  (S/N): ").lower().strip()
    crimes = [pergunta_1, pergunta_2, pergunta_3, pergunta_4, pergunta_5]
    contar = crimes.count("s")
    #Código
    if contar == 2:
        print("Suspeito!")
    elif contar >= 3 and contar <= 4:
        print("Cúmplice!")
    elif contar == 5:
        print("Assasino!")
    else:
        print("Inocente!")

#Atividade 2
def atividade_2():
    #Variáveis
    valor_nota = 0
    notas = [ ]
    #Código
    while not valor_nota <= -1:
        valor_nota = float(input("Digite o valor da nota ou digite -1 ou um número menor que 0 para parar: "))
        notas.append(valor_nota)
    del notas[-1]
    print(" \n")
    print(f"Você digitou {len(notas)} notas")
    print(f"Sendo elas: {notas}")
    print(" \n")
    quantidade = len(notas)
    print(f"Ao contrário é: ")
    for nota in range(quantidade -1, -1, -1): 
        print(notas[nota])
    print(" \n")
    soma = sum(notas)
    print(f"A soma das notas é: {soma}")
    print(" \n")
    media = soma / quantidade
    print(f"A média das notas é: {media}")
    print(" \n")
    if quantidade > 0:
        media = soma / quantidade
    else:
        media = 0
    acima_média = sum(1 for nota in notas if nota > media)
    abaixo_média = sum(1 for nota in notas if nota < media )
    
    print(f"Quantidade de notas acima da média: {acima_média}\n")
    print(f"Quantidade de notas abaixo da média: {abaixo_média}\n")

    print("Obrigado por usar o programa!")

def atividade_3():
    numeros_por_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
    'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 
    'dezoito', 'dezenove', 'vinte', 'vinte e um', 'vinte e dois', 'vinte e três', 
    'vinte e quatro', 'vinte e cinco', 'vinte e seis', 'vinte e sete', 'vinte e oito', 
    'vinte e nove', 'trinta', 'trinta e um', 'trinta e dois', 'trinta e três', 
    'trinta e quatro', 'trinta e cinco', 'trinta e seis', 'trinta e sete', 
    'trinta e oito', 'trinta e nove', 'quarenta'
    )

    # Solicitando um número ao usuário
    numero = int(input("Digite um número entre 0 e 40: "))

    # Verificando se o número está dentro do intervalo válido
    if 0 <= numero <= 40:
    # Imprimindo o número por extenso
        print(f"O número {numero} por extenso é: {numeros_por_extenso[numero]}")
    else:
        print("Número fora do intervalo válido.")

def atividade_4():
    #Intervalos
    intervalos = [299, 399, 499, 599, 699, 799, 899, 999]

    #salários
    salarios = [0] * (len(intervalos) + 1)  # +1 para o intervalo "R$1000 em diante"

    #input vendedores
    vendedores = int(input("Digite o número de vendedores: "))

    #Laço de repetiçãp
    for i in range(vendedores):
        vendas = float(input("Digite as vendas do vendedor {}: ".format(i + 1)))
        salario = 200 + (vendas * 0.09)

        #loop
        for a in range(len(intervalos)):
            if salario < 200 + intervalos[a]:
                salarios[a] += 1
                break
        else:
            salarios[-1] += 1

    #Código

    print("Salários:")
    print("R$200 - R$", 200 + intervalos[0], ":", salarios[0])
    for i in range(1, len(intervalos)):
        print("R$", 200 + intervalos[i-1] + 1, "- R$", 200 + intervalos[i], ":", salarios[i])
    print("R$1000 em diante:", salarios[-1])

    print("Salários:")
    print("R$200 - R$299:", salarios[0])
    print("R$300 - R$399:", salarios[1])
    print("R$400 - R$499:", salarios[2])
    print("R$500 - R$599:", salarios[3])
    print("R$600 - R$699:", salarios[4])
    print("R$700 - R$799:", salarios[5])
    print("R$800 - R$899:", salarios[6])
    print("R$900 - R$999:", salarios[7])
    print("R$1000 em diante:", salarios[8])


def atividade_5():
    times = ("Flamengo", " Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", "Atlético-MG", "Internacional", "Fluminense", "Botafogo", "Vasco", "Bahia", "Goiás", "Atlético-PR", "Sport", "Chapecoense", "Ceará", "Fortaleza", "Avaí", "CSA")
    print("Os 5 primeiros colocados:", times[:5])
    print("Os últimos 4 colocados:", times[-4:])
    print("Times em ordem alfabética:", sorted(times))
    print("Posição do São Paulo:", times.index("São Paulo") + 1)


def atividade_6():
    import random

    numeros = tuple(random.randint(1, 100) for _ in range(5))
    print("Números gerados:", numeros)
    print("Menor número:", min(numeros))
    print("Maior número:", max(numeros))


def atividade_7():
    carros = ["FUSCA", "GOL", "VECTRA", "PALIO", "UNO"]
    consumo = [10, 12, 15, 11, 13]

    print("Carro mais econômico:", carros[consumo.index(min(consumo))])
    for i, carro in enumerate(carros):
        litros = 1000 / consumo[i]
        custo = litros * 5.50
        print("Carro {}: {} km/l, {} litros para 1000 km, R$ {:.2f}".format(carro, consumo[i], litros, custo))


def atividade_8():
    valores = tuple(int(input("Digite um valor: ")) for _ in range(4))
    print("Quantas vezes apareceu o valor 9:", valores.count(9))
    print("Posição do valor 1:", valores.index(1) + 1 if 1 in valores else "Não encontrado")
    print("Números pares:", [valor for valor in valores if valor % 2 == 0])


def atividade_9():
    numeros = []
    while True:
        numero = int(input("Digite um número (-1 para sair): "))
        if numero == -1:
            break
        numeros.append(numero)

    print("Quantos números foram digitados:", len(numeros))
    print("Lista ordenada de forma decrescente:", sorted(numeros, reverse=True))
    print("Valor 2 foi digitado e está na lista:", 2 in numeros)


def atividade_10():
    numeros = []
    for i in range(5):
        numero = int(input("Digite um número: "))
        numeros.append(numero)
        for j in range(i - 1, -1, -1):
            if numeros[j] > numero:
                numeros[j + 1] = numeros[j]
                numeros[j] = numero
                break
        else:
            numeros[0] = numero

    print("Lista ordenada:", numeros)




