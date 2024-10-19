from time import sleep
import os
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar()

#Atividade 1
def Atividade_1():
    #Variáveis
    num = int(input("De qual número você deseja a tabuada: "))
    num_tabuada = int(input("Até qual número que você quer a tabuada: "))
    
    #Código
    for numeros in range(1, num_tabuada + 1):
        print(f"{num} x {numeros} = {num * numeros}")

    
#Atividade 2
def Atividade_2():
    i =  201
    while i >= 1:
        i -= 1
        print(f"{i} segundos")
        sleep(1)


#Atividade 3
def Atividade_3():
    #Variáveis
    contagem = 0
    lista = []
    for contagem in range(101):
        if contagem % 2 != 0:
            lista.append(contagem)
            print(contagem)
    print(f"De 0 a 100 tem {len(lista)} números.")
            
def Atividade_4():
    #Entrada de valores
    numero = int(input("Digite um número inteiro positivo: "))
    #Testa se o numero é menor ou igual a 1
    if numero <= 1:
        print(F"\n {numero} não é um número primo.")
    else:
    #Teste para saber se o numero é primo
        for i in range(2, int(numero**0.5) + 1):
        #Se o número for divisível por algum número menor que ele mesmo, não é primo
            lista = []
            for i in range(1, numero + 1):
                if numero % i == 0:
                    lista.append(i)
            print(f"{numero} não é primo e tem {len(lista)} divisores.")
            break
        #Se o numero for divisivel somente por ele mesmo e 1, é primo
        else:
            print(f"O {numero} é primo.")

def Atividade_5():
    nome = input("Qual seu nome")
    print(f"Seja bem-vindo {nome} qualquer coisa estou a disposição.")

def Atividade_6():
    num = int(input("Qual numero você quer elevado ao quadrado."))
    print(f"O número {num} elevado ao quadrado é {num **2}.")

def Atividade_7():
    print("Atividade 7")
    lista = ['Ana', 'Carlos', 'Daiane', 'Fernando', 'Maria']
    print(lista)
    del lista[2]
    lista.insert(2, 'Jaime')
    print(f"Sua nova lista é {lista}\n ")
    print("Atividade 8")
    lista.append('Paulo')
    print(f"{lista}\n" )
    print("Atividade 9")
    lista.insert(2, 'Eliane')
    print(f"{lista}\n")
    print("Atividade 10")
    del lista[1]
    print(lista)
    print("Atividade 11")
    print(f"{lista[1]}, {lista[2]}, {lista[3]}")
    print(lista[-1])

def Atividade_12():
    produto1 = {'Nome':"caneta", 'preço': 'R$2.50' }
    produto2 = {'Nome':"caderno", 'preço': 'R$15.90' }
    produto3 = {'Nome':"lápis", 'preço': 'R$5.80' }
    produto4 = {'Nome':'borracha', 'preço': 'R$0.50'}
    produto5 = {'Nome': 'Clips', 'preço': 'R$1.00'}

    dicionário = {
        'produto1': produto1,
        'produto2': produto2,
        'produto3': produto3,
        'produto4': produto4,
        'produto5': produto5
    
    }   
    print(dicionário['produto1']['Nome'])
    print(dicionário['produto1']['preço'])
    

    
def Atividade_13():
    linguagens = ['C', 'JavaScript', 'Lua', 'Python']

    if 'Python' in linguagens:
        print('Sim, Python está na lista')
    else:
        print('A linguagem de programação Python não consta na lista.')

def Atividade_14():
    linguagens = {'alto nivel':"Python", 'medio nivel':'C', 'baixo nivel':'Assembly'}

    if "alto nivel" in linguagens:
        print('Sim, Python está no dicíonario')
    else:
        print('A linguagem de programação Python não consta no dicionário.')

def Atividade_15():
    filmes_lista1 = ["Oppenheimer", "2023", "Christoper Nolan"]
    filmes_lista2 = ["Django Livre", "2012", "Tarantino"]
    filme1 = {'Filme': filmes_lista1[0], "Ano":filmes_lista1[1], "Diretor":filmes_lista1[2]}
    filme2 = {'Filme': filmes_lista2[0], "Ano":filmes_lista2[1], "Diretor":filmes_lista2[2]}
    filme = input("Qual filme você deseja visualizar: (1 ou 2): ")

    if filme == '1':
        print(filme1)
    elif filme == '2':
        print(filme2)


def Atividade_16():
    nome = input("Qual seu nome completo: ")
    idade = input("Qual sua idade: ")
    sexo = input("Qual seu sexo: ")
    civil = input("Qual seu estado cívil: ")
    nacionalidade = input("Qual sua nacionalidade: ")
    faixa = float(input("Qual sua faixa de renda: "))

    dados = {"Nome":nome, "Idade":idade, "Sexo":sexo, "Estado civil":civil, "Nacionalidade":nacionalidade, "Faixa de renda":faixa}
    print(dados)

def Atividade_17():     
    pergunta1 = input("Qual o caractére se usa para fazer multiplicação em python ? ")
    if pergunta1 == "*":
        print("Resposta correta")
    else:
        print("Resposta incorreta")
    pergunta2 = input("Qual o comando usamos para definir uma função em python?  ").lower()
    if pergunta2 == "def":
        print("Resposta correta")
    else:
        print("Resposta incorreta")
    pergunta3 = input("Qual o caractére se usa para atribuir uma variável em python ? ")
    if pergunta3 == "=":
        print("Resposta correta")
    else:
        print("Resposta incorreta")
     
def Atividade_18():
    def funcao():
        print("Atividade 18")
        #Atividade 19
        funcao1 = "Caetanopolis"
        print("Atividade 20")
        print(funcao1)
    funcao()

Atividade = (input("Qual atividade você deseja visualizar: "))

if Atividade == "1":
    Atividade_1()
elif Atividade == "2":
    Atividade_2()
elif Atividade == "3":
    Atividade_3()
elif Atividade == "4":
    Atividade_4()
elif Atividade == "5":
    Atividade_5()
elif Atividade == "6":
    Atividade_6()
elif Atividade == "7":
    Atividade_7()
elif Atividade == '12':
    Atividade_12()
elif Atividade == '13':
    Atividade_13()
elif Atividade == '14':
    Atividade_14()
elif Atividade == '15':
   Atividade_15()
elif Atividade == '16':
    Atividade_16()
elif Atividade == '17':
   Atividade_17()
elif Atividade == '18':
    Atividade_18()