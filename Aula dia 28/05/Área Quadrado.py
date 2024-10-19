import os
def limpar_tela():
    os.system('cls')

limpar_tela()

#Começo
base = float(input("Qual o tamanho do lado (em metros)?:"))
area = base * base

if base < 0 :
    print("Não é possível calcular sua área!")
    
else:
    print(f"O valor da área é {area}m²")