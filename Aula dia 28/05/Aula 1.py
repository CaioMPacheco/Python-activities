#Código para limpar tela
import os
def limpar_tela():
    os.system('cls')

limpar_tela()

#Variáveis

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

#Algoritmo

if n1 == 0:
    print ("Essa conta não é possível pois 0 não é divisível")
elif n2 == 0:
    print ("Essa conta não é possível pois 0 não é divisível")
else:
    print (f"Sua divisão tem o seguinte valor: {n1/n2}")

limpar_tela