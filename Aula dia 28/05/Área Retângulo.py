import os
def limpar_tela():
    os.system('cls')

limpar_tela()

#Começo
base = float(input("Qual o tamanho da base (em metros)?:"))
altura = float(input("Qual o tamanho da altura (em metros)?:"))
area = base * altura

if base < 0 :
    print("Não é possível calcular sua área!")

elif altura < 0 :
    print("Não é possível calcular sua área!")
    
else:
    print(f"O valor da área é {area}m²")