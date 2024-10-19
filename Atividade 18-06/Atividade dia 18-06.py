'''1- Crie um programa que leia um nome completo de uma pessoa e mostra na tela:

a) O nome com todas letras malúsculas

b) O nome com todas as letras minusculas

c) Quantas letras ao todo. "Sen considerar os espacos".

d) Quantas letras tem apenas o primerio nome.

2- Faça um programa que leia um número de 0  à 9.999 e mostre na tela cada um dos digitos separados:

Exemplo: 1328

Unidade: 8

Dezena: 2

Centena: 3

Milhar: 1

OBS: Use a string e faça outro usando a matematica.

3-CRIE UM PROGRAMA que LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM O NOME "SANTO

4-CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA & DIGA SE ELA TÊM. "SILVA" NO NOME

5- FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:

a) QUANTAS VEZES APARECE A LETRA A.

b) Em qual posição ELA APARECE PELA PRIMEIRA VEZ.

c) Em QUAL POSIÇÃO ELA APARECE PELA ULTIMA VEZ.
6-Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o último nome separadamente.

Exemplo:
Entrada: ANGILEY JOSE DE MOURA
Saída: Primeiro nome: ANGILEY
       Último nome: MOURA
7-Faça um programa que gere um número aleatório e apresente na tela em que faixa de números ele se encontra.

Exemplo de faixas:
0 - 333
334 - 666
667 - 999
> 999 - Imprime "ERRO"'''

import os
def limpar():
    os.system('cls')
limpar()

#Atividade 1
def atividade_1():
    #Variáveis
    nome_completo = input("Digite seu nome completo: ")
    nome_maiusculo = nome_completo.upper()#a)
    nomem_inusculo = nome_completo.lower()#b)
    letras_totais = len(nome_completo.replace(" ", "")) #c)
    primeiro_nome = nome_completo.split()[0] 
    letras_primeiro = len(primeiro_nome)#d)

    #Código
    print(f"a) O nome em maiúsculo é: {nome_maiusculo}.")
    print("------------------------------------------------------")
    print(f"b) O nome em minúsculo é: {nomem_inusculo}.")
    print("------------------------------------------------------")
    print(f"c) O total de letras é: {letras_totais}.")
    print("------------------------------------------------------")
    print(f"d) O primeiro nome é: {primeiro_nome} e tem {letras_primeiro} letras.")
    print("------------------------------------------------------")

#Atividade 2
def atividade_2():
    #Variáveis
    número = int(input("Digite um número entre 0 e 9.999: "))
    #Código matemática
    if número < 0 or número > 9999:
        print("Não é possível fazer com este número")
    else:
        print("Código com matemática")
        unidade = número % 10
        dezena = (número // 10) % 10
        centena = (número // 100) % 10
        milhar = (número // 1000) % 10

        print(f"Unidade: {unidade}")
        print(f"Dezena: {dezena}")
        print(f"Centena: {centena}")
        print(f"Milhar: {milhar}")
    #Código string
    #variáveis
        print("Código com string")
        número_str = str(número)
        unidade_str = número_str[0:1]
        dezena_str = número_str[1:2]
        centena_str = número_str[2:3]
        milhar_str = número_str[3:4]
        #código
        print(f"Unidade: {unidade_str}")
        print(f"Dezena: {dezena_str}")
        print(f"Centena: {centena_str}")
        print(f"Milhar: {milhar_str}")

def atividade_3():
    #Variáveis
    nome_cidade = input("Digite o nome da cidade: ").capitalize()
    #Código
    if nome_cidade[:5] == "Santo":
        print("Começa com Santo!")
    else:
        print("Não começa com Santo!")

def atividade_4():
    #Variáveis
    nome_pessoa = input("Digite seu nome completo: ")
    #Código
    if "silva" in nome_pessoa.lower():
        print("Seu nome tem Silva!")
    else:
        print("Seu nome não tem Silva!")

def atividade_5():
    #Variáveis
    frase = input("Digite uma frase: ").strip()
    As = ['á', 'ã', 'à', 'â', 'À', 'Â', 'Ã', 'Á', 'A']

    for letra in As:
        frase = frase.replace(letra, 'a')

    contar_a = frase.lower().count('a')
    #Código
    print(f"A frase tem {contar_a} A ou a!")

    primeiro = frase.lower().find('a')
    print(f"A primeira letra 'a' aparece na posição {primeiro + 1}.")

    ultima_posicao = frase.lower().rfind('a')
    print(f"A última letra 'a' aparece na posição {ultima_posicao +1 }.")

def atividade_6():
    #Variáveis
    nome = input("Qual o seu nome : ")
    primeiro_nome = nome.split()[0]
    ultimo_nome = nome.split()[-1]

    #Código
    print(f"Seu primeiro nome é {primeiro_nome} e o seu último nome é {ultimo_nome}")

def atividade_7():
    #Variáveis
    import random
    número_aleatório = random.randint(0, 1500)
    #Código
    if número_aleatório <= 333:
        print("Ele está na faixa entre 0 e 333")
    elif número_aleatório <= 666 and número_aleatório > 333:
        print("Ele está na faixa entre 334 e 666")
    elif número_aleatório <= 999 and número_aleatório > 666:
        print("Ele está na faixa entre 667 e 999")
    elif número_aleatório > 999:
        print("ERROR - O número é maior que 999")  