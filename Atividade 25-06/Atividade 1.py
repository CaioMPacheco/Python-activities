import os

def limpar():
    os.system("cls")

limpar()

def atividade_1(): #atividade 1
    print("Exercício 1")
    print("--------------------------------------------------------------------------------------------")
    #Variáveis:
    nomes = ["Maria", "Letícia", "Bruna", "Luca", "Vitor"]

    #Código:
    for nome in nomes: #Repetição para convidar todos
        print(f"Olá tudo bem {nome}, gostaria de te chamar para meu janter hoje á noite, te espero aqui!")
    print(" \n")
    print("Exercício 2")
    print("--------------------------------------------------------------------------------------------")

#Começo atividade 2:
    print(f"A convidada {nomes[1]} não poderá vir!") #Comando para falar que Vitor não irá
    del nomes[-1] #Comando para tirar o nome Vitor da lista.
    nomes.append("Ruan") #Comando para adicionar Ruan na lista

    for nome in nomes: #Nova repetição sem Vitor e com Ruan
        print(f"Olá tudo bem {nome}, gostaria de te chamar para meu jantar hoje á noite, te espero aqui!")

#Começo atividade 3:
    print(" \n")
    print("Exercício 3")
    print("--------------------------------------------------------------------------------------------")
    print("Consegui uma mesa maior agora posso convidar mais 3 pessoas!")
    nomes.insert(0, "Angiley") #Comando para adicionar Angiley no início da lista
    nomes.insert(4, "Victor") #Comando para adicionar Victor ao meio da lista
    nomes.append("João") #Comando para adicionar João na lista
    
    for nome in nomes: #Nova lista com novos convidados.
        print(f"Olá tudo bem {nome}, gostaria de te chamar para meu jantar hoje á noite, te espero aqui!")

#Começo atividade 4
    print(" \n")
    print("Exercício 4")
    print("--------------------------------------------------------------------------------------------")
    print("Infelizmente a mesa não chegará a tempo, poderei chamar apenas 2 pessoas.") 
    print(f"{nomes.pop(1)} infelizmente você não poderá mais vir") #Tirando Maria da lista.
    print(f"{nomes.pop(2)} infelizmente você não poderá mais vir") #Tirando Bruna da lista.
    print(f"{nomes.pop(5)} infelizmente você não poderá mais vir") #Tirando João da lista.
    print(f"{nomes.pop(3)} infelizmente você não poderá mais vir") #Tirando Luca da lista.
    print(f"{nomes.pop(0)} infelizmente você não poderá mais vir") #Tirando Angiley da lista.
    print(f"{nomes.pop(2)} infelizmente você não poderá mais vir") #Tirando Ruan da lista. 

    for nome in nomes: #Lista Nova com apenas 2 convidados
        print(f"Olá tudo bem {nome}, você está confirmado para o jantar!")
    
    del nomes[0] #Tirando Letícia da lista
    del nomes[0] #Tirando Victor da lista

    print(nomes) #Mostrando que a lista ta vazia.

atividade_1()
